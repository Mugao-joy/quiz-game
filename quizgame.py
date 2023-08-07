print('Welcome to my compute game')
intro = input("Would you like to play? ")
if intro.lower() != "yes" :
    quit()

print('Great, lets get started')
score = 0

answer = input('what is the capital city of kenya? ')
if answer.lower() == 'nairobi':
    print('That is correct')
    score += 1
else:
    print('That is incorrect!')

answer = input('which month does valentines fall on? ')
if answer.lower() == 'february':
    print('That is correct')
    score += 1

else:
    print('That is incorrect!')

answer = input('which team won in the recent U20 rugby championships? ')
if answer.lower() == 'spain':
    print('That is correct')
    score += 1
else:
    print('That is incorrect!')
answer = input('what does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('That is correct')
    score += 1
else:
    print('That is incorrect!')
print('You got ' + str(score) + ' questions correct!')
print('Final score ' + str((score / 4) * 100)+ '%')


