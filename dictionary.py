not_robot = 'hello gruh'
guess_count=0
guess_limit=5
out_of_guesses = False
guess = None

while guess != not_robot and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('enter a guess: ')
        guess_count += 1
        if guess == not_robot:
            print('you win!')
            break
    else:
        out_of_guesses = True
        print('you lose!')
