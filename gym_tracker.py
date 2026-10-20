from datetime import date
import json

# def read_json():
#     with open("data_workouts.json", "r") as file:
#         workouts = json.load(file)
#     return workouts

# def write_json():
#     with open("data_workouts.json", "w") as file:
#         create_list = []
#         json.dump(create_list, file, indent=4)

# try:
#     read_json()
# except FileNotFoundError:
#     write_json()
# except json.JSONDecodeError:
#     write_json()
# finally:
#     workouts = read_json()

workouts = [
    {
        "group": "biceps",
        "exercise": "гантели",
        "date": "2026-09-26",
        "sets": [
            {
                "weight": 14,
                "reps": 7
            },
            {
                "weight": 14,
                "reps": 7
            },
            {
                "weight": 14,
                "reps": 7
            }
        ]
    }
]

workout_groups = {
    1: {"name" : "biceps", "exercise": {1: "гантели", 2: "туриник", 3: "кривой", 4: "блок"}},
    2: {"name": "chest", "exercise": {1: "жим", 2: "рек флай", 3: "блок"}}
    }

def opener_exercise_in_group(group):
    for index, item in workout_groups[group]["exercise"].items():
        print(f"{index} - {item}")

    print("\n(If your exercise is not on the list, write 0 and add it)\n")
    exercise_choice = int(input("Enter a exercise: "))
    
    if exercise_choice == 0:
        new_exercise = str(input("Enter a new exercise: ")).lower()
    
        if str(input(f"Are you sure to add - {new_exercise}\ny/n\n")) == "y":
            workout_groups[group]["exercise"][len(workout_groups[group]["exercise"]) + 1] = new_exercise
        else: print(new_exercise, "- not added.")
    else:
        current_exercise = workout_groups[group]["exercise"][exercise_choice]
        current_weight = int(input("Enter the weight: "))
        current_reps = int(input("Enter repetions: "))
        
        # workout = {}
        # sets = []
        set = {}; set["weight"] = current_weight; set["reps"] = current_reps

        input()

        print(set)




def add_workout():
    for index, item in enumerate(workout_groups.values(), start=1):
        print(f"{index} - {item['name']}")

    group_choice = int(input("\nChoice group: ")); print("\n")
    opener_exercise_in_group(group_choice)

    # workout = {}
    # wo_sets_list = []
    # for i in sets.split():
    #     wo_set = {}
    #     weight, reps = i.split('x')
    #     wo_set["weight"] = int(weight)
    #     wo_set["reps"] = int(reps)
    #     wo_sets_list.append(wo_set)
    # workout["sets"] = wo_sets_list
    # workout["exercise"] = exercise
    # workout["date"] = str(date.today())

    # progress = get_progress(workout)

    # if progress is None: print("\nThe training session was added for the first time")
    # elif progress > 0: print(f"\nProgress: +{progress} kg")
    # elif progress < 0: print(f"\nProgress: {progress} kg")
    # else: print("\nThere is no progress")

    # workouts.append(workout)

    # with open("data_workouts.json", "w") as file:
    #     json.dump(workouts, file, indent=4)


# def get_progress(workout):
#     last_workouts = []
#     max_weight_in_last = None
#     max_weight_in_current = None

#     for i in workouts:
#         if i["exercise"] == workout["exercise"]:
#             last_workouts.append(i)

#     if last_workouts:
#         last = last_workouts[-1]
#         for i in last["sets"]:
#             if max_weight_in_last is None or i["weight"] > max_weight_in_last:
#                 max_weight_in_last = i["weight"]
    
#         for i in workout["sets"]:
#             if max_weight_in_current is None or i["weight"] > max_weight_in_current:
#                 max_weight_in_current = i["weight"]
#         return max_weight_in_current - max_weight_in_last

# def show_workouts():
#     if workouts:
#         for i in workouts:
#             print(f"{i['exercise']} - {i['date']} : ", end='')
#             sets_str = " , ".join(f"{s['weight']} kg - {s['reps']}" for s in i['sets'])
#             print(sets_str)
#     else: print("No workouts")

# def get_max_weight(user_input):
#     max_weight = None

#     for i in workouts:
#         if i["exercise"] == user_input:
#             for s in i["sets"]:
#                 if max_weight is None or s["weight"] > max_weight:
#                     max_weight = s["weight"]
#     return max_weight

# def get_last_workouts(user_exc):
#     last_workouts = []

#     for i in workouts:
#         if i["exercise"] == user_exc:
#             last_workouts.append(i)

#     if last_workouts:
#         print("\n")
#         for i in last_workouts[-3:]:
#             print(f"{i['exercise']} - {i['date']} : ", end='')
#             sets_str = " , ".join(f"{s['weight']} kg - {s['reps']}" for s in i['sets'])
#             print(sets_str)
#     else: print("\nExercise not found")

while(True):
    command = input("\n1 - add\n2 - show\n3 - max weight\n4 - last workouts\nq - exit\n\nEnter a number: ")
    if command == "q": break
    if command == "1": add_workout()
    if command == "2": print("\n"); show_workouts()
    if command == "3":
        max_weight = get_max_weight(input("\nExercise: "))

        if max_weight is None:
            print("\nExercise not found")
        else:
            print("\nMax weight:", max_weight, 'kg')

    if command == "4": get_last_workouts(input("\nExercise: ")) 