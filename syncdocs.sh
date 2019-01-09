#! /bin/sh
rsync -av --delete-after --exclude=.git --exclude=.gitignore --exclude-from=.gitignore ./docs/build/html/ ./ --dry-run
