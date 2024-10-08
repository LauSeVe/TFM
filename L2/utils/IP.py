from scapy.all import IP
import ipywidgets as widgets
from IPython.display import display
from traitlets import traitlets
from PIL import Image, ImageDraw, ImageFont

class ButtonPacket(widgets.Button):
    def __init__(self, packet=None, *args, **kwargs):
        super(ButtonPacket, self).__init__(*args, **kwargs)
        self.add_traits(packet=traitlets.Any(packet))

# Create widgets for user input
# IP
version_ip_widget = widgets.Text(value="4", description="Version:")
IHL_ip_widget = widgets.Text(value="5", description="IHL:")
TOS_ip_widget = widgets.Text(value="0", description="TOS:")
len_ip_widget = widgets.Text(value="20", description="Total Length:")
iden_ip_widget = widgets.Text(value="0", description="Identification:")
flags_ip_widget = widgets.Text(value="0", description="Flags:")
fragoff_ip_widget = widgets.Text(value="0", description="Fragment Offset:")
TTL_ip_widget = widgets.Text(value="64", description="TTL:")
protocol_ip_widget = widgets.Text(value="147", description="Protocol:")
checksum_ip_widget = widgets.Text(value="0", description="Header Checksum:")
src_ip_widget = widgets.Text(value="135.41.1.1", description="Source Address:")
dst_ip_widget = widgets.Text(value="135.41.1.2", description="Destination Address:")

# Button to create the IP Header
button_IP = ButtonPacket(description="Set IP Header", packet=None)

def ip_header_widget():
    # Attach the function to the button click event
    button_IP.on_click(button_click_ip)
    
    # Display the widgets and button
    display(version_ip_widget, 
            IHL_ip_widget, 
            TOS_ip_widget, 
            len_ip_widget, 
            iden_ip_widget, 
            flags_ip_widget, 
            fragoff_ip_widget, 
            TTL_ip_widget, 
            protocol_ip_widget, 
            checksum_ip_widget, 
            src_ip_widget, 
            dst_ip_widget,
            button_IP)
    
    return button_IP

# Define the function to be called on button click
def button_click_ip(b):
    try:
        b.packet = create_ip_header(
            int(version_ip_widget.value),
            int(IHL_ip_widget.value),  
            int(TOS_ip_widget.value),
            int(len_ip_widget.value),
            int(iden_ip_widget.value),
            int(flags_ip_widget.value),
            int(fragoff_ip_widget.value),
            int(TTL_ip_widget.value),
            int(protocol_ip_widget.value),
            int(checksum_ip_widget.value),
            src_ip_widget.value,
            dst_ip_widget.value
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)


# Function to create and display packet headers
def create_ip_header(version_ip, IHL_ip, TOS_ip, len_ip, iden_ip, flags_ip, fragoff_ip, TTL_ip, protocol_ip, checksum_ip, src_ip, dst_ip, ):
    # Create an IP packet
    ip_packet = IP(version=version_ip, 
                   ihl=IHL_ip, 
                   tos=TOS_ip, 
                   len=len_ip, 
                   id=iden_ip, 
                   flags=flags_ip, 
                   frag=fragoff_ip, 
                   ttl=TTL_ip, 
                   proto=protocol_ip, 
                   chksum=checksum_ip, 
                   src=src_ip, 
                   dst=dst_ip,
                   )
    return ip_packet  

