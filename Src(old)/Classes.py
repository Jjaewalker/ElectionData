import csv

# define the party class, name, the amount of votes, percentage of votes and candidate name
# class keyword is used to define a blueprint for creating objects
"""converts the variable 'v' to an integer. The int() function in Python"""
"""Represents a political party."""


class Party:
    #__init__ method is a constructor method The __init__ method takes the following parameters and assigns them to the object's attributes:
    def __init__(self, name):
        self.description= {'name':name, 'members':0,'votes':0}

    def IncrementmemberCount(self):
        """Increments the count of members in the party."""
        self.description['members'] += 1
    def IncrementVotesCount(self,v):
        """Increments the total votes for the party."""
        self.description['votes'] += int(v)
    def GetName(self):
        """Returns the name of the party."""
        return self.description['name']
    def GetTotalVotes(self):
        return self.description['votes']
    def __str__(self):
        return self.description['name'] + " has " + f"{self.description['members']} members and " + f"{self.description['votes']} total votes"
    def AddVotes(self,v):
        self.description['votes']= int(v)
        """Adds votes to the MP's total."""
    def GetVotes(self):
        return self.description['votes']
    """Returns the total votes received by the MP."""
    def GetParty(self):
        return self.description['party']


class MP:
    def __init__(self, name, party, constituency, votes_received, gender):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes_received = votes_received
        self.gender = gender


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
