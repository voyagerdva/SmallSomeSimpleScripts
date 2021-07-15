#######################################################################
#
#   hou to find all same letters in string and delete it from string
#   - finally string without paired letters should remain
#
#######################################################################

import A_stack as st

def removePairLetters(S):
    st.clear()

    for letter in S:
        if st.is_empty():
            st.push(letter)
        else:
            if letter == st.check():
                st.pop()
            else:
                st.push(letter)
    return st.show()
