import requests as rq

class Telegram ():
    def __init__(self, chat_id):
        self.TOKEN = '6091261455:AAEQ6ZZlLqkLYyNOOZkDpujQJ3dyLjAfzj8'
        self.chat_id = chat_id
    
    def  message (self, position, crypto, usdInvest, price, leverage, stopLoss, takeProfit):
        if position == 'openLong':
            message = ("Bonjour, 👋\n\n"
                        "🚨 Je suis ravi de vous informer que j'ai ouvert une nouvelle position pour vous.🚨 \n\n"
                        "Voici les détails de la transaction : 📈 \n\n"

                        "       Crypto : ", crypto, "\n"
                        "       Type de position : open long\n"
                        "       Usd Investit :", usdInvest,"\n"
                        "       Prix d'ouverture : ", price ,"\n"
                        "       Leverage : ", leverage ,"\n"
                        "       Stop loss : ", stopLoss, "\n"
                        "       Take profit : ", takeProfit ,"\n\n"

                        "Je surveillerai attentivement l'évolution de cette position et vous informerai de tout changement important. 📣\n\n"

                        "Cordialement,\n"
                        "Votre AVA Bot de trading. 🤖")
        
        elif position =='openShort':
            message = ("Bonjour, 👋\n\n"
            "🚨 Je suis ravi de vous informer que j'ai ouvert une nouvelle position pour vous.🚨 \n\n"
            "Voici les détails de la transaction : 📉 \n\n"

            "       Crypto : \n"
            "       Type de position : \n"
            "       Usd Investit : \n"
            "       Prix d'ouverture : \n"
            "       Stop loss : \n"
            "       Take profit : \n\n"

            "Je surveillerai attentivement l'évolution de cette position et vous informerai de tout changement important. 📣\n\n"

            "Cordialement,\n"
            "Votre AVA Bot de trading. 🤖")
            
        elif position == 'closeLongPosition' :   
            message = ("Bonjour, 👋\n\n"
                "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
                "Voici les détails de la transaction : 📈 \n\n"

                "       Crypto : \n"
                "       Type de position : \n"
                "       Fermeture par: \n"
                "       Performance : \n"
                "       Usd Gagné/Perdu: \n"
                "       Prix de fermeture : \n\n"
                
                "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

                "Cordialement,\n"
                "Votre AVA Bot de trading. 🤖")
            
        elif position == 'closeShortpopsition':
            message = ("Bonjour, 👋\n\n"
                        "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
                        "Voici les détails de la transaction : 📉 \n\n"

                        "       Crypto : \n"
                        "       Type de position : \n"
                        "       Fermeture par: \n"
                        "       Performance : \n"
                        "       Usd Gagné/Perdu: \n"
                        "       Prix de fermeture : \n\n"
                        
                        "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

                        "Cordialement,\n"
                        "Votre AVA Bot de trading. 🤖")
            
        elif position == 'stopLossHit':
            message = ("Bonjour, 👋\n\n"
                        "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
                        "Voici les détails de la transaction : 📉 \n\n"

                        "       Crypto : \n"
                        "       Type de position : \n"
                        "       Fermeture par: \n"
                        "       Performance : \n"
                        "       Usd Gagné/Perdu: \n"
                        "       Prix de fermeture : \n\n"
                        
                        "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

                        "Cordialement,\n"
                        "Votre AVA Bot de trading. 🤖")
            
        elif position == 'takeProfitHit':
            message = ("Bonjour, 👋\n\n"
                        "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
                        "Voici les détails de la transaction : 📉 \n\n"

                        "       Crypto : \n"
                        "       Type de position : \n"
                        "       Fermeture par: \n"
                        "       Performance : \n"
                        "       Usd Gagné/Perdu: \n"
                        "       Prix de fermeture : \n\n"
                        
                        "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

                        "Cordialement,\n"
                        "Votre AVA Bot de trading. 🤖") 
            
        url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(self.TOKEN, self.chat_id, message)
        rq.get(url).json()
        return(message)
    
    
if __name__ == '__main__':
    chat_id = "6210537537"
    telegram = Telegram(chat_id)
    telegram.message('openLong', crypto = 'BTC/USDT', usdInvest = 19, price = 190, leverage = 2, stopLoss = 1829, takeProfit = 345)