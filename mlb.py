# -----------------------------------------------------
# File: mlb.py
# Description: mlb.py is a simulation of an MLB season.
# Author: Stephen Ou
# -----------------------------------------------------

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

for league, divisions in mlb.iteritems():
	for division, teams in divisions.iteritems():
		for team in teams:
			print "%s in %s in %s" % (team, division, league)