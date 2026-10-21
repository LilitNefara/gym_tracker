from datetime import date
import json

workouts = [
    {"exercise": "jim leja", "weight": 70, "reps": 10, "date": "01.01.2000"},
    {"exercise": "prised", "weight": 100, "reps": 8, "date": "01.01.2000"},
    {"exercise": "jim leja", "weight": 75, "reps": 8, "date": "01.01.2000"},
    {"exercise": "jim leja", "weight": 80, "reps": 6, "date": "01.01.2000"}
]

def add_workout():
    try:
        workout = {}
        exercise, weight, reps = input("\nAdd a exercise: ").rsplit(' ', 2)
        workout["exercise"] = exercise
        workout["weight"] = int(weight)
        workout["reps"] = int(reps)
        workout["date"] = date.today().strftime("%d.%m.%Y")

        progress = get_progress(workout)
        if progress is None: print("\nThe training session was added for the first time")
        elif progress > 0: print(f"\nProgress: +{progress} kg")
        elif progress < 0: print(f"\nProgress: {progress} kg")
        else: print("\nThere is no progress")

        workouts.append(workout)

    except ValueError:
        print("\nValueError")

def get_progress(check_progress):
    last_workouts = []
    result = None

    for i in workouts:
        if i["exercise"] == check_progress["exercise"]:
            last_workouts.append(i)

    if last_workouts:
        print("\n")
        last = last_workouts[-1]
        print(f"{last['exercise']} - {last['weight']} kg x {last['reps']} | {last['date']}")
        print(f"{check_progress['exercise']} - {check_progress['weight']} kg x {check_progress['reps']} | {check_progress['date']}")
        result = check_progress['weight'] - last['weight']

    return result

def show_workouts():
    for i in workouts:
        print(f"{i['exercise']} - {i['weight']} kg x {i['reps']} | {i['date']}")

def get_max_weight(user_input):
    max_weight = None

    for i in workouts:
        if i["exercise"] == user_input:
            if max_weight is None or i["weight"] > max_weight:
                max_weight = i["weight"]
    return max_weight

def get_last_workouts(user_exc):
    last_workouts = []

    for i in workouts:
        if i["exercise"] == user_exc:
            last_workouts.append(i)

    if last_workouts:
        print("\n")
        for ex in last_workouts[-3:]:
            print(f"{ex['exercise']} - {ex['weight']} kg x {ex['reps']} | {ex['date']}")

while(True):
    command = input("\n1 - add\n2 - show\n3 - max weight\n4 - last workouts\nq - exit\n\nEnter a number: ")
    if command == "q": break
    if command == "1": add_workout()
    if command == "2": print("\n"); show_workouts()
    if command == "3":
        max_weight = get_max_weight(input("\nExercise: "))

        if max_weight is None:
            print("\nExercise not found.")
        else:
            print("\nMax weight:", max_weight)

    if command == "4": get_last_workouts(input("\nExercise: ")) 