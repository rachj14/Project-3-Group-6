# Project-3-Group-6 - Rachel, Malini, Masih and Rafi

# Project Title: Exploring different factors impacting Mental Health

## Introduction:
Mental health is a pressing concern influenced by various environmental and lifestyle factors. This project aims to investigate the relationship between music consumption, social media usage, air pollution levels, and mental health outcomes using data available on Kaggle. Through efficient data analysis and visualization techniques, we aim to uncover insights that may inform future research or interventions.

## Objectives:
- Analyse survey results on music consumption habits, social media usage patterns, air pollution exposure, and self-reported mental health indicators.
- Identify correlations between these factors to understand their potential impact on mental well-being.
- Create clear and concise visualizations using Python's Matplotlib library to present findings.
- Develop a preliminary interactive dashboard prototype using Flask and basic JavaScript functionality for data exploration.

## Methodology:
- Data Collection: Utilise provided datasets on music & mental health, social media & mental health, and air pollution & mental health surveys.
- Data Preprocessing: Quickly clean and preprocess the survey data using Python's Pandas library to handle missing values and merge datasets if necessary.
- Exploratory Data Analysis (EDA): Conduct brief EDA to identify initial trends and correlations in the datasets. Use Matplotlib to create simple visualizations such as bar plots, scatter plots, or pie charts.
- Statistical Analysis: Perform basic statistical analysis to assess correlations between music, social media, air pollution, and mental health variables.
- Dashboard Development: Develop a basic web-based dashboard prototype using Flask for the backend and minimal JavaScript for simple interactivity.

## Expected Deliverables:
- Preliminary analysis report summarizing key findings and insights.
- Simple visualizations showcasing correlations between factors.
- Basic interactive dashboard prototype allowing for limited data exploration.

## Research Questions:
1. The effects of music on mental health.
2. The effects of social media use on mental health.
3. The effects of air pollution on mental health.
4. The effects of unemployment on mental health.

## Datasets Stored in Databases:
- Social media dataset: social_media.csv file imported and stored in a MongoDB database as "mentalhealthDB". Class "social_media" created to store the documents, as shown below.
<img width="1432" alt="Screenshot 2024-04-03 at 9 50 14 pm" src="https://github.com/rachj14/Project-3-Group-6/assets/151903302/faefa0b1-b5f2-4dea-8c33-4e9bb9be59d3">

## Interacting and Using the Project:
1. Run App.py and then copy the address into your webpage.
2. This will open our homepage "Mental Health" dashboard. This shows a bar graph and map view of the mean Mental Health scores across the world. Select a different county using the drop-down menu.
3. Scroll down to the bottom and select the "Music Page" link which will direct you to a html page with analysis of how music impacts mental health.
4. Navigate back to the Mental Health dashboard homepage. Now, click on the "Social Media Page" link to direct you to the html page with analysis of how social media impacts mental health.

## Ethical Considerations:
- An ethical consideration with using the Social Media dataset is that the dataset captured personal information such as the respondents' age, gender and relationship status, which can be used as identifiers of an individual if the responses are to be kept anonymous.
- The dataset also includes data such as the state of the respondent's mental health, which could be considered as sensitive.

## Conclusion:
This project aims to provide a preliminary exploration of the relationships between music, social media, air pollution, and mental health.  

## Resources:
https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results
Music & Mental Health Survey Results - 
Survey results on music taste and self-reported mental health

https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health
Social Media and Mental Health - 
Correlation between Social Media use and General Mental Well-being

https://www.kaggle.com/datasets/programmerrdai/mental-health-dataset
Worldwide Mental Health dataset - 
Identifying the trend of Mental Health Issues 

https://www.kaggle.com/datasets/michaelacorley/unemployment-and-mental-illness-survey/data
Unemployment and Mental Health - 
Exploring the causation of high unemployment among the mentally ill

