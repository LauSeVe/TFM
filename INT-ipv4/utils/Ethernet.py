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
dst_mac_widget = widgets.Text(value="22:33:44:55:66:01", description="Destination MAC:")
src_mac_widget = widgets.Text(value="22:33:44:55:66:11", description="Source MAC:")


# Button to create the IP Header
button_Ether = ButtonPacket(description="Set Ethernet Header", packet=None)

def ethernet_header_widget():
    # Attach the function to the button click event
    button_Ether.on_click(button_click_Ether)
    
    # Display the widgets and button
    display(dst_mac_widget,
            src_mac_widget,
            button_Ether)
    
    return button_Ether

# Define the function to be called on button click
def button_click_Ether(b):
    try:
        b.packet = create_ether_header(
            dst_mac_widget.value,
            src_mac_widget.value,
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)

