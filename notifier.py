import requests
import os
from datetime import datetime

# TODO: Import update interval and selected teams

# Obtain information of all matches for current date

# Match <Selected Teams> with the current information and extract their ids

# TODO: Define a dict that contains the matches as keys and the most recent event number as value
# TODO: Add a match if the match has started
# TODO: Remove match if it is has ended
    # TODO: Update List every <Update Interval> seconds after a match starts
    # TODO: Break if the list is empty
class MackolikRunner(object):
    def __init__(self):
        self.s = requests.Session()
        self.all_matches_url = "https://www.mackolik.com/perform/p0/ajax/components/competition/livescores/json?"
        self.match_event_url = "https://www.mackolik.com/ajax/football/key-events?"
#...HEADERS...#######################################################################################################################################
        self.general_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'DNT': '1',
                'Host': 'www.mackolik.com',
                'Priority': 'u=0, i',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'TE': 'trailers',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
                }
        self.match_event_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'DNT': '1',
                'Host': 'www.mackolik.com',
                'Priority': 'u=0, i',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'TE': 'trailers',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
                }
#...FUNCTIONS...#####################################################################################################################################


    def getResponse(self, url, parameters, headers):
        response = self.s.get(url, headers=headers, params=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request to {url} returned {response.status_code}!")
            return None

    def getAllMatches(self):
        today = datetime.today().strftime('%Y-%m-%d')
        parameters = "sports[]=Soccer&matchDate="+today
        all_matches = self.getResponse( self.all_matches_url , parameters , self.general_header )
        if all_matches:
            all_matches = all_matches.get('data').get('matches')
            #print(all_matches)
            return all_matches
        else:
            return None

    def getEvent(self, all_matches, team_name, event_num):
        if all_matches:
            for match in all_matches:
                current_match = all_matches.get(match)
                if current_match.get("state") == "live":
                    home_team = current_match.get("homeTeam").get("name")
                    away_team = current_match.get("awayTeam").get("name")
                    if (home_team == team_name) or (away_team == team_name):
                        #print(match)
                        parameters = "ajaxViewName=events&matchId="+match
                        match_events = self.getResponse(self.match_event_url, parameters , self.match_event_header)
                        match_title = home_team + " - " + away_team
                        #print(match_events)
                        if match_events and len(match_events.get("data").get("keyEvents"))>event_num:
                            #TODO set different behaviour for different event types
                            events = match_events.get("data").get("keyEvents")[event_num]
                            #print(str(match_events.get("data").get("keyEvents")[event_num])+"\n")
                            event_type = events.get("type")
                            player = events.get("playerName")
                            min = events.get("timeMin")
                            # Too lazy to write cases for each event type
                            player_out = ""
                            sub_event = ""
                            score = ""
                            if event_type == "substitute":
                                player_out = events.get("playerOutName")
                            elif event_type == "goal":
                                score = events.get("score")
                            else:
                                sub_event = events.get("subType")
                            os.system(f"./notifications.sh -t '{event_type}' -c '{sub_event}' -p '{player}' -po '{player_out}' -s '{score}' -ti '{min}' -tt '{match_title}'")

                            return True
        return False

    def mainLoop(self, teams_list):
        while(1):
            all_matches = self.getAllMatches()
            for i in range(len(teams_list)):
                #TODO check whether the event was displayed or not before calling the method
                team_name, event_num = teams_list[i]
                event_ready = self.getEvent(all_matches, team_name, event_num)
                if event_ready:
                    event_num += 1
                    teams_list[i] = (team_name, event_num)



def main():
    teams_list = []

    fetcher = MackolikRunner()
    fetcher.mainLoop(teams_list)



if __name__ == "__main__":
    main()
