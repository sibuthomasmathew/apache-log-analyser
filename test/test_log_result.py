import unittest
from log_analyser import LogAnalyser


class TestLogAnalyser(unittest.TestCase):
    def setUp(self):
        self.page_hit = {
            'b': 5,
            'e': 2,
            'a': 27,
            'd': 10,
            'c': 19,
            'g': 33,
            'f': 12 }
        
        self.total_requests_counter = 100
        self.request_success_counter = 80


    def test_top_result(self):
        expected_result = {
            'g': 33,
            'a': 27,
            'c': 19,
            'f': 12,
            'd': 10 }

        self.assertEqual(
            LogAnalyser.get_top_result(self, self.page_hit, 5),
            expected_result,
            'Incorrect Order')

    def test_http_request_percentage(self):
        self.assertEqual(
            LogAnalyser.get_http_success_percentage(self),
            80,
            'Incorrect Percentage')

if __name__ == '__main__':
    unittest.main()
