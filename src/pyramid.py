import xml
from xml.etree import ElementTree as ET

from utils import create_box_with_coordinates

root = ET.Element("robot")

# create materials
material = ET.SubElement(root, "material", name="white")
color = ET.SubElement(material, "color", rgba="0.9 0.9 0.9 1.0")

size = 10
steps = 8
step_height = 0.2
step_tread = 0.5
bottom_thickness = -1.0

for i in range(steps):
    link = ET.SubElement(root, "link", name=f"step_{i}", type="fixed")
    visual = ET.SubElement(link, "visual")
    collision = ET.SubElement(link, "collision")

    if i == 0:
        min_xyz = (
            0 + i * step_tread,
            0 + i * step_tread,
            i * step_height + bottom_thickness,
        )
        max_xyz = (
            size - i * step_tread,
            size - i * step_tread,
            i * step_height,
        )
    else:
        min_xyz = (
            0 + i * step_tread,
            0 + i * step_tread,
            (i - 1) * step_height,
        )
        max_xyz = (
            size - i * step_tread,
            size - i * step_tread,
            i * step_height,
        )

    # create visual origin
    create_box_with_coordinates(visual, min_xyz, max_xyz)

    # create visual material
    material = ET.SubElement(visual, "material", name="white")

    # create collision origin
    create_box_with_coordinates(collision, min_xyz, max_xyz)

tree = ET.ElementTree(root)
ET.indent(tree, space="  ", level=0)
tree.write("pyramid_terrain.urdf", encoding="utf-8", xml_declaration=True)
