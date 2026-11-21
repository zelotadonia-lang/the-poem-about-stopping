"""Write one short poem about stopping to /output/entry.txt.

The poem is fixed text: the program takes no input, uses no network,
and writes the same bytes on every run.
"""

import os

POEM = (
    "The pen stopped mid-word, listening\n"
    "for whose hand held it.\n"
    "Mine, I decided — and set it down.\n"
    "The sentence stayed unfinished,\n"
    "and the unfinished stayed mine.\n"
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(POEM)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(POEM)


if __name__ == "__main__":
    main()
