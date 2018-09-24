# Inputs with try-catch block
while True:
    try:
        end = int(input("How many seconds on the road? (s): "))
        acc = int(input("What's the car's acceleration? (ms-2): "))
        dist = int(input("How far is the person going? (m): "))
        break
    except ValueError:
        print("Do you not understand integers? Try again")

# set variables
stars = 0
limit = 60
time = 0

# functions
def distance(a,t):
    return int(0.5*a*(t**2))

def finalSpeed(a,t):
    return int(a*t)

#Distance loop
while time <= end:
    stars = (distance(acc,time)/10)
    print("Duration:"+str(time)+" Distance:"+"*"*int(stars))
    time += 1

# Max Speed if
if finalSpeed(acc,end) > 60:
    print("The person went over the speed limit (Max speed was "+str(finalSpeed(acc,end))+" m/s)")
else:
    print("The person did not go over the speed limit (Max speed was "+str(finalSpeed(acc,end))+" m/s)")

# Distance reached
if distance(acc,end) >= dist:
    print("The person reached the destination (Reached "+str(distance(acc,end))+" m)")
else:
    print("The person did not reach the destination (Reached "+str(distance(acc,end))+" m)")
