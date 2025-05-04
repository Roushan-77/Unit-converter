from flask import Flask
import os

# Get the absolute path to the parent directory 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Set template and static folder paths relative to where app is created
app = Flask(
    __name__,
    template_folder=os.path.join(project_root, 'templates'),
    static_folder=os.path.join(project_root, 'static')
)

from unit_converter import route


