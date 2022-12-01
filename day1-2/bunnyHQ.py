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

    filePath_Data = "day1_1.txt"
    directions = ["N", "E", "S", "W"]
    current_direction = 0
    current_x_position = 0
    current_y_position = 0
    '''
    print directions[-4]
    for i in range(-20, 20):
        print "\noriginal i: ",i
        if (i > 3) or (i < -4):
            i = (i % 4)
        print "new i: ", i
        print directions[i]
    '''
    xy_pos = []
    with open(filePath_Data) as f:
        lines = f.read().strip().split(',')
        clean_lines = [l.strip() for l in lines if l.strip()]

        for cmd in clean_lines:
            if cmd[0] == "R":
                current_direction = current_direction + 1
            elif cmd[0] == "L":
                current_direction = current_direction - 1
            steps = int(cmd[1:])

            if (current_direction > 3) or (current_direction < -4):
                current_direction = (current_direction % 4)



            current_direction_nesw = directions[current_direction]

            if current_direction_nesw == "N":
                current_y_position = current_y_position + steps

            elif current_direction_nesw == "E":
                current_x_position = current_x_position + steps

            elif current_direction_nesw == "S":
                current_y_position = current_y_position - steps

            elif current_direction_nesw == "W":
                current_x_position = current_x_position - steps

            current_xy_pos = str(current_x_position) + "," + str(current_y_position)
            xy_pos.append(current_xy_pos)
        '''
            for xy in xy_pos:
                if current_xy_pos == xy:
                    print "found: ", current_xy_pos, "and: ", xy

        '''


        for xy in xy_pos:
            a = 0
            for xy2 in xy_pos:
                if xy == xy2:
                    a += 1
                    if a > 1:
                        print xy
        print set([x for x in xy_pos if xy_pos.count(x) > 1])
        print current_x_position
        print current_y_position
        print xy_pos



if __name__ == '__main__':
    main()
