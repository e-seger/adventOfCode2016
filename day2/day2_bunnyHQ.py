#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      esekh3
#
# Created:     01-12-2016
# Copyright:   (c) esekh3 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    filePath_Data = "day2.txt" # #"slask.txt"#
    keypad = [[1, 2, 3],        # keypad[row][col]
              [4, 5, 6],
              [7, 8, 9]]

    keypad2 = [
                        ['1'],
                   ['2', '3', '4'],        # keypad2['row']['col']
              ['5', '6', '7', '8', '9'],
                   ['A', B', C'],
                       ['D']
              ]

    #keypad = keypad2

    row = 1
    col = 1
    print "start position: ",keypad[row][col]
    code = []
    path = []
    with open(filePath_Data) as f:
        all_lines = f.readlines()
        for line in all_lines:

            for cmd in range(0, len(line)):
                col_old = col
                row_old = row

                try:
                    if line[cmd] == "R":
                        col += 1
                    elif line[cmd] == "L":
                        col -= 1
                    elif line[cmd] == "U":
                        row -= 1
                    elif line[cmd] == "D":
                        row += 1
                    if col < 0:
                        col = 0
                    if row < 0:
                        row = 0
                    #print "ok: ",keypad[row][col]
                    path.append(keypad[row][col])

                except IndexError:
                    #print "error: ", keypad[row_old][col_old]
                    col = col_old
                    row = row_old
                    path.append(keypad[row][col])
                #print "cmd: ", line[cmd], "\tkey: ",keypad[row][col]

            code.append(keypad[row][col])
                #print "cmd: ", line[cmd], "\tkey: ",code
        print "code: ", code

if __name__ == '__main__':
    main()
