# -----------------------------------------------------
# File: mlb.py
# Description: mlb.py is a simulation of an MLB season.
# Author: Stephen Ou
# -----------------------------------------------------

import random, sys, getopt, operator, collections

def get_options():
	options = [
		{
			"short": "h",
			"full": "help",
			"default": False,
			"description": "Display this message."
		}, {
			"short": "r",
			"full": "no-rankings",
			"default": False,
			"description": "The rankings will not be displayed."
		}, {
			"short": "s",
			"full": "scores",
			"default": False,
			"description": "Display the scores."
		}, {
			"short": "d",
			"full": "distribution",
			"default": False,
			"description": "Display the score distribution."
		}, {
			"short": "i",
			"full": "num-division",
			"default": 4,
			"description": "The number of games a team plays its division rivals at home."
		}, {
			"short": "j",
			"full": "num-league",
			"default": 2,
			"description": "The number of games a team plays its league rivals at home."
		}, {
			"short": "k",
			"full": "num-others",
			"default": 1,
			"description": "The number of games a team plays its non-league rivals at home."
		}
	]
	return options

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


def get_config(argv, options):
	config = {}
	optstr = ""
	for option in options:
		config[option["short"]] = option["default"]
		optstr += option["short"]
		if option["default"]:
			optstr += ":"
	opts, args = getopt.getopt(argv, optstr)
	for opt, arg in opts:
		for option in options:
			if opt in ("-" + option["short"], "--" + option["full"]):
				if arg == "":
					config[option["short"]] = True
				else:
					config[option["short"]] = arg
	return config


def display_help_messages(options):
	for option in options:
		print "Short Name: %s" % option["short"]
		print "Full Name: %s" % option["full"]
		print "Default: %s" % option["default"]
		print "Description: %s" % option["description"]


def get_scores():
	home_score, away_score = 0, 0
	for i in range(9):
		if random.choice([True, False]):
			home_score += 1
		else:
			away_score += 1
	return home_score, away_score


def add_game(games, home_team, away_team):
	games.append({
		"home_team": home_team,
		"away_team": away_team
	})


def add_division_games(mlb, games, num):
	for league, divisions in mlb.iteritems():
		for division, teams in divisions.iteritems():
			for home_team in teams:
				for away_team in teams:
					if home_team is not away_team:
						for i in range(num):
							add_game(games, home_team, away_team)


def add_league_games(mlb, games, num):
	for league, divisions in mlb.iteritems():
		for home_division, home_teams in divisions.iteritems():
			divisions_to_play = [division for division in divisions.keys() if division is not home_division]
			for away_division, away_teams in divisions.iteritems():
				if away_division in divisions_to_play:
					for home_team in home_teams:
						for away_team in away_teams:
							for i in range(num):
								add_game(games, home_team, away_team)


def add_other_games(mlb, games, num):
	for home_league, home_divisions in mlb.iteritems():
		leagues_to_play = [league for league in mlb.keys() if league is not home_league]
		for away_league, away_divisions in mlb.iteritems():
			if away_league in leagues_to_play: 
				for home_division, home_teams in home_divisions.iteritems():
					for home_team in home_teams:
						for away_division, away_teams in away_divisions.iteritems():
							for away_team in away_teams:
								for i in range(num):
									add_game(games, home_team, away_team)


def plan_schedule(mlb, games, num_division, num_league, num_others):
	num_division, num_league, num_others = int(num_division), int(num_league), int(num_others)
	add_division_games(mlb, games, num_division)
	add_league_games(mlb, games, num_league)
	add_other_games(mlb, games, num_others)
	random.shuffle(games)


def play_games(games):
	for index, game in enumerate(games):
		home_score, away_score = get_scores()
		games[index]["home_score"] = home_score
		games[index]["away_score"] = away_score


def initializeTeams(mlb, rankings):
	for league, divisions in mlb.iteritems():
		for division, teams in divisions.iteritems():
			for team in teams:
				rankings[team] = {
					"games_won": 0,
					"games_lost": 0,
					"points_won": 0,
					"points_lost": 0
				}


def create_rankings(mlb, games, rankings):
	initializeTeams(mlb, rankings)
	for game in games:
		rankings[game["home_team"]]["points_won"] += game["home_score"]
		rankings[game["home_team"]]["points_lost"] += game["away_score"]
		rankings[game["away_team"]]["points_won"] += game["away_score"]
		rankings[game["away_team"]]["points_lost"] += game["home_score"]
		if game["home_score"] > game["away_score"]:
			rankings[game["home_team"]]["games_won"] += 1
			rankings[game["away_team"]]["games_lost"] += 1
		else:
			rankings[game["home_team"]]["games_lost"] += 1
			rankings[game["away_team"]]["games_won"] += 1


def display_scores(games):
	for game in games:
		print "%-24s %d - %d %24s" % (
			game["home_team"],
			game["home_score"],
			game["away_score"],
			game["away_team"]
		)


def display_distribution(games):
	game_count = [0 for i in range(9)]
	for game in games:
		game_count[game["home_score"] - 1] += 1
	total_count = sum(game_count)
	for index, count in enumerate(game_count):
		percent = count * 100 / float(total_count)
		print "%d %6.2f%%  %s" % (index + 1, percent, "+" * int(round(percent)))


def sort_rankings(rankings):
	return collections.OrderedDict(sorted(rankings.items(), key=operator.itemgetter(1)))


def display_rankings(rankings):
	rankings = sort_rankings(rankings)
	for team, stats in rankings.iteritems():
		print ("%-24s %d W {s} %d L {s} %d S {s} %d G" % (
			team,
			stats["games_won"],
			stats["games_lost"],
			stats["points_won"],
			stats["points_lost"]
		)).format(s=" " * 2)


def main(argv):
	options = get_options()
	config = get_config(argv, options)
	if config["h"]:
		display_help_messages(options)
	mlb, games, rankings = create_mlb(), [], {}
	plan_schedule(mlb, games, config["i"], config["j"], config["k"])
	play_games(games)
	create_rankings(mlb, games, rankings)
	if config["s"]:
		display_scores(games)
	if config["d"]:
		display_distribution(games)
	if not config["r"]:
		display_rankings(rankings)

if __name__ == "__main__":
   main(sys.argv[1:])