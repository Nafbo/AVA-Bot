# AVA-Bot
<p>AVA Bot is a trading robot that will help you make money without you having to do anything.</p>
<p>Thanks to CCXT and BitGet API, we give you the possibility to have  functional trading strategy but not only Indeed thanks to the anlayse of the sentiments of the crypto currencies market, with the help of the Twitter API, the Fear and Greed and the scrapping of the FED website, we realize an accurate analysis of the sentiments of this so complex market that are the crypto currencies.</p> 
<p>But in parallel, using the ccxt api, we carry out an analysis of the market using several indicators.</p>
<p>All this allows us to have a reliable and testable strategy, which we use in our automated trading robot.</p>
<p>With this trading robot you will be able to choose the way it works, the risk you accept in your trade but also the crypto currencies you want to trade and how many simultaneous open positions you want.</p>
<p>To visualize all these features, we have developed a React application , which is deployable locally, or globally using AWS.</p>
<p>Finally, we have linked a database to our app, in this way your informations remains when you log into your account.</p>


## Deploy the sentimental strategy (in AWS)
<p>First you need to have an AWS account and connect to it (on the root service).</p>
<p>You need to create an EC2 instances and to connect to it. I invite you to follow this tutorial to do it.<p>
<p><link>https://www.youtube.com/watch?v=lxSNeF7BAII&ab_channel=StephaneMaarek</link></p>
<p>When you are connect to your command terminal you need to clone the LiveBot branch of this github:</p>
<pre><code>git clone --single-branch --branch SentimentalStrategy https://github.com/Nafbo/AVA-Bot.git</code></pre>
<p>After you need to install the different package (updates and requirements):</p>
<pre><code>bash insatall.sh</code></pre>
<pre><code>bash env_var_setup.sh</code></pre>
<p>Check that your code works properly by running it:</p>
<pre><code>python3 AVA-Bot/main.py</code></pre>
<p>When your code is ready, you need to créate a crontab to have your code run every 15 min:</p>
<pre><code>crontab -e</code></pre>
<p>Chosoe the 1 option.</p> 
<p>Added at the end of the displayed code the following line to confirm the automatic launch of the code</p>
<pre><code>*/15 * * * * python3 AVA-Bot/main.py >> cronlog.log</code></pre>
<p>The cronlog.log file will be your error history or what is returned by your code.</p>


## Deploy your trading bot (in AWS)
<p>You need to create an other EC2 instances and connect it:</p>
<p>Clone the LiveBot branch in the instances</p>
<pre><code>git clone --single-branch --branch LiveBot https://github.com/Nafbo/AVA-Bot.git</code></pre>
<p>After you need to install the different package (updates and requirements):</p>
<pre><code>bash insatall.sh</code></pre>
<pre><code>bash env_var_setup.sh</code></pre>
<p>Check that your code works properly by running it:</p>
<pre><code>python3 AVA-Bot/main.py</code></pre>
<p>When your code is ready, you need to créate a crontab to have your code run every hour:</p>
<pre><code>crontab -e</code></pre>
<p>Chosoe the 1 option.</p> 
<p>Added at the end of the displayed code the following line to confirm the automatic launch of the code</p>
<pre><code>0 * * * * python3 AVA-Bot/main.py >> cronlog.log</code></pre>
<p>The cronlog.log file will be your error history or what is returned by your code.</p>
<p>You have now a ready trading Bot with all the strategy.</p>


