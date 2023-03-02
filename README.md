# AVA-Bot
initié instances AWS (avec unbuntu)
git clone une branche
bash insatall.sh
bash env_var_setup.sh
crontab -e
option 1
rajouter en bas du code : 0 * * * * python3 AVA-Bot/src/app/LiveBot/BotTrading.py >> cronlog.log
