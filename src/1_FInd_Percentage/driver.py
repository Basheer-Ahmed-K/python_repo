from util import findPercentage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
ans = findPercentage(student_marks[query_name])
print(ans)
