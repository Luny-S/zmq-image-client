import numpy as np
import cv2 as cv

import zmq
import time


def makeImage():
    pixelRed = [np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]
    pixelGreen = [np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]
    pixelBlue = [np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]

    array = np.array([
        [pixelRed, pixelGreen, pixelBlue, pixelGreen, pixelRed],
        [pixelGreen, pixelBlue, pixelRed, pixelGreen, pixelBlue],
        ], dtype='uint8')

    return array


def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.setsockopt(zmq.CONFLATE, 1)
    socket.bind("tcp://*:5555")

    print("Starting server")
    while True:
        socket.send(makeImage().tobytes())
        time.sleep(1)


if __name__ == '__main__':
    main()
