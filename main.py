import cv2
import imutils
import socketio
import time
from pyzbar import pyzbar


cap = cv2.VideoCapture(0)

sio = socketio.Client()
last_code = ""


def release_ratchet():
	...

def access_denied():
	...

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on("return-in")
def on_message(data):
	print(data)

def make_request( code ):
	sio.emit("get-in", {'ra': code})
	
def main():
	while True:

		is_ok, img = cap.read()
		
		if is_ok:
			
			img = imutils.resize(img, 400)
			
			qrcodes = pyzbar.decode(img)
			
			for qrcode in qrcodes:
				(x, y, w, h) = qrcode.rect
				cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
				
				qrcodedata = qrcode.data.decode("utf-8")
				qrcodetype = qrcode.type
				
				text = f"{qrcodedata}"
				
				make_request(text)
				
				cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
				
			
			cv2.imshow("qrcode detector", img)
			if cv2.waitKey(1) == ord("q"):
				break
		else:
			print("Erro ao iniciar captura.")
			break

if __name__ == "__main__":
	sio.connect('https://1992-200-131-11-6.ngrok.io/')

	main()

cap.release()
cv2.destroyAllWindows()
