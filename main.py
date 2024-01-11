import random
from Character import Character
from Fabric import Fabric

players={
    {"name":"Pablo","color":"yellow",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     },
    
    {"name":"Matt","color":"cyan",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     },
    
    {"name":"Ishan","color":"red",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     },
    
    {"name":"Vittorio","color":"purple",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     },
    
    {"name":"Giacomo","color":"blue",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     },
    
    {"name":"Piotr","color":"green",
     "skills":[("attack", 10),
               ("attack_kamehameha", 20)]
     }
    }

bots={"Cliring": "yellow",
         "Bulma": "cyan",
         "Krillin": "red",
         "Piccolo": "purple",
         "Gohan": "blue",
         "Trunks": "green"}

for player in players:
    player = player["name"]
    stenght = random.randint(1,100)
    defence = random.randint(1,100)
    intel = random.randint(1,100)
    life = random.randint(1,1000)
    print(f"{player} {color}")
    playerCreated = Character(player, stenght, defence, intel, life, color)
    players[player]=playerCreated
    print(f"{players[player].attributes()}")


skills = ["attack", "attack_kamehameha"]
dead_players = []
turns= 20



# print all the player in like a table one from the other
# def print_players(players:dict):
#     print("Players status:")
#     status = ""
#     length = len(players)+1
#     for name,player in players.items():
#         status += f"{player.get_name()}"
#         status += f"{player.get_strength()}"
#         status += f"{player.get_defence()}"
#         status += f"{player.get_intelligence()}"
#         status += f"{player.get_life()}"
#     status += "\n"
#     print(status)
    

# print_players(players)

for i in range(turns):
    
    print(f"Turn {i+1}")
    list_players = list(players.keys())
    random_player = random.choice(list_players)
    enemys=[enemy for enemy in list_players if enemy != random_player]
    random_enemy = random.choice(enemys)
    random_skill = random.choice(skills)
    
    while len(dead_players) < len(players) or turns > 0:
        
        if players[random_player].is_alive() == False:
            dead_players.append(players[random_player])
        
        if random_skill == "attack":
            players[random_player].attack(players[random_enemy])
        elif random_skill == "attack_kamehameha":
            players[random_player].attack_kamehameha(players[random_enemy])
        
        if players[random_enemy].is_alive() == False:
            dead_players.append(players[random_enemy])
        
        if len(dead_players) > 0:
            turns -= 1

# print_players(players)
    

# print(goku)
# print(vegeta)
# print(Cliring)

# goku.attack(vegeta)
# goku.attack(vegeta)
# vegeta.attack(goku)
# vegeta.attack_kamehameha(goku)
# goku.attack(vegeta)
# goku.attack_kamehameha(vegeta)
# goku.attack(vegeta)
# goku.attack_kamehameha(vegeta)
# goku.attack(vegeta)




# print(goku)
# print(vegeta)
