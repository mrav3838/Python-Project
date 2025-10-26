questions = [
    ["Who is Max Verstappen?", "Actor", "Footballer", "Racing Driver", "Musician", 3],
    ["Who was Thomas Shelby?", "Racing Driver", "Fictional Character", "Politician", "Scientist", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["What is the largest mammal?", "Elephant", "Hippopotamus", "Giraffe", "Blue Whale", 4],
    ["Largest continent on Earth?", "Asia", "Africa", "Europe", "Antarctica", 1],
    ["Who won 2021 Abu Dhabi Grand Prix?", "Lewis Hamilton", "Max Verstappen", "Valtteri Bottas", "Sebastian Vettel", 2],
    ["How many Championship is hold by lewis hamilton in total", "11", "7", "3", "5", 2]]

prizes = [100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 50000000]
sum = 0
for q in questions:
    print(q[0])
    print("1.", q[1])
    print("2.", q[2])
    print("3.", q[3])
    print("4.", q[4])

    ans = int(input("Enter your answer (1-4): "))
    if ans == q[5]:
        prize = prizes[questions.index(q)]
        print(f"Correct! You have won Rs.{prize} for this question\n")
        sum += prize
    else:
        print("Incorrect answer. Game over! Better luck next time.")
        break

print(f"Congratulations! You have won a total of Rs.{sum}")