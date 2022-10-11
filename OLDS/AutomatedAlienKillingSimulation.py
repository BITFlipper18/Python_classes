import random
import time

#Red aliens +2 lives
#Green alien +1 lives
#Yellow alien -2 lives
#If lives go to 0, you die

redAlien = +1
greenAlien = +2
yellowAlien = -2
totalLives = 3
#TODO A formula to not allow totalLives-counter to be less then 0 (no negatives)

Aliens = ('greenAlien', 'redAlien', 'yellowAlien')
alien_color = random.choice(Aliens)

print(f"\nYou are about to enter an automated Alien-killing simulation! The rules are:")
time.sleep(3)
print(f"1) You start with {totalLives} lives.")
time.sleep(2)
print(f"2) Killing a redAlien gives you {redAlien} life.")
time.sleep(2)
print(f"3) Killing a greenAlien gives you {greenAlien} lives.")
time.sleep(2)
print(f"4) Killing a yellowAlien takes you {yellowAlien} lives.")
time.sleep(2)
print(f"5) If you end up with 0 lives, you DIE!!!\n\n")
time.sleep(4)

while totalLives > 0:
    print("An Alien is approaching .. you are fReAkIn out! And you SHOOT! .. It looks pretty dead to me!")
    targetedAlien = random.choice(Aliens)
    time.sleep(1)
    print("You approach the dead Alien .. and .. ")
    time.sleep(2)
    print(f"It is a {targetedAlien}!\n")
    time.sleep(1)
    if targetedAlien == "redAlien":
        print(f"Well done! A redAlien offers you {redAlien} life!\n")
        totalLives += (redAlien)
        time.sleep(1)
        print(f"You now have {totalLives} lives!")
        time.sleep(1)
        print("OK, now let's head to home. You look pretty freaked-out!\n")
        time.sleep(1)
        print("But wait!\n")
        time.sleep(2)

    elif targetedAlien == "greenAlien":
        print(f"Well done! A greenAlien offers you {greenAlien} life!\n")
        totalLives += (greenAlien)
        time.sleep(1)
        print(f"You now have {totalLives} lives!")
        time.sleep(1)
        print("OK, now let's head to home. You look pretty freaked-out!\n")
        time.sleep(1)
        print("But wait!\n")
        time.sleep(2)

    elif targetedAlien == "yellowAlien":
        print(f"Ohhh nooo! A yellowAlien costs you {yellowAlien} lives!\n")
        totalLives += (yellowAlien)
        time.sleep(1)
        print(f"You now have {totalLives} lives!")
        time.sleep(1)

        if totalLives < 1:
            print("and ... You are DEAD!!")
            break
        else:
            print("OK, now let's head to home. You look pretty freaked-out!\n")
            time.sleep(1)
            print("But wait!\n")
            time.sleep(2)




