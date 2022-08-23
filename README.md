# Quantum_Hackathon
## Problem Statement 
Create a working interactive ‘program’ (it can be a website, game, app, etc.) in which a human user is facing off against a quantum computer. This is broad on purpose - the program can be built in many different ways. Your program should implement strategies that seriously challenge the human player. The implementation must utilize more than just probabilities related to measuring quantum states. You must use Qiskit to program the computer’s gameplay strategy, and as much as possible, the strategy should be implemented with quantum circuits and quantum gates on real quantum hardware (although using the Simulator is understandable given the time limit).
## Solution: MILQ Simluator 
### Game Description 
Our game is defined as a party affliation congestion game. Specifically, is a set of cows on a field. The number of cows at the beginning can be changed, but we will mostly start with 4 cows. On the field, we have two separate farms with two cows each. One side has chocolate milk cows and the other has strawberry milk cows. The player starts as the chocolate milk cow farmer, and the Quantum AI starts as the strawberry milk cow farmer. The goal of the player is to make all the cows on the field all chocolate milk cows. This can be done by strategic breeding and moving cows. The game has three distinct stages: the moving stage, the breeding stage, and the death stage. These stages repeat until all the cows are all either strawberry or chocolate milk cows. If all the cows are chocolate milk, then the player wins! If all the cows are strawberry milk, the Quantum AI wins! 
#### Moving Cows 
First, the player will have the option to move one of their cows to the other farmer's field. A player must move one cow they control. All chocalate milk cows are controlled by the player, no matter what farm they are one. Thus the player must stragetically move their cows so that the chocolate milk cows outbread the strawberry milk cows (this will be explained in the next section). Similarly, the Quantum AI will be forced to move one of their strawberry milk cows as well.
#### Breeding 
After both players move a respective cow, the breeding process takes place. One each farm, two random cows will choose to breed. Their offspring will either be a strawberry or chocolate milk cow. This depends on the gene makeup of each cow. 
#### Genes 
Each cow has a set of three genes, and all three of those genes can be either brown, pink, or nothing. A cow with a majority of either the pink or brown gene will be a chocolate or strawberry milk cow. If there is a tie, for example a cow can have a pink, brown, and none gene makeup, then the cow is randomly selected to be a chocolate or strawberry milk cow. 
#### Death 
The last mechanic in the MILQ Simluator game, is the death mechanic. At the end of each breeding stage, one cow from each respective farm dies. The probabilty of a cow dieing is based on its age (how many turns the cow has been on the board). 
### Quantum AI 
The controller of the strawberry cows is a Quatum AI. We designed this through a series of mathematical reductions and QAOA optimizations. First our game is a congestion game, and then can be reduce to the Not-alll Equal (NAE) SAT problem. We can further reduce the NAE SAT problem to NAE 3-SAT, and reduce it a final time to the well studeid Max-Flow problem (all reductions are polynomial time).  We then use QAOA to find the best solution to the Max-Flow problem, and we use this solution to generate the next move in our congestion game. For a more detailed explanation, please see the Hackathon_Math.pdf in the Documents foler. 
## Step-by-Step Gameplay
