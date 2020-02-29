# HW4: Learning Processes & Threads

## Task 1
Using the twitter feed, construct a daily video summarizing a twitter handle day <br/>
Convert text into an image in a frame <br/>
Do a sequence of all texts and images in chronological order. <br/>
Display each video frame for 3 seconds <br/>

Using tweepy to grab tweets and then put them in an image with background. <br/>
In this assignment I use tweets from Boston University. <br/>

## Task 2
Establish a processing criteria:<br/>
How many API calls you can handle simultaneously and why? <br/>
For example, run different API calls at the same time?<br/>
Split the processing of an API into multiple threads?<br/>
Recommendation for working on the homework:  <br/>
### Step 1:
Develop a queue system that can exercise your requirements with stub functions.
### Step 2: 
Develop the twitter functionality with an API
### Step 3:
Integrate them
Include tracking interface to show how many processes are going on and success of each
### Test
- create a folder named "tweets" to hold all the tweets.
- Run the file ```queue_sys.py```
```
python queue_sys.py
```
<p align="middle">
  ![terminal](https://github.com/BUEC500C1/video-Yufeng-L/blob/master/task2/result.png)
</p>
### Videos Created 
<p align="middle">
  Since those videos are large, (rejected by Github, here is the screenshot after running queue)
</p>
![videocreated](https://github.com/BUEC500C1/video-Yufeng-L/blob/master/task2/videoscreated.png)
###  Images Grabbed
<p align="middle">
  In tweets folder in task2, sample images grabbed are shown.
</p>
![images](https://github.com/BUEC500C1/video-Yufeng-L/blob/master/task2/imagesgrabbed.png)

### CPU Usage when calling multiple APIs
![cpuuse](https://github.com/BUEC500C1/video-Yufeng-L/blob/master/task2/callingapi.png)





