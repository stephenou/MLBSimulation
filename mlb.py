# -----------------------------------------------------
# File: mlb.py
# Description: mlb.py is a simulation of an MLB season.
# Author: Stephen Ou
# -----------------------------------------------------

import random

def get_scores():
	home_score = away_score = 0
	for i in range(9):
		if random.choice([True, False]):
			home_score += 1
		else:
			away_score += 1
	return home_score, away_score

def addGame(games, home_team, away_team):
	games.append({
		"home_team": home_team,
		"away_team": away_team
	})

def create_mlb():
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
	return mlb

def addIntraDivisionIntraLeagueGames(mlb, games, standings):
	for league, divisions in mlb.iteritems():
		for division, teams in divisions.iteritems():
			for home_team in teams:
				for away_team in teams:
					if home_team is not away_team:
						for i in range(1):
							addGame(games, home_team, away_team)

def addInterDivisionIntraLeagueGames(mlb, games, standings):
	for league, divisions in mlb.iteritems():
		for home_division, home_teams in divisions.iteritems():
			divisions_to_play = [division for division in divisions.keys() if division is not home_division]
			for away_division, away_teams in divisions.iteritems():
				if away_division in divisions_to_play:
					for home_team in home_teams:
						for away_team in away_teams:
							for i in range(1):
								addGame(games, home_team, away_team)

def addInterDivisionInterLeagueGames(mlb, games, standings):
	for home_league, home_divisions in mlb.iteritems():
		leagues_to_play = [league for league in mlb.keys() if league is not home_league]
		for away_league, away_divisions in mlb.iteritems():
			if away_league in leagues_to_play: 
				for home_division, home_teams in home_divisions.iteritems():
					for home_team in home_teams:
						for away_division, away_teams in away_divisions.iteritems():
							for away_team in away_teams:
								for i in range(1):
									addGame(games, home_team, away_team)

def planSchedule(mlb, games, standings):
	addIntraDivisionIntraLeagueGames(mlb, games, standings)
	addInterDivisionIntraLeagueGames(mlb, games, standings)
	addInterDivisionInterLeagueGames(mlb, games, standings)

def playGames(games):
	for index, game in enumerate(games):
		home_score, away_score = get_scores()
		games[index]["home_score"] = home_score
		games[index]["away_score"] = away_score

def displayScores(games):
	for game in games:
		print "%s %d - %d %s" % (
			game["home_team"],
			game["home_score"],
			game["away_score"],
			game["away_team"]
		)

# Main flow starts here

games = []
standings = []
mlb = create_mlb()
planSchedule(mlb, games, standings)
playGames(games)
displayScores(games)