from os import remove
import re
from pathlib import Path
from datetime import datetime

YEAR = str(datetime.now().year)

def scrub_readme(readme):
    text = remove_code_blocks(readme)
    text = remove_empty_sections(text)
    text = remove_r_references(text)
    return text


def remove_code_blocks(readme):
     text = re.sub(r"^```[^\S\r\n]*[a-z]*(?:\n(?!```$).*)*\n```", '', readme, 5, re.MULTILINE)
     return text


def get_readme():
    print(Path(__file__).resolve().parent.parent / 'data' / YEAR)
    data_directories = (Path(__file__).resolve().parent.parent / 'data' / YEAR).iterdir()
    dir_path = max([x.as_posix() for x in data_directories if x.is_dir()])
    readme_path = [x.as_posix() for x in Path(dir_path).iterdir() if 'readme' in x.as_posix().lower()][0]
    with open(readme_path, 'r+') as file:
        readme = file.read()

    return readme_path, readme

def remove_empty_sections(readme):
    headers = [
        "Get the data here",
        "Cleaning Script",
    ]
    text = str(readme)
    for header in headers:
        text = text.replace(header, '')

    return text

def remove_r_references(readme):
    references = [
        "{rtweet}",
    ]

    text = str(readme)
    for line in text.split('\n'):
        for ref in references:
            if ref in line:
                text = text.replace(line, '')
    return text


if __name__ == "__main__":
    path, readme = get_readme()
    readme = readme.replace("{r}", '')
    readme = scrub_readme(readme)
    with open(path, 'w') as file:
        file.write(readme)
    

    




