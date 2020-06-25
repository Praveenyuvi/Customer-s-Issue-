# Exercise 1
# Predict agent avaliablity

import datetime 
import random as r
from Issue import Issue
from Agent import Agent

def create_issue(start_time, resolved_status, answer_time, resolved_time, abandoned_time): # function to initilize issus object

    issue = Issue(start_time, resolved_status, answer_time, resolved_time, abandoned_time)
    return issue

def generate_random_issue(num): # Generating random issues
    num = int(num)
    issues = []
    # Fixind the date to generate issues for present day
    TODAY = datetime.datetime.now() # returns present datatime object
    YEAR = TODAY.year
    MONTH = TODAY.month
    DAY = TODAY.day
    HOUR = TODAY.hour or 1 

    for i in range(num):
        start_time = datetime.datetime(YEAR,MONTH,DAY,r.randrange(0,HOUR),r.randrange(0,60),r.randrange(0,60)) # generating random time upto the present time
        resolved_status = True if(r.randint(0,1)==1) else False # assgning ramsom staus
        answer_time = start_time
        abandoned_time = None
        resolved_time = None
        issues.append(create_issue(start_time, resolved_status, answer_time, resolved_time, abandoned_time)) # Appending issue in list

    issues.sort(key=lambda issue: issue.start_time)  # sorting according to the issue arrival time (Start time)

    for i in range(num):
        assume_issue_result_in =  datetime.timedelta(hours=1, minutes=(r.randrange(1,45))) # Assuming issue is solved or abounded  within 45 mins 
        if i != 0:
            if(issues[i-1].resolved_time and issues[i].start_time < issues[i-1].resolved_time): # comparing start time to previous issue's resolve time
                issues[i].answer_time = issues[i-1].resolved_time
            elif(issues[i-1].abandoned_time and issues[i].start_time < issues[i-1].abandoned_time): # comparing start time to previous issue's abounded time
                issues[i].answer_time = issues[i-1].abandoned_time
            else:
                issues[i].answer_time = issues[i].start_time
            
            if(issues[i].resolved_status == True):
                issues[i].resolved_time = add_datetime(issues[i].answer_time, assume_issue_result_in)
                issues[i].abandoned_time = None
            else:
                issues[i].abandoned_time = add_datetime(issues[i].answer_time, assume_issue_result_in)
                issues[i].resolved_time = None
        else:
            issues[i].answer_time = issues[i].start_time # if First the start time is same as answer time
            if(resolved_status == True):
                issues[i].resolved_time = add_datetime(issues[i].answer_time, assume_issue_result_in)
                issues[i].abandoned_time = None
            else:
                issues[i].abandoned_time = add_datetime(issues[i].answer_time, assume_issue_result_in)
                issues[i].resolved_time = None    
            
    return issues

def add_datetime(datetime1, datetime2): # adding datetime with deltatime 
    return datetime1 + datetime2

# def agentAvaliability(agent):
    
#     for issue in agent.issues_assigned:
#         print(issue)


if __name__ == '__main__':

    agnet_tom = Agent(1, 'Praveen', generate_random_issue(10))
    # this is just for test puropse
    for i in agnet_tom.issues_assigned:
        print(i.resolved_status)
        print(i.start_time)
        print(i.answer_time)
        print(i.resolved_time)
        print((i.abandoned_time))
        print()

    print(agnet_tom.busy_till)
    print(agnet_tom.is_busy)
    print(agnet_tom.check_agent_avaliablity())