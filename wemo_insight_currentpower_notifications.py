import urllib2
import time

from ouimeaux.environment import Environment

env = Environment()
env.start()
env.discover(10)

while True:
        InsightParams=env.get_switch('WeMo Insight').insight.GetInsightParams()
        InsightParams=str(InsightParams)
        InsightParamsSplit=InsightParams.split("|")
        CurrentPower=InsightParamsSplit[7]
        CurrentPower=float(CurrentPower)
        CurrentPower=CurrentPower/1000
        CurrentPower=str(CurrentPower)
        print CurrentPower
        emoncmsURLhosted="http://emoncms.org/input/post.json?node=2&apikey=APIKEY&csv="
        PostURL=emoncmsURL + CurrentPower
        urllib2.urlopen(PostURL).read()

        time.sleep(1)
