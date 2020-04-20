# TDI-Challenge

TDI Challenge consists of 3 sections. **Python** is used as the primary tool for scripting. **Jupyter notebook** is used as the IDE. 

## 1. Proposed Project:
### College Completion 
Over the past decade, I had the opportunity to work and serve both at the community college level and university level. I found the distribution of available resources and student demographics to be different. Naturally, as a researcher and professor, I was curious to find out the impact of disparities on students' performance outcome. Picking a metric to evaluate such hypothesis is not trivial. However, many scholars in the field of education believe that "student completion" (AKA graduation rate) is a relatively thorough metric. Therefore, for the proposed project I am using a publicly available dataset gathered from nearly all degree-granting institutions in the US to compare the completion rate within 4-year and 2-year colleges. Additionally, the dataset includes the students' completion based on various factors such as race, the state, gender and year.

#### Step 1: College Completion Dataset

**Source**

The link to the publicly available dataset and summary is provided [here](https://data.world/databeats/college-completion/workspace/project-summary?agentid=databeats&datasetid=college-completion). 
These data were pulled from the College Completion microsite produced by The Chronicle of Higher Education with support from the Bill & Melinda Gates Foundation. 

**About the data**

**_The institutions_**

College Completion examines data and trends at 3,800 degree-granting institutions in the United States (excluding territories) that reported a first-time, full-time degree-seeking undergraduate cohort, had a total of at least 100 students at the undergraduate level in 2013, and awarded undergraduate degrees between 2011 and 2013. It also includes colleges and universities that met the same criteria in 2010.

**_Graduation rates_**

Graduation data from the National Center for Education Statistics’ Integrated Postsecondary Education System is limited to tracking completions for groups of first-time, full-time degree-seeking students at the undergraduate level.

**_Race and ethnicity_**

Until 2009, the NCES classified students in seven ways: White, non-Hispanic; Black, non-Hispanic; American Indian/Alaskan Native; Asian/Pacific Islander; unknown race or ethnicity; and nonresident. In addition to creating a stronger separation between race and ethnicity categories, two new race categories were created: Native Hawaiian or Other Pacific Islander (previously combined with Asian students) and students who belong to two or more races.

**_Efficiency measures_**

“Awards per 100 full-time undergraduate students” includes all undergraduate-level completions reported by the institution to the NCES: bachelor’s degrees, associate degrees, and certificate programs of less than four years in length. Full-time-equivalent undergraduates are estimated from the number of credit hours taken at the institution in an academic year. To account for changes in enrollment, the resulting metric is a three-year average of data from 2011, 2012, and 2013.

#### Step 2: Exploratory Data Analysis

First, I import the required libraries: NumPy, Pandas, Matplotlib and Seaborn. Then I import the dataset. I check the data and calculate the key statistics on all numeric columns. I use pairplots to find any correlation between data or catch any trends in the beginning. Now I have a good glimpse of the data. Next, I would like to explore any relationship between graduation rate and race between males and females. Heatmap seems like a good choice and in fact it yields a beautiful graph. Moreover, I would like to find out the graduation rate nationwide and rank all states accordingly. Bar graphs seems the right choice. Moreover, I am interested in producing an interactive plot of the US with each state indicating the graduation rate using Chart Studio package. 

#### Step 3: Data Modeling, Prediction and Evaluation

The next step is to pick a model to fit the data. Having experience with neural network in the past, I am inclined to use ANN for modeling and predictions for this dataset. However, I need to prepare the data furthermore before feeding it to my model. Most importantly, I replace the categorical variables with dummy variables. Split the data into test, validation, and train subsets. 


## 2. Medicare Part D Prescription Drug coverage
### Data Manipulation

The Center for Medicare & Medicaid Services publishes aggregate information on Medicare Part D Prescription Drug coverage. We will be investigating their "Provider Summary Table", which reports on the prescriptions covered by Medicare Part D for each health-care provider. The first questions will address only data from 2017. The last two questions compare the 2017 data with 2016 data. The NPI code can be used to track providers across years.

I insert Numpy, Pandas, 2017 and 2016 datasets. Gather the head, info, and description of the data. Using groupby, pivot_tables and merge seems very useful for this section.

## 3. Coins Payment Problem:
### Statistics and Probability
I answer the coin payment problem by writing a simple algorithm calculating the payment for N number of coins and find the mean and standard deviation via simulation.
