Forecasting the Pulse of NYC: An Uber Trip Analysis
My Journey with this Project

I’ve always been fascinated by how cities move — the rush hours, the calm hours, the weekend shifts, and how all of it forms a rhythm. When I found this Uber dataset with over 4.5 million trip records from NYC, I wanted to see if I could do more than analyze it.
I wanted to see if I could predict the city’s behavior.

This project started with a simple question:

Can I accurately forecast hourly Uber demand using machine learning?

The dataset was originally obtained by FiveThirtyEight through a Freedom of Information request. That makes it real, messy, and full of natural patterns — perfect for building a meaningful forecasting model.

The Toolkit I Used

Language: Python

Core Libraries:

pandas and numpy: For cleaning, exploring, and handling millions of rows efficiently.

matplotlib and seaborn: For visualizing demand patterns and trends.

scikit-learn: For implementing baseline machine learning models.

xgboost: The model that ultimately delivered the best accuracy.

streamlit: To deploy the final model into an interactive app.

How I Built It: From Raw Data to a Working Forecast

My process went step-by-step, transforming raw CSV files into a model that predicts the next hour’s Uber demand.

1. Wrangling the Data

The dataset came split across six monthly files (April–September 2014). I combined them into one large dataframe and converted the Date/Time column into a proper datetime format.
This step was essential — nothing works without clean and consistent timestamps.

2. Finding the Patterns (EDA)

Once the data was cleaned, I explored it through visualizations. What stood out right away:

Evening rush hours

Early-morning drops (around 3–5 AM)

Weekend demand spikes

A noticeable trend shift around mid-September

These patterns helped guide the modeling strategy.

3. Teaching the Model to Understand Time

Models don’t understand time by default.
So I created a 24-hour sliding window, meaning:

To predict the next hour, the model looks at the previous 24 hours of demand.

This gave the model a sense of daily cycles and repeated patterns.

4. Training the Models

I trained three main models:

Random Forest

Gradient Boosting (GBRT)

XGBoost

To avoid data leakage, I split the data chronologically, not randomly:

Training: April 1 → September 14

Testing: September 15 onward

XGBoost clearly performed best.

5. Evaluating Performance

I evaluated all models using MAPE (Mean Absolute Percentage Error) because it’s intuitive and works well for demand forecasting.

The final XGBoost model achieved roughly:

≈ 9–10% MAPE,
meaning it predicts hourly demand with over 90% accuracy.

What I Discovered

NYC truly follows a pattern, even hour-to-hour.

Demand is very predictable, especially with the right features.

XGBoost outperformed other models, especially in capturing subtle patterns.

A trend shift in September plays a big role in separating the training/testing periods.

Good feature engineering matters more than fancy models.

Getting This Running Yourself

If you want to try the code or run the app locally, here’s how:

1. Clone the repository
git clone https://github.com/Kunal355/Uber-trip-Analysis.git
cd Uber-trip-Analysis

2. Set up your environment
python -m venv venv
.\venv\Scripts\activate       # for Windows
pip install -r requirements.txt

3. Run the Streamlit app
cd deployment
streamlit run app.py


This will open the interactive prediction app in your browser.

Dataset Source

The dataset used in this project can be found here:
https://www.kaggle.com/datasets/amirmotefaker/uber-dataset-from-april-to-september-2014

Project Structure
Uber-trip-Analysis/
│
├── Uber_Trip_Demand_Forcasting.ipynb     # Full notebook: cleaning, EDA, training
│
├── deployment/
│   ├── app.py
│   ├── hourly_counts.csv
│   ├── uber_xgb_model.pkl
│   ├── requirements.txt
│
└── README.md



Final Thoughts

This project took me from raw messy CSV files to a fully deployed prediction app.
It taught me how real-world forecasting works, how to design features for time-series problems, and how powerful models like XGBoost can be.

If you're interested in urban data, forecasting, or machine learning, this project is a great example of how these pieces come together.
