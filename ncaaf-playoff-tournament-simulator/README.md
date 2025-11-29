\# NCAAF Playoff Tournament Simulator

\#\# Disclaimer on Usage of Generative AI  
While this work was created by me, the code itself was largely generated through prompting GenAI (ChatGPT). I provided the prompts and any necessary code debugging throughout the process \- but it was artificial intelligence that was the primary developer for the Python script.

\#\# Overview  
This code first inputs a CSV file containing twelve NCAAF teams, their seed for the tournament (\#1 through \#12), and their Predictive Rating from [TeamRankings.com](http://TeamRankings.com). Then, using these twelve teams, it runs a defined number of simulations of the NCAAF playoff format, simulating each individual game using a random normal distribution. Finally, it outputs the percentage probability (out of 100\) for each team to win in each round of the playoff.

\#\# NCAAF Playoff Format  
This simulator is based on the current twelve-team NCAAF playoff format. Details on this format can be found here \- https://en.wikipedia.org/wiki/College\_Football\_Playoff.

\#\# Libraries  
pandas, numpy, and collections (using Counter)

\#\# Input  
The input is set up by creating a CSV with twelve NCAAF teams, their seed for the simulated playoff (\#1 through \#12), and their Predictive Rating from TeamRankings.com.

\#\# Output in Console  
This code provides its output in the console containing the percentage probabilities (out of 100\) of each team winning in each round of the playoff.

Here is a sample output from the console:  

Round of twelve percentages:  
       Team  Percentage  
     Texas        92.36  
   Georgia        90.16  
Notre Dame        68.04  
  Michigan        59.29  
 Tennessee        40.71  
Texas Tech        31.96  
Arizona St         9.84  
  NC State         7.64  

Elite eight percentages:  
        Team  Percentage  
     Oregon        74.15  
    Ohio St        66.90  
       Utah        60.19  
    Georgia        55.83  
Mississippi        42.03  
      Texas        39.20  
 Notre Dame        24.53  
   Michigan        15.92  
  Tennessee         9.93  
 Texas Tech         8.57  
 Arizona St         2.14  
   NC State         0.61  

Final four percentages:  
        Team  Percentage  
    Ohio St        46.53  
       Utah        32.45  
     Oregon        30.47  
    Georgia        30.41  
      Texas        18.63  
Mississippi        18.15  
 Notre Dame        13.75  
 Texas Tech         3.96  
   Michigan         3.47  
  Tennessee         1.82  
 Arizona St         0.33  
   NC State         0.03  

National champion percentages:  
        Team  Percentage  
    Ohio St        35.60  
     Oregon        18.76  
       Utah        11.86  
    Georgia        10.64  
 Notre Dame         8.90  
      Texas         5.24  
Mississippi         4.86  
 Texas Tech         2.01  
   Michigan         1.49  
  Tennessee         0.60  
 Arizona St         0.03  
   NC State         0.01

\#\# Additional Assumptions and Considerations  
Home Field Advantage:  
Home-field advantage is taken into account for game simulations in the first round only, where the real-life format gives home-field advantage to the higher seed. For the game simulations, I adjusted the input “spreads” (used as the mean for each random normal distribution) by 2.6 points in favor of the home team, as taken from [TeamRankings.com](http://teamrankings.com/).

Random Normal Distribution Inputs:  
Each "game" was simulated with a single random normal distribution, where the mean was the projected score differential (Home Team Predictive Rating \- Away Team Predictive Rating \+ 2.6), and the standard deviation was 13.89. I do not remember exactly where I first found this 13.89 number, but it may have been from this article, which cites the same standard deviation for NCAAF games \- [https://www.footballperspective.com/a-monte-carlo-based-comparison-of-college-football-playoff-systems/](https://www.footballperspective.com/a-monte-carlo-based-comparison-of-college-football-playoff-systems/).
