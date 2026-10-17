import time
import random

sentences = [
        "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class.", 
    "There should be no complian make a blinder."
]

def measure_accuracy(user_input, test_sentences):
    correct_char = sum(1 for a , b in zip(user_input , test_sentences) if a == b)
    accuracy = (correct_char / len(test_sentences ))* 100 if test_sentences else 0
    return accuracy

def typing_test():
    test_sentences = random.choice(sentences)
    print("Type the following sentences as fast as you can")
    print(test_sentences)
    input("Press enter when you are ready ...")
    start_time = time.time()
    user_input = input("\n start typing.. \n")
    end_time = time.time()
    time_taken = end_time - start_time
    words_count = len(test_sentences.split(" "))
    

    print("result..")
    print(f"time taken : {time_taken} seconds")
    print(f"word types : {words_count}")
    print(f"Typing speed : {words_count / (time_taken / 60):.2f} words per minutes")
    accuracy = measure_accuracy(user_input , test_sentences)
    print(f"Accuracy : {accuracy:.2f}%")


typing_test()