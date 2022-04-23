### Abstract

Cryptocurrencies are playing a pivotal role in digitalizing money. With the exponential rise in the previous decade, the cryptocurrency market is a three trillion-dollar market attracting many new investors every day. In our work, we aim to help new cryptocurrency investors devise an investment strategy through ex-post-facto research. We use 2-sample one-tailed T-tests to compare group means and aim to test the statistical difference. We test if tokens give better returns than coins and if minable coins give better  returns than non-mineable ones. We also test the market sentiment if Mondays give better results than  investments on other weekdays. The final method aims to detect a time-lagged cross-correlation between  traded volume and daily average returns. At a significance level of 0.05, we get statistically significant results with a p-value of 4.385e-06(p<0.0001) and 0.03825 for the first two testsrespectively. For the third  test, we do not have enough evidence to reject the market sentiment. For the correlation test, we found  a -0.15 correlation for log return and traded volume with a one-day lag. From the investor’s point of view, our work suggests that investing in tokens over coins gives better returns. If the investor still wants to invest in coins, mineable is better than non-mineable. The investor can invest on any of the days. We  would recommend an investor trade a particular cryptocurrency if it had a low return the previous day.


### Introduction
The cryptocurrency market is a three trillion-dollar industry [1] attracting many new investors daily. Over the past decade, the overall market growth has been exponential, and its assets gained wide acceptance as digital currencies. Its decentralized nature offers freedom to the user, keeping their transactions 
confidential and unforgeable. Cryptocurrencies are also playing a pivotal role in digitalizing money. Like  the equities stock market, we see a variety of products and categories in the cryptocurrency market. 

Apart from the benefits offered above, the cryptocurrency market has some caveats. Its inherent market  traits – high volatility, unregulated structure – are the primary concerns that drive away many traditional and new investors to appreciate its potential and adapt. We followed a structured approach of breaking down the bigger question into multiple smaller hypotheses through our analysis.

### Goal and Motivation
Our analysis aims to help new cryptocurrency investors devise an investment strategy through ex-postfacto research. As it is a growing and volatile market, the motivation for this project is to understand the cryptocurrency market dynamics and how knowing it better can help us formulate and suggest more 
informed investment decisions to new investors. Our motivation is curiosity-driven too. We read about many market sentiments that sprout from  empirical studies. We were curious to see if these sentiments have any statistical significance. Hence, we  performed statistical tests on a couple of market sentiments - returns on Mondays are significantly higher than on other days of the week, the impact of traded volume on price returns.

![flowchart](/Documentation/Cryptocurrency.PNG)

### Problem Scope
The analysis was performed on the historical data of cryptocurrency returns and volume from November  2019 to November 2020. The trade date range was limited to 1 year in 2020 as it captures the properties of the matured market, which began during the start of the decade. It also contains recent trends of cryptocurrencies like Dogecoin, which gathered public attention over the last few years. The date range also captures a good picture of volatility and market reaction to the COVID pandemic.
After the background research, we finalized the below questions which we analyzed in detail 

1. Do coins and tokens have the same average yearly returns?
2. 2. Do mineable and non-mineable coins have the same average yearly returns?
3. 3. Are Mondays more favorable for trading cryptocurrencies?
4. 4. Is there a cross-correlation (or lagged correlation) between traded volume and returns in the 
cryptocurrencies?

### Dataset 
The dataset used for this analysis is “Historical data on the trading of cryptocurrencies”
. The dataset contains daily trading data for 4137 crypto coins and tokens. It has a total of 5 years of data from Dec 2015 to Nov 2020 with 2.4M records. The data is collected from multiple cryptocurrency trading platforms. As stated in the above section, the current analysis is limited to the most recent 1-year period i.e., November 2019 to November 2020. Each record in the dataset has the attributes - Trade Date,  Volume, Price USD, Market cap, Capitalization Change 1day, USD Price change 1day, Crypto Name, Crypto Type, Ticker, Max Supply, Site URL, GitHub URL, Mineable, Platform Name, and Industry Name. Along with  these, we derive a few aggregate fields for better statistical analysis which are further discussed in each hypothesis test.
