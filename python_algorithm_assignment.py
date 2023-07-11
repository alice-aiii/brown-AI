# task 1: convert hours to minutes
hr = int(input("enter number of hours: "))
def hr_to_min(h):
    return str(h*60)
print(str(hr) + " hour(s) equal " + hr_to_min(hr) + " minute(s).")

# task 2: convert hours to minutes OR minutes to hours
def min_to_hr(min):
    return str(min/60)
# determine if the user wants to convert from hr to min, or min to hr
h_or_min = input("type hm for converting hours to minutes, type mh for converting minutes to hours: ")
if (h_or_min == "hm"):
    hour_time = int(input("enter number of hours: "))
    print(str(hour_time) + " hour(s) equal " + hr_to_min(hour_time) + " minute(s).")
if (h_or_min == "mh"):
    minute_time = int(input("enter number of minutes: "))
    print(str(minute_time) + " minute(s) equal " + min_to_hr(minute_time) + "hour(s).")

# task 3: count number of letters in a word
word = input("word: ")
print(str(word) + " has " + str(len(word)) + " letter(s).")