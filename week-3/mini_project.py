day = input("What day of the week is it? (Monday, Tuesday, etc.): ").lower()
tod = input("What time of day is it? (Morning, afternoon, evening): ").lower()

activities = {
    "Monday": {
        "Morning": "Go for a morning run",
        "Afternoon": "Do some work",
        "Evening": "Make some tea"
    },
    "Tuesday": {
        "Morning": "Make some breakfast!",
        "Afternoon": "Listen to a podcast",
        "Evening": "relax with a good book or movie"
    },
    "Wednesday": {
        "Morning": "Do some morning stretches",
        "Afternoon": "Make a fun snack!.",
        "Evening": "Text a friend"
    },
    "Thursday": {
        "Morning": "Do a puzzle",
        "Afternoon": "Learn something new",
        "Evening": "Try out a new recipe"
    },
    "Friday": {
        "Morning": "Make a healthy breakfast",
        "Afternoon": "catch up with a friend",
        "Evening": "Relax for a while!"
    },
    "Saturday": {
        "Morning": "Enjoy a nice breakfast",
        "Afternoon": "Go to the library",
        "Evening": "Watch a movie"
    },
    "Sunday": {
        "Morning": "Sleep in.",
        "Afternoon": "Visit the park.",
        "Evening": "Go to a restaurant"
    }
}

if day in activities:
    if tod in activities[day]:
        Suggestion = activities[day][tod]
        print(f"Suggestion: {Suggestion}")
    else:
        print("time of day isn't recognized. Please try again!")
else:
    print("Sorry, the day of the week isn't recognized. Please try again.")
