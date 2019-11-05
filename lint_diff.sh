#!/usr/bin/env bash
# Copyright: 2017, Loic Esteve
# License: BSD 3 clause
# Ref: https://github.com/sardana-org/sardana/blob/develop/ci/lint_diff.sh

# This script is used on Travis CI (linting stage) to check that PRs does not add
# any linting violations.

# It relies on two things:
#   - computing a similar diff to what github is showing in a PR.
#   The diff is done between:
#       1. The common ancestor of the local branch and the ska-sa/<repo> remote.
#       2. The local branch
#           - run `flake8 --diff --show-source` on the computed diff [Default]
#
# Additional features:
#   - bash scripts/lint_diff.sh can be run locally for quick turn-around
#     (and it accepts additional linter options)

LINTER=${LINTER:='flake8'}
PARENT_BRANCH=${PARENT_BRANCH:="master"}
EXT=${EXT:="\.py$"}

while getopts ":x:b:e:o:r:h" OPTIONS; do
  case $OPTIONS in
    x)
      LINTER=${OPTARG}
      ;;
    b)
      PARENT_BRANCH=${OPTARG}
      ;;
    e)
      EXT=${OPTARG}
      ;;
    o)
      OPTS=${OPTARG}
      ;;
    r)
      REPO_NAME=${OPTARG}
      ;;
    h)
      echo -e "Usage: $0 [options]\n"
      echo -e "Options:"
      echo -e "  -x\t Lint command. (default: flake8)"
      echo -e "  -b\t Parent branch. (default: master)"
      echo -e "  -e\t File extension regex. (default: *.py)"
      echo -e "  -o\t Additional linter options. (default: None)"
      echo -e "  -r\t Name of the repository. (required)"
      echo -e "  -h\t Show this help message and exit."
      exit 0
      ;;
    \?)
      echo -e "Invalid option: ${OPTARG} \n$0 -h for help" >&2
      exit 1
      ;;
    :)
      echo -e "Option -${OPTARG} requires an argument\n$0 -h for help" >&2
      exit 1
      ;;
  esac
done

# exit script if any of the subsequent commands fails.
set -o errexit
# pipefail is necessary to propagate exit codes.
set -o pipefail

if [ -z "${REPO_NAME}" ]; then
    echo "Repository name not given."
    echo "See usage: $0 -r <repository name>"
    exit 1
fi
# Find the current repository name.
PROJECT="ska-sa/${REPO_NAME}"
# Find the remote with the project name (upstream in most cases)
REMOTE=$(git remote -v | grep "${PROJECT}" | cut -f1 | head -1 || echo 'origin')
# find the common ancestor between $LOCAL_BRANCH_REF and $REMOTE/$PARENT_BRANCH
LOCAL_BRANCH_REF=$(git rev-parse --abbrev-ref HEAD)
echo -e "\nLast 2 commits in ${LOCAL_BRANCH_REF}:"
echo -e '------------------------------------------------------------------------------\n'
git log -2 "${LOCAL_BRANCH_REF}"

REMOTE_DEVELOP_REF="${REMOTE}/${PARENT_BRANCH}"
# Make sure that $REMOTE_DEVELOP_REF is a valid reference
echo -e "\nFetching ${REMOTE_DEVELOP_REF}"
echo -e '------------------------------------------------------------------------------\n'

# Try to fetch refs from github ssh, if fails fetch from https
git fetch -v --progress git@github.com:"${PROJECT}.git" \
    "${PARENT_BRANCH}":refs/remotes/"${REMOTE_DEVELOP_REF}" "${PARENT_BRANCH}" || \
git fetch -v --progress https://github.com/"${PROJECT}.git" \
    "${PARENT_BRANCH}":refs/remotes/"${REMOTE_DEVELOP_REF}" "${PARENT_BRANCH}"

LOCAL_BRANCH_SHORT_HASH=$(git rev-parse --short "${LOCAL_BRANCH_REF}")
REMOTE_DEVELOP_SHORT_HASH=$(git rev-parse --short "${REMOTE_DEVELOP_REF}")

# Very confusing: need to use '..' i.e. two dots for 'git
# rev-list' but '...' i.e. three dots for 'git diff'
DIFF_BRANCHES="${REMOTE_DEVELOP_REF}...${LOCAL_BRANCH_REF}"
DIFF_RANGE="${REMOTE_DEVELOP_SHORT_HASH}...${LOCAL_BRANCH_SHORT_HASH}"
REV_RANGE="${REMOTE_DEVELOP_SHORT_HASH}..${LOCAL_BRANCH_SHORT_HASH}"

echo -e "\nRunning ${LINTER} on the diff in the range (${DIFF_BRANCHES}) \n${DIFF_RANGE}"
echo -e "\n($(git rev-list "${REV_RANGE}" | wc -l) commit(s)):"
echo -e '------------------------------------------------------------------------------\n'

# We ignore all non defined files/extensions.
# We need the following command to exit with 0 hence the echo in case
# there is no match
MODIFIED_FILES=$(git diff --name-only "${DIFF_RANGE}" | grep -E ${EXT} || echo "no_match")

if [[ "$MODIFIED_FILES" == "no_match" ]]; then
    echo "No python files have been modified."
else
    # temporarily mask the errexit option cause we want to capture the exit
    # code and print a dedicated output
    set +o errexit

    # check if linter is installed, if not try to install it.
    if ! command -v ${LINTER} >/dev/null 2>&1; then
        pip install ${LINTER} >/dev/null 2>&1 || exit 1
    fi
    # check if linter is flake8, and amend additional configurations
    if [[ "$LINTER" == "flake8" ]]; then
        LINTER="${LINTER} --diff --config=setup.cfg"
    fi

    # Conservative approach: diff without context so that code that
    # was not changed does not create failures
    git diff --unified=0 $DIFF_RANGE -- $MODIFIED_FILES | ${LINTER} ${OPTS}
    RET=$?

    # exit script if any of the subsequent commands fails
    set -o errexit

    if [ "${RET}" -eq 0 ]; then
        echo -e "No problem detected by ${LINTER}\n"
    else
        echo '----------------------Linting Failed!!!------------------------------------'
        echo "'black' and 'autopep8' tool may be useful in fixing these errors."
        echo -e "More information on: https://pypi.python.org/pypi/autopep8.\n"
        echo -e "Remember that ci/lint_diff.sh can be run locally for quick turn-around"
        echo -e "(you will need ${LINTER} installed) - just commit your changes and run "
        echo -e "the script.\n"
        exit $RET
    fi
fi
