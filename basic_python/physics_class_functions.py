## Physics Class Project - CodeAcademy
## Initial Variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

##### Temperatures #####
## Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

## Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = (c_temp * (9/5)) + 32
    return f_temp

## Test f_to_c with 100 degrees
f100_in_celsius = f_to_c(100)
print("100F to Celsius: " + str(f100_in_celsius))

## Test c_to_F with f100_in_celsius degrees
c0_in_fahrenheit = c_to_f(0)
print("0C to Fahrenheit: " + str(c0_in_fahrenheit))
##### Temperatures #####

##### Basic Physics Equations #####
## Force
def get_force(mass, acceleration):
    force = mass * acceleration
    return force

## Test get_force with train_mass & acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

## Energy
def get_energy(mass, c = 3*10**8):
    energy = mass * c ** 2
    return energy

## Test get_energy with bomb_mass
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

## Work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

## Test get_work with train_mass, train_acceleration, & train_distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " +
      str(train_distance) + " meters.")