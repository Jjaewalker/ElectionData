#Define variable to load the dataframe
def __str__(self):
        return self.name

class Constituency:
    def __init__(self, name, registered_voters, total_votes_cast):
        self.name = name
        self.registered_voters = registered_voters
        self.total_votes_cast = total_votes_cast
        self.mps = []

    def add_mp(self, mp):
        self.mps.append(mp)

    def get_total_party_votes(self, party):
        total_votes = self.total_votes_cast
        if total_votes == 0:
            return 0
        party_votes = self.get_total_party_votes(party)
        return (party_votes / total_votes) * 100

    def get_mp_by_name(self,name):
        for mp in self.mps:
            if mp.name.lower() == name.lower():
                return mp
            return None

    def __str__(self):
        return f"Constituency: {self.name}, Registered Voters: {self.registered_voters},Total Votes cats: {self.total_votes_cast}"
