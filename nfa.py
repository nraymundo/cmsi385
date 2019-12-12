import re

# file = open("input.txt", "r")
file = open("test.txt", "r")
start_state = (file.readline()).strip().split('=')
start_state = start_state[1]
accept_states = (file.readline()).strip().split('=')
accept_states = accept_states[1].split(',')
# accept_states = map(lambda s: s.strip(), accept_states)
# start_state = list(filter(None, re.split(r'[=\n]', file.readline())))[1]
# accept_states = list(filter(None, re.split(r'[,\=\n]', file.readline())))
# if (len(accept_states) == 2):
#     accept_states = accept_states[1]
# elif (len(accept_states) == 3):
#     accept_states = accept_states[1:]

print("start", start_state)
print("accept", accept_states)

string = input("Please enter a string: ")

obj = {}
arr = []
for lines in file:
    myList = list(filter(None, re.split(r'[=\:\->\n]', lines)))
    arr += [myList]
file.close()

listOfLambdas = []
for i in range(len(arr)):
    # print("array:", arr)
    if ((arr[i][0], arr[i][1]) in obj):
        # print(i, "first if array", (arr[i][0], arr[i][1]))
        valList = []
        # print("array:", arr)
        for j in range(i-1, len(arr)):
            # print("arrays", arr[j])
            # print("prev arrays:", arr[j])
            # print("array here:", arr[i])
            if (len(arr[j]) == 3 and ((arr[j][0], arr[j][1]) in obj)):
                # print("tuple i", (arr[i][0], arr[i][1]))
                # print("tuple j", (arr[j][0], arr[j][1]))
                # print("obj", obj)
                # print(arr[j][2])
                valList.append(arr[j][2])
                # valList.append(arr[j][2])
                # print("valList:", valList)
        # obj[(arr[i][0], arr[i][1])] = valList
        # print("valList:", valList)
        # print("obj", obj[(arr[i][0], arr[i][1])])
        if (isinstance(obj[(arr[i][0], arr[i][1])], list) and (len(obj[(arr[i][0], arr[i][1])]) > 1)):
            break
        obj[(arr[i][0], arr[i][1])] = valList
        # print("valList2:", valList)
        # print("obj", obj[(arr[i][0], arr[i][1])])
    elif (len(arr[i]) == 3):
        # print(i, "second if array", (arr[i][0], arr[i][1]))
        obj[(arr[i][0], arr[i][1])] = [arr[i][2]]
        # print("obj", obj)
    elif (len(arr[i]) == 2):
        if ((arr[i][0], 'lambda') in obj):
            listOfLambdas += [arr[i][1]]
            obj[(arr[i][0], 'lambda')] = listOfLambdas
        else:
            listOfLambdas += [arr[i][1]]
            obj[(arr[i][0], 'lambda')] = listOfLambdas
        # print("obj", obj)

# print("obj", obj)

nfa = obj

print(nfa)


def acceptNFA(string, start_state, accept_states, nfa):
    current_states = [start_state]
    print(current_states)
    for letters in string:
        temp_list = []
        for state in current_states:
            print("state", state)
            print("letter", letters)
            if ((state, letters) in nfa):
                # print("check", nfa[(state, letters)])
                temp_list += nfa[(state, letters)]
                print("temp", temp_list)
                current_states = temp_list
    print("accept", accept_states)
    print("curr", current_states)
    for a_states in accept_states:
        for c_states in current_states:
            print("c", c_states)
            print("a", a_states)
            if c_states in accept_states:
                print("True")
                return True
    return False


    # def lambdaNFA(nfa, start_state, accept_states, string, i, max_length):
    #     for states in nfa:
    #         if ('lambda' in states):
    #             for current_state in nfa[states]:
    #                 if acceptNFA(nfa, current_state, accept_states, string, i, max_length):
    #                     return True
    #         return False
if acceptNFA(string, start_state, accept_states, nfa):
    print('Accepted')
else:
    print('Rejected')
