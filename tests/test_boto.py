import unittest
from playground.create_boto import create_bucket

class TestBoto(unittest.TestCase):

    def test_create_s3(self):
        assert create_bucket("nguyen-bucket-test") == False