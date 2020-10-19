# discord-rich-presence-python
[![codecov](https://codecov.io/gh/TennisBowling/discord-rich-presence-python/branch/main/graph/badge.svg?token=FKSZTY790B)](undefined)
discord-rich-presence-python is code that will display your ram and cpu usage as rich presence on discord.

## usage

Have python3, pip3, and discord desktop installed.
Install the requirements for the program with ```pip3 install -r requirements.txt``` in command prompt.
Run the program with python3 main.py 
Enjoy!

### suggestions

Any suggestions for code changes or new assets (images, names) should be posted in issues.


#### how testing works

There are no "real" tests on the code itself, as the code requires to connect to a rpc endpoint set up by discord. What travis ci does is install requirements, and use coverage.py to run coverage tests on main-testing.py, which is main.py but without the loops (to be able to finish) and without rpc.connect (which is connecting to discord endpoint, which isn't possible). Then the coverage report is posted to codecov.