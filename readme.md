# Program Synthesis Project
-----------------------------------------------------------
## Final project for UT Austin Programming Synthesis Class
### Project is focused on learning grammars for generating programs to mimic the behavior of an RL policy
### Control flow is as follows:
* First an RL policy is trained with SAC or PPO
* Second We generate a number of random grammars
* Grammars are used to generate programs designed to mimic the behavior of the RL policy
* Grammars are then recombined based on performance using an evolutionary algorithm
