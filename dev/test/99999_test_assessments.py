import unittest
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
        assessments = ass.Assessments(url_connection=ctt.CELLAR_CONNECTION)
        query_results = assessments.get_assessment()
        print(query_results)
        return


if __name__ == '__main__':
    unittest.main()
