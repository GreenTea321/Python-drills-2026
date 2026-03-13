class KOFAnalyzer:
    def __init__(self, fighter: str):
        self.fighter = fighter # 'self' anchors the data to the instance
        self._matches = [] # Underscores signals internal Match Log

    def log_match(self, result: str):
        self._matches.append(result) # Accessing the instance-state
        self._calculate_win_rate() # Internal logic trigger

    def _calculate_win_rate(self):
        # Implementation for Internal Forensic Analysis
        pass # Implementation detail: 'Opt-in' risk if called externally