#!/bin/bash

# Color settings
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if there is a parent commit (to avoid errors on the first commit)
if git rev-parse --verify HEAD^ >/dev/null 2>&1; then
  # If there is a parent commit, perform a diff comparison
  MODIFIED_FILES=$(git diff --name-only HEAD^ HEAD)
else
  # If this is the first commit, list the files in the current commit
  MODIFIED_FILES=$(git ls-tree --name-only -r HEAD)
fi

echo "Modified files:"
echo "$MODIFIED_FILES"

# Filter out files outside the 'members/' directory, while ignoring the '.gitmodules' file
NON_MEMBER_FILES=$(echo "$MODIFIED_FILES" | grep -vE '^members/|^\.gitmodules$')

if [ -n "$NON_MEMBER_FILES" ]; then
  echo -e "${RED}Error: The following non-members/ files were modified (excluding .gitmodules):${NC}" >&2
  echo -e "${YELLOW}$NON_MEMBER_FILES${NC}" >&2
  exit 1
else
  echo -e "${GREEN}Only members/ directory or .gitmodules was modified. Proceeding...${NC}"
fi
