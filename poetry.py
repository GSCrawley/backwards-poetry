
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

def lines_printed_numbered(lines_list):
    '''prints a numbered list'''
    for index, value in enumerate(lines_list, 1):
        print("{}. {}".format(index, value))

def lines_printed_backwards(lines_list):
    '''this function takes in a list of strings containing the lines of your poem as arguments and
    will print the poem lines out in reverse with the line numbers reversed'''
    #reverse the lines_list
    i= len(lines_list)
    lines_list.reverse()
    for line in lines_list:
        print(line)
        print(i)
        i = i-1
    print(line)

#use loop to print out items in lines_list

def lines_printed_random(lines_list):
    '''randomly select lines from a list of strings and print them out in random order'''
    import random
    for line in lines_list:
        random.shuffle(lines_list)
        print(line)

#get poem string into list of lines
lines_list = poem.split("\n")
lines_printed_numbered(lines_list)
print( )
print("BACKWARDS")
lines_printed_backwards(lines_list)
print( )
print("RANDOMIZED")
lines_printed_random(lines_list)
