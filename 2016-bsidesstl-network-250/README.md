
# Cyberville Level 2 (200-300pt Challenge)

This challenge requires the competitor to use knowledge of web URL parameter vulnerabilities and basic UNIX commands. The scenario is set up to where Cyberville's Paula O's Pancake House has created a website to attract customers, which has been directly connected to their billboard in order to save funds. Using the URL parameter exploit, a user is to gain escalated access to the ssh port on the same box in order to run a script that will change the text on the billboard and output the key.

Note that the user "pancakes" has read and execute access on the program which contains the key, but not enough access to take down the box.

#### To build
1. Pull the repository
2. Run ```docker-compose up -d```.
3. Run ```docker ps``` and copy the ID of the running container.
4. Run ```docker exec -it [CONTAINER ID] bash```.
5. Run ```service ssh start```.

#### Solution
1. Visit the entrypoint (a specified IP for the challenge) in the browser. The user will land on the homepage of Paula O's Pancake House.
2. Click on ```Menu```.
3. Change the URL parameter to ```?day=;ls ../../../``` and visit that page. This will show the directory listing for the root directory.
4. Change the URL parameter to ```?day=../../../../BILLBOARD_INSTRUCTIONS.txt``` and visit that page. This will give the user a username and password for the ssh login.
5. In a terminal window, run ```ssh pancakes@[CHALLENGE IP]```.
6. Enter the password from the instructions file you viewed.
7. Run ```ls```. Notice there is an executable called ```change_msg.sh```.
8. Run ```./change_msg.sh```.
9. Copy the outputed key and paste it into the scoreboard for points.


Key: MCA-A82D90C6