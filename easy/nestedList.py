# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# ------------SOLUTION-----------------------

if __name__ == '__main__':
    d={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name]=score
        
    y=list(d.values())
    x = min(y)
    try:
        while True:
            y.remove(x)
    except ValueError:
        pass
    second=min(y)
    keys = [k for k, v in d.items() if v == second]
    keys.sort()
    for i in range(0,len(keys)):
        print(keys[i])

  