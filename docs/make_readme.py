#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import os.path
import sys

import readmemaker
from path import Path


PROJECT_NAME = "DateTimeRange"
OUTPUT_DIR = ".."


def write_examples(maker):
    maker.set_indent_level(0)
    maker.write_chapter("Examples")

    example_root = Path(os.path.join("pages", "examples"))
    example_file_list = [
        "Create_and_convert_to_string.rst",
        "Get_iterator.rst",
        "Test_whether_a_value_within_the_time_range.rst",
        "Test_whether_a_value_intersect_the_time_range.rst",
        "Make_an_intersected_time_range.rst",
        "Make_an_encompassed_time_range.rst",
        "Truncate_time_range.rst",
    ]

    for example_file in example_file_list:
        maker.write_file(example_root.joinpath(example_file))

    maker.inc_indent_level()
    maker.write_chapter("For more information")
    maker.write_line_list(
        [
            "More examples are available at ",
            "https://datetimerange.rtfd.io/en/latest/pages/examples/index.html",
            "",
            "Examples with IPython Notebook is also available at ",
            "https://nbviewer.jupyter.org/github/thombashi/%s/tree/master/ipynb/DateTimeRange.ipynb"
            % (PROJECT_NAME),
        ]
    )


def main():
    maker = readmemaker.ReadmeMaker(PROJECT_NAME, OUTPUT_DIR, is_make_toc=True)

    maker.write_chapter("Summary")
    maker.write_introduction_file("summary.txt")
    maker.write_introduction_file("badges.txt")

    write_examples(maker)

    maker.write_file(maker.doc_page_root_dir_path.joinpath("installation.rst"))

    maker.set_indent_level(0)
    maker.write_chapter("Documentation")
    maker.write_line_list(["https://datetimerange.rtfd.io/"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
