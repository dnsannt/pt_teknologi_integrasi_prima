open_list = ["123", "{", "abcd", "[", "123", "(", "4"]
close_list = ["sss", "}", "bb", "]", "dd", ")", "5"]

# FUNCTION CHECK


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"


# TRUE
string = "123{abcd[123(45)dd]bb}sss"
print(string, "-", check(string))

# FALSE
string = "abcd(ex45{uuuu)000]ccc"
print(string, "-", check(string))
