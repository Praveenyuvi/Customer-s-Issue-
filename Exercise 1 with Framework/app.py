from flask import Flask, render_template, request
from markupsafe import escape
from ex1 import Agent, generate_random_issue
import datetime 

app = Flask(__name__)
app.config['DEBUG'] = True # Debugging mode on
agent = None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate-issues',methods = ['GET', 'POST'])
def generate():
    global agent
    if( request.method == 'GET'):
        total_issue = request.args.get('total-issue')
        agent = Agent(1, 'Praveen', generate_random_issue(total_issue))
        return render_template('index.html', agent = agent)
    else:
        return 'SomeThing Went Wrong Pleas try again'

@app.route('/check-avaliablity', methods = ['POST'])
def avaliablity():
    global agent
    if(request.method == 'POST' and agent != None):
        agent_avaliablity = agent.check_agent_avaliablity()
        if(agent_avaliablity != True):
            day_diff = (agent_avaliablity.day-datetime.datetime.now().day)
            avaliable_day = 'Today' if day_diff == 0 else 'Tomorrow' if day_diff == 1 else 'on '+ agent_avaliablity.strftime('%D')
            print(day_diff,avaliable_day)
            agent_avaliablity =  avaliable_day + ' at ' +agent_avaliablity.strftime('%H:%M:%S')
        return render_template('index.html', agent_avaliablity = agent_avaliablity)
    else:
        return render_template('index.html', agent_avaliablity = True)


if __name__ == '__main__':
    app.run()
