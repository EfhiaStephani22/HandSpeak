GESTURE_MAP = {
    (0,0,0,0,0): "Hello",
    (1,0,0,0,0): "Yes",
    (0,1,0,0,0): "No",
    (0,1,1,0,0): "Thank You",
    (0,1,1,1,0): "Please",
    (0,1,1,1,1): "Sorry",
    (1,1,1,1,1): "Help",
    (1,1,0,0,0): "Stop",
    (0,0,1,0,0): "Go",
    (0,0,1,1,0): "Come",

    (0,0,0,1,0): "Wait",
    (0,0,0,1,1): "Good",
    (1,0,0,1,0): "Bad",
    (1,0,0,1,1): "Yes Please",
    (1,1,0,0,1): "No Thanks",
    (1,1,1,0,0): "Welcome",
    (0,1,0,1,0): "Bye",
    (0,1,0,1,1): "Take Care",
    (0,1,1,0,1): "Love",
    (1,0,1,0,0): "Like",

    (1,0,1,1,0): "Dislike",
    (1,0,1,1,1): "Food",
    (1,1,0,1,0): "Water",
    (1,1,0,1,1): "Hungry",
    (1,1,1,0,1): "Thirsty",
    (0,1,1,1,0): "Sleep",
    (0,0,1,1,1): "Work",
    (0,1,0,0,1): "Home",
    (1,0,0,0,1): "School",
    (1,0,0,1,0): "Office",

    (0,0,0,0,1): "Friend",
    (0,0,1,0,1): "Family",
    (0,1,0,1,0): "Doctor",
    (1,1,0,0,0): "Hospital",
    (0,1,1,0,0): "Emergency",
    (1,0,1,0,1): "Phone",
    (1,1,1,1,0): "Money",
    (0,1,1,1,1): "Time",
    (1,0,1,1,1): "Where",
    (1,1,0,1,1): "Why"
}

def get_gesture_text(fingers):
    return GESTURE_MAP.get(tuple(fingers), "Unknown Gesture")
