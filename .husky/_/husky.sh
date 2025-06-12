#!/bin/sh

if [ -f ~/.huskyrc ]; then
  . ~/.huskyrc
fi

npm_lifecycle_event=husky

exit 0
