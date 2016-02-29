from app import app
import unittest
#if this app were any good, we'd have tests.

class FlaskTestCase(unittest.TestCase):

    #ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# self.assertTrue(b'Error message' in response.data)

if __name__ == '__main__':
    unittest.main()
