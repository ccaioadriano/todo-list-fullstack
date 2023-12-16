import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_tasks(self):
        response = self.app.get('/tarefas')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [{'completed': True, 'description': 'Description', 'id': 1, 'title': 'Title'}])


if __name__ == '__main__':
    unittest.main()
