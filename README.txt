The way that I approached this challenge was to:

1. Load the two datasets, musk_data and west_data;
2. Generate a random number between 0 and 1 to choose between the two celebrities;
3. If 1 was chosen, then the first tweet from Elon Musks's Twitter account will be displayed.
   If 2 was chosen, then the first tween from Kanye West's Twitter account will be displayed.
   Here, the "first tweet" will be referenced as 'index' in the program.
4. After displaying the 'text' component of the Tweet, the program will prompt the user to
   guess who Tweeted said quote. If they were right, a point will be recorded in win_count, and
   the program will tell them that they were correct. If they were wrong, a point will be
   recorded in lose_count, and the program will tell them that they were wrong.
5. The user will then be asked if they would like to continue the program, in which if they say
   yes, the "game" within the while loop will continue. If they say no, the user will exit the
   while loop and will be thanked for participating in the game.

I was not able to complete this program because at lines 52 and 55, I was not able to
load the 'text' component of a Tweet from a specific tweet. If I had more time, I would look into
what

res = conn.getresponse()
musk_data = res.read()

means, and how the data is being stored. I had thought that musk_data would be in the form of
a json file, but after testing, only an array of integers would be printed out when attempting
to print a specific index of the dataset.
