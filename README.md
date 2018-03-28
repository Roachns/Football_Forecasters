# Football_Forecasters

Use logistic regression from sklearn to train a model that will generate win probabilties for college football games.  We will use a variety of football efficiency stats to train the model.  Example stats:
* offensive net passing yards per attempt
* offensive rushing yards per attempt
* offensive interceptions per attempt
* offensive fumbles per play
* defensive net passing yards per attempt
* defensive ruhsing yards per attempt
* team penalty yards per play
* home field adavantage (non-efficiency stat)

We'll compute stats for every FBS vs FBS game from 2008-2016.  Once the model has been created, we'll use the 2017 season to demo a front end that will display the win probabilties for each game.

Additonal goals:
* explore other stats beyond the ones listed above to fine tune the model

Visualization concept:

![](example_stats.PNG)
