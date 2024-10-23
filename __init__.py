# User input
# Example Usage
gains = {'Kp': 0.15, 'Ki': 0.0, 'Kd': 0.6}
controller = Controller(gains)

# is there a way to get the current error 
control_action = controller.PD_control(error)
