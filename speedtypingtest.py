#SPEED TYPING TEST PROJECT
import time
def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)

    input("Press Enter to start...")

    start_time = time.time()

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    words = len(text.split())
    characters = len(text.replace(" ", ""))
    wpm = words / (elapsed_time / 60)
    accuracy = calculate_accuracy(text, user_input)

    print("\nResults:")
    print("Elapsed Time: {:.2f} seconds".format(elapsed_time))
    print("Speed: {:.2f} WPM (Words per Minute)".format(wpm))
    print("Accuracy: {:.2f}%".format(accuracy))

def calculate_accuracy(original, typed):
    correct_characters = 0
    for c1, c2 in zip(original, typed):
        if c1 == c2:
            correct_characters += 1
    accuracy = (correct_characters / len(original)) * 100
    return accuracy

if __name__ == "__main__":
    speed_typing_test()

