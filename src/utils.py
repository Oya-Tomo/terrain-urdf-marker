import xml.etree.ElementTree as ET


def create_box_with_coordinates(root, min_xyz, max_xyz):
    origin = ET.SubElement(
        root,
        "origin",
        xyz=f"{(min_xyz[0] + max_xyz[0]) / 2} {(min_xyz[1] + max_xyz[1]) / 2} {(min_xyz[2] + max_xyz[2]) / 2}",
        rpy="0 0 0",
    )
    geometry = ET.SubElement(root, "geometry")
    box = ET.SubElement(geometry, "box")
    box.set(
        "size",
        f"{max_xyz[0] - min_xyz[0]} {max_xyz[1] - min_xyz[1]} {max_xyz[2] - min_xyz[2]}",
    )
