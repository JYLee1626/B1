# Controller class that takes in a dictionary of gains from the user
# and computes the control action based on the current error and the previous error

class Controller:
    def __init__(self, gains):
        """
        Initialize the PD controller with proportional and derivative gains.
        
        Parameters:
        Takes in a dictionary of gains with keys 'Kp' , 'Ki', Kd'
        """
        self.Kp = gains['Kp']
        self.Kd = gains['Kd']
        self.Ki = gains['Ki']
        self.prev_error = 0.0  # Initialize the previous error to 0

    def PD_control(self, error):
        """
        Compute the control action based on the current error and the previous error.
        
        Parameters:
        error (float): The current error (difference between reference and current depth).
        
        Returns:
        control_action (float): The control action to be applied.
        """
        # PD control law
        control_action = self.Kp * error + self.Kd * (error - self.prev_error) 
        
        # Update the previous error
        self.prev_error = error
        
        return control_action

    def reset(self):
        """
        Reset the previous error. Useful if starting a new simulation or mission.
        """
        self.prev_error = 0.0

