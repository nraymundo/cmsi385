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

for i in range(len(arr)):
    if ((arr[i][0], arr[i][1]) in obj):
        # print("first if array", (arr[i][0], arr[i][1]))
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
        if isinstance(obj[(arr[i][0], arr[i][1])], list):
            break
        obj[(arr[i][0], arr[i][1])] = valList
    elif (len(arr[i]) == 3):
        # print("second if array", (arr[i][0], arr[i][1]))
        obj[(arr[i][0], arr[i][1])] = [arr[i][2]]
        # print("obj", obj)
    elif (len(arr[i]) == 2):
        # print("third if array", (arr[i][0], arr[i][1]))
        obj[(arr[i][0], 'lambda')] = [arr[i][1]]
        # print("obj", obj)

# print("obj", obj)

nfa = obj

# print(nfa)

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
    return acceptNFA(nfa, start_state, accept_states, string, 0, 0, max_length)

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


def acceptNFA(nfa, start_state, accept_states, string, i, edges, max_length):
    nextStates = start_state
    # print("i", i)
    if (i >= len(string)):
        # print("hi")
        if (start_state in accept_states):
            return True
        return False
    for transitions in nfa:
        # print(transitions)
        # print(string[i])
        if (string[i] in transitions and nextStates in transitions):
            # print("transitions", transitions)
            # print("nfa[transitions]", nfa[transitions])
            nextStates = nfa[transitions]
            # print("nextStates", nextStates)
            break
        # else:
        #     return False
    for next in nextStates:
        if acceptNFA(nfa, next, accept_states, string, i+1, edges+1, max_length):
            return True
    return False

    # if (edges > max_length and string != ''):
    #     return False
    # if (i >= len(string)):
    #     if (start_state in accept_states):
    #         return True
    #     if lambdaNFA(nfa, start_state, accept_states, string, i, edges+1, max_length):
    #         return True
    #     return False
    # if (string[i] in )

    # if (string[i] in nfa[start_state]):
    #     nextStates = nfa[start_state][string[i]]
    # elif lambdaNFA(nfa, start_state, accept_states, string, i, edges, max_length):
    #     return True
    # else:
    #     return False
    # for curr in nextStates:
    #     if acceptNFA(nfa, curr, accept_states, string, i+1, edges+1, max_length):
    #         return True
    # if lambdaNFA(nfa, start_state, accept_states, string, i, edges, max_length):
    #     return True
    # return False

# def acceptNFA(nfa, start, ends, string, i, edges, max_length):
#     if (edges > max_length and string != ''):
#         return False
#     if (i >= len(string)):
#         if (start in ends):
#             return True
#         if lamdaNFA(nfa, start, ends, string, i, edges+1, max_length):
#             return True
#         return False
#     if (string[i] in nfa[start]):
#         nextStates = nfa[start][string[i]]
#     elif lamdaNFA(nfa, start, ends, string, i, edges, max_length):
#         return True
#     else:
#         return False
#     for curr in nextStates:
#         if acceptNFA(nfa, curr, ends, string, i+1, edges+1, max_length):
#             return True
#     if lamdaNFA(nfa, start, ends, string, i, edges, max_length):
#         return True
#     return False


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
