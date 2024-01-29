#!/usr/bin/env python3
"""This is a pagination exercise module"""


def index_range(page: int, page_size: int) -> tuple:
    """this method returns the index_range of a page and the page_size"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
