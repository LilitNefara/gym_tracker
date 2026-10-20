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
    1: {"name" : "biceps", "exercise": {1: "гантели", 2: "турник", 3: "кривой", 4: "блок"}},
    2: {"name": "chest", "exercise": {1: "жим", 2: "рек флай", 3: "блок"}}
    }

def add_workout():
    # Просмотр групп мышц
    for index, item in enumerate(workout_groups.values(), start=1):
            print(f"{index} - {item['name']}")
    
    group = int(input("\nChoice group: ")); print("\n")
    
    # Просмотр упражнений (внутри групп мышц)
    for index, item in workout_groups[group]["exercise"].items():
        print(f"{index} - {item}")

    print("\n(If your exercise is not on the list, write 0 and add it)\n")
    exercise_choice = int(input("Enter a exercise: "))
    
    if exercise_choice == 0:
        # Добавление упражнений
        new_exercise = str(input("Enter a new exercise: ")).lower()
    
        if str(input(f"Are you sure to add - {new_exercise}\ny/n\n")) == "y":
            workout_groups[group]["exercise"][len(workout_groups[group]["exercise"]) + 1] = new_exercise
        else: print(new_exercise, "- not added.")
    else:
        current_exercise = workout_groups[group]["exercise"][exercise_choice]
        
        # 1 set
        current_weight = int(input("Enter the weight: "))
        sets = []
        set = {}; set["weight"] = current_weight; set["reps"] = int(input("Enter repetions: "))
        sets.append(set)
        set_counter = 0
        
        # 2 set
        print(f"{current_exercise} | {set_counter + 1}: {sets[set_counter]['weight']}x{sets[set_counter]['reps']}")
        edit = int(input("\nIf you want change weight, enter - 0\n"))
            
        if edit == 0:
            current_weight = int(input("Enter the new weight: "))
            edit = int(input("Enter repetions: "))
            
        set = {}; set["weight"] = current_weight; set["reps"] = edit
        sets.append(set)
        set_counter += 1
        
        # 3 set
        print(f"{current_exercise} | {set_counter + 1}: {sets[set_counter]['weight']}x{sets[set_counter]['reps']}")
        edit = int(input("\nIf you want change weight, enter - 0\n"))
            
        if edit == 0:
            current_weight = int(input("Enter the new weight: "))
            edit = int(input("Enter repetions: "))
            
        set = {}; set["weight"] = current_weight; set["reps"] = edit
        sets.append(set)

        print(f"{current_exercise} | {sets[0]['weight']}x{sets[0]['reps']} {sets[1]['weight']}x{sets[1]['reps']} {sets[2]['weight']}x{sets[2]['reps']}")

        # Проверка данных перед сохранением
        if input("Save = 'y'\nCancel 'n'\n") == "y":
            workout = {}
            workout["group"] = workout_groups[group]["name"]
            workout["exercise"] = current_exercise
            workout["date"] = str(date.today())
            workout["sets"] = sets

            workouts.append(workout)
            print("\nWorkout is recorded")
        else: 
            print("\nWorkout is not recorded")

def show_workouts():
    if workouts:
        for i in workouts:
            print(i)
    else: print("No workouts")

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