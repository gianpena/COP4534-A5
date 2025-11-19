#!/bin/bash

GREEN=$'\033[0;32m'
RED=$'\033[0;31m'
RESET=$'\033[0m'

for f in ./*; do
  script_name=$(basename "$f" .py)
  if [[ ! -d "$f" ]]; then
    continue
  fi

  echo "Grading ${f}..."
  for t in "${f}"/*.in; do
    name=$(basename "${t}" .in)
    if diff <(python "${f}/${script_name}.py" < "${t}") "${f}/${name}.out" >/dev/null 2>&1; then
      echo -e "${t}:\t${GREEN}CORRECT${RESET}"
    else
      echo -e "${t}:\t${RED}WRONG ANSWER${RESET}"
    fi
  done
  echo ""
done