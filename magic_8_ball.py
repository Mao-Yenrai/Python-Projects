#Project description: magic ball 8 (ball of fate) - a humorous way to predict the future. 
#The program asks the user to ask a question in order to randomly answer it.
#Traditionally, the ball has 20 answers, which can be divided into four groups: Positive, Hesitantly Positive, Neutral, Negative.
#So... let's begin?


from random import choice
game = 'on'
print('The magic ball welcomes you!')
name = input('How can I address you?\nEnter name: ')

magic_answers =  ['Undoubtedly!', 'I think so - yes.', '''It's not clear yet, try again...''', '''Don't even think about it.''',
                  'Predetermined.', 'Most likely.',    'Ask later.', 'My answer is - no.', 'No doubt about it.',
                  'Good prospects.', 'Better not to tell.', 'According to my information - no.',
                  'Definitely yes!', 'The signs say yes.', '''It's impossible to predict now.''',
                  'The outlook is not very good.',
                  'You can be sure of this.', 'Yes.', 'Concentrate and ask again.', 'Highly doubtful.']


while game == 'on':
    question = input(f'{name}, enter your question of interest: ')
    print(f'The wind of time says: {choice(magic_answers)}')
    restart = input('Do you still have questions? (yes = continue): ')
    if restart == 'yes' or restart == 'lf':
        continue
    else:
        print('Thank you for playing. Have a good mood!')
        game = 'off'