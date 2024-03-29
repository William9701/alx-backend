#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0,
                        page_size: int = 10) -> Dict:
        """This is the get_hyper_index"""
        assert index is None or (
                isinstance(index, int) and index >= 0), "Invalid index"
        assert isinstance(page_size,
                          int) and page_size > 0, "Page size must be a " \
                                                  "positive integer"

        # If index is None, set it to 0
        index = index or 0

        # Get the dataset
        dataset = self.dataset()

        # Verify that the index is in a valid range
        assert index < len(dataset), "Index out of range"

        # Calculate the start and end indexes for the current page
        start_index = index
        end_index = min(index + page_size, len(dataset))

        # Get the actual page of the dataset
        data = dataset[start_index:end_index]

        # Calculate the next index to query with
        next_index = end_index if end_index < len(dataset) else None

        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
