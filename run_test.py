#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

import sys
import pytest


def main():
    """docstring."""
    arg = sys.argv[-1] if len(sys.argv) > 1 else ""

    args = [
        f"tests/{arg}",  # test suite
        "--capture=no",
        "--durations=10",
        "--import-mode=importlib",
        "--doctest-modules",
        "--capture=no",
        "-vvv",
    ]

    return pytest.main(args)


if __name__ == "__main__":
    result = main()
    sys.exit(int(result))
