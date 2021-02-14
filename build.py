from jinja2 import Environment, FileSystemLoader
from pathlib import Path


""" Serve the website
python -m http.server --directory ./_site/
"""

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('hello.html')
output = template.render(name="Harry Potter")
o = Path.cwd()
o = o / Path('_site/index.html')
with o.open(mode='w') as fh:
    fh.write(output)
    