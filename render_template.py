from jinja2 import Environment, FileSystemLoader
import os

# Load the template file
env = Environment(loader=FileSystemLoader(searchpath="./"))
template = env.get_template("mainfest/deploy.yaml.j2")

# Define variables to replace in the template
variables = {
    "image_tag": os.getenv("IMAGE_TAG", "latest"),
}

# Render the template with variables
rendered_template = template.render(variables)

# Save the rendered template to a file
with open("mainfest/deploy.yaml", "w") as f:
    f.write(rendered_template)
