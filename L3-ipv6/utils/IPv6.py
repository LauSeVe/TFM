from scapy.all import IPv6
import ipywidgets as widgets
from IPython.display import display
from traitlets import traitlets
from PIL import Image, ImageDraw, ImageFont

class ButtonPacket(widgets.Button):
    def __init__(self, packet=None, *args, **kwargs):
        super(ButtonPacket, self).__init__(*args, **kwargs)
        self.add_traits(packet=traitlets.Any(packet))

# Create widgets for user input
# IPv6
src_ip_widget = widgets.Text(value="2001:db8:b57:6602::bef6:4118", description="Source Address:")
dst_ip_widget = widgets.Text(value="2001:db8:b57:6603::bef6:4118", description="Destination Address:")

# Button to create the IPv6 Header
button_IPv6 = ButtonPacket(description="Set IPv6 Header", packet=None)

def ip_header_widget():
    # Attach the function to the button click event
    button_IPv6.on_click(button_click_ip)
    
    # Display the widgets and button
    display(src_ip_widget, 
            dst_ip_widget,
            button_IPv6)
    
    return button_IPv6

# Define the function to be called on button click
def button_click_ip(b):
    try:
        b.packet = create_ipv6_header(
            src_ip_widget.value,
            dst_ip_widget.value
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)


# Function to create and display packet headers
def create_ipv6_header(src_ip, dst_ip):
    # Create an IPv6 packet
    ipv6_packet = IPv6(src=src_ip, 
                       dst=dst_ip, nh=147)
    return ipv6_packet  
