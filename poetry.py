
poem = '''BE HERE NOW.
I find myself, In Time.
Yesterday consists of moments;
Now passed through
the realm of my experience
And which exist forever Now
Beyond my sphere of influence.
The future is decided Now,
Beginning chain reaction…
Tomorrow is this moment
Now, awaiting transformation…
All that ever is is Now,
This present circumstance…
Fleeting Yet eternal Now
Pregnant With Potential Now
The Culmination Of Every Moment Passed…
Now upon Now in a spiral dance,
Is all that I have ever been,
And all that I have yet to be,
All present Now, this moment…
Within Me.
Right Now.'''

def lines_printed_backwards(lines_list):
    '''this function takes in a list of strings containing the lines of your poem as arguments and
    will print the poem lines out in reverse with the line numbers reversed'''
    #reverse the lines_list
    lines_list.reverse()
#
# for lines in poem:
    print(lines_list)

    #TODO: use loop to print out items in lines_list
    pass

def lines_printed_random(lines_list):
    '''randomly select lines from a list of strings and print them out in random order'''
    import random
    random.shuffle(lines_list)
    print(lines_list)

def my_custom_function():
    '''does something of my choosing TODO: comment later'''


#testing code
#TODO: get poem string into list of lines
lines_list = poem.split("\n")
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
