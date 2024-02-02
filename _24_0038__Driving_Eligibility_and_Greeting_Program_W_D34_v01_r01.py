# age: float
# name: str
# height: float
# is_human = bool

def police_to_verify_driving_eligibility(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive  # return it as an output

print(police_to_verify_driving_eligibility(12))
print(police_to_verify_driving_eligibility(19))

# We can actually use the output from this function just above here, to create a print statement:
if police_to_verify_driving_eligibility(19):
    print("You may pass.")
else:
    print("Pay a fine.")

#It would make things easier by declaring a type for a specific input.
# so instead of us accidentally doing this:
# if police_to_verify_driving_eligibility("twelve"):

# we can specify the type of data type for that input:
# def police_to_verify_driving_eligibility(age: int) -> :
#     if police_to_verify_driving_eligibility("twelve"):

def police_to_verify_driving_eligibility_strict(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive  # return a Bool as expected

def greeting(name: str) -> str:
    return "Hello " + name
