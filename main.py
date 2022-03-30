import cv2
import imutils
import socketio
import time
from pyzbar import pyzbar
from gpio_control import *

WS_URL = "https://25d5-200-131-11-6.ngrok.io/"
SEND_TOPIC = "get-in"
RECEIVE_TOPIC = "return-in"

cap = cv2.VideoCapture(0)

sio = socketio.Client()

def release_ratchet():
    print("Acesso permitido.")
    
    open()


def access_denied():
    print("Acesso negado.")
    
    close()


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


@sio.on(RECEIVE_TOPIC)
def on_message(data):
    print(data)
    
    if "error" in data:
    	if not data["error"]:
    		release_ratchet()
    	else:
    		access_denied()


def make_request(code):
    sio.emit(SEND_TOPIC, {"ra": code})


def main():
	last_code = ""
	
	while True:
		is_ok, img = cap.read()
		
		if is_ok:
		
			img = imutils.resize(img, 400)

			qrcodes = pyzbar.decode(img)

			for qrcode in qrcodes:
				(x, y, w, h) = qrcode.rect
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
				qrcodedata = qrcode.data.decode("utf-8")
				qrcodetype = qrcode.type

				text = f"{qrcodedata}"

				if text != last_code:
					last_code = qrcodedata
					print(text)
					make_request(qrcodedata)
				else:
					time.sleep(1.0)
					
				cv2.putText(
                    img,
                    text,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2,
                )

			cv2.imshow("qrcode detector", img)
			if cv2.waitKey(1) == ord("q"):
				break
		else:
			print("Erro ao iniciar captura.")
			break
			
if __name__ == "__main__":
    config_gpio()

    sio.connect(WS_URL)

    main()

cap.release()
cv2.destroyAllWindows()
sio.disconnect()
