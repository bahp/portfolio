# Generic
import argparse

# Pathlib
from pathlib import Path

# Jinja
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2 import Environment


class AttrDict(dict):
    """Dictionary subclass whose entries can be accessed by attributes"""
    def __init__(self, *args, **kwargs):
        def from_nested_dict(data):
            """ Construct nested AttrDicts from nested dictionaries. """
            if not isinstance(data, dict):
                return data
            else:
                return AttrDict({key: from_nested_dict(data[key])
                                    for key in data})

        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

        for key in self.keys():
            self[key] = from_nested_dict(self[key])

class Card:
    """The class card."""
    s = 4
    visible = True
    thumbnail = None

    def __init__(self, d):
        for k, v in d.items():
            setattr(self, k, v)

        if self.thumbnail is None:
            self.thumbnail = 'thumbnail-%s.jpg' % self.name

    def thumbnail_path(self):
        return "docs/static/imgs/%s" % self.thumbnail


# Initialize parser
parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("-t", "--thumbnail",
    action='store_true', default=False, help="Include thumbnails.")

# Read arguments from command line
args = parser.parse_args()

# Compute the thumbnails
if args.thumbnail:
    exec(open("create_imgs.py").read())


# import pyyaml module
import yaml
from yaml.loader import SafeLoader

# Load configuration
CONFIG = None
with open('config.yaml') as f:
    CONFIG = AttrDict(yaml.load(f, Loader=SafeLoader))

# Create cards
cards = [Card(c) for c in CONFIG.portfolio.projects]

# Set template environment
tmp_loader = FileSystemLoader(searchpath='docs/static/tmps')
tmp_environment = Environment(loader=tmp_loader)
tmp_index = tmp_environment.get_template('base_.html')

# Render template
html = tmp_index.render(cards=cards, thumbnail=args.thumbnail)

# Save index file
with open("./index.html", "w") as fh:
    fh.write(html)