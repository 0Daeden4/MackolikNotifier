import requests
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
        print(all_matches)

def main():
    fetcher = MackolikRunner()
    fetcher.getAllMatches()



if __name__ == "__main__":
    main()
