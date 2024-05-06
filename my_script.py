# start = 'start program...'
# print(start)
def gather_animal_info():
    animal_info = {}

    species = input ("enter animal: ")
    is_mammal = input ("is it a mammal: ")
    num_legs = input ("how many legs does it have? ")
    has_tail = input ("does it have a tail? ")
    num_seen = input ("how many {}'s have you seen? ".format(species))

    animal_info ["species"] = species
    animal_info ["is_mammal"] = is_mammal
    animal_info ["num_legs"] = num_legs
    animal_info ["has_tail"] = has_tail
    animal_info ["num_seen"] = num_seen

    return animal_info

animal_info = gather_animal_info()

animal_info['num_seen'] = int(animal_info['num_seen'])

if animal_info['num_seen'] <= 10:
    print("youve seen less than 10{}'s".format(animal_info['species']))
elif animal_info['num_seen'] > 10 and animal_info['num_seen'] < 100:
    print("youve seen between 10 and 100 {}'s".format(animal_info['species']))
elif animal_info['num_seen'] >= 100:
    print("youve seen 100 or more {}".format(animal_info["species"]))

animal_info['is_mammal'] = bool(animal_info['is_mammal'])
animal_info['has_tail'] = bool(animal_info['has_tail'])
print(type(animal_info['is_mammal']))
print(type(animal_info['has_tail']))

if (animal_info['is_mammal'] == True or animal_info['has_tail'] == True) and not (animal_info['is_mammal'] == True and animal_info['has_tail'] == True):
    print("a {} is either a mammal or has a tail but not both".format(animal_info['species']))

else:
    print("a {} is neither a mammal nor has a tail, or it has both".format(animal_info['species']))


# def favorite_animal(species, is_mammal, num_legs, has_tail):
#     print("animal:", species, is_mammal, num_legs, has_tail)

# favorite_animal(species, is_mammal, num_legs, has_tail)

# for i in range(5):
#     print(i)

# n = 5
# while n <= 15:
#     print(n)
#     n += 1

# foods = ["nuggets", "pizza", "burgers", "pie", "hotdogs"]
# for food in foods:
#     print(food)

print(animal_info)