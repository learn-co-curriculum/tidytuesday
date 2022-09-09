from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell, writes
from scrub_readme import get_readme
from pathlib import Path

def _readme():
    readmepath, readme = get_readme()
    dirpath = Path(readmepath).resolve().parent.as_posix()
    return dirpath, readmepath, readme

def create_index():
    dirpath, readmepath, readme = _readme()
    intro_cell = new_markdown_cell(source=readme)
    start_cell = new_code_cell(source='# Happy coding! <3')
    notebook = new_notebook(cells=[intro_cell, start_cell])
    return notebook

def save_index(index):
    dirpath, readmepath, readme = _readme()
    index_path = Path(dirpath) / 'index.ipynb'
    with open(index_path.as_posix(), 'w') as file:
        json = writes(index)
        file.write(json)



if __name__ == "__main__":
    dirpath, readmepath, readme = _readme()
    index = create_index()
    save_index(index)

    with open(Path(__file__).resolve().parent / 'open_directory.txt', 'w') as file:
        file.write((Path(dirpath) / 'index.ipynb').as_posix())

