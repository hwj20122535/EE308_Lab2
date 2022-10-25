import re
filename=input("Please input the name of the file: ")
level=int(input("Please input the completion level: "))
def get_text():

    file = open(filename, "r", encoding="UTF-8")  #Ensure normal opening
    text = file.read()      #read file
    for i in '!#$%&()+,-.:;<=>?@[\\]^_{|}~':  # Remove the punctuation
        text = text.replace(i, " ")
    file.close()
    return text



def words_filter():
    text = get_text().replace("else if", "elseif")    # replace else if with elseif
    wordlist = text.split()
    return wordlist


words = words_filter()
fWords = []
counts1 = {}
keyWords = ["auto", "break", "case", "char", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return",
            "short", "signed", "sizeof", "static", "struct",
            "switch", "typedef", "union", "unsigned",
            "void", "volatile", "while", "elseif"]

def first_question():  # Number of output keywords.
    cnt = 0
    for word in words:
        if len(word) == 1 or (word not in keyWords):
            continue
        counts1[word] = counts1.get(word, 0) + 1
        fWords.append(word)
        cnt = cnt + 1
    cnt = cnt + counts1.get("elseif", 0)
    print("total num: {}".format(cnt))
    return cnt


def second_question(counts):
    num = counts.get("switch", 0)
    print("switch num: {}".format(num))
    if num == 0:
        print("case num: {}".format(num))
        return
    list2 = []
    flag = -1
    for word in words:
        if word == "switch":
            list2.append(0)
            flag += 1
        elif word == "case":
            list2[flag] += 1
        else:
            continue
    print("case num: ", end="")
    print(" ".join(str(x) for x in list2))
    return list2


def third_question():
    list3 = []
    num_if_else = 0
    for word in fWords:
        if word == "if":
            list3.append(word)
        elif word == "elseif" and list3[-1] != "elseif":
            list3.append(word)
        elif word == "else":
            if list3[-1] == "if":
                list3.pop()
                num_if_else += 1
    print("if-else num: {}".format(num_if_else))
    return  num_if_else

def fourth_question():
    list4 = []
    num_if_elseif_else = 0
    for word in fWords:
        if word == "if":
            list4.append(word)
        elif word == "elseif" and list4[-1] != "elseif":
            list4.append(word)
        elif word == "else":
            if list4[-1] == "elseif":
                list4.pop()
                list4.pop()
                num_if_elseif_else += 1
    print("if-elseif-else num: {}".format(num_if_elseif_else))
    return num_if_elseif_else

def solve():
        if level == 1:
            first_question()
        elif level == 2:
            first_question()
            second_question(counts1)
        elif level == 3:
            first_question()
            second_question(counts1)
            third_question()
        elif level == 4:
            first_question()
            second_question(counts1)
            third_question()
            fourth_question()
        return counts1
solve()