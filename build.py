from jinja2 import Environment, FileSystemLoader
from pathlib import Path


""" Serve the website
python -m http.server --directory ./_site/
"""

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('base.html')
output = template.render(
  title="INDEX"
)
o = Path.cwd()
o = o / Path('_site/index.html')
with o.open(mode='w') as fh:
    fh.write(output)
    
"""
About
"""
# /about.html
template = env.get_template('about.html')
output = template.render(
  title="ABOUT ME"
)
o = Path.cwd()
o = o / Path('_site/about.html')
with o.open(mode='w') as fh:
    fh.write(output)

"""
Teaching
"""
# /teaching.html
template = env.get_template('teaching.html')
output = template.render(
  title="TEACHING"
)
o = Path.cwd()
o = o / Path('_site/teaching.html')
with o.open(mode='w') as fh:
    fh.write(output)
    