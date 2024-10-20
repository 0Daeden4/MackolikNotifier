#!/usr/bin/env bash

help_message(){
  echo -e "Possible options:
  -c\t Card color
  -i\t Path for Icon
  -p\t Defines player or player in
  -po\t Defines player out
  -t\t Signifies event type
  -ti\t Sets time
  -tt\t Defines title"
}

CARD=""
ICON=""
MESSAGE=""
PLAYER=""
PLAYER_OUT=""
SCORE=""
TYPE=""
TITLE=""
TIME=""
OUTLINE_COLOR="#cedbf0"
BACKGROUND_COLOR="#3667b5"

for arg in "$@"; do
  case $arg in
    -h|--help)
      help_message
      exit 1
      ;;
    -c|--card)
      CARD="$2"
      shift 2
      ;;
    -i|--icon)
      ICON="$2"
      shift 2
      ;;
    -p|--player)
      PLAYER="$2"
      shift 2
      ;;
    -po|--player-out)
      PLAYER_OUT="$2"
      shift 2
      ;;
    -s|--score)
      SCORE="$2"
      shift 2
      ;;
    -t|--type)
      TYPE="$2"
      shift 2
      ;;
    -tt|--title)
      TITLE="$2"
      shift 2
      ;;
    -ti|--time)
      TIME="$2"
      shift 2
      ;;
  esac
done

if [ "$TYPE" = "card" ]; then
  if [ "$CARD" = "yc" ]; then
    BACKGROUND_COLOR="#ccb21d"
    TITLE+="$(echo -e "\nYELLOW CARD")"
    MESSAGE="$(echo -e "$PLAYER recieved a yellow card!\nMinute: $TIME")"
  else
    BACKGROUND_COLOR="#c21e15"
    OUTLINE_COLOR="#000000"
    TITLE+="$(echo -e "\nRED CARD")"
    MESSAGE="$(echo -e "$PLAYER recieved a red card!\nMinute: $TIME")"
  fi

elif [ "$TYPE" = "goal" ]; then
    BACKGROUND_COLOR="#2cb307"
    OUTLINE_COLOR="#ffffff"
    if [ "$PLAYER" = "None" ]; then
      TITLE+="$(echo -e "\n$SCORE")"
      MESSAGE="$(echo -e "GOAL!\nMinute: $TIME")"
    else
      TITLE+="$(echo -e "\n$SCORE")"
      MESSAGE="$(echo -e "$PLAYER scored a goal!\nMinute: $TIME")"
    fi

elif [ "$TYPE" = "penalty-missed" ]; then
    BACKGROUND_COLOR="#cc4d12"
    OUTLINE_COLOR="#000000"
    TITLE+="$(echo -e "\nPENALTY MISSED")"
    MESSAGE="$(echo -e "$PLAYER missed a penalty!\nMinute: $TIME")"

else
    TITLE+="$(echo -e "\nSUBSTITUTION")"
    MESSAGE="$(echo -e "Player out: $PLAYER_OUT\nPlayer in: $PLAYER\nMinute: $TIME")"
fi
notify-send -t 10000 -h string:bgcolor:$BACKGROUND_COLOR -h string:frcolor:$OUTLINE_COLOR "$TITLE" "$MESSAGE"
