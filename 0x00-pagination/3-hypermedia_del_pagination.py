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

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with the current start index of the return page,
        the next index to query with, the current page size, and the actual page of the dataset.

        Parameters:
        index (int): The current start index of the return page. Default is 0.
        page_size (int): The current page size. Default is 10.

        Returns:
        dict: A dictionary with the following key-value pairs:
            - 'index': The current start index of the return page.
            - 'next_index': The next index to query with.
            - 'page_size': The current page size.
            - 'data': The actual page of the dataset.
        """

        # Verify that index is in a valid range
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        dataset_size = len(dataset)

        # Verify that index is less than the size of the dataset
        assert index < dataset_size

        data = []
        next_index = index

        # Collect page_size number of items from the indexed dataset
        while len(data) < page_size and next_index < dataset_size:
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }
