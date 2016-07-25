import unittest
import lib

def isValid(discs):
    return discs == sorted(discs)

def aux(pegs, moves, count):
    if len(moves) > count ** 4:
        return []
    if len(pegs[1][1]) == count:
        return moves
    for p1, discs1 in pegs:
        assert all(type(i) == int  for i in discs1)
        if not discs1:
            continue
        for p2, discs2 in pegs:
            if p1 == p2 or (p2, p1) in moves:
                continue
            newDiscs2 = discs1[:1] + discs2
            if isValid(newDiscs2):
                newDiscs1 = discs1[1:]
                newPegs = [
                    (p, newDiscs1) if p == p1 else
                    (p, newDiscs2) if p == p2 else (p, discs)
                    for p, discs in pegs
                ]
                res = aux(newPegs, moves + [(p1, p2)], count)
                if len(res) > 0:
                    return res
    return []


def hanoi(count, pegs):
    pegs = [(pegs[0], range(count))] + [(p, []) for p in pegs[1:]]
    return aux(pegs, [], count)

def simulation(count, pegs, moves):
    print moves
    pegs_dict = {}
    for p in pegs:
        pegs_dict[p] = []
    pegs_dict[pegs[0]] = range(count)
    for f, t in moves:
        try:
            disc = pegs_dict[f].pop(0)
        except (IndexError):
            raise False
        pegs_dict[t].insert(0, 0)
        if not (isValid(pegs_dict[f]) and isValid(pegs_dict[t])):
            return False
    return len(pegs_dict[pegs[1]]) == count


class HanoiTestCase(unittest.TestCase):

    def test_hanoi(self):
        result = hanoi(2, ['a', 'b', 'c'])
        self.assertTrue(
            simulation(2, ['a', 'b', 'c'], result)
        )

    def test_is_valid(self):
        self.assertTrue(isValid([0, 1]))


if __name__ == '__main__':
    unittest.main()
