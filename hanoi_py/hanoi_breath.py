import unittest
import lib

def deep_copy(d):
    new_d = {}
    for k, v in d.items():
        new_d[k] = v[:]
    return new_d

def is_goal_state(pegs, goal_peg, count):
    assert goal_peg in pegs.keys()
    return len(pegs[goal_peg]) == count

def get_next_states(pegs_dict):
    for peg, discs in pegs_dict.items():
        if not discs: # no discs to move
            continue
        for next_peg, new_discs in pegs_dict.items():
            if peg == next_peg:
                continue
            if not new_discs or discs[0] < new_discs[0]:
                new_pegs_dict = deep_copy(pegs_dict)
                disc_to_move = new_pegs_dict[peg].pop(0)
                new_pegs_dict[next_peg].insert(0, disc_to_move)
                yield new_pegs_dict, (peg, next_peg)

# create list of possible moves
# for each move create list of po
def hanoi(count, pegs):
    pegs_dict = {}
    for p in pegs:
        pegs_dict[p] = []
    pegs_dict[pegs[0]] = range(count)
    states = [(pegs_dict, [])]
    while True:
        for state, moves in states:
            print 'top', state, moves
            assert len(moves) < 20
            new_possible_states = []
            if is_goal_state(state, pegs[1], count):
                return moves
            for new_state, new_move in get_next_states(state):

                print 'bottom', new_state, new_move, moves
                is_cycle = new_state in states or (moves and new_move[::-1] == moves[-1])
                print is_cycle, is_goal_state(state, pegs[1], count)
                if is_cycle:
                    continue
                else:
                    new_possible_states.append((new_state, moves + [new_move]))
        states = new_possible_states
        print 'states', states
    assert False

class HanoiTestCase(unittest.TestCase):

    def test_hanoi(self):
        res = hanoi(1, ['a', 'b'])
        self.assertEqual(
            res,
            [('a', 'b')]
        )
        self.assertTrue(lib.simulation(1, ['a', 'b'], res))

    def test_hanoi_complex(self):
        res = hanoi(2, ['a', 'b', 'c'])
        self.assertEqual(
            res,
            [ ("a","c"), ("a","b"), ("c","b") ]
        )
        self.assertTrue(lib.simulation(2, ['a', 'b', 'c'], res))

    def test_hanoi_complex_3(self):
        res = hanoi(3, ['a', 'b', 'c'])
        self.assertEqual(
            res,
            [ ("a","c"), ("a","b"), ("c","b") ]
        )
        self.assertTrue(lib.simulation(2, ['a', 'b', 'c'], res))

    def test_get_next_states_one_variant(self):
        self.assertSequenceEqual(
            list(get_next_states({'a': [0], 'b': []})),
            [({'a': [], 'b': [0]}, ('a', 'b'))]
        )

    def test_get_next_states_forbiden_passes(self):
        self.assertSequenceEqual(
            list(get_next_states({'a': [0], 'b': [1]})),
            [({'a': [], 'b': [0, 1]}, ('a', 'b'))]
        )
        self.assertSequenceEqual(
            list(get_next_states({'a': [1], 'b': [0]})),
            [({'a': [0, 1], 'b': []}, ('b', 'a'))]
        )

    def test_get_next_states_two_possibilities(self):
        self.assertSequenceEqual(
            list(get_next_states({'a': [0], 'b': [], 'c': [] })),
            [
                ({'a': [], 'b': [], 'c': [0]}, ('a', 'c')),
                ({'a': [], 'b': [0], 'c': []}, ('a', 'b')),
            ]
        )


if __name__ == '__main__':
    unittest.main()
