#!/usr/bin/env bash

set -euo pipefail

build_file=".build_number"
build_number=1

if [[ -f "$build_file" ]]; then
    build_number=$(( $(<"$build_file") + 1 ))
fi

printf '%s\n' "$build_number" > "$build_file"
cc -DBUILD_NUMBER="$build_number" hello.c -o hello
