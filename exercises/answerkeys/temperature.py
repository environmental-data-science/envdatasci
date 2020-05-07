class Temperature:
    """
    A class used to represent the temperature

    Attributes
    ----------

    temperature : float
        temperature, in °F or °C

    unit : str
        units of temperature

    Methods
    -------

    get_K()
        returns temperature in K
        
    get_C()
        returns temperature in °C
    
    get_F()
        returns temperature in °F

    """
    def __init__(self, value=74.0, unit='F'):
        '''
        PARAMETERS:
        ----------
        value : int or float
            temperature (default is 74.0)
        
        unit : str
            units of temperature (default is F)
        '''
        self.value = value
        self.unit = unit
        self.temp_K = self.get_K()

    def get_K(self):
        """ Converts temperature to K

        Converts temperature to K using the equation
        
            T_K = T_C + 273.15
        
        where T_K is the temperature in K and T_C is the temperature in °C. If necessary, the temperature is
        first converted from °F to °C according to the equation
        
            T_C = (T_F - 32) * (5./9.)

        where T_F is the temperature in °F.

        Returns:
        --------

        T : temperature in K

        """
        unit = self.unit
        T = self.value

        # If T is in Fahrenheit, convert to C:
        if unit == 'F':
            T = (T - 32) * (5./9.)
            unit = 'C' # Re-assign unit to C

        # If T is in Celsius, convert to Kelvin
        if unit == 'C':
            T = T + 273.15

        return T

    def get_C(self):
        """ Converts temperature to C

        Converts temperature to C using the equation
        
            T_C = (T_F - 32) * (5./9.)
        
        where T_F is the temperature in Fahrenheit and T_C is the temperature in °C. 

        Returns:
        --------

        T : temperature in C

        """
        unit = self.unit
        T = self.value

        # If T is in Fahrenheit, convert to C:
        if unit == 'F':
            T = (T - 32) * (5./9.)
        # If T is in Celsius, do nothing
        if unit == 'C':
            T = T

        return T

    def get_F(self):
        """ Converts temperature to F

        Converts temperature to F using the equation
        
            T_F = (T_C * (9./5.)) + 32
        
        where T_F is the temperature in Fahrenheit and T_C is the temperature in °C. 

        Returns:
        --------

        T : temperature in F

        """
        unit = self.unit
        T = self.value

        # If T is in Celsius, convert to F:
        if unit == 'C':
            T = (T * (9./5.)) + 32

        # If T is in Fahrenheit, do nothing
        if unit == 'F':
            T = T

        return T