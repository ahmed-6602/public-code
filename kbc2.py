n = int(input())
student_marks ={}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = 'scores'
    output = []
for i in student_marks[name]:
        output +=[scores]
        result = sum(output)/len(output)
        print(result)
