import pypot.dynamixel as dyna


ports = dyna.get_available_ports()

if not ports:
    raise IOError('no port located!')

print('ports found',ports)

print('connecting on first available port: ',ports[0])
dxl_io = dyna.DxlIO(ports[0])

motors = dxl_io.scan()
if not motors:
    raise IOError('no motors connected!')
print('Connected motors: ',motors)

