dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()

errors = [w for w in sentence if w not in dictionary]

if errors:
    print('\n'.join(errors))
else:
    print('OK')
