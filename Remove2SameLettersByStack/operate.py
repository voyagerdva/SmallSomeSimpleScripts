#######################################################################
#
#   hou to find all same letters in string and delete it from string
#   - finally string without paired letters should remain
#
#######################################################################

import A_stack as st

def removePairLetters(S):
    S1 = ""
    st.clear()
    
    for letter in S:
        if st.is_empty():
            st.push(letter)
            S1 = S1 + letter
        else:
            if letter == st.pop():
                S1 = S1[:-1]
                st.push(S1[-1:])
            else:
                st.push(letter)
                S1 = S1 + letter
    return S1
