#Hola -> HolaHolaHola
#Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas" #We make sure tht the input is a string
        return string*n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi"))

#Second example
def make_division_by(den):
    def numerator(x :int):
        assert type(x) == int, "Only integers available" 
        assert den != 0, "You cannot divide by zero"
        return x/den
    return numerator

def main():
    divided_by_2 = make_division_by(2)
    print(divided_by_2(10)) #Expected value: 5


if __name__ == '__main__':
    #run8() 
    main()