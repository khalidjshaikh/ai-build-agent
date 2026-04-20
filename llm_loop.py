#!/usr/bin/env python3

import subprocess


def should_build(prompt: str) -> bool:
    prompt = prompt.lower()
    keywords = ("build", "compile", "make")
    return any(keyword in prompt for keyword in keywords)


def should_run(prompt: str) -> bool:
    prompt = prompt.lower()
    keywords = ("run", "execute", "start")
    return any(keyword in prompt for keyword in keywords)


def main() -> int:
    print("Enter prompts. Type 'exit' or 'quit' to stop.")

    while True:
        try:
            prompt = input("llm> ").strip()
        except EOFError:
            print()
            break

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit"}:
            break

        if should_build(prompt):
            print("Invoking ./build.sh")
            subprocess.run(["./build.sh"], check=True)
            print("Build complete.")
        if should_run(prompt):
            print("Running ./hello")
            subprocess.run(["./hello"], check=True)
        if not should_build(prompt) and not should_run(prompt):
            print("No build or run action requested.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
