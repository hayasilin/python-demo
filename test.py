# import sys

# line = sys.stdin.readline()

# def permuta(line, step = 0):
#   if step == len(line):
#     print(line)
#   else:
#     for i in range(step, len(line)):
#       string_c = [c for c in line]
#       string_c[step], string_c[i]= string_c[i], string_c[step]
#       permuta(string_c, step + 1)



def permutate(line, step = 0):
    if step == len(line):
        print('result')
        print(line)
    else:
        for i in range(len(line)):
            string_c = [c for c in line]
            print('string_c')
            print(string_c)
            string_c[step], string_c[i]= string_c[i], string_c[step]
            permutate(string_c, step + 1)


if __name__ == '__main__':
    line = ["a","b","c"]
    print(permutate(line))