day = input("What day of the week is it? (Monday, Tuesday, etc.): ").lower()
tod = input("What time of day is it? (Morning, afternoon, evening): ").lower()

activities = {
    "monday": {
        "morning": "Go for a morning run",
        "afternoon": "Do some homework",
        "evening": "Make some tea"
    },
    "tuesday": {
        "morning": "Make some breakfast!",
        "afternoon": "Listen to a podcast",
        "evening": "relax with a good book or movie"
    },
    "wednesday": {
        "morning": "Do some morning stretches",
        "afternoon": "Make a fun snack!.",
        "evening": "Text a friend"
    },
    "thursday": {
        "morning": "Do a puzzle",
        "afternoon": "Learn something new",
        "evening": "Try out a new recipe"
    },
    "friday": {
        "morning": "Make a healthy breakfast",
        "afternoon": "catch up with a friend",
        "evening": "Relax for a while!"
    },
    "saturday": {
        "morning": "Enjoy a nice breakfast",
        "afternoon": "Go to the library",
        "evening": "Watch a movie"
    },
    "sunday": {
        "morning": "Sleep in.",
        "afternoon": "Visit the park.",
        "evening": "Go to a restaurant"
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
