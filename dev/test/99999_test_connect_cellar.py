import unittest
import sys
import logging
import cfg.ctt as ctt

LOG = '../log/resource_relations_test.log'
# io.drop_file(LOG)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO, filename=LOG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logger = logging.getLogger('resource_relations')


class ConnectCellarTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ConnectCellarTest, self).__init__(*args, **kwargs)

    def setUp(self) -> None:
        return

    @staticmethod
    def test_001_connect_cellar_test(self):
        return


if __name__ == '__main__':
    unittest.main()
