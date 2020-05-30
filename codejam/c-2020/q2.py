import sys
T = sys.stdin.readline()
def read_test_case():

    U = sys.stdin.readline()
    qr_pairs = []

    for _ in range(1000):
        pair = sys.stdin.readline().split()
        # Pair = (Q_i, R_i), Q_i = M_i for problem set 1-2
        pair = (int(pair[0]), pair[1])

        qr_pairs.append(pair)

    return(int(U), qr_pairs)


U, qr_pairs = read_test_case()
possible_range = 10**U
responses = {i:[] for i in range(1,possible_range+1)}

for query, res in qr_pairs:

    responses[query].append(res)


# prev_set = set(responses[possible_range])
# for i in range(possible_range - 1, 0, -1):

def get_n(responses, n, U, digits = [None for _ in range(10)]):

    possible = []
    for u in range(0, U+1):
        for i in range(n* (10**u), (n+1) * (10**u)):

            if u == U and i > 1:
                return possible
            
            # print(i)

            response_list = responses[i]
            for response in response_list:
                if response and len(response) == u+1 and response[0] not in set(digits):
                    possible.append(response[0])

    return possible



# def get_n(responses, n, digits = [None for _ in range(10)]):

#     possible = set()

#     for i in range(n, n+1):

#         response_list = responses[i]

#         for response in response_list:

#             if response not in set(digits):

#                 possible.add(response)
    
#     for i in range(n*10, (n+1) * 10):

#         response = responses[i]

#         for response in response_list:

#             if response and len(response) == 2 and response[0] not in set(digits):

#                 possible.add(response)
    
#     return possible

    
num_1 = get_n(responses, 1, U)


digits = [None for _ in range(10)]
if len(set(num_1)) == 1:
    digits[1] = num_1.pop()

print(num_1)

for i in range(2, 10):

    num_i = get_n(responses, i, U, digits)

    num_i = set(num_i)

    if len(num_i) == 1:
        digits[i] = num_i.pop()
    else:
        pass
    print(num_i)
    print(digits)





