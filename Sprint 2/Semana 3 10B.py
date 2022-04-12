truclass Lamp :
    # guardar o valor 
    # true if light is on
    # false if light is off
    isOn = bool
    # method to turn on the light
    def turnOn(self) :
        self.isOn = True
        print("Light on? " + str(self.isOn))
    # method to turnoff the light
    def turnOff(self) :
        self.isOn = False
        print("Light on? " + str(self.isOn))
class Main :
    @staticmethod
    def main( args) :
        # create objects led and halogen
        led = Lamp()
        halogen = Lamp()
        # turn on the light by
        # calling method turnOn()
        led.turnOn()
        # turn off the light by
        # calling method turnOff()
        halogen.turnOff()
    

if __name__=="__main__":
    Main.main([])