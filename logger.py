from datetime import datetime

current_date_and_time = datetime.now().strftime('%m-%d-%Y')

# Extract the date from the datetime object




class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        # Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        number_vaccinated = round(pop_size * vacc_percentage)
        with open(self.file_name, 'w') as file:
            file.write(f'''
    Population: {pop_size}
    Initial Infected: {pop_size * basic_repro_num}
    Virus: {virus_name} 
        Reproductive Number: {basic_repro_num}
        Mortality_rate: {mortality_rate}
    Date of simulation: {current_date_and_time}\n
    ''')

        # : Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # : Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

    def log_interactions(self, step_number, number_of_new_infections, new_deaths, total_deaths, alivecount, vaccinated):
        with open(self.file_name, 'a') as file:
            file.write(f'''
    Step Number: {step_number}
    New Infections: {number_of_new_infections}
    New Deaths: {new_deaths}
    Current Population:
        Alive: {alivecount}
        Deaths: {total_deaths}
        Vaccinated: {vaccinated}
    ''')

        # Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        

    def log_infection_survival(self, living, dead, vaccinations, reason_for_end, total_interactions, total_vaccine_interactions, total_infectious_interactions):
        with open(self.file_name, 'a') as file:
            file.write(f'''
---END OF SIMULATION---
    Total Living: {living}
    Total Dead: {dead}
    Number of Vaccinations: {vaccinations}
    Reason for end of simulation: {reason_for_end}
    Total Interactions: {total_interactions}
    Total non-infectious: {total_vaccine_interactions}
    Total Infectious Interactions: {total_infectious_interactions}
                       ''')

    def log_time_step(self, time_step_number):
        with open(self.file_name, 'a') as file:
            file.write(f'Time Ste: {time_step_number}')