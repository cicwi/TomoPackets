import tomop
import numpy as np


def callback(orientation, slice_id):
    print("callback called")
    print(orientation)
    return [4, 4], np.array([0, 255, 0, 255, 255, 0, 255, 0, 255,
                             0, 0, 255, 255, 0, 0,
                             255], dtype='float32')

serv = tomop.server("scene name")

vdp = tomop.volume_data_packet(
    serv.scene_id(),
    np.array([8, 8, 8], dtype='int32').tolist(),
    np.zeros(8 * 8 * 8, dtype='float32'))

serv.send(vdp)

serv.set_callback(callback)
serv.serve()
