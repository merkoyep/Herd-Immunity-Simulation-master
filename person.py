import random
import math
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  # int
        # Define the other attributes of a person here
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True #Assumption all subjects are alive to start'

    def did_survive_infection(self):
        # return boolean of if person has survived infection
        # assuming infection is truthy
        if self.infection:
            mortality_risk = random.random() #0-1.0
            if self.is_vaccinated or mortality_risk >= self.infection.mortality_rate:
                return True
            else:
                return False
        else:
            return True
                


if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # complete your own assert statements that test
    # the values of each attribute
    assert infected_person._id == 3
    assert infected_person.is_alive == True
    assert infected_person.infection.name == "Dysentery"
    assert infected_person.infection.repro_rate == 0.7
    assert infected_person.infection.mortality_rate == 0.2
    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 100):
        new_person = Person(i, False)
        people.append(new_person)
    virus = Virus("Diphthera", 0.55, 0.65)
    patient_zero = Person(99, False, virus)
    people.append(patient_zero)
    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 
    survived = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            survived += 1
        else:
            did_not_survive += 1
    print(f'Survived: {survived}, Deceased: {did_not_survive}')


    #  Loop over all of the people 
    #  If a person is_alive True add one to did_survive
    #  If a person is_alive False add one to did_not_survive

    # When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 
    spreading_virus = Virus("Tubucerlosis", 0.55, 0.9)
    first_spread = math.floor(100 * spreading_virus.repro_rate)
    healthy_people = 100 - first_spread
    interacted_people = []
    spreader_survived = 0
    spreader_did_not_survive = 0
    spreader_infected = 0
    for i in range(1, first_spread + 1):
        new_person = Person(i, False, spreading_virus)
        interacted_people.append(new_person)
    for i in range(first_spread + 1, healthy_people + first_spread):
        new_person = Person(i, False)
        interacted_people.append(new_person)
    print(first_spread)
    print(healthy_people)

    for person in interacted_people:
        if person.did_survive_infection() or person.infection is None:
            spreader_survived += 1
        elif not person.did_survive_infection():
            spreader_did_not_survive += 1
        if person.infection:
            spreader_infected += 1
    infected_count = sum(1 for person in interacted_people if person.infection is not None)
    print(f'Total Interacted People: {len(interacted_people)}, Infected: {infected_count}, Uninfected: {len(interacted_people) - infected_count}')

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.