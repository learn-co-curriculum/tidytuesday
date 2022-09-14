git add .
git commit -m 'commiting unstaged changes'
git checkout master
git pull https://github.com/rfordatascience/tidytuesday.git master
git checkout flatiron
git checkout master data/
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "${parent_path}"
python scrub_readme.py
python create_index.py
notebook_dir=$(cat open_directory.txt)
rm open_directory.txt
cd ..
git add data/
git rm data.txt
git rm -r static/
git rm -r tidytuesday_tweets/
git checkout --ours .
git commit -m 'updating data files'
jupyter lab $notebook_dir