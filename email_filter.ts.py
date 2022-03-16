import unittest

from email_filter import filter_rows


class MyTestCase(unittest.TestCase):
    def test_filter_emails(self):
        # filter out bad emails
        filtered = filter_rows([{'name': 'Charlie', 'email': 'Charlie@charlie.com'},
                                {'name': 'Bad', 'email': 'Bad@bad.com'}],
                               ['Alice'],
                               ['@Bad.com'],
                               name_col_name='name',
                               email_col_name='email')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'Charlie')
        self.assertEqual(filtered[0]['email'], 'Charlie@charlie.com')

    def test_filter_names(self):
        # filter out bad names
        filtered = filter_rows([{'name': 'Charlie', 'email': 'charlie@charlie.com'},
                                {'name': 'Bad', 'email': 'Bad@bad.com'}],
                               ['BAD'],
                               ['@google.com'],
                               name_col_name='name',
                               email_col_name='email')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'Charlie')
        self.assertEqual(filtered[0]['email'], 'charlie@charlie.com')


if __name__ == '__main__':
    unittest.main()
