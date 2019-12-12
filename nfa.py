import re

# file = open("input.txt", "r")
file = open("test.txt", "r")
start_state = list(filter(None, re.split(r'[=\n]', file.readline())))[1]
# print("start state:", start_state)
accept_states = list(filter(None, re.split(r'[,\=\n]', file.readline())))
if (len(accept_states) == 2):
    accept_states = accept_states[1]
elif (len(accept_states) == 3):
    accept_states = accept_states[1:]
# print("accept states:", accept_states)

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

# for i in range(len(arr)):
#     if (arr[i][0] in obj and not (len(arr[i]) == 2)):
#         # print(arr[i])
#         valList = []
#         for i in range(len(arr)):
#             if (len(arr[i]) == 3):
#                 valList.append([arr[i][2]])
#         obj2 = {}
#         obj2[arr[i][1]] = valList
#         # print("obj2", obj2)
#         obj[arr[i][0]] = obj2
#         # print("obj", obj)
#     elif (len(arr[i]) == 3):
#         # print(arr[i])
#         obj2 = {}
#         obj2[arr[i][1]] = [arr[i][2]]
#         obj[arr[i][0]] = obj2
#         # print("obj", obj)
#     elif (len(arr[i]) == 2):
#         # print(arr[i])
#         obj2 = {}
#         obj2['lambda'] = [arr[i][1]]
#         obj[arr[i][0]] = obj2
#         # print("obj", obj)

# nfa = {'q0':
#        {'0': ['q1'],
#         'lambda': ['q1']
#         },
#        'q1':
#        {'0': ['q0', 'q2'],
#         '1': ['q1', 'q2']
#         },
#        'q2':
#        {'0': ['q2'],
#         '1': ['q1']
#         }
#        }

# nfa = {
#       ('q0', 'a'): ['q1', 'q2', 'q0'],
#       ('q0', 'lambda'): 'q2'
# }


def accept(nfa, start_state, accept_states, string):
    k = 0
    for states in nfa:
        if ('lambda' in states):
            k = k + len(nfa[states])

    max_length = k + (1 + k)*len(string)
    return acceptNFA(nfa, start_state, accept_states, string, 0, max_length)

# def accept(nfa, start, ends, string):
#     k = 0
#     for states in nfa:
#         if ('lamda' in nfa[states]):
#             k = k + len(nfa[states]['lamda'])

#     max_length = k + (1 + k)*len(string)
#     return acceptNFA(nfa, 'q0', ['q1'], string, 0, 0, max_length)
# I don't get why it returns ['q1'] and not just 'q1'

# q0: start state, q1: final state(s)

# {
# ('q0', '0'): ['q0'],
# ('q0', '1'): ['q1'],
# ('q1', '0'): ['q2'],
# ('q1', '1'): ['q0'],
# ('q2', '0'): ['q1'],
# ('q2', '1'): ['q2']
# }


def acceptNFA(nfa, start_state, accept_states, string, i, max_length):
    if (i >= len(string)):
        if (start_state in accept_states):
            return True
        else:
            return False
        if lambdaNFA(nfa, start_state, accept_states, string, i, max_length):
            return True
    nextStates = start_state
    for transitions in nfa:
        if (string[i] in transitions and start_state in transitions):
            nextStates = nfa[transitions]
            break
        elif lambdaNFA(nfa, start_state, accept_states, string, i, max_length):
            return True
    print(nextStates)
    for next in nextStates:
        if acceptNFA(nfa, next, accept_states, string, i+1, max_length):
            return True
        if lambdaNFA(nfa, start_state, accept_states, string, i, max_length):
            return True
    return False


def lambdaNFA(nfa, start_state, accept_states, string, i, max_length):
    for states in nfa:
        if ('lambda' in states):
            for current_state in nfa[states]:
                if acceptNFA(nfa, current_state, accept_states, string, i, max_length):
                    return True
        return False

    # if ('lamda' in nfa[start_state]):
    #     for curr in nfa[start_state]['lamda']:
    #         if acceptNFA(nfa, curr, accept_states, string, i, max_length):
    #             return True
    # return False


# def lambdaNFA(nfa, start, ends, string, i, edges, max_length):
#     if ('lamda' in nfa[start]):
#         for curr in nfa[start]['lamda']:
#             if acceptNFA(nfa, curr, ends, string, i, edges+1, max_length):
#                 return True
#     return False


if accept(nfa, start_state, accept_states, string):
    print('Accepted')
else:
    print('Rejected')


# def acceptNFA(nfa, start_state, accept_states, string, i, edges, max_length):
#     nextStates = start_state
#     print("i", i)
#     if (edges > max_length and string != ''):
#         return False
#     if (i >= len(string)):
#         if (nextStates in accept_states):
#             print("whattup")
#             return True
#         else:
#             print("bro")
#             return False
#         # if lambdaNFA(nfa, start_state, accept_states, string, i, edges+1, max_length):
#         #     return True
#     for transitions in nfa:
#         print("transitions", transitions)
#         print("string[i]", string[i])
#         if (string[i] in transitions and nextStates in transitions):
#             # print("transitions", transitions)
#             # print("nfa[transitions]", nfa[transitions])
#             nextStates = nfa[transitions]
#             print("nextStates", nextStates)
#             break
#         # elif lambdaNFA(nfa, start_state, accept_states, string, i, edges, max_length):
#         #     return True
#         # else:
#         #     return False
#     for next in nextStates:
#         print("next", next)
#         if acceptNFA(nfa, next, accept_states, string, i+1, edges+1, max_length):
#             return True
#     # if lambdaNFA(nfa, start_state, accept_states, string, i, edges, max_length):
#     #     return True
#     return False
