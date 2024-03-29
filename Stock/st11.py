import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as data
import yfinance as yf
from keras.models import load_model
import streamlit as st
import plotly.graph_objs as go
import datetime
import sklearn 
import streamlit.components.v1 as components

import streamlit as st    
st.title("Stock Market Analysis")
today = datetime.date.today()
start = '2010-01-01'
end = today.strftime('%Y-%m-%d')
st.sidebar.title("Predictive Analysis of Stock Market Trends:           ")
user_input = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL",key="stock_symbol")

df = yf.download(user_input, start=start, end=end)

model=load_model("keras model.h5")


    #Splitting Data into Training and Testing using MinMaxScaler

data_training = pd.DataFrame(df['Close'][0: int(len(df)*0.70)])
data_testing= pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
data_training_array= scaler.fit_transform(data_training)
data_testing_array= scaler.fit_transform(data_testing)


past_100_days = data_training.tail(100)
final_df = past_100_days._append(data_testing, ignore_index=True)

input_data=scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

x_test , y_test =np.array(x_test) , np.array(y_test);

    #predication making
test_predication = model.predict(x_test)
scaler.scale_

scaling_factor = 1/scaler.scale_[0]
y_test = y_test*scaling_factor
test_predication=test_predication*scaling_factor

# Sidebar navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Stock Analysis", "Predection","Chattbot","Stock News"])

