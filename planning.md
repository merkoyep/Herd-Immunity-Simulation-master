- [] Get your data for virus name, mortality rate, and reproductive rate from [this Guardian article](https://www.theguardian.com/news/datablog/ng-interactive/2014/oct/15/visualised-how-ebola-compares-to-other-infectious-diseases).
- During every time step of the simulation, **every sick person** should randomly interact with **100 other people** in the population. The chance of a sick person infecting a person that they interact with is the virus's reproductive rate. Example: if a virus has a reproductive rate of 15, then, on average, a sick person should infect 15 of the 100 people they interact with during that time step.
  - [] On tick, sick person total x 100 people => Encounters property = true
    - [] && if encountered, reproductive rate proportion of 100 becomes infected
      - [] of those infected, those vaccinated will not be actually infected. (Rule 2 &3)
      - []
  
  - [] Infected 
    - [] vaccinated variable = false
  - Uninfected
    - [] Encounters property = false or true
    - []

- Initial size of the population
- Initial number of infected people
- Name of the virus
- Stats for the virus
- Date the simulation was run

#### While Simulation Runs: Display  Every Iteration

- The number of new infections
- The number of deaths
- Statistics for the current state of the population:
 
    - Total number of living people
    - Total number of dead people
    - Total number of vaccinated people
             
 #### After Simulation Ends: Summary
 
 - Total living
 - Total dead
 - Number of vaccinations
 - Why the simulation ended
 - Total number of interactions that happened in the simulation
 - Number of interactions that resulted in vaccination
 - Number of interactions that resulted in death