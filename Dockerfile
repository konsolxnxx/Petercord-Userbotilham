# We're using Ubuntu 20.10
FROM xnewbie/xbotrmx:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b pocong https://github.com/X-Newbie/Xbot-Remix /home/userbot/
RUN mkdir /home/userbot/bin/
WORKDIR /home/userbot/

CMD ["python3","-m","userbot"]
