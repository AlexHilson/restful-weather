#!/usr/bin/env python

import unittest

import mock

from harvest import scrape, WCSMetadata


class TestHarvest(unittest.TestCase):
    @mock.patch('harvest.WCSMetadata')
    def test_correct(self, mock_WCSMetadata):
        config = {'model_a': {'url': 'http://localhost:8080'},
                  'model_b': {'url': 'http://localhost:8888'}}
        mock_WCSMetadata.return_value = True
        expected = {'model_a': True, 'model_b': True}
        result = scrape(config)
        self.assertEqual(result, expected)

    @mock.patch('harvest.WCSMetadata')
    def test_kwargs(self, mock_WCSMetadata):
        config = {'model_a': {'url': 'http://0', 'key': '123'}}
        result = scrape(config)
        mock_WCSMetadata.assert_called_with('http://0', key='123')

    def test_missing_url(self):
        config = {'model_a': {'key': 'abcd'}}
        with self.assertRaises(KeyError):
            result = scrape(config)
