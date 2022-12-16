dagen_van_week = ("ma", "di", "wo", "do", "vr", "za", "zo")

dag_stoppen = input("welke dag wil je stoppen?")
i = 0

while dag_stoppen != dagen_van_week[i]:
    print(dagen_van_week[i])
    i += 1
print(dag_stoppen)