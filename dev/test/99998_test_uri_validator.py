import unittest
import validators
import cfg.ctt as ctt
import com.assessments.assessments as ass

# LOG = '../log/resource_relations_test.log'
# io.drop_file(LOG)
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
# level=logging.INFO, filename=LOG)
# logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
# logger = logging.getLogger('resource_relations')


class TestAssessments(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAssessments, self).__init__(*args, **kwargs)

    def setUp(self) -> None:
        return

    @staticmethod
    def test_001_connect_cellar_test():
        a = validators.url('http://data.europa.eu/w21/9e31097b-33c6-4b18-8b4b-fae8a6fd89e9')
        return


if __name__ == '__main__':
    unittest.main()
