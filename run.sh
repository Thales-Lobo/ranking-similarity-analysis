#!/bin/bash
# Script to clean images directory and optionally run main.py with arguments

# Default paths and command
MAIN_PY="python3 src/main.py"
CLEAN_IMAGES=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -c|--clean)
        CLEAN_IMAGES=true
        shift # past argument
        ;;
        *)    # unknown option
        # pass any other arguments to main.py
        MAIN_PY="$MAIN_PY $1"
        shift # past argument
        ;;
    esac
done

# Clean images directory if flag is set
if [ "$CLEAN_IMAGES" = true ]; then
    echo "Cleaning images directory..."
    rm -rf src/data/images/*
    exit 0  # Exit script after cleaning images
fi

# Run main.py with passed arguments
echo "Running main.py..."
$MAIN_PY
