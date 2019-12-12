import re

file = open("test2.txt", "r")
start_state = (file.readline()).strip().split('=')
start_state = start_state[1]
accept_states = (file.readline()).strip().split('=')
accept_states = accept_states[1].split(',')

# print("start", start_state)
# print("accept", accept_states)

string = input("Please enter a string: ")

obj = {}
arr = []
for lines in file:
    myList = list(filter(None, re.split(r'[=\:\->\n]', lines)))
    arr += [myList]
file.close()

listOfLambdas = []
for i in range(len(arr)):
    if ((arr[i][0], arr[i][1]) in obj):
        valList = []
        for j in range(i-1, len(arr)):
            if (len(arr[j]) == 3 and ((arr[j][0], arr[j][1]) in obj)):
                valList.append(arr[j][2])
        if (isinstance(obj[(arr[i][0], arr[i][1])], list) and (len(obj[(arr[i][0], arr[i][1])]) > 1)):
            break
        obj[(arr[i][0], arr[i][1])] = valList
    elif (len(arr[i]) == 3):
        obj[(arr[i][0], arr[i][1])] = [arr[i][2]]
    elif (len(arr[i]) == 2):
        if ((arr[i][0], 'lambda') in obj):
            listOfLambdas += [arr[i][1]]
            obj[(arr[i][0], 'lambda')] = listOfLambdas
        else:
            listOfLambdas += [arr[i][1]]
            obj[(arr[i][0], 'lambda')] = listOfLambdas

nfa = obj

# print(nfa)


def acceptNFA(string, start_state, accept_states, nfa):
    current_states = [start_state]
    exists = False
    # print(current_states)
    for letters in string:
        temp_list = []
        # print("nfa", nfa)
        # print("current state", current_states)
        for state in current_states:
            # print("state,letters", (state, letters))
            if not ((state, letters) in nfa):
                # print("not in here")
                exists = False
            else:
                # print("it's here")
                exists = True
        if not (exists):
            return False
        for state in current_states:
            # print("state", state)
            # print("letter", letters)
            if ((state, letters) in nfa):
                temp_list += nfa[(state, letters)]
                # print("temp", temp_list)
                current_states = temp_list
    #     print("curr states now", current_states)
    # print("accept", accept_states)
    # print("curr", current_states)
    for a_states in accept_states:
        for c_states in current_states:
            # print("c", c_states)
            # print("a", a_states)
            if c_states in accept_states:
                # print("True")
                return True
    return False


def checkLambda(transition, string, start_state, accept_states, nfa):
    if not ('lambda' in transition):
        return False
    print("lambda start", start_state)
    print("lambda accept", accept_states)
    print("lambda nfa", nfa)
    print("lambda transition", transition)
    print("check it", nfa[transition])
    temp_list = []
    for state in nfa[transition]:
        print("state", state)
        # print("nfa", nfa[(state, 'lambda')])
        # if (nfa[(state, 'lambda')]):
        #     print(checkLambda(string, state, accept_states, nfa))
        # print("check", nfa[(state, letters)])
        temp_list += nfa[transition]
        print("temp", temp_list)
        current_states = temp_list
    return current_states


if acceptNFA(string, start_state, accept_states, nfa):
    print('Accepted')
else:
    print('Rejected')
