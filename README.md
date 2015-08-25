I like sports. I thought it would be fun to run a full MLB season (in a slightly different format) in less than a second. This is the result.

# How does it work?

Once you pull the project and change into its directory, type `python mlb.py` or `./mlb.py` to run the program. It will generate a ranking table like the one below.

San Francisco Giants     58 W    44 L    478 S    440 G
Toronto Blue Jays        57 W    45 L    481 S    437 G
Washington Nationals     57 W    45 L    479 S    439 G
Los Angeles Dodgers      57 W    45 L    472 S    446 G
Cincinnati Reds          57 W    45 L    469 S    449 G
Colorado Rockies         57 W    45 L    467 S    451 G
Detroit Tigers           56 W    46 L    490 S    428 G
Pittsburgh Pirates       56 W    46 L    474 S    444 G
Houston Astros           55 W    47 L    481 S    437 G
Kansas City Royals       54 W    48 L    469 S    449 G
Philadelphia Phillies    54 W    48 L    451 S    467 G
Baltimore Orioles        53 W    49 L    482 S    436 G
Oakland Athletics        53 W    49 L    455 S    463 G
Miami Marlins            52 W    50 L    467 S    451 G
Arizona Diamondbacks     52 W    50 L    456 S    462 G
Chicago Cubs             52 W    50 L    454 S    464 G
Minnesota Twins          52 W    50 L    439 S    479 G
New York Yankees         51 W    51 L    459 S    459 G
Milwaukee Brewers        50 W    52 L    463 S    455 G
New York Mets            49 W    53 L    448 S    470 G
Texas Rangers            48 W    54 L    441 S    477 G
Boston Red Sox           47 W    55 L    454 S    464 G
Atlanta Braves           47 W    55 L    454 S    464 G
Tampa Bay Rays           47 W    55 L    435 S    483 G
San Diego Padres         46 W    56 L    459 S    459 G
Cleveland Indians        45 W    57 L    433 S    485 G
St. Louis Cardinals      44 W    58 L    452 S    466 G
Seattle Mariners         42 W    60 L    440 S    478 G
Chicago White Sox        41 W    61 L    440 S    478 G
Anaheim Angels           41 W    61 L    428 S    490 G

# Options

- `-h`: display help message.
- `-r`: don't display the rankings
- `-s`: display the scores
- `-d`: display the score distributions
- `-i <num>`: the number of games a team plays its division rivals at home (default: 4)
- `-j <num>`: the number of games a team plays its league rivals at home (default: 2)
- `-k <num>`: the number of games a team plays its non-league rivals at home  (default: 1)