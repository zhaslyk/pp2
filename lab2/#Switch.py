#Switch (Match) / If Elif Else
#-----------------------------------
day = 3
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case _: print("Other day")
#-----------------------------------
ext = ".jpg"
match ext:
    case ".png" | ".jpg": print("Image file")
    case ".mp4": print("Video file")
    case _: print("Unknown file")
#-----------------------------------
color = "red"
if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
else:
    print("Wait")
#-----------------------------------
actions = {1: "Start", 2: "Stop"}
print(actions.get(1, "Unknown action"))
#-----------------------------------
status_code = 404
match status_code:
    case 200: print("OK")
    case 404: print("Not Found")
    case 500: print("Server Error")
#-----------------------------------