
from jinja2 import Environment, FileSystemLoader
import os

# Define the path to the manifest directory
env = Environment(loader=FileSystemLoader(searchpath="./"))
template = env.get_template("deploy.yaml.j2")

# Load the template file from the manifest directory
env = Environment(loader=FileSystemLoader(searchpath=manifest_path))
template = env.get_template("deploy.yaml.j2")

# Define variables to replace in the template
variables = {
    "image_tag": os.getenv("IMAGE_TAG", "latest"),
}

# Render the template with variables
rendered_template = template.render(variables)

# Save the rendered template to a file in the manifest directory
with open("manifest/deploy.yaml", "w") as f:
    f.write(rendered_template)
