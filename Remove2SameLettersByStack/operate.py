#######################################################################
#
#   hou to find all same letters in string and delete it from string
#   - finally string without paired letters should remain
#
#######################################################################

import A_stack as st

def find(S):
    S1 = ""
    st.clear()
    
    for letter in S:
        if st.is_empty():
            st.push(letter)
            S1 = S1 + letter
            continue
        else:
            if letter == st.pop():
                S1 = S1[:-1]
                st.push(S1[-1:])
                continue
            else:
                st.push(letter)
                S1 = S1 + letter
    return S1
      
S_new = find(S1)
print(f"Новая строка получилась '{S_new}'")
