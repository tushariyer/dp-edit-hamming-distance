# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:44:43 2016

CS 290 Homework 2 - Dynamic Programming Problems

@author: tushariyer
"""
import datetime as d

def main():
    m1 = "\n\nThis project uses two int lists called s1 and s2.\nThe script will print out the answer to the question along with the time taken to complete it (in seconds).\nWe can use this to see how each change for edit distance affects the runtime complexity.\nS1 & S2 are as follows:\n\n"    
    print m1    
    
    #defining the lists
    s1 = [1,2,3,4,5,6,7,8,9,0]
    print s1
    s2 = [1,1,2,3,3,4,6,43,3,4,5,3,24,5,6,7,8,9,0]
    print s2
    
    #Print out question 1
    print "\nQuestion 1 - Hamming Distance:"
    t1 = d.datetime.now();
    print hammingDistance(s1, s2) #run method
    print (d.datetime.now() - t1).total_seconds() #time taken
    
    #Print out question 2
    print "\nQuestion 2 - Edit Distance:"
    t2 = d.datetime.now();
    print editDistance(s1, s2) #run method
    print (d.datetime.now() - t2).total_seconds() #time taken
    
    #Print out question 3
    print "\nQuestion 3 - Edit Distance with Backpointers:"
    t3 = d.datetime.now();
    print editPointBack(s1, s2) #run method
    print (d.datetime.now() - t3).total_seconds() #time taken
    
    #Print out question 4
    print "\nQuestion 4 - Edit Distance in O(m):"
    t4 = d.datetime.now();
    print editDistLen(s1, s2) #run method
    print (d.datetime.now() - t4).total_seconds() #time taken
    
    m2 = "\n\nWe can see from this how using backpointers improves the runtime of edit distance.\nRunning it in O(m) improved it further."
    print m2
    
#Hamming Distance - Problem 1
def hammingDistance(s1, s2):
    #test that they have values
    if len(s1) == 0: return len(s2)
    if len(s2) == 0: return len(s1)
        
    #Convert the int lists to strings
    str1 = ''.join(str(e) for e in s1)
    str2 = ''.join(str(e) for e in s2)
        
    #Counter set at zero
    hamDist = 0
    
    
    for i in xrange(0, len(str1)):
        #If the values at the specified index aren't equal
        if str1[i] != str2[i]:
            #increment
            hamDist += 1
            
    #Return the total count.
    return hamDist

#Edit Distance - Problem 2
def editDistance(s1, s2, memo=None):
    #initialise memory
    if memo is None: memo = {}
    
    #test that they have values
    if len(s1) == 0: return len(s2)
    if len(s2) == 0: return len(s1)
    
    #if the lengths are aready in memory, return it
    if (len(s1), len(s2)) in memo:
        return memo[(len(s1), len(s2))]
        
    #use recursion to break the strings into smaller cross-sectinos
    delt = 1 if s1[-1] != s2[-1] else 0
    #diagonals
    cross = editDistance(s1[:-1], s2[:-1], memo) + delt
    #verticals 
    tall = editDistance(s1[:-1], s2, memo) + 1
    #horizontal
    flat = editDistance(s1, s2[:-1], memo) + 1
    #concatenation of answer
    ans = min(cross, tall, flat)
    
    #equate the variables to the answer
    memo[(len(s1), len(s2))] = ans
    
    #return answer
    return ans

#Edit Distance with Backpointers - Problem 3
def editPointBack(s1, s2):
    #convert int lists to strings
    str1 = ''.join(str(e) for e in s1)
    str2 = ''.join(str(e) for e in s2)
    
    #two variables which store the length of the strings
    m = len(str1)
    n = len(str2)

    # Create a table to store results
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Complete d[][] from the bottom-upwards
    for i in range(m+1):
        for j in range(n+1):
 
            #If first is empty, insert all of second
            if i == 0:
                dp[i][j] = j
 
            #If second is empty, delete all from second
            elif j == 0:
                dp[i][j] = i
 
            #If last values match, return the substring without them.
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            #Consider all combinations
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   #insertion
                                   dp[i-1][j],   #deletion
                                   dp[i-1][j-1]) #substitution
 
    #return answer
    return ((dp[m][n]) - 2)

#Edit Distance with O(len(s2)) - Problem 4
def editDistLen(s1, s2):
    #If s1 is shorter, switch the lists and restart
    if len(s1) < len(s2):
        return editDistLen(s2, s1)

    #if s1 is greater or equal to s2
    if len(s2) == 0:
        return len(s1)

    #length of the previous row
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        #add one for current row
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            #j+1 because the row is greater than s2 by 1
            insertions = previous_row[j + 1] + 1            #insertion
            deletions = current_row[j] + 1                  #deletions
            substitutions = previous_row[j] + (c1 != c2)    #substitutions
            current_row.append(min(insertions, deletions, substitutions))
            
        #the previous row is now the current row
        previous_row = current_row
    
    #return answer
    return previous_row[-1]

#Use the main method to begin.
if __name__ == '__main__':
    main()
