# 2468scoutingApp
This is FRC team 2468's code for our Scouting Application meant to be used at FIRST PowerUp competitions to determine and rank the best teams for alliance selection. It works by using the iPad Application to manually input objective data (such as cubes scored in the switch/scale), and creates a QR code, which is then read in by a third-party program, zbarcam. The output of zbarcam is then read in by scoutingApp.py, which will store interpret the data and store it in JSON. Finally, you can make two different kinds of outputs from the data collected: a spreadsheet which details all of the objective stats that each team scouted has in a match, and a radar plot showing their relative strengths. The iOS portion was developed by Vrishab Madduri, ELi Bradley, and Ahir Chatterjee. The rest of the scripts were written by Ahir Chatterjee.
