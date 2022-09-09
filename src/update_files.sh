git checkout master
git pull origin master
git checkout flatiron
git checkout master data/
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "${parent_path}"
python scrub_readme.py
python create_index.py
notebook_dir=$(cat open_directory.txt)
rm open_directory.txt
git add ../data
git commit -m 'updating data files'
jupyter lab $open_directory

