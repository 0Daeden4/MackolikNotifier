# Goals

The idea was to create a script to display match scores by "scraping" mackolik and use a notification service, which allows the customization of 
notifications.

## General

You can customize the notification settings and behaviour in notifications.sh.

## Requirements

Aside from the content of requirements.txt, dunst is also required for this to work.
More of dunst: https://dunst-project.org/
Don't forget to chmod notifications.sh!

## TODO

The project is still on its early stages and there are a lot of things to be done such as:

  - Make update interval customizeable and make team selection easier
  - Import update interval and selected teams
  - Match <Selected Teams> with the current information and extract their ids
  - Find the api request which calls out the penalty calls
