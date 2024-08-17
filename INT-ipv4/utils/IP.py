from scapy.all import *
import ipywidgets as widgets
from IPython.display import display
from traitlets import traitlets
from PIL import Image, ImageDraw, ImageFont
from scapy.layers.inet import _IPOption_HDR
from utils.MRI import *

class ButtonPacket(widgets.Button):
    def __init__(self, packet=None, *args, **kwargs):
        super(ButtonPacket, self).__init__(*args, **kwargs)
        self.add_traits(packet=traitlets.Any(packet))

# Create widgets for user input
# IP
src_ip_widget = widgets.Text(value="135.41.1.1", description="Source Address:")
dst_ip_widget = widgets.Text(value="135.41.2.1", description="Destination Address:")

# Button to create the IP Header
button_IP = ButtonPacket(description="Set IP Header", packet=None)

def ip_header_widget():
    # Attach the function to the button click event
    button_IP.on_click(button_click_ip)
    
    # Display the widgets and button
    display(src_ip_widget, 
            dst_ip_widget,
            button_IP)
    
    return button_IP

# Define the function to be called on button click
def button_click_ip(b):
    try:
        b.packet = create_ip_header(
            src_ip_widget.value,
            dst_ip_widget.value
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)


# Function to create and display packet headers
def create_ip_header(src_ip, dst_ip):
    # Create an IP packet
    ip_packet = IP(src=src_ip, 
                   dst=dst_ip, 
                   proto=147,
                   options=IPOption_MRI(count=0, swtraces=[])
                   )
    return ip_packet  
