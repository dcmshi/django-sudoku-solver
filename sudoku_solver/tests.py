import re

from django.test import SimpleTestCase

# A well-known puzzle with 30 givens; 0 is a blank cell.
PUZZLE = (
    '530070000600195000098000060800060003400803001'
    '700020006060000280000419005000080079'
)
SOLVED = 'I solved this puzzle for you'
INVALID = 'Your puzzle seems to be invalid or incomplete!'


def post_data(cells, total=81):
    data = {
        'form-TOTAL_FORMS': str(total),
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '81',
        'form-MAX_NUM_FORMS': '81',
        'action': 'solve',
    }
    for i, ch in enumerate(cells[:total]):
        data[f'form-{i}-value'] = '' if ch == '0' else ch
    return data


class SolveTests(SimpleTestCase):
    def test_home_renders_81_cells(self):
        html = self.client.get('/').content.decode()
        self.assertEqual(html.count('name="form-'), 81 + 4)

    def test_solves_puzzle_with_blank_cells(self):
        html = self.client.post('/', post_data(PUZZLE)).content.decode()
        self.assertIn(SOLVED, html)
        first_row = [re.search(rf'name="form-{i}-value" value="(\d)"', html)[1] for i in range(9)]
        self.assertEqual(''.join(first_row), '534678912')

    def test_rejects_fewer_than_17_givens(self):
        sparse = PUZZLE[:20] + '0' * 61
        html = self.client.post('/', post_data(sparse)).content.decode()
        self.assertIn(INVALID, html)

    def test_rejects_a_short_board(self):
        html = self.client.post('/', post_data(PUZZLE, total=80)).content.decode()
        self.assertIn(INVALID, html)
