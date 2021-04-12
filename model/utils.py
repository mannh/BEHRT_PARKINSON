def age_vocab(max_age, mon=1, symbol=None):
    age2idx = {}
    idx2age = {}
    if symbol is None:
        symbol = ['PAD', 'UNK']

    for i in range(len(symbol)):
        age2idx[str(symbol[i])] = i
        idx2age[i] = str(symbol[i])

    if mon == 12:
        for i in range(max_age):
            age2idx[str(i)] = len(symbol) + i
            idx2age[len(symbol) + i] = str(i)
    elif mon == 1:
        for i in range(max_age * 12):
            age2idx[str(i)] = len(symbol) + i
            idx2age[len(symbol) + i] = str(i)
    else:
        age2idx = None
        idx2age = None
    return age2idx, idx2age


def weeks_vocab(max_years, symbol=None):
    weeks2idx = {}
    idx2weeks = {}
    if symbol is None:
        symbol = ['PAD', 'UNK']
    for i in range(len(symbol)):
        weeks2idx[str(symbol[i])] = i
        idx2weeks[i] = str(symbol[i])
    for i in range(int(max_years * 52)):
        weeks2idx[str(i)] = len(symbol) + i
        idx2weeks[len(symbol) + i] = str(i)


def days2weeks(days):
    return int(days / 7)
