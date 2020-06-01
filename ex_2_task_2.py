# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, tooZipFile The class for reading and writing ZIP files.  See section 
# - when it comes to how to react to an error, your user MUST re-enter a string, b ut it's up to 
#   you how helpful you want to be
#   - you could just list all the rules on error and demand a correct email
#   - you could list the appropriate error message returned from you function and demand a correct email
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and will be laborious to test!
# - your function will return either True or a error code. When validating an input string with it
# - Note that the check for a valid email is a bit weird (b/c of my spec):
#   - if the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use
#   - in your flow control, if you want to do something fancy

# Once you're solved this, run some tests. Again, manually copy/paste the console output in a
# text file (results2.txt)

# solution

# import your function from the previous .py file as a module (you can abbreviate it)

# use ex_2_task_2 here instead once your function works!
from ex_2_task_1_solution import is_valid_email_address as is_valid 

gave_up = False
attempts_left = 3

# your code start
while True:
    email = input("email address?")
    r, err_str = is_valid(email)

    if r == None:
        print(email, "is valid!")
        break
    
    # error
    attempts_left -= 1

    # no attempts left - bail out 
    if attempts_left == 0:
        gave_up = True
        print("No attempts left, bailing out")
        break

    print(email, "is invalid!")
    print("Reason:", err_str)
    print(f"Try again, {attempts_left} attempts left")

# your code end
if not gave_up:
    print("valid email", email)
else:
    print("invalid email", email)