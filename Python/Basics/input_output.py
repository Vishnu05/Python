
# for getting standard input we can use input functions
# by default all the values entered in the input is string have to make explicty typecast to change
# the datatype

a = input('Enter you value : ')

if a.isdigit:
   # print('the input you provided is a number : ' + str(tyep(a)))
   print('hi')
else:
    print('that is a non number')

print('type of input' + str(type(a)))
print('The entered value is ' + str(a))

# import 

# if __name__ == '__main__':
#     n = int(raw_input())
#     student_marks = {}
#     for _ in range(n):
#         line = raw_input().split()
#         name, scores = line[0], line[1:]
#         scores = map(float, scores)
#         student_marks[name] = scores
#     query_name = raw_input()


#     raw_input()

# input, gettling all the values in single line 

line_input = input("Enter the values in a single line").split()

print('line input is ', line_input)

val = dict()
# val[line_input[0]] = 