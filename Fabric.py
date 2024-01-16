import json
import random
from Character import Character

class Player(Character):
        
        def __init__(self, name, color, skills=[]):
            super().__init__(name, color, skills)
            self.strength = 0
            self.defence = 0
            self.intel = 0
            self.life = 0
        
        
        def random_status(self):
            self.strength = random.randint(1,100)
            self.defence = random.randint(1,100)
            self.intel = random.randint(1,100)
            self.life = random.randint(1,1000)
        
        def custom_status(self, strength, defence, intel, life):
            self.strength = strength
            self.defence = defence
            self.intel = intel
            self.life = life
        
        def get_status(self):
            return f"{self.strength} {self.defence} {self.intel} {self.life}"
        
        def __str__(self):
            return f"{self.name} {self.color} {self.get_status()}"
        
        
        

class Fabric:
    
    def __init__(self, players, bots):
        self.read_players = players
        self.bots = bots
        self.dead_players = []
        self.players_data = "players_data.json"
    
    
    def load_players(self):
        with open(self.players_data, "r") as file:
            self.read_players = json.load(file)
    
    def create_players(self):
        
        if self.read_players == None:
            print("No players to create")
            
        for player in self.read_players:
