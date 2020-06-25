class Issue(object): 
    start_time = None # Start time when the issue is generated
    resolved_status = None # Status of issue, resolved or abounded : true or false
    answer_time = None # Time when agent will start working on issue
    resolved_time = None # Resolved time
    abandoned_time = None # abounded time

    def __init__(self, start_time, resolved_status, answer_time, resolved_time, abandoned_time):
        self.start_time = start_time
        self.resolved_status = resolved_status
        self.answer_time = answer_time
        self.resolved_time = resolved_time
        self.abandoned_time = abandoned_time
