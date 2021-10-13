class Car(object):
    def __init__(self, model, color, company, speedLimit):
        self.color= color
        self.model= model
        self.company= company
        self.speedLimit=speedLimit
    
    def start(self):
        print('started')
    
    def stop(self):
        print('stopped')
    
    def accelarate(self):
        print('accelarating')
    
    def changeGear(self):
        print('gear Changed')
    

audi= Car('A6', 'white','audi','80')
print(audi.color)
print(audi.model)

scorpio=Car('Mhwak', 'white', 'Madindara', '300')
print(scorpio.model)