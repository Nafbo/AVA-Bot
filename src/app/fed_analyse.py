import requests
import nltk
from selenium import webdriver
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def analyze_fed_news_for_btc():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.federalreserve.gov/newsevents/pressreleases.htm")

    # Cliquez sur la case à cocher pour la politique monétaire
    monetary_policy_checkbox = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[2]/div/div[1]/form/div[4]/div[1]/label/input')))
    monetary_policy_checkbox.click()

    submit_checkbox = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[2]/div/div[1]/form/div[5]')))
    submit_checkbox.click()

    # Cliquez sur l'article le plus récent
    recent_article = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="article"]/div[1]/div[1]/div[2]/p[1]/span/a'))
    )
    recent_article.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='article']/div[3]")))
    text = element.text

    driver.quit()

    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        sentiment = sentiment_analyzer.polarity_scores(sentence)['compound']
        if ("bitcoin" or "crypto" or "cryptomonnaie" or "crypto-actifs") in sentence.lower() and sentiment >= 0.05:
            return "Bonnes nouvelles pour le BTC actuellement:", sentence
        elif ("discount rate" or "credit rate" or "unemployment rate" or "inflation") in sentence.lower() and sentiment >= 0.05:
            return "Bonnes nouvelles pour le BTC actuellement:", sentence
        elif ("discount rate" or "credit rate" or "unemployment rate" or "inflation") in sentence.lower() and sentiment <= -0.05:
            return "Mauvaises nouvelles pour le BTC actuellement:", sentence
        elif ("bitcoin" or "crypto" or "cryptomonnaie" or "crypto-actifs") in sentence.lower() and sentiment <= -0.05:
            return "Mauvaises nouvelles pour le BTC actuellement:", sentence
    else :
        return "FED : pas de nouvelles pour le BTC actuellement"
