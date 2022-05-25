class Patient:
    def __init__(self, name):
        self.name = name
        self.observations=[]
        
alice = Patient('alice')
print(alice.name)