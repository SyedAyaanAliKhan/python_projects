import cv2
from pyzbar.pyzbar import decode

def scan_qr():
    cap = cv2.VideoCapture(0)
    scanned = False

    while True:
        success, frame = cap.read()
        if not success:
            break

        for barcode in decode(frame):
            data = barcode.data.decode('utf-8')
            if not scanned:
                print("Hi, you just scanned this QR code!, -Ayaan")
                print("QR Code Content:", data)
                scanned = True

        cv2.imshow('QR Code Scanner - Press Q to Quit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or scanned:
            break

    cap.release()
    cv2.destroyAllWindows()

scan_qr()
