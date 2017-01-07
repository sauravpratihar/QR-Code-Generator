import pyqrcode

x = 201301001
while x <= 201301010:
	url = pyqrcode.create(x)
	with open('QR/' + str(x) + '.png', 'w') as fstream:
		url.png(fstream, scale=20)
	# same as above
	url.png('QR/' + str(x) + '.png', scale=20)
	print(str(x) + " Done")
	x = x + 1
	# in-memory stream is also supported
