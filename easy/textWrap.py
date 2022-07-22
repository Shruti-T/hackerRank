# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# -----------------------------SOLUTION------------------------------
import textwrap

def wrap(string, max_width):
    l=len(string)
    ans=""
    for i in range(0,l,max_width):
        ans+=string[i:i+max_width]+"\n"
    return ans.rstrip(ans[-1])

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result