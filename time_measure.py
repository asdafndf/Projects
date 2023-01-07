#MEASURE EXECUTION TIME


#execution time of a single line of code:
#r: number of runs (optional)
#n: number of loops (optional)
%timeit -r5 -n10 [x for x in range(1000000)]


#execution time of multiple lines of code:
# %%timeit has to be the first line in the cell, otherwise UsageError
%%timeit -r5 -n10
sum_x = 0
for i in range(1000000):
    sum_x += i


#execution time of a function:
import timeit
def addition():
    print('Addition:', sum(range(1000000)))
#number of times to run the code
n = 5
#calculate total execution time
result = timeit.timeit(stmt='addition()', globals=globals(), number=n)
#get the average execution time
print(f"Execution time is {result / n} seconds")


#measure the CPU execution time:
#to measure execution time (Wall time) use time.time() instead
import time
start_time = time.process_time()
sum_x = 0
for i in range(1000000):
    sum_x += i
# wait for 3 seconds
time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)
end_time = time.process_time()
total_time = end_time - start_time
print(f'CPU Execution time: {total_time} seconds')


