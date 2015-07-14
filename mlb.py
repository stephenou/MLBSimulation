# -----------------------------------------------------
# File: mlb.py
# Description: mlb.py is a simulation of an MLB season.
# Author: Stephen Ou
# -----------------------------------------------------

def get_scores():
	home_score = random.randInt(0, 9)
	away_score = 9 - home_score
	return home_score, away_score

# Teams are categorized by league, and then by division.
mlb = {
	"American League": {
		"East": [
			"Baltimore Orioles",
			"Boston Red Sox",
			"New York Yankees",
			"Tampa Bay Rays",
			"Toronto Blue Jays"
		],
		"Central": [
			"Chicago White Sox",
			"Cleveland Indians",
			"Detroit Tigers",
			"Kansas City Royals",
			"Minnesota Twins"
		],
		"West": [
			"Anaheim Angels",
			"Houston Astros",
			"Oakland Athletics",
			"Seattle Mariners",
			"Texas Rangers"
		]
	},
	"National League": {
		"East": [
			"Atlanta Braves",
			"Miami Marlins",
			"New York Mets",
			"Philadelphia Phillies",
			"Washington Nationals"
		],
		"Central": [
			"Chicago Cubs",
			"Cincinnati Reds",
			"Milwaukee Brewers",
			"Pittsburgh Pirates",
			"St. Louis Cardinals"
		],
		"West": [
			"Arizona Diamondbacks",
			"Colorado Rockies",
			"Los Angeles Dodgers",
			"San Diego Padres",
			"San Francisco Giants"
		]
	}
}

games = []
standings = []

for league, divisions in mlb.iteritems():
	for division, teams in divisions.iteritems():
		for home_team in teams:
			for away_team in teams:
				if home_team is not away_team:
					for i in range(1):
						home_score, away_score = get_scores()
						games.append({
							"home_team": home_team,
							"away_team": away_team,
							"home_score": home_score,
							"away_score": away_score
						})

for game in games:
	print "%s %d - %d %s" % (
		game["home_team"],
		game["home_score"],
		game["away_team"],
		game["away_score"]
	)

# for league, divisions in mlb.iteritems():
# 	for division, teams in divisions.iteritems():
# 		for team in teams:
# 			print "%s in %s in %s" % (team, division, league)