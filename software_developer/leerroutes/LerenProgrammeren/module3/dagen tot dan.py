dagen_van_week = ("ma", "di", "wo", "do", "vr", "za", "zo")

dag_stoppen = input("welke dag wil je stoppen?")

for dag in dagen_van_week:
   print(dag)
   if dag == dag_stoppen:
      break