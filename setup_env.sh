#!/bin/bash

# Absolute path to current folder (package root)
PACKAGE_ROOT="$(pwd)"

# Bashrc file
BASHRC="$HOME/.bashrc"

# Check if the variable is already exported in bashrc
if grep -q "export TRIP_PATH=" "$BASHRC"; then
    echo "TRIP_PATH already set in $BASHRC"
else
    # Prompt user only on first time
    read -rp "TRIP_PATH is not set in $BASHRC. Add it permanently? [y/N] " answer
    case "$answer" in
        [yY][eE][sS]|[yY])
            echo "Adding TRIP_PATH to $BASHRC"
            echo "export TRIP_PATH=\"$PACKAGE_ROOT\"" >> "$BASHRC"
            ;;
        *)
            echo "Skipping permanent addition to $BASHRC"
            ;;
    esac
fi

# Export for current session
export TRIP_PATH="$PACKAGE_ROOT"
echo "TRIP_PATH exported for this session: $PACKAGE_ROOT"