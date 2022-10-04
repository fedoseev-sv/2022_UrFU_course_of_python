import numpy as np

def random_predict(number: int = 1) -> int:
    """
    to guess number.

    Args:
        number (int, optional): A numer for predict. Defaults to 1.

    Returns:
        int: A number try.
    """
    
    count: int = 0

    while True:
        count += 1
        predicte_number = np.random.randint(1, 101) # to generate a number  
        if number == predicte_number:
            break # to end cycle
    
    return(count)

def score_game(random_predict) -> int:
    """to calculate a avarege score predicted number.

    Args:
        random_predict (int): A function for predict.

    Returns:
        int: to calculated a average score predicted number. 
    """
    
    countList = [] 
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        countList.append(random_predict(number))

    score = int(np.mean(countList))
    
    return score
    
#RUN'
if __name__ == '__main__':
    print(f"Avarage {score_game(random_predict)}")