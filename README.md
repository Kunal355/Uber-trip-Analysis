# Forecasting the Pulse of NYC: An Uber Trip Analysis

##  My Journey with this Project

I've always been fascinated by the rhythms of a big city. When I found this dataset—a massive log of over 4.5 million Uber trips in NYC—I saw an opportunity to do more than just crunch numbers. I wanted to see if I could teach a machine to understand and predict the city's pulse.

This project is my journey into doing just that. It started with a simple question: **Can I accurately forecast the demand for Ubers on an hourly basis?**

The data itself has a cool backstory: it was originally obtained by the news site FiveThirtyEight through a Freedom of Information request. This means it's real, messy, and reflects the actual state of NYC back in 2014. My goal was to turn this raw data into a story and, ultimately, a predictive tool.

---

## 🛠 The Toolkit I Used

*   **Language:** Python
*   **Core Libraries:**
    *   `pandas` & `numpy`: My go-to tools for wrangling and exploring the data.
    *   `matplotlib` & `seaborn`: For bringing the data to life through visualizations.
    *   `scikit-learn`: The foundation for my machine learning pipeline.
    *   `xgboost`: The heavy-hitter I brought in to get the best possible predictive performance.

---

##  How I Built It: From Raw Data to a Working Forecast

My process wasn't a straight line, but it followed a few key stages:

1.  **Wrangling the Data:** The first step was messy. I had to combine six different monthly CSV files and wrestle the `Date/Time` columns into a format Python could understand. This was the crucial foundation for everything that followed.

2.  **Finding the Patterns (EDA):** This was the fun part! I started plotting the data to see what stories it would tell. I immediately saw clear patterns: the morning lulls, the evening rush, and the weekend spikes. This confirmed that the demand wasn't random—it was predictable.

3.  **Teaching the Model to See Time:** A machine learning model doesn't inherently understand time. I had to engineer features to give it context. I settled on a "sliding window" approach: to predict the next hour's demand, the model looks at the demand from the previous 24 hours. This helps it learn daily cycles.

4.  **Choosing and Training the Models:** I started with a solid baseline, **Random Forest**, which is great for its stability. Then, to push for higher accuracy, I moved to **XGBoost**, a more powerful algorithm known for winning data science competitions. I was careful to split my data chronologically to avoid the classic mistake of letting my model "peek" into the future.

5.  **Checking My Work:** I evaluated my models using the Mean Absolute Percentage Error (MAPE). My final XGBoost model achieved a **MAPE of 8.37%**, which I was really happy with. It means, on average, my hourly forecast is off by less than 9%.

---

##  What I Discovered

*   **The City Never Sleeps (but it does nap):** The data clearly shows demand dropping off around 4-5 AM before roaring back to life for the morning commute.
*   **XGBoost is a Powerhouse:** While Random Forest did a good job, XGBoost's ability to learn from its mistakes sequentially really made a difference in accuracy.
*   **Forecasting is More Than a Hunch:** This project proved that we can move beyond guesswork and use data to make highly accurate predictions about human behavior, which has huge implications for logistics and resource management.

---

##  Getting this Running Yourself

Want to dive in and play with the code? Here’s how:

1.  **Clone this repo:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/uber-trip-forecasting.git
    cd uber-trip-forecasting
    ```

2.  **Set up your environment:**
    ```bash
    # I recommend using a virtual environment
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Grab the data:**
    *   You can find the dataset on [Kaggle](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city ).
    *   Create a `data` folder in this project and drop the `uber-raw-data-*.csv` files in there.