if page == "Home":
    
    # Apply custom CSS to style the Home page
    st.markdown("""
        <style>
            body {
                background-color: #fff;
                color: #000;
            }

            .home-container {
                background-color: #000;
                color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
            }

            nav {
            display: flex;
            justify-content: center;
            background-color: #000;
            padding: 10px;
            margin-top: 20px;
            }

            nav a {
                color: #fff;
                margin: 0 15px;
                text-decoration: none;
                font-weight: bold;
                font-size: 18px;
                transition: color 0.3s ease-in-out, background-color 0.3s ease-in-out;
                padding: 8px 16px;
                border-radius: 8px;
            }

            nav a:hover {
                color: #3498db;
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }

            .about-contact-container {
            display: flex;
            justify-content: space-around;
            margin-top: 30px;
        }

        .about-contact-card {
            background-color: #fff;
            color: #000;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 45%;
            transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
        }

        .about-contact-card:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # HTML content for the home page
    st.markdown("""
        <div class="home-container">
            <header style="text-align: center; background-color: #000; padding: 40px; color: #fff;">
                <h1 style="font-size: 48px; margin: 0; font-family: 'Arial Black', sans-serif; letter-spacing: 2px;">
                    Stock Prediction And Analysis</h1>
            </header>    
            <nav>
                <a href="/">Home</a>
                <a href="/browse">Stock Analysis</a>
                <a href="/feedback">Predictions</a>
                <a href="/about">Chatbott</a>
                <a href="/contact">Stock News</a>
                <a href="/login">About Us</a>
            </nav>
            
        <div class="about-contact-container">
            <div class="about-contact-card">
                <h2>About Us</h2>
                <p>Why Choose Us?<br> Elevate insights with Moving Average for trend precision, visualize forecasts vividly using Matplotlib, and stand out in stock market analysis with captivating visuals.</p>
                </div>
            <div class="about-contact-card">
                <h2>Our Team</h2>
                <p>Connect with our talented team for inquiries, support, or collaboration opportunities.<br>
                Developed by- Team Aztecs
                </p>
            </div>

    """, unsafe_allow_html=True)

elif page == "Stock Analysis":


    st.subheader("Data from 2010 to 2023")
    data1 = pd.DataFrame(df)

    st.dataframe(data1.tail(15))


    #Closing price with month and year using moving average
    fig_all = plt.figure(figsize=(18, 12))
    plt.plot(df.Close)

    ma30 = df.Close.rolling(30).mean()
    fig_ma30 = plt.figure(figsize=(12, 6))
    plt.plot(ma30)

    ma365 = df.Close.rolling(365).mean()
    fig_ma365 = plt.figure(figsize=(12, 6))
    plt.plot(ma365)

    button_container = st.columns(3)

    # Create buttons for each plot
    if button_container[0].button("Show Closing Prices"):
        st.subheader("Closing Price VS Time Chart")
        st.pyplot(fig_all)

    if button_container[1].button("Show MA30"):
        st.subheader("Closing Price of 30 days")
        st.pyplot(fig_ma30)

    if button_container[2].button("Show MA365"):
        st.subheader("Closing Price of 365 days")
        st.pyplot(fig_ma365)
    #load my model
    model=load_model("keras model.h5")


    #Splitting Data into Training and Testing using MinMaxScaler

    data_training = pd.DataFrame(df['Close'][0: int(len(df)*0.70)])
    data_testing= pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))
    data_training_array= scaler.fit_transform(data_training)
    data_testing_array= scaler.fit_transform(data_testing)


    past_100_days = data_training.tail(100)
    final_df = past_100_days._append(data_testing, ignore_index=True)

    input_data=scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test , y_test =np.array(x_test) , np.array(y_test);

    #predication making
    test_predication = model.predict(x_test)
    scaler.scale_

    scaling_factor = 1/scaler.scale_[0]
    y_test = y_test*scaling_factor
    test_predication=test_predication*scaling_factor

    st.subheader("predication vs orignal")
    fig2=plt.figure(figsize=(12,6))
    plt.plot(y_test, 'b', label = 'Original Price')
    plt.plot(test_predication,'r', label ='Preditemp_inputcted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig2)
    

elif page == "Predection":
    st.title("Stock Market Analysis")

    # demonstrate prediction for next 50 days  with closing price
    x_input=data_testing_array[len(data_testing_array) - 100:].reshape(1,-1)
    opening=list(x_input)
    opening=opening[0].tolist()

    from numpy import array
    lst_output=[]
    n_steps=100
    i=0
    while(i<50):

        if(len(opening)>100):
            #print(opening)
            x_input=np.array(opening[1:])
            #print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)
            #print("{} day output {}".format(i,yhat))
            opening.extend(yhat[0].tolist())
            opening=opening[1:]
            #print(opening)
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input = x_input.reshape((1,n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            opening.extend(yhat[0].tolist()) 
            lst_output.extend(yhat.tolist())
            i=i+1

    lst_output=scaler.inverse_transform(lst_output)
    arr = lst_output



    #opening
    #Splitting Data into Training and Testing

    data_training_open = pd.DataFrame(df['Open'][0: int(len(df)*0.70)])
    data_testing_open= pd.DataFrame(df['Open'][int(len(df)*0.70): int(len(df))])
    from sklearn.preprocessing import MinMaxScaler
    scaler_open = MinMaxScaler(feature_range=(0,1))

    data_testing_array_open= scaler_open.fit_transform(data_testing_open)
    x_input_open=data_testing_array_open[len(data_testing_array_open) - 100:].reshape(1,-1)
    temp_input_open=list(x_input_open)
    temp_input_open=temp_input_open[0].tolist()

    from numpy import array

    lst_output_open=[]
    n_steps=100
    i=0
    while(i<50):

        if(len(temp_input_open)>100):
            #print(temp_input)
            x_input_open=np.array(temp_input_open[1:])
            #print("{} day input {}".format(i,x_input_open))
            x_input_open=x_input_open.reshape(1,-1)
            x_input_open = x_input_open.reshape((1, n_steps, 1))
            #print(x_input)
            yhat_open = model.predict(x_input_open, verbose=0)
            
            temp_input_open.extend(yhat_open[0].tolist())
            temp_input_open=temp_input_open[1:]
            #print(temp_input)
            lst_output_open.extend(yhat_open.tolist())
            i=i+1
        else:
            x_input_open = x_input_open.reshape((1,n_steps,1))
            yhat_open = model.predict(x_input_open, verbose=0)
            temp_input_open.extend(yhat_open[0].tolist())
            lst_output_open.extend(yhat_open.tolist())
            i=i+1

    lst_output_open=scaler_open.inverse_transform(lst_output_open)
    arr_open = lst_output_open

    #High
    #Splitting Data into Training and Testing

    data_training_high = pd.DataFrame(df['High'][0: int(len(df)*0.70)])
    data_testing_high= pd.DataFrame(df['High'][int(len(df)*0.70): int(len(df))])
    from sklearn.preprocessing import MinMaxScaler
    scaler_high = MinMaxScaler(feature_range=(0,1))

    data_testing_array_high= scaler_high.fit_transform(data_testing_high)
    x_input_high=data_testing_array_high[len(data_testing_array_high) - 100:].reshape(1,-1)
    temp_input_high=list(x_input_high)
    temp_input_high=temp_input_high[0].tolist()

    from numpy import array

    lst_output_high=[]
    n_steps=100
    i=0
    while(i<50):

        if(len(temp_input_high)>100):
            #print(temp_input)
            x_input_high=np.array(temp_input_high[1:])
            #print("{} day input {}".format(i,x_input_high))
            x_input_high=x_input_high.reshape(1,-1)
            x_input_high = x_input_high.reshape((1, n_steps, 1))
            #print(x_input)
            yhat_high = model.predict(x_input_high, verbose=0)
            
            temp_input_high.extend(yhat_high[0].tolist())
            temp_input_high=temp_input_high[1:]
            #print(temp_input)
            lst_output_high.extend(yhat_high.tolist())
            i=i+1
        else:
            x_input_high = x_input_high.reshape((1,n_steps,1))
            yhat_high = model.predict(x_input_high, verbose=0)
            temp_input_high.extend(yhat_high[0].tolist())
            lst_output_high.extend(yhat_high.tolist())
            i=i+1

    lst_output_high=scaler_high.inverse_transform(lst_output_high)
    arr_high = lst_output_high

    #low
    #Splitting Data into Training and Testing

    data_training_Low = pd.DataFrame(df['Low'][0: int(len(df)*0.70)])
    data_testing_Low= pd.DataFrame(df['Low'][int(len(df)*0.70): int(len(df))])
    from sklearn.preprocessing import MinMaxScaler
    scaler_Low = MinMaxScaler(feature_range=(0,1))

    data_testing_array_Low= scaler_Low.fit_transform(data_testing_Low)
    x_input_Low=data_testing_array_Low[len(data_testing_array_Low) - 100:].reshape(1,-1)
    temp_input_Low=list(x_input_Low)
    temp_input_Low=temp_input_Low[0].tolist()

    from numpy import array

    lst_output_Low=[]
    n_steps=100
    i=0
    while(i<50):

        if(len(temp_input_Low)>100):
            #print(temp_input)
            x_input_Low=np.array(temp_input_Low[1:])
            #print("{} day input {}".format(i,x_input_Low))
            x_input_Low=x_input_Low.reshape(1,-1)
            x_input_Low = x_input_Low.reshape((1, n_steps, 1))
            #print(x_input)
            yhat_Low = model.predict(x_input_Low, verbose=0)
            
            temp_input_Low.extend(yhat_Low[0].tolist())
            temp_input_Low=temp_input_Low[1:]
            #print(temp_input)
            lst_output_Low.extend(yhat_Low.tolist())
            i=i+1
        else:
            x_input_Low = x_input_Low.reshape((1,n_steps,1))
            yhat_Low = model.predict(x_input_Low, verbose=0)
            temp_input_Low.extend(yhat_Low[0].tolist())
            lst_output_Low.extend(yhat_Low.tolist())
            i=i+1

    lst_output_Low=scaler_Low.inverse_transform(lst_output_Low)
    arr_Low = lst_output_Low

    h = pd.DataFrame(arr_Low, columns=['Low'])

    g = pd.DataFrame(arr_high, columns=['High'])

    f = pd.DataFrame(arr_open, columns=['Open'])

    k =pd.DataFrame(arr, columns=['Close'])



    k['DailyChange'] = k['Close'].diff()
    k['PercentageChange'] = (k['DailyChange'] / k['Close'].shift(1)) * 100
    k['PercentageChange'] = k['PercentageChange'].map("{:.2f}%".format)
    result_df = pd.concat([h, g, f, k], axis=1)


    # def color_negative_red(value):
    #     if value < 0:
    #         return 'color: red'
    #     elif value > 0:
    #         return 'color: green'
    #     else:
    #         return 'color: black'  # Assuming black for zero change

    # Apply conditional formatting to font color based on PercentageChange
    # def color_negative_red_percent(value):
    #     if '%' in value:  # Check if the value contains a percentage sign
    #         value = float(value.replace('%', ''))  # Remove percentage sign and convert to float
    #         if 
    #  < 0:
    #             return 'color: red'
    #         elif value > 0:
    #             return 'color: green'
    #         else:
    #             return 'color: black'  # Assuming black for zero change

    # styled_result_df = result_df.style.applymap(color_negative_red, subset=['DailyChange']) \
    #                                 .applymap(color_negative_red_percent, subset=['PercentageChange'])

    fig = go.Figure(data=[go.Candlestick(x=result_df.index,
                    open=result_df['Open'],
                    high=result_df['High'],
                    low=result_df['Low'],
                    close=result_df['Close'])])

    st.plotly_chart(fig)

    # Display the styled DataFrame using Streamlit
    st.write(result_df)


    fig3= plt.figure(figsize=(12,6))
    plt.plot(k.Close)
    st.pyplot(fig3)

    st.title("Next 5 Years Returns")

    # Input for the stock symbol
    #user_input = st.text_input("Enter the Stock Ticker", "AAPL", key="stock_symbol_input")

    # Check for changes in the input field
    if st.session_state.stock_symbol is not None:
        try:
            # Download historical data
            stock_data = yf.download(user_input, start="2023-01-01", end="2028-01-01")

            if not stock_data.empty and len(stock_data['Adj Close']) >= 2:
                # Calculate returns over the next 5 years
                returns_next_5_years = (stock_data['Adj Close'].iloc[-1] / stock_data['Adj Close'].iloc[0] - 1) * 100

                # Display the returns
                st.write(f"{user_input} returns over the next 5 years: {returns_next_5_years:.2f}%")
                st.write("Recommendation Moodel")

                # Display recommendation with colored box
                if returns_next_5_years >= 0:
                    st.markdown('<div style="padding: 10px; color: white; background-color: green; text-align: center;">Yes</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="padding: 10px; color: white; background-color: red; text-align: center;">No</div>', unsafe_allow_html=True)

            else:
                st.write("Error: Insufficient data for calculating returns.")

        except Exception as e:
            st.write(f"Error: {str(e)}")
    else:
        st.write("Enter a stock symbol to get the returns.")
    # Add content for the analysis page

elif page == "Chatbot":
    # Fetch historical data
        symbol=user_input
        def fetch_stock_data(symbol):
    # Fetch data from Yahoo Finance
                stock_data = yf.Ticker(symbol)
                return stock_data
        try:
            stock = fetch_stock_data(symbol)

            st.write(f"### {symbol} Stock Information")
            st.write(stock.info)

            # Chatbot interaction
            st.write("### Ask a question:")
            question = st.text_input("Type here...")

            if st.button("Ask"):
                if question.lower() == "closing price":
                    st.write(f"The closing price of {symbol} is ${stock.history(period='1d')['Close'].iloc[-1]}")

                elif question.lower() == "opening price":
                    st.write(f"The opening price of {symbol} was ${stock.history(period='1d')['Open'].iloc[0]}")

                elif question.lower() == "volume":
                    st.write(f"The volume of {symbol} traded today is {stock.history(period='1d')['Volume'].iloc[-1]}")

                elif question.lower() == "top gainer":
                    top_gainer = stock.history(period='1d').nlargest(1, 'Close')
                    st.write(f"The top gainer today is {top_gainer.index[0]} with a closing price of ${top_gainer['Close'].iloc[0]}")

                elif question.lower() == "top loser":
                    top_loser = stock.history(period='1d').nsmallest(1, 'Close')
                    st.write(f"The top loser today is {top_loser.index[0]} with a closing price of ${top_loser['Close'].iloc[0]}")

                else:
                    st.write("I'm sorry, I don't understand that question.")

        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")
    
elif page == "Stock News":
    def get_stock_news(ticker, num_news=5):
        stock = yf.Ticker(ticker)
        news = stock.news
        return news[:num_news]

    # Streamlit app content
    st.title("Real-Time Stock News")

    # Sidebar for user input
    ticker = user_input
    num_news = st.sidebar.slider("Number of News Articles", 1, 10, 5)

    # Display stock news
    st.header(f"Latest News for {ticker}")
    news_list = get_stock_news(ticker, num_news)

    for news_item in news_list:
        title = news_item.get('title', 'Title Not Available')
        date = news_item.get('date', 'Date Not Available')
        summary = news_item.get('summary', 'Summary Not Available')
        url = news_item.get('url', 'URL Not Available')

        st.subheader(title)
        st.write(f"Published: {date}")
        st.write(f"Summary: {summary}")
        st.write(f"URL: {url}")
        st.markdown("---")  # Separator between news articles
