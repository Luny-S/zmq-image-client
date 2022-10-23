import numpy as np
import cv2 as cv

import zmq
import time


def main():
    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to image server…")
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt(zmq.SUBSCRIBE, b'')

    for request in range(10):
        deserialized = np.frombuffer(socket.recv(), dtype=np.uint8)
        img = np.reshape(deserialized, newshape=(2, 5, 3))

        print(img)

        cv.imshow("Client received", cv.resize(img, (1000,200)))
        cv.waitKey(10)


if __name__ == '__main__':
    main()
