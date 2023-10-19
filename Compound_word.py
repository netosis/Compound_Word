import time
#first we will read the test file and check what all can be done with it
start_time=time.time()
file=open("Input_02.txt",'r')

#now the words are collected in a list and sorted according to their length
file_data=sorted([i.replace('\n','') for i in file],key=len)
#A 'Set' data structure is used for better runtime while searching for the presence of words in the data
file_set=set(file_data)

#This is the function that will check wheather the given word is made up of multiple words present in the file or not
def checker(word,word_set):
    if len(word)==0: return True
    for i in range(1,len(word)+1):
        pre=word[:i]
        suff=word[i:]
        if pre in word_set and checker(suff,word_set):
            return True
    return False

largest=''
s_largest=''

for i in file_data:
    if checker(i,file_set):
        
        if len(largest)<len(i):
            s_largest=largest
            largest=i
        elif len(s_largest)<len(i):
            s_largest=i
        
print('Largest Word is "{}" with length of {} characters'.format(largest,len(largest)))
print('Second Largest Word is "{}" with length of {} characters'.format(s_largest,len(s_largest)))
end_time = time.time()
time_taken = end_time - start_time
print('The total time taken by the whole code to run is :-',time_taken)