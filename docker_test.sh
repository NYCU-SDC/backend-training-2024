#!/bin/bash

# Define a function to print a separator that matches the terminal width
print_separator() {
    local message=" $1 " # Get the function argument as the message
    local term_width=$(tput cols) # Get the terminal width
    local equals_width=$(( (term_width - ${#message}) / 2 )) # Calculate the number of equal signs

    # Output the separator line
    printf '%*s' "$equals_width" | tr ' ' '='
    printf '%s' "$message"
    printf '%*s\n' "$equals_width" | tr ' ' '='
}

print_separator "Check files change"
./.github/scripts/check_files.sh

print_separator "Install requirements"
docker exec -t -w "/mnt/app" fastapi_app pip install -r requirements.txt

print_separator "Run pytest"
docker exec -t -w "/mnt" fastapi_app sh -c "rm -f /mnt/test*"
docker exec -t -w "/mnt" fastapi_app cp -fr .github/scripts/* ./
docker exec -t -w "/mnt" fastapi_app pytest
