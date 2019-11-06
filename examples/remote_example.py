"""Remote server example

This examples shows how to send data to a server (a running RECAST3D
process, for instance) running on a remote server.
"""
import tomop
import numpy as np

# The ports given below are the default ports. It is unlikely that you
# want to change them. The remote host must be changed to run this
# example.
remote_host = "example.com"
remote_port1 = 5555
remote_port2 = 5556

def callback(orientation, slice_id):
    print("callback called")
    print(orientation)
    return [4, 4], np.array([0, 255, 0, 255, 255, 0, 255, 0, 255,
                             0, 0, 255, 255, 0, 0,
                             255], dtype='float32')

serv = tomop.server(
    "scene name",
    f"tcp://{remote_host}:{remote_port1}",
    f"tcp://{remote_host}:{remote_port2}",
)

vdp = tomop.volume_data_packet(
    serv.scene_id(),
    np.array([8, 8, 8], dtype='int32').tolist(),
    np.zeros(8 * 8 * 8, dtype='float32'))

serv.send(vdp)

serv.set_callback(callback)
serv.serve()
