The RandoBlazer Generator Sim is a small portion of a larger project to port a Super Nintendo randomizer romhack of 
**Soul Blazer** to python. The original code was forked from another repository in Github and modified. In this port, 
the randomization logic has been replaced with a network graph model to enable more advanced progression logic. For 
those unfamiliar with "Randomizers", this project would use randomness with logical limitations to scramble the items 
in a game and place them throughout the game world in a unique arrangement. This, combined with other quality-of-life 
changes to the game code can make an old game feel new and interesting.

Originally intended for debugging placement logic, this app graphically demonstrates the new network graph logic for 
world progression and deterministic randomization of such. Specify a seed name to have reproducable random logic, or 
leave the seed blank to have one generated completely at random.

Using the app requires no prior knowledge or pre-requisites. Check it out!

* [Github Repository](https://github.com/jnschurig/RandoBlazer/tree/py-conversion).
* [Streamlit App](https://randoblazer-generator-sim.streamlit.app/)
