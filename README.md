RECOMMENDATIONS-BASED-ON-YOUR-FACEBOOK-LIKES-AND-INTERESTS
==========================================================
Note: Step 6 is on a work-in-progress stage

Step1: 

Remove the noise (likes and interest in foreign language) from the dataset:

Having a file of 1 GB with millions of records the first step involved cleaning of the dataset to remove noises and 
likes that had foreign accent.
No. of user records: 176610
Python Code: part1a.py
File Created: Cleanedup_File.csv
Time taken for part3_find_highfreqpair.py code to complete: 8-10mins

Step2: 

I used the Cleanedup_File.csv file to plot the like-frequency histogram:
Number of unique likes and interest: 3414905
Inter-quartile Range of frequencies:
25th percentile: 1
50th percentile: 1
75th percentile: 2
90th percentile: 5
95th percentile: 11
97.5th percentile: 26
99.5th percentile: 161
Mean: 6
Standard Deviation: 103.11
Minimum count of frequency of likes: 27712
Python Code: Histogram.py
File Created: Histogram_1.png, Histogram_2.png, Histogram_3.png

Step 3: High Frequency Like and Interest Page Pairs:

This step tries to answer the question “when a user likes A, they also like B”.It shows the most frequently occurring 
like pairs

File used: Cleanedup_File.csv
Number of likes and interests with its frequency(number of people liking the page) arranged in descending order: 1550
Python Code: Pair.py
File obtained: HighFrequencyLike_1235_File.csv

Step 4: Recommended Likes

The high frequency like pair available from the above step irrespective of the user’s current preferences 
or its similarity with other users is used for recommendation purpose based on an inputted set of Likes.
For example if you submit (Kayne West, JayZ, Dr. Dre) it might recommend to you (Notorious
B.I.G., Tupac, Kid Cudi, Eminem).
Data used to created sql table: High__Freq_Like_Pairs.csv
Python Code Used: Q4_DBStorage.py,Part3.py


Step 5: Recommended Users

When a user submits a set of likes and interests, the outcome is a set of users which closely match the set of likes 
and interests from the user input.For example, if you submit (Kanye West, JayZ, Dr. Dre) it might recommend to you:
● User Mr. Exact (Kanye West, JayZ, Dr. Dre)
● User Mrs. Close (Kanye West, Biggie, Tupac)
● User Ms. Kind of Close (Rihanna, Kid Cudi, Eminem)
Data used to created sql table: HighFreqUserLikes.csv
Python Code Used: Q4_DBStorage.py, Part4.py

Step 6: Recommendations based of User Preference and Similarity between likes and interests

This is a work-in-progrss step where I have used Apache Mahout to create recommendations on user preference and 
interst and like similarity.Right now I  am working on building a restful API for the recommender system










