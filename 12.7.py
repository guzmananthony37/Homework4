#Anthony Guzman       CIS2348          12.7		1503239
def get_age():
    age = int(input())
    if age<18 or age >75:
        raise ValueError("Invalid age.")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate=220-age #calculate 70% of 220 minus age
    heart_rate*=0.7
    return heart_rate

if __name__ == "__main__":
    try:
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
        age = get_age()
        rate=fat_burning_heart_rate(age) #call method to calculate heart rate
        print("Fat burning heart rate for a",age,"year-old: ",end="") #print result
        print(rate,"bpm")
    except ValueError as excpt: #If exception occurs, handle them with printing message on console
        print(excpt)
        print("Could not calculate heart rate info.\n")