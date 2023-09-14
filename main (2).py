#Implement a class called  player that represplayer that represents a cricket player.The player class play() which prints The player is playing cricket.Derive two classes,Batsman and Bowler,from the player class.Override the play() method in each derived class to print "The Batsman is batting" and "The Bowler is bowling",respectively.Write a program to create objects  of both the Batsman  and Bowler  classes  and call the playe() for each object.

# Define the player class

class player:

    def player(self):

        print("The player is playing cricket.")

  # Define the Batsman class,derived from player 

class Batsman(player):

    def play(self):

        print("The batsman is batting.")

# Define the Bowler class, derived from player 

class Bowler(player):

    def play(self):

        print("The Bowler is bowler is bowling.")

# Create objects of Batsman and Bowler  classes 

batsman = Batsman()

Bowler = Bowler()

# Call the play() method for each object 

batsman.play()

Bowler.play()