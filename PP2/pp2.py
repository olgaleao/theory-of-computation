import sys

class Stack:
    def __init__(self):
        self.items = ['$']

    def pop(self):
        return self.items.pop()

    def push(self, newitem):
        self.items.append(newitem)

    def top(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == ['$']
    
def solve(st, line):
    line_empty = all(s == ' ' for s in line)
    if line_empty:
        return True

    for i in line:
        if i == '{' or i == '(' or i == '[':
            st.push(i)
        elif i == '}' and st.top() == '{':
            st.pop()
        elif i == ')' and st.top() == '(':
            st.pop()
        elif i == ']' and st.top() == '[':
            st.pop()
        elif i != ' ':
            return False

    return st.is_empty()

def main():
    full_line = ''
    for line in sys.stdin:
        line = line.splitlines()[0]
        if line == '':
            break
        st = Stack()
        full_line += line
        print(solve(st, line))
    print(solve(st, full_line))
    
if __name__ == '__main__':
    main()