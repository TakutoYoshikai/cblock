import cv2
import tkinter
from threading import Thread

def open_camera():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 2)
    while (cap.isOpened()):
        ret, frame = cap.read()
    cap.release()


def main():
    thread = Thread(target=open_camera)
    thread.setDaemon(True)
    thread.start();
    root = tkinter.Tk()
    root.title("cblock is enabled")
    root.resizable(False, False)
    w = root.winfo_screenwidth()
    w = w - 300
    root.geometry("300x1+" + str(w) + "+0")
    root.mainloop()

if __name__ == "__main__":
    main()
