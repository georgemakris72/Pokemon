print("hi")

class Pokemonz(object):
    def __init__(self,location,trainer,PokeDex_number,type):
        self.location=location
        self.trainer=trainer
        self.PokeDex_number=PokeDex_number
        self.type=type
        self.battle=0
        self.stagebattle=self.battle
        self.stages=["Level0", "Level1", "Level2", "Level3", "Level4" "Level5"]
        self.currentstage=self.stages[0]
        self.evolved=True
    def XP(self):
        self.battle=self.battle+1
        print("You have won a battle!")
    def evolvingStage(self):
        if (self.battle>self.stagebattle):
            self.stagebattle=self.stagebattle+1
            self.currentstage=self.stages[self.stagebattle]
            print("You are now evolving")
    def hasEvolved(self):
        if (self.evolved):
            print("You have now reached {}".format(self.currentstage))


class Character(Pokemonz):
    def __init__(self,name,age,weekness):
        Pokemonz.__init__(self,"Russia","Troy",401,"quick")
        self.name=name
        self.age=age
        self.weekness=weekness
    def attacking(self):
        print("You are attacking")
        Pokemonz.XP(self)
    def evolving(self):
        print("You are ready to evolve.")
        Pokemonz.evolvingStage(self)
        Pokemonz.hasEvolved(self)

lance=Character("Duggan",24, "spiders")
# lance.attacking()
# lance.evolving()
# lance.attacking()
# lance.evolving()
