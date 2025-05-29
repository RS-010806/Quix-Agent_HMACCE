class Memory:
    def __init__(self):
        self.successes = {}
        self.human_interventions = {}

    def store_success(self, program_name, fix, defect_type, status=None, log=None):
        self.successes[program_name] = {
            'fix': fix,
            'defect_type': defect_type,
            'status': status,
            'log': log
        }

    def store_human_intervention(self, program_name, fix, defect_type):
        self.human_interventions[program_name] = {
            'fix': fix,
            'defect_type': defect_type
        } 