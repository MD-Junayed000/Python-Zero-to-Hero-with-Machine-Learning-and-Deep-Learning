# Decorator = A function that extends the behaviour of another function
#             without modifying the base function
#             Pass the base function as a argument to the decorator

##            @add_spriinkles ### additional
##             get_icecream('vanilla')- base unchangeable

### Returning a function
def add_sprinkles(func):
    #def wrapper():
        print('YOu add sprinkles😶‍🌫️')
        func()
    #return wrapper


@add_sprinkles ### extended feature
def get_icecream():
    print('Here is your icecream👹👹')


#get_icecream()




