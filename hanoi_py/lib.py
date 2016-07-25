
class ValidationError: Exception

def isValidPeg(discs):
    return discs == sorted(discs)

def simulation(count, pegs, moves):
    pegs_dict = {}
    for p in pegs:
        pegs_dict[p] = []
    pegs_dict[pegs[0]] = range(count)
    for f, t in moves:
        try:
            disc = pegs_dict[f].pop(0)
        except (IndexError):
            raise ValidationError
        pegs_dict[t].insert(0, 0)
        if not (isValid(pegs_dict[f]) and isValid(pegs_dict[t])):
            raise ValidationError
    return len(pegs_dict[pegs[1]]) == count
