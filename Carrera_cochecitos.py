import random
import time
import os

def start_race():
    print("Semaforo: Rojo 🔴 ")
    time.sleep(2)
    print("Semaforo: Amarillo 🟡 ")
    time.sleep(2)
    print("Semaforo: Verde 🟢 ")
    time.sleep(2)

def race(track_length: int):
    start_race()
    
    track1,track2, track3 = create_tracks(track_length)
    
    print_race(track1, track2, track3)
    
    position1, position2, position3 = len(track1) - 1, len(track2) - 1, len(track3) - 1
    
    crash1, crash2, crash3 = False, False, False
    
    while position1 > 0 and position2 > 0 and position3 > 0:
        
        time.sleep(1)
        
        track1[position1] = "_"
        track2[position2] = "_"
        track3[position3] = "_"
        
        position1 -= 0 if crash1 else random.randint(1, 3)
        position2 -= 0 if crash2 else random.randint(1, 3)
        position3 -= 0 if crash3 else random.randint(1, 3)
        
        crash1, crash2, crash3 = False, False, False
        
        position1 = 0 if position1 < 0 else position1
        position2 = 0 if position2 < 0 else position2
        position3 = 0 if position3 < 0 else position3
        
        if track1 [position1] == "🌲":
            crash1 = True
        if track2 [position2] == "🌲":
            crash2 = True
        if track3 [position3] == "🌲":
            crash3 = True
        track1[position1] = "💥" if crash1 else "  🚗 "
        track2[position2] = "💥" if crash2 else "  🏍 "
        track3[position3] = "💥" if crash3 else "  🏃‍♂️ 🐉 "
            
        print_race(track1,track2, track3)
            
        check_race(position1, position2, position3)
        
def create_tracks(track_length: int) -> (list, list):
    track = ["_"] * track_length

    def add_trees(track: list) -> list:
        trees = random.randint(1, 8)
        for _ in range(trees):
            tree_position = random.randint(0, len(track) - 1)
            track[tree_position] = "🌲"
        
        return track

    track1,track2,track3 =add_trees(track.copy()), add_trees(track.copy()), add_trees(track.copy())

    track1.insert(0, "🏁")
    track1.append(" 🚗 ")
    track2.insert(0, "🏁")
    track2.append(" 🏍 ")
    track3.insert(0, "🏁")
    track3.append(" 🏃‍♂️ 🐉 ")

    return (track1, track2, track3)

def print_race(track1: list, track2: list, track3: list):
    #os.system("clear")
    os.system("cls") #windows
    print("".join(track1))
    print("".join(track2))
    print("".join(track3))
    print("")

def check_race(position1: int, position2: int, position3: int):
    if position1 == 0 and position2 == 0 and position3 == 0:
        print("Empate")
    elif position1 == 0 and position2 == 0:
        print("Gana el coche 🚗")
    elif position1 == 0 and position3 == 0:
        print("Gana la moto 🏍")
    elif position2 == 0 and position3 == 0:
        print("Gana el dragon 🏃‍♂️ 🐉")

race(100)