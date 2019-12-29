import unittest
import logging
from logging import Logger
from space_sdk.space import *


class TestBase(unittest.TestCase):

    logger: Logger

    def setUp(self) -> None:
        self.logger = logging.getLogger('test_logs.log')
        print(self.logger)
