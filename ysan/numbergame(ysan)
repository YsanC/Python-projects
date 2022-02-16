#(ysan method lol)
import random
choice1 = random.choice(range(21))

score_p = 0
score_ai = 0
round = 0
###START###
print("\nWelcome to the number game. You will play a game out of 5.")
print("The rules are simple, you have to guess the number the cpu choose")
print("You have a one out of twenty odds, good luck!")

###MIDDLE###
num = 5
for l in range(num):
  round = round + 1
  print("\nRound", round)
  game1 = int(input("\nPlease insert number 1-20: "))
  if game1 == choice1:
    print("\nNo way you guessed correctly lol, good job!")
    print("Maybe you should roll in genshin")
    score_p = score_p + 1
    print("\nThis is the current score")
    print("Player:", score_p)
    print("CPU:", score_ai)
  elif game1 != choice1:
    print("\nNice try you got it wrong tho hahaha")
    print("Maybe save your primos in genshin for next patch >:)")
    score_ai = score_ai + 1
    print("\nThis is the current score")
    print("Player:", score_p)
    print("CPU:", score_ai)

###END###
  if score_p == 5:
    print("Congrats, you won!")
    print("\nLive on rng king!")
    print("Player:", score_p)
    print("CPU:", score_ai)
    print("YOU WIN!")
  
  if score_ai == 5:
    print("Nice try you almost won (I hope)")
    print("\nBut maybe next time play when you feel luckier")
    print("Player:", score_p)
    print("CPU:", score_ai)
    print("CPU WINS")
