# Write your own Range function that take three parameters (start, stop and step) as an input
# and return the list of integer numbers.

def rangFunction(start,stop,step):
    result_list=[]
    if step>0:
        while start<stop:
            result_list.append(start)
            start+=step
    elif step<0:
        while start>stop:
            result_list.append(start)
            start+=step
    return result_list

num=rangFunction(1,10,2)
print( "The range function result is: ",num)