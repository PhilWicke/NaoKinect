from primesense import openni2, nite2

openni2.initialize()     # can also accept the path of the OpenNI redistribution
nite2.initialize()

if (nite2.is_initialized()):
    print("nite2 initialized")
else:
    print("nite2 not initialized")

dev = openni2.Device.open_any()
print(dev.get_sensor_info(openni2.SENSOR_DEPTH))

nite2.UserTracker(dev)

depth_stream = dev.create_depth_stream()
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
depth_stream.stop()

openni2.unload()