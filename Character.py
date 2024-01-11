
class Colors:
    
    def __init__(self):
  
        self.colors = {"red": "\033[31m", "green": "\033[32m",
                         "yellow": "\033[33m", "blue": "\033[34m",
                         "purple": "\033[35m", "cyan": "\033[36m",
                         "white": "\033[37m"}
    
    def set_color(self, color):
        if color in self.colors:
            return self.colors[color.lower()]
        else:
            print("Color not found")
            return self.set_white()
    
    def set_white(self):
        return self.colors["white"]

class TextColors(Colors):
        
        def __init__(self):
            super().__init__()
            
        def text(self, text, color):
            start_color = self.set_color(color)
            end_color = self.set_white()
            
            return f"""{start_color}{text}{end_color}"""

class Skill:
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def name(self):
        return self.name
    
    def damage(self):
        return self.damage

    
    def get_skill(self):
        return f"{self.name} {self.damage} "
    
    def __str__(self):
        return f"{self.name} {self.damage} "

class Character(TextColors, Skill):
    
    def __init__(self, name, strength, defence, intelligence, life, color, skills=[]):
        super().__init__()
        self.__name = name
        self.__strength = strength
        self.__defence = defence
        self.__intelligence = intelligence
        self.__life = life
        self.__color = color
        self.skills = skills        
        

    def get_name(self):
        return self.__name
    
    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strength(self, strength):
        self.__strength = strength
    
    def get_defence(self):
        return self.__defence
    
    def get_intelligence(self):
        return self.__intelligence
    
    def get_life(self):
        return self.__life
    
    def get_color(self):
        return self.__color
    
    def add_skill(self, skill):
        self.skills.append(skill)
            
    def attack(self, enemy):
        
        if enemy.is_alive():
            print(self.text(
                text=f"{self.__name} is physic attacking {enemy.__name}",
                color=self.get_color()))

            attack_damage = self.damage(enemy)
            enemy.__life -= attack_damage
        else:
            enemy.__death()
    
    def attack_kamehameha(self, enemy):
        
        if enemy.is_alive():
            print(self.text(
                text=f"{self.__name} Kamehamehaaaaaaaaaaaa... to {enemy.__name}",
                color=self.__color))
            
            attack_damage = self.magic_damage(enemy)
            enemy.__life -= attack_damage
            
            if enemy.is_alive():
                print(self.text(f"Now {enemy.__name} has ♥ {enemy.__life}  left.",
                            color=enemy.get_color()))
                print(f"{enemy.__name} is still alive !")
            else:
                enemy.__death()
        else:
            enemy.__death()
    
    def damage(self, enemy):
        return self.__strength - enemy.__defence
    def magic_damage(self, enemy):
        return self.__intelligence - enemy.__defence

    def is_alive(self):
        return self.__life > 0
    def __death(self):
        self.__life = 0
        print(f"Stop attacking to {self.__name} is dead!")
    
    def attributes(self):
        attributes= self.text(text=
                f"""
                {self.__name.upper()}
                ---------------------------------
                ♥ : {self.__life}
                Strength: {self.__strength}
                Intelligence: {self.__intelligence}
                Defence: {self.__defence}
                """,
                color=self.__color
                )
        return attributes
         
    
    def __str__(self):
        
        return self.attributes()