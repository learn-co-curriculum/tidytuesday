git checkout master
git pull origin master
git checkout flatiron
git checkout master data/
python scrub_readme.py
git add data
git commit -m 'updating data files'

