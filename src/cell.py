import xml
from xml.etree import ElementTree as ET
import random

from utils import create_box_with_coordinates

root = ET.Element("robot", name="cell_terrain")

# create materials
material = ET.SubElement(root, "material", name="white")
color = ET.SubElement(material, "color", rgba="0.9 0.9 0.9 1.0")

size = 10
rows = 10
cols = 10
max_height = 0.1
min_height = 0.0
bottom_thickness = -1.0

for i in range(rows):
    for j in range(cols):
        link = ET.SubElement(root, "link", name=f"cell_{i}_{j}", type="fixed")
        visual = ET.SubElement(link, "visual")
        collision = ET.SubElement(link, "collision")

        width = size / cols
        height = random.uniform(min_height, max_height)
        length = size / rows

        # create visual origin
        create_box_with_coordinates(
            visual,
            (j * width, i * length, bottom_thickness),
            ((j + 1) * width, (i + 1) * length, height),
        )

        # create visual material
        material = ET.SubElement(visual, "material", name="white")

        # create collision origin
        create_box_with_coordinates(
            collision,
            (j * width, i * length, bottom_thickness),
            ((j + 1) * width, (i + 1) * length, height),
        )

for i in range(rows):
    if i > 0:
        joint = ET.SubElement(
            root, "joint", name=f"cell_{i - 1}_{0}_top_joint", type="fixed"
        )
        ET.SubElement(joint, "parent", link=f"cell_{i - 1}_{0}")
        ET.SubElement(joint, "child", link=f"cell_{i}_{0}")
        ET.SubElement(joint, "origin", xyz="0 0 0", rpy="0 0 0")
    for j in range(cols - 1):
        joint = ET.SubElement(root, "joint", name=f"cell_{i}_{j}_joint", type="fixed")
        ET.SubElement(joint, "parent", link=f"cell_{i}_{j}")
        ET.SubElement(joint, "child", link=f"cell_{i}_{j + 1}")
        ET.SubElement(joint, "origin", xyz="0 0 0", rpy="0 0 0")

tree = ET.ElementTree(root)
ET.indent(tree, space="  ", level=0)
tree.write("cell_terrain.urdf", encoding="utf-8", xml_declaration=True)
