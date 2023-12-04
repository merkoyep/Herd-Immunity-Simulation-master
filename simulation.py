import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, inital_infected=1):
        # Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_vaccinated = round(self.vacc_percentage * self.pop_size)
        self.inital_infected = inital_infected
        self.infected_people = []
        self.total_deaths = 0
        self.newly_infected = []
        self.simulation_log = Logger("simulationLog.txt")
        self.interaction_count = 0
        self.interacted_people = set()
        self.vaccination_interactions = 0
        self.infectious_interactions = 0
        # Store the virus in an attribute
        # Store pop_size in an attribute
        # Store the vacc_percentage in a variable
        # Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # Call self._create_population() and pass in the correct parameters.
        self._create_population()

    def _create_population(self):
        self.person_list = []
        vaccinated_count = self.initial_vaccinated
        for n in range(0, self.pop_size):
            if n < self.inital_infected:
                new_person = Person(n, False, self.virus)
                self.person_list.append(new_person)
                self.infected_people.append(new_person)
            else:
                if vaccinated_count > 0:
                    new_person = Person(n, True)
                    self.person_list.append(new_person)
                    vaccinated_count -= 1
                else:
                    new_person = Person(n, False)
                    self.person_list.append(new_person)
                
        # Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # : Return the list of people
        return self.person_list

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.

        has_unvaccinated_living_people = any(person.is_alive and not person.is_vaccinated for person in self.person_list)
        has_infected_people = any(person.is_alive and person.infection for person in self.person_list)
        has_uninfected_living_people = any(not person.infection and person.is_alive for person in self.person_list)

        if has_uninfected_living_people and has_unvaccinated_living_people and has_infected_people:
            return True
        elif not has_infected_people:
            return False
    #Possible cases
    #Vaccinated, not infected | Vaccinated & infected

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        self.time_step_counter = 0
        should_continue = True

        
        self.simulation_log.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            # Increment the time_step_counter
            self.time_step_counter += 1
            self.time_step()
            # or every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            should_continue = self._simulation_should_continue()
        # Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        if self.alive_count == 0:
            end_reason = 'Everyone is dead.'
        elif self.vaccinated_count + self.total_deaths == self.pop_size:
            end_reason = 'Everyone alive is vaccinated.'
        elif not self.infected_people:
            end_reason = 'The disease died out!'
        self.simulation_log.log_infection_survival(self.alive_count, self.total_deaths, self.vaccinated_count, end_reason, self.interaction_count, self.vaccination_interactions, self.infectious_interactions)
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # Loop over your population
        self.fatalities = 0

        for person in self.infected_people:

            if not person.did_survive_infection():
                person.is_alive = False
                self.fatalities += 1
                self.total_deaths += 1
            else:
                person.is_vaccinated = True
                interacted = []
                for n in range(100):
                    random_person = self.person_list[random.randint(0, len(self.person_list) - 1)]
                    self.interaction_count += 1
                    if random_person not in interacted and random_person.is_alive:
                        self.interaction(person, random_person)
                        interacted.append(random_person)
                interacted = []

        self.infected_people = [person for person in self.person_list if person.infection and person.is_alive]
        new_infections = len(self.newly_infected)
        self._infect_newly_infected()
        self.alive_count = 0
        self.vaccinated_count = 0
        for person in self.person_list:
            if person.is_alive:
                self.alive_count += 1
            if person.is_vaccinated:
                self.vaccinated_count += 1
        self.simulation_log.log_interactions(self.time_step_counter, new_infections, self.fatalities, self.total_deaths, self.alive_count, self.vaccinated_count)
        self.newly_infected = []
        self.interacted_people = set()
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person


    def interaction(self, infected_person, random_person):
        # Finish this method.
        if (
            random_person.is_alive 
            and not random_person.infection 
            and not random_person.is_vaccinated
            ):
            infection_risk = random.random()
            if infection_risk < self.virus.repro_rate:
                if random_person not in self.newly_infected and random_person not in self.interacted_people:
                    self.newly_infected.append(random_person)
                    self.interacted_people.add(random_person)
                    self.infectious_interactions += 1
            else:
                random_person.is_vaccinated = True
                self.vaccination_interactions += 1


        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # : Call logger method during this method.
        

    def _infect_newly_infected(self):
        # Call this method at the end of every time step and infect each Person.
        for person in self.newly_infected:
            person.infection = self.virus
            self.infected_people.append(person)
        # Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.



if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 100

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
