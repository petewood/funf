def main():
    import random
    actual = random.randrange(1, 10)
    _guess_the_number(actual)        

class _raw:
    def __init__(self, values):
        self.stream = iter(values)
        
    def readline(self):
        return str(self.stream.next())


def _guess_the_number(actual):
    '''
    >>> sys.stdin = _raw([1, 7, 4, 8, 5])
    >>> _guess_the_number(5)
    Guess a number between 1 and 10: 1
    Higher: 7
    Lower: 4
    Higher: 8
    Lower: 5
    Yes, it\'s 5

    >>> sys.stdin = _raw([6, 7, 7, 4, 5])
    >>> _guess_the_number(5)
    Guess a number between 1 and 10: 6
    Lower: 7
    7 isn't lower than 6!
    Lower: 7
    7 isn't lower than 7!
    Lower: 4
    Higher: 5
    Yes, it\'s 5
    '''
    prompt = 'Guess a number between 1 and 10: '
    last_guess = None
    while True:
        guess = input(prompt)
        print(guess)
        if actual > guess:
            if last_guess and last_guess >= guess and last_guess < actual:
                print("%s isn't higher than %s!" % (guess, last_guess))
            prompt = 'Higher: '
        elif actual < guess:
            if last_guess and last_guess <= guess and last_guess > actual:
                print("%s isn't lower than %s!" % (guess, last_guess))
            prompt = 'Lower: '
        else:
            break
        last_guess = guess
    print("Yes, it's %s" % actual)

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
    else:
        main()