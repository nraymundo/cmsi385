import re

# file = open("test.txt", "r")
file = open("input.txt", "r")
# file = open("test2.txt", "r")
start_state = (file.readline()).strip().split('=')
start_state = start_state[1]
accept_states = (file.readline()).strip().split('=')
accept_states = accept_states[1].split(',')

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


def acceptNFA(string, start_state, accept_states, nfa):
    current_states = [start_state]
    exists = False
    for letters in string:
        temp_list = []
        list_of_relations = []
        for state in current_states:
            if ((state, letters) in nfa):
                exists = True
                break
            elif ((state, 'lambda') in nfa):
                for transitions in nfa:
                    list_of_relations.append(transitions)
                for trans in list_of_relations:
                    if (trans[1] == letters):
                        exists = True
                        break
                    else:
                        exists = False
            else:
                exists = False
        if not (exists):
            return False
        for state in current_states:
            if ((state, letters) in nfa):
                temp_list += nfa[(state, letters)]
                current_states = temp_list
            elif ((state, 'lambda') in nfa):
                temp_list += nfa[(state, 'lambda')]
                current_states = temp_list
                temp_list = []
                for state in current_states:
                    if ((state, letters) in nfa):
                        temp_list += nfa[(state, letters)]
                        current_states = temp_list
    for a_states in accept_states:
        for c_states in current_states:
            if c_states in accept_states:
                return True
    return False


if acceptNFA(string, start_state, accept_states, nfa):
    print('Accepted')
else:
    print('Rejected')
