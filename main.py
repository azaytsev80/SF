import numpy as np

# The function generates random number and counts for how many times function game_core algorithm guesses the fugure
def score_game(game_score):
    count_ls= []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"The program guessed number for {score} times")
    return score

# The function calculates number which was generated in score_game function
def game_core(number):
    count = 1
    min = 1
    max = 101
    predict = (max+min) // 2
    while predict != number:
        count += 1
        if number > predict:
            min = predict
        else:
            max=predict
        predict = (max + min) // 2
    return count

score_game(game_core)