from scapy.all import Ether
import ipywidgets as widgets
from IPython.display import display
from traitlets import traitlets
from PIL import Image, ImageDraw, ImageFont

class ButtonPacket(widgets.Button):
    def __init__(self, packet=None, *args, **kwargs):
        super(ButtonPacket, self).__init__(*args, **kwargs)
        self.add_traits(packet=traitlets.Any(packet))

# Create widgets for user input
# Ethernet
src_mac_widget = widgets.Text(value="22:33:44:55:66:01", description="Source MAC:")
dst_mac_widget = widgets.Text(value="22:33:44:55:66:11", description="Destination MAC:")
type_widget = widgets.Text(value="0800", description="Type:")




# Button to create the IP Header
button_Ether = ButtonPacket(description="Set Ethernet Header", packet=None)

def ethernet_header_widget():
    # Attach the function to the button click event
    button_Ether.on_click(button_click_Ether)
    
    # Display the widgets and button
    display(src_mac_widget,
            dst_mac_widget,
            type_widget,
            button_Ether)
    
    return button_Ether

# Define the function to be called on button click
def button_click_Ether(b):
    try:
        b.packet = create_ether_header(
            src_mac_widget.value,
            dst_mac_widget.value,
            int(type_widget.value,16)
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)


# Function to create and display packet headers
def create_ether_header(src_mac, dst_mac, type):
    # Create an Ethernet packet
    ethernet_packet = Ether(dst=dst_mac, src=src_mac, type=type)
    return ethernet_packet  


def createEthernetImage(etherheader):
    # Open an image
    imageEthernet = Image.open("./images/ethernet.png")

    # Create a drawing object
    draw = ImageDraw.Draw(imageEthernet)

    # Choose a font and size
    font = ImageFont.load_default(size=30) 

    # Choose text color
    text_color = (0, 0, 0)  # Black

    # dst
    text_position = (45, 180)
    text = str(etherheader.packet.dst)
    draw.text(text_position, text, font=font, fill=text_color)

    # src
    text_position = (365, 180)
    text = str(etherheader.packet.src)
    draw.text(text_position, text, font=font, fill=text_color)

    # type
    text_position = (800, 180)
    text = str(etherheader.packet.type)
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the modified image
    imageEthernet.save("./images/ethernet_header_configured.png")

    return imageEthernet
