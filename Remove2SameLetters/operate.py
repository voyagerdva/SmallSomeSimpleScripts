#######################################################################
#
#   hou to find all same letters in string and delete it from string
#   - finally string without paired letters should remain
#
#######################################################################

def find(S):
    i = 0
    while i < len(S) - 1:
        if S[i] == S[i + 1]:
            S1 = S[:i] + S[(i + 2):]
            S = S1
            i = -1
        i += 1
    print(f"output string = '{S}'")
    return S