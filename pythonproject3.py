#By Brandon2023

import random

tries = int("4")
score = int("0")
cpu_score = int("0")

#rando reqiurements
pp = [69, 10]

selection = input("\nplease select: Easy / Medium / Pain: ")
print("\nWell if you choose pain you baccially have a 1 in 999999998 chance of winning against the CPU")
print("\nRules:")
print("You must guess the correct number from the ranges stated, if you get it wrong -1 lives will be gone and score will be deducted, if you get it right then +1 to your score")
print("\nYou have a total of 5 rounds")

while tries >= 0:
  if selection == ("Easy") or selection == ("easy"):
      easy_random = random.choice(range(11))
      potato = int(input("\nInsert number from 0 to 10: "))
      if potato == easy_random:
        print("\nwow u win good job")
        score = score + 1
        tries = tries - 1
        print("\nYour score is: " + str(score))
        print("\nNext round starting goood luck!")
      elif potato != easy_random:
        tries = tries - 1
        scoure = score - 1
        cpu_score = cpu_score + 1
        print("\nur wrong")
        print("\nNext round starting goood luck!")

  if selection == ("Medium") or selection == ("medium"):
      medium_random = random.choice(range(51))
      apple = int(input("\nInsert number from 0 to 50: "))
      if apple == medium_random:
        print("\nwow u win good job")
        score = score + 1
        tries = tries - 1
        print("\nYour score is: " + str(score))
        print("\nNext round starting goood luck!")
      elif apple != medium_random:
        tries = tries - 1
        scoure = score - 1
        cpu_score = cpu_score + 1
        print("\nur wrong")
        print("\nNext round starting goood luck!")

  if selection == ("Pain") or selection == ("pain"):
      pain_random = random.choice(range(51))
      coconut = int(input("\nInsert number from 0 to 50: "))
      if coconut == pain_random:
        print("\nwow u win good job")
        score = score + 1
        tries = tries - 1
        print("\nYour score is: " + str(score))
        print("\nNext round starting goood luck!")
      elif coconut != pain_random:
        tries = tries - 1
        scoure = score - 1
        cpu_score = cpu_score + 1
        print("\nur wrong")
        print("\nNext round starting goood luck!")

  if tries == -1:
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\njk game over")
    print("\nYour score is: " + str(score))
    print("\nCPU score is: " + str(cpu_score))
    if score >= cpu_score:
      print("\nPlayer has won!")
    else:
      print("\nCPU has won!")