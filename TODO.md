# TODO

## Defects

- [ ] Platforms always need to be within reach of the duck's max jump height. No impossible platforms.

## Features

- [x] procedural generate platforms upward.
- [x] increment score as duck goes upward.
- [x] game over screen when falling off the bottom.
- [x] [HIGH PRIORITY] Use assets within assets/images for game
  - duck should use duck.png and duck_quack.png when quacking.
    1st level AKA screen height should use game_background.png, then progress as follows
    sky1 - sky5
    space1 - space4
    then progress through each colored background in any order.
    If the player gets through all the levels, they win. Implement a win screen like the game over screen.

## Tech Debt

- [ ] implement proper linting that enforces python standards. Include the linting as part of a pre commit hook
- [ ] implement automatic code formatting with prettier (or other if there is something more python focused). Add .vscode/settings.json to ensure all devs automtically have formatting on save/paste.

## Deployment

- [ ] Use Pygbag to prepare the game to be deployed as a PWA on heroku or vercel... some free hosting.
