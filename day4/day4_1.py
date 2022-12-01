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

from collections import Counter
import string

def main():
    sum_of_IDs = 0
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    filePath_Data = "slask.txt"#"day4.txt" # #"slask.txt"#
    #char_dict = dict.fromkeys(string.ascii_lowercase, 0)
    with open(filePath_Data) as f:
        all_lines = f.readlines()
        for line in all_lines:
            real_room = 0
            actual_chars = []
            line_list = line.split("[")
#            char_dict = dict.fromkeys(line_list[0], 0)
#            for letter in alphabeth:
#                for character in line_list[0]:
#                    if letter == character:
#                        char_dict[letter] += 1

            letters = Counter(line_list[0])
            temp = "".join(sorted(letters.keys()))
            answer_key = list(line_list[1])
            answer_key = answer_key[0:-2]

            for character in temp:#:letters.keys():
                if character in alphabeth:
                    actual_chars.append(character)
            #print actual_chars
            #print answer_key
            for i in range(0, len(answer_key)):
                if answer_key[i] == actual_chars[i]:
                    real_room = 1
                else:
                    real_room = 0
                    break

            temp = str(line_list[0])
            ID = ""
            for i in (-3, -2, -1):
                ID = ID + temp[i]
            ID = int(ID)
            print "ID: ",ID
            if real_room == 1:
                print "real ID: ", ID
                sum_of_IDs = sum_of_IDs + ID
            else:
                print "fake room: ", ID, "actual: ",actual_chars, "answer_key: ", answer_key
        print "sum: ",sum_of_IDs


if __name__ == '__main__':
    main()
