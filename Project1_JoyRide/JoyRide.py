# CODE CELL

# Before/After running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# You need to wait for the Kernel Ready message.


car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    velocity_request = 0
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this example the car will drive forward for three seconds
    # and then backs up until its pos_y is less than 32 then comes to a stop by braking
    velocity_request = calc_velocity_request(pos_y)
    throttle, brake = ctrl_velocity(velocity,velocity_request)
    steering_angle = steervehicle(pos_x)

    car_parameters['throttle'] = throttle
    car_parameters['brake'] = brake
    car_parameters['steer'] = steering_angle

    return car_parameters

def steervehicle(pos_x):
    if (pos_x < 125.5):
        steering_angle = 25
    elif ((pos_x > 126.1) and (pos_x < 128.9)):
        steering_angle = -25
    else:
        steering_angle = 0
    return steering_angle

def calc_velocity_request (pos_y):
    velocity_request = 0
    
    if pos_y < 32:
        velocity_request = -1
    else:
        velocity_request = 0
    return velocity_request
    
def ctrl_velocity(velocity,velocity_request):
    throttle = 0
    brake = 0
    enable_controller = 0
    if (enable_controller):
        factor = 0.5
        ctrl_deviation = velocity_request - velocity
        throttle = ctrl_deviation * factor
        
    else:
        if (velocity_request > 0):
            throttle = 1
            brake = 0
        elif (velocity_request < 0):
            throttle = -1
            brake = 0
        else:
            throttle = 0
            brake = 1
    
    throttle = limit_throttle(throttle)
    return throttle, brake
    
def limit_throttle(value):
    return_value = 0
    max_throttle = 1
    min_throttle = -1

    if value > max_throttle:
        return_value = max_throttle
    elif value < min_throttle:
        return_value = min_throttle
    else:
        return_value = value

    return return_value 


control(126, 31, 0, 0)
print("throttle:",car_parameters["throttle"])
print("brake:",car_parameters["brake"])
print("steer:",car_parameters["steer"])
# import src.simulate as sim
# sim.run(control)
    