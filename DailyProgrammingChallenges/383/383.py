#!/usr/bin/python

def same_necklace( a, b ):
    result = necklace_test(a, b)
    print("String a: " + a + " String b: " + b + " Result: " + str(result))

def necklace_test( a, b ):
    if ( len(a) != len(b) ):
        return False
    if ( a == b ):
        return True
    if ( len(a) == 1 ):
        return False;
    for index in range( 1, len(a) ):
        a = a[1:] + a[0]
        if ( a == b ):
            return True
    return False

# Now you can call the function
print("Main challenge #383 results:")
same_necklace("nicole", "icolen") #=> true
same_necklace("nicole", "lenico") #=> true
same_necklace("nicole", "coneli") #=> false
same_necklace("aabaaaaabaab", "aabaabaabaaa") #=> true
same_necklace("abc", "cba") #=> false
same_necklace("xxyyy", "xxxyy") #=> false
same_necklace("xyxxz", "xxyxz") #=> false
same_necklace("x", "x") #=> true
same_necklace("x", "y") #=> false
same_necklace("xy", "yx") #=> true
same_necklace("x", "xx") #=> false
same_necklace("x", "") #=> false
same_necklace("", "") #=> true


#Bonus 1:

def repeats( a ):
    input = "String a: " + a
    b = a
    total = 1
    if ( len(a) == 0 or len(a) == 1 ):
        print(input + " Result: ", total)
        return 1
    for index in range( 1, len(a) ):
        a = a[1:] + a[0]
        if ( a == b ):
            total = total + 1
    print(input + " Result: ", total)
    return total

# Now you can call the function
print()
print("Bonus 1 challenge #383 results:")
repeats("abc") #=> 1
repeats("abcabcabc") #=> 3
repeats("abcabcabcx") #=> 1
repeats("aaaaaa") #=> 6
repeats("a") #=> 1
repeats("") #=> 1


#Bonus 2:

def search( group ):
    while ( len(group) >= 4 ):
        #print("Checking " + group[0])
        matches = [group[0]]
        total = 1
        for index in range( 1, len(group) ):
            if ( necklace_test(group[0], group[index]) ):
                matches.append(group[index])
                total = total + 1
        if ( total == 4 ):
            return matches
        else:
            group.pop(0)
    return False

#[https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt]
print()
print("Bonus 2 challenge #383 results:")
text_file = open("enable1.txt", "r")
lines_with_newline = text_file.readlines()
lines = [x[:-1] for x in lines_with_newline]
matches = False
words_dict = {}
for word in lines:
    if ( len(word) >= 4 ):
        if ( not len(word) in words_dict ):
            words_dict[len(word)] = []
        words_dict[len(word)].append(word)
for index in range(4, len(words_dict)):
    #print("Checking words with ", index, " letters.")
    if ( index in words_dict ):
        matches = search(words_dict[index])
        if ( matches ):
            print(matches)
            break
