# nfl_overtime
Basic calculation to determine the historical probability of NFL teams winning the overtime coin toss and winning the game.

**nfl_overtime.py** uses [pro-football-reference.com](https://www.pro-football-reference.com/) (now stathead.com) data from 2012-2020 to calculate the probability of winning an NFL overtime game given that your team has won the overtime coin toss.

In the NFL, overtime rules are such that the first team that scores a touchdown wins the game. In some scenarios, a game goes to overtime, the team that wins the coin toss elects to have the first possession, scores a touchdown, and ends the game without the other team's offense ever touching the field in overtime. Since the NFL's overtime rules differ from college football overtime rules (where both teams generally get a possession unless the defense scores on the first possession), how often does the team that wins the overtime coin toss win the game?

This program uses data (**overtimes_clean.xlsx**) from 135 NFL overtime games from 2012-2020. I found that:

* Of the teams who **won** the overtime coin toss, 51.9% won the game, 41.5% lost, and 6.7% tied

* Of the teams who **lost** the overtime coin toss, 41.5% won the game, 51.9% lost, and 6.7% tied

There is clearly an advantage to winning the coin toss, but I expected the ~52% of teams that won the coin toss won the game to be closer to 70%.

I initially used **data_acquisition.py** to get the data into spreadsheet form. The next day, all of the detailed search information went behind a paywall at [stathead.com](https://stathead.com). I may well be the last person to get information from the search before it went behind the paywall!
