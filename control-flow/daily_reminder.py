task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priotity task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}' is a high priority task that is flexible.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priotity task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}' is a medium priority task that is flexible.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priotity task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}' is a low priority task that is flexible.")