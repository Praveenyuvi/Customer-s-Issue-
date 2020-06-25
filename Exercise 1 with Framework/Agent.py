import datetime 

class Agent(object):
    agent_name = None
    agent_id = None
    is_busy = False
    busy_till = None
    issues_assigned = None

    def __init__(self,agent_name,agent_id, issues_assigned):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.issues_assigned = issues_assigned
        self.process_issues()
    
    def process_issues(self):
        for issue in self.issues_assigned:
            if(self.busy_till):
                if (self.busy_till > (issue.resolved_time or  issue.abandoned_time) ):
                    self.busy_till =  ((issue.resolved_time or issue.abandoned_time) + ( (issue.resolved_time or issue.abandoned_time) - self.busy_till))
                else:
                    self.busy_till = issue.resolved_time or issue.abandoned_time

            else:
                self.busy_till = issue.resolved_time or issue.abandoned_time
       
        if(datetime.datetime.now() < self.busy_till):
            self.is_busy =  True
            
    def check_agent_avaliablity(self):
        if (self.busy_till < datetime.datetime.now()):
            return True
        else:
            return (datetime.datetime.now() + (self.busy_till - datetime.datetime.now()))