import sys

sys.stdin = open("input.in", "r")
sys.stdout = open("output.out", "w")

num_people, num_pets = map(int, input().split())

PeoplePref = []
PetsPref = []

for person in range(num_people):
  person_pref = list(map(int, input().split()))
  PeoplePref.append(person_pref)

for pet in range(num_pets): 
  pet_pref = list(map(int, input().split()))
  PetsPref.append(pet_pref)


FreePeople = list(range(num_people))
Current = [None] * num_pets
Next = [0] * num_people

while FreePeople:
  p = FreePeople[-1]
  t = PeoplePref[p][Next[p]]
  
  if Current[t] == None:
    Current[t] = p
    FreePeople.remove(p)

  else:
    p_prime = Current[t]
    if PetsPref[t].index(p) < PetsPref[t].index(p_prime):
      Current[t] = p
      FreePeople.remove(p)
      FreePeople.append(p_prime)

  Next[p] += 1

print(Current)
