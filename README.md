# cse6242-final-project


## Data Collection
All data collection information is contained in data_collection folder and its README


## Description
### emotion_barchart.html
1. Bar chart of relevant data against time. Segmented by sentiment. Use the selector to choose variable to examine out of "Number of tweets", "Number of sensitive tweets", "Likes" and "Retweets". Choose check boxes to filter out positive, negative and neutral tweets. Data aggregated weekly
2. Bar chart of relevant data against time. Segmented by emotion. Use the selector to choose relevant variables outs of "Number of Tweets", "Number of Sensitive Tweets", "Likes" and "Retweets". Choose check boxes to filter by "Fear", "Surprise", "Happy", "Anger" and others. Data aggregated weekly
3. Scatter plots of columns. Choose independent and dependent variables from lists of date, sentiments, emotions and vaccination status. Each circle represents one tweet.
All plots built with D3, JavaScript, HTML and CSS. Tested with data sampled from Twitter API. Please see https://observablehq.com/@d3/histogram and https://observablehq.com/@d3/scatterplot from the creators of D3 for more information

### choropleth.html
1. Map of Traditional (Positive/Negative Dimensions) Sentiment and Emotion (Happy, Angry, Suprise, Sad, and Fear Dimensions) Sentiment across the months of 2021 and 2022. The dimension which has the highest value compared to the other dimensions are displayed. Use the radio to toggle between visualizing Positive/Negative and Emotion. Use the slider to change the month that is visualized. A legend is also displayed.
2. Hover over the state to view more metadata about the state. 
    1. The Sentiment Values on each dimension are shown at one section.
    2. Next section shows the Vaccine Rate information. The First and Second Dose Vaccine Rates are shown. The Difference in vaccine rates from the previous month is also shown. For the first month, the previous month is assumed to be zero. Notice a negative difference might be due to population decrease.
    3. Next Section shows the political leaning of the state. This information is from the the results of the 2020 election.
    4. The last tweet shows the top tweet during that month. This can represent the state's overall opinion on Covid. We also list the city where this tweet was tweeted from!
3. Click on the state to see the visualization of the First and Second Vaccine Percent Difference by the size of the circle! Also notice that the color of the cirle represents the political leaning of the state: Blue as Democrat and Red as Republican. You might need to zoom out or scroll down to view these visuals!

## Installation
All bar charts and Scatter plots require JavaScript, HTML, CSS and Python in order to execute. Associated D3 packages needed are in dist folder for choropleth.html. For the emotion_barchart.html, D3 and associated packages are loadedfrom Content Delivery Network and does not require installation or extra files.

## Execution
Run a Python http server `python -m http.server 8000` in the root folder

To view the Choropleth, navigate to choropleth.html at localhost:8000 on your web browser in the choropleth folder. Ensure the final.css, election_results.csv, high_like_tweets.csv, and monthly_vax_sentiment_emotion2.csv exists in this folder!

To view the bar charts, navigate to emotion_barchart.html at localhost:8000 in this root folder.
Ensure the data_with_sentiment_and_emotion.csv file exists in the root folder.




