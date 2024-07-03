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
src_ip_widget = widgets.Text(value="135.41.67.1", description="Source Address:")
dst_ip_widget = widgets.Text(value="135.41.67.2", description="Destination Address:")

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
def create_ip_header(src_ip, dst_ip, ):
    # Create an IP packet
    ip_packet = IP(src=src_ip, 
                   dst=dst_ip,
                   )
    return ip_packet  


def createIPImage(ipheader):
    # Open an image
    imageIP = Image.open("./images/ip.png")

    # Create a drawing object
    draw = ImageDraw.Draw(imageIP)

    # Choose a font and size
    font = ImageFont.load_default(size=30) 

    # Choose text color
    text_color = (0, 0, 0)  # Black

    # Source Address
    text_position = (850, 510)
    text = str(ipheader.packet.src)
    draw.text(text_position, text, font=font, fill=text_color)

    # Destination Address
    text_position = (850, 620)
    text = str(ipheader.packet.dst)
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the modified image
    imageIP.save("./images/ip_header_configured.png")

    return imageIP
