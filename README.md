# Fire
An example of a more thorough look into predicting fires in northeast Portugal.

Find the dataset used [here](http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/) and the starting code for SKLearn [here](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)


_Requirements_ 

* Python 2.7.x
* [SKLearn](http://scikit-learn.org/stable/install.html)
* [Numpy](http://www.scipy.org/Installing_SciPy) _"Shouldn't you already have that installed?"_
* For the love of god, an OSX machine

**Special thanks to Cortez and Morais for their data collection and work as well as the UCI Machine Learning Repository**

##Quickstart

> python fires.py
>
> _Beginning prediction_
>
> _302 Correct predictions_
> _163 Incorrect predictions_
> _34 False Positives (Predicted fire but actually not)_
> _0 False Negatives (Predicted no fire, actually was)_
> _62 Near misses (Off by 1 class)_
> _67 Severe misses (off by more than 1 class)_


##Overview
First and foremost, nothing has been written here that has not already been investigated by Cortez and Morais in their generous donation of the above-referenced data set out of the UCI Machine Learning repository.  I instead sought to expand their classification system employed to move away from a regression system instead to a more classification-oriented design that seeks to output a _'level of severity'_ of fire as opposed to continuous prediction of land area burned. 

After some initial attempts to simply replicate results obtained from the discussion on the UCI page mentioned above, it seemed to be apparent that while the predicted values were close, they didn't give any particularly useful information in terms of the _general severity_ of a coming fire.  This is where I decided to instead group the values together into somewhat arbitrary categories.  Where it gets more interesting, however, is how close these arbitrary categories actually are to what a real-world firefighter might want. 

###Differences
The dataset, while incredibly clean, actually needed some slight modification from its initial form.  I first started by cleaning all values within the enclosed .csv file by removing any commas and unnecessary formatting as well as sorting the data by output area burned (usefor for finding these arbitrary classes).

Careful, since I sorted on output area, we have to **>>>random.shuffle()** the data after we read it in.  We're allowed to get away with this since there aren't too many rows to hold in memory.

From here, I also decided to discretize the 'day' and 'month' values in the set into appropriate integers spread over the appropriate numbers of features (e.g. Monday -> 1 -> (1, 0, 0, 0, 0, 0, 0), March -> 3 -> (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)).  This seemed to be a more accurate way of giving our SVM the data vs. weighting months.  Give it more neurons? Wait, wrong classifier... </sarcasm>

