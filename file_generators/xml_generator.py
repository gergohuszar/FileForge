import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


class XmlGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        # Create the root element
        root = ET.Element("root")

        # Add child elements
        child1 = ET.SubElement(root, "child1")
        child1.text = "This is child 1"

        child2 = ET.SubElement(root, "child2")
        child2.text = content

        # Adding an element with attributes
        child3 = ET.SubElement(
            root, "child3", attrib={"attribute1": "value1", "attribute2": "value2"}
        )
        child3.text = "This is child 3 with attributes"

        # Convert the element tree to a string
        xml_str = prettify(root)

        # Write the XML to a file
        with open(f"{filename}.xml", "w") as f:
            f.write(xml_str)
