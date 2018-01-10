# UFO_sighting
A pet project for data storytelling. More information to my BLOG[(here)](http://binda.blog/2018/01/07/ufo_sighting1).

### Library used
* Python Version: 3.6.4 
* Packages Used: pandas, datetime, re, matplotlib, numpy, nltk, scikit-learn, wordcloud

### Dataset Source
* Origin data source: Infochimps.com
* data source: github-johnmyleswhite/ML_for_Hackers/01-Introduction/data/ufo/ufo_awesome.tsv

### Data Structure

	| DateOccurred | DateReported | Location 	  | ShortDescription | Duration | LongDescription 		   |
    --------------------------------------------------------------------------------------------------------
	| 19951009	   | 19951009 	  | Iowa City, IA | 	 			 | 	 	    | Man repts. witnessing... |
	| 19951010	   | 19951011 	  | Milwaukee, WI | 	 			 | 2 min.	| Man  on Hwy 43 SW of ... |
    | 19950202	   | 19950203	  |	Denmark, WI	  | cone 			 | 75 min	| Caller, and apparently...|

### Questions
1. Have UFO sightings increased? Have UFO sightings existed fixed frequency?
2. Have UFO sightings differences in the different state?
3. What do eyewitness sighting?

### Process

1. We do data cleansing and use python3 plotting library - "matplotlib" to achieve data visualization. Then, we try to explain the implied meaning of the figure. 
2. We do data pre-processing and use python3 machine learning library - "scikit-learn" to count tf-idf. We find 5 top keywords for each document based on tf-idf value. Then, we plot the wordcloud and try to explain the implied meaning of the figure.

### Result

__Question 1. Have UFO sightings increased? Have UFO sightings existed fixed frequency?__

We plot the number of witnesses for each year. As shown in Figure 1-UFO Sighting, The UFO sightings mainly occur between 1950 and 2010 and increase yearly. As shown in Figure 2-UFO Sighting(1990-2010), UFO sightings have increased sharply in 1990 to 2010. UFO sightings rise as high as 4,000 in 2008 and 2009.
(From the data, it's true.We don't know collect ways from the dataset, So we aren't sure whether technical progress to change people's number of returns.)

__Question 2. Have UFO sightings differences in the different state?__

We focus the range of 1990-2010 and plot the number of witnesses for each year in each state. As shown in Figure 3, CA (California) and WA (Washington State) is significantly more than the other states. CA has been a steady increase yearly. WA is more consistent and seem to have a cyclical peak. Other regions have the sudden peak. Some states have the same situation. For example, the peak of FL (Florida) and IL (Illinois) are similar that both peaks are in 2003 to 2004. OR (Oregon) and NY (New York) also have similar peak in 1999 to 2010. MI (Michigan) and NC (North Carolina) have similar curves.

__Question 3. What do eyewitness sighting?__

We plot wordcloud based on tf-idf. As shown in Figure 4, the eyewitness use "craft, aircraft, plane, cigar, fireball, triangle, disk, or satellite" to describe UFO. The eyewitness saw the UFO where usually has "moon, cloud, star, or lake". The UFO appeared with "flash, light, move, orb, or jet". The color of light often is "orange, green, or red". The eyewitness saw the UFO usually with family such as husband.

Further, we use 2-gram to understand more detail describes. Different color or format of light, like "red light, orang light, ball light, amber light, white light, flash light, blue light or green light". Different shape, like "egg shape, boomerang shape, black triangle, triangle format, orange ball". And other describes, like "green firebal, vapor trail, big dipper".

<div align="center">
	<img src="https://i.imgur.com/SKwTHR9.png" height="300px" alt="Figure 1" >
	<img src="https://i.imgur.com/g1OY3e9.png" height="300px" alt="Figure 2" >
</div>

![Figure 3](https://i.imgur.com/fEh23TJ.png "Figure 3")

<div align="center">
	<img src="https://i.imgur.com/HBfccgC.png" height="300px" alt="Figure 4" >
	<img src="https://i.imgur.com/oUqgeBR.png" height="300px" alt="Figure 5" >
</div>
