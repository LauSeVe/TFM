from scapy.all import *
import ipywidgets as widgets
from IPython.display import display
from traitlets import traitlets
from PIL import Image, ImageDraw, ImageFont

TYPE_EPHeader = 0x93

class EPHeader(Packet):
    Name = "EPHeader"
    fields_desc = [
        BitField("hawkID", 0, 16),
        BitField("exercise", 0, 4),
        BitField("ethernet", 0, 1),
        BitField("ipv4", 0, 1),
        BitField("ipv6", 0, 1),
        BitField("correct", 0, 1),
        StrFixedLenField("info", b"\x00" * 20, length=20),
    ]
bind_layers(IP, EPHeader, proto=TYPE_EPHeader)

class ButtonPacket(widgets.Button):
    def __init__(self, packet=None, *args, **kwargs):
        super(ButtonPacket, self).__init__(*args, **kwargs)
        self.add_traits(packet=traitlets.Any(packet))

# Create widgets for user input
# EPHeader
hawkID_epheader_widget = widgets.Text(value="4010", description="HawkID:")
exercise_epheader_widget = widgets.Text(value="0", description="Exercise:")
ethernet_epheader_widget = widgets.Text(value="0", description="Ethernet:")
ipv4_epheader_widget = widgets.Text(value="0", description="IPv4:")
ipv6_epheader_widget = widgets.Text(value="0", description="IPv6:")
correct_epheader_widget = widgets.Text(value="0", description="Correct:")
info_epheader_widget = widgets.Text(value="0", description="Info:")


# Button to create the EP Header
button_EPHeader = ButtonPacket(description="Set EP Header", packet=None)

def ep_header_widget():
    # Attach the function to the button click event
    button_EPHeader.on_click(button_click_epheader)
    
    # Display the widgets and button
    display(hawkID_epheader_widget,
            exercise_epheader_widget,
            ethernet_epheader_widget,
            ipv4_epheader_widget,
            ipv6_epheader_widget,
            correct_epheader_widget,
            info_epheader_widget,
            button_EPHeader
            )
    
    return button_EPHeader

# Define the function to be called on button click
def button_click_epheader(b):
    try:
        b.packet = create_ep_header(
            int(hawkID_epheader_widget.value),
            int(exercise_epheader_widget.value),
            int(ethernet_epheader_widget.value),
            int(ipv4_epheader_widget.value),
            int(ipv6_epheader_widget.value),
            int(correct_epheader_widget.value),
            bytes(info_epheader_widget.value, "utf-8")
        )

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)


# Function to create and display packet headers
def create_ep_header(hawkID, exercise, ethernet, ipv4, ipv6, correct, info):
    # Create an EP packet
    ep_packet = EPHeader(hawkID=hawkID,
                        exercise=exercise,
                        ethernet=ethernet,
                        ipv4=ipv4,
                        ipv6=ipv6,
                        correct=correct,
                        info=info
                    )
    return ep_packet  


def createEPImage(epheader):
    # Open an image
    imageEP = Image.open("./images/ep.png")

    # Create a drawing object
    draw = ImageDraw.Draw(imageEP)

    # Choose a font and size
    font = ImageFont.load_default(size=30) 

    # Choose text color
    text_color = (0, 0, 0)  # Black
   

    # HawkID
    text_position = (180, 195)
    text = str(epheader.packet.hawkID)
    draw.text(text_position, text, font=font, fill=text_color)

    # exercise
    text_position = (180, 165)
    text = str(epheader.packet.exercise)
    draw.text(text_position, text, font=font, fill=text_color)

    # ethernet
    text_position = (180, 135)
    text = str(epheader.packet.ethernet)
    draw.text(text_position, text, font=font, fill=text_color)

    # ipv4
    text_position = (180, 105)
    text = str(epheader.packet.ipv4)
    draw.text(text_position, text, font=font, fill=text_color)

    # ipv6
    text_position = (180, 75)
    text = str(epheader.packet.ipv6)
    draw.text(text_position, text, font=font, fill=text_color)

    # correct
    text_position = (180, 45)
    text = str(epheader.packet.correct)
    draw.text(text_position, text, font=font, fill=text_color)

    # Info
    text_position = (180, 225)
    text = str(epheader.packet.info)
    draw.text(text_position, text, font=font, fill=text_color)


    # Save the modified image
    imageEP.save("./images/ep_header_configured.png")

    return imageEP
