# import logging
import os
import numpy as np
from PIL import Image
from Transmitters.qpsk import QPSKTransmitter

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('main')

# SETUP
image_directory = os.path.join(os.getcwd(), 'pictures', 'input')
output_directory = os.path.join(os.getcwd(), 'pictures', 'output')


# IMAGE UTILITIES

def array_from_image(image_path: str) -> np.ndarray:
	"""Loads an image from the specified path and returns it as a numpy array"""
	with Image.open(image_path) as im:
		image_array = np.array(im)
	return image_array


def send_image(filename: str):
	print("Transmitting image", filename, "via QPSK")
	transmitter = QPSKTransmitter(10)
	input_image = array_from_image(os.path.join(image_directory, filename))
	output_image = transmitter.transmit_byte_array(input_image.flatten()).reshape(input_image.shape)

	pillow_image = Image.fromarray(output_image, 'RGB')
	pillow_image.save(os.path.join(output_directory, 'reconstructed_' + filename))

	print(
		f"RESULTS:\n",
		f"Equal: {np.array_equal(input_image, output_image)}\n",
	)


print("-- START --")
send_image('racoon_40px.png')
print("-- FINISHED --")
