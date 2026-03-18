import time
import random

player_alive = True
door_closed = False
vent_closed = False

animatronics = ["Lefty", "Scrap Baby", "Scraptrap", "Molten Freddy"]

def warning(anim):
    print(f"\n⚠ WARNING: {anim} is coming to the FRONT DOOR!")
    print("You have 3 seconds to react!")

    time.sleep(3)

    action = input("Type: door / vent / cam / audio : ")

    if action == "door":
        print("🚪 Front door closed!")
        return True

    elif action == "vent":
        print("🌀 Vent door closed!")
        return True

    elif action == "cam":
        print("📷 You check the cameras...")
        print(f"You see {anim} in the hallway!")

        lure = input("Play audio lure? (yes/no): ")

        if lure == "yes":
            print("🔊 Audio lure played. Animatronic walks away.")
            return True
        else:
            print(f"💀 {anim} enters the office!")
            return False

    elif action == "audio":
        print("🔊 You play an audio lure.")
        print(f"{anim} follows the sound away.")
        return True

    else:
        print(f"💀 {anim} attacks!")
        return False


print("🎮 Mini FNAF Pizzeria Simulator Night")
print("Watch the doors, vents, and cameras...\n")

while player_alive:

    time.sleep(2)

    event = random.choice(["attack", "nothing"])

    if event == "attack":
        anim = random.choice(animatronics)
        player_alive = warning(anim)

    else:
        print("👀 The office is quiet...")

print("\n☠ GAME OVER")