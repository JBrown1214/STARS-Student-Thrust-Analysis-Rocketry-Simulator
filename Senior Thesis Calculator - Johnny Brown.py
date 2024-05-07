class Motor:
    def __init__(self, mass, burn_time, impulse_total, p_exit, altitude):
        self.mass = mass
        self.burn_time = burn_time
        self.impulse_total = impulse_total
        self.p_exit = p_exit
        self.Altitude_m = altitude
        self.p_ambient = 101325* ((1 - ((2.25577*(10**-5))*self.Altitude_m))**5.25588)
        self.m_dot = self.mass / self.burn_time
        self.v_exit = self.impulse_total / self.mass
    
    def get_mass(self):
        return self.mass
    def get_burn_time(self):
        return self.burn_time
    def get_impulse_total(self):
        return self.impulse_total
    def get_exit_velocity(self):
        return self.__V_exit
    def get_mass_flow_rate(self):
        return self.__M_dot
    def get_exit_pressure(self):
        return self.__P_exit
    def get_altitude(self):
        return self.__Altitude_m

    def set_mass(self, mass):
        self.mass = mass
    def set_burn_time(self, burn_time):
        self.burn_time = burn_time
    def set_impulse_total(self, impulse_total):
        self.impulse_total = impulse_total
    def set_mass_flow_rate(self, new_M_dot):
        self.__M_dot = new_M_dot
    def set_exit_velocity(self, new_V_exit):
        self.__V_exit = new_V_exit
    def set_exit_pressure(self, new_P_exit):
        self.__P_exit = new_P_exit
    def set_altitude(self, new_Altitude_m):
            self.__Altitude_m = new_Altitude_m

class Bell_Nozzle(Motor):
    def __init__(self, mass, burn_time, impulse_total, p_exit, altitude, exit_area):
        super().__init__(mass, burn_time, impulse_total, p_exit, altitude)()
        self.exit_area = exit_area
        self.thrust = (self.m_dot * self.v_exit) + ((self.p_exit - self.p_ambient)*self.exit_area)

class Aerospike_Nozzle(Motor):
    def __init__(self, mass, burn_time, impulse_total, p_exit_nozzle, altitude, p_exit_centerbody, p_base):
        super().__init__(mass, burn_time, impulse_total, p_exit_nozzle, altitude)()
        self.p_exit_centerbody = p_exit_centerbody
        self.p_base = p_base
        #self.thrust calculation

nozzle_type = input('What type of nozzle will be tested? (bell/aerospike):')
motor_class = input('What class of motor will be tested? (A/B/C/D/):')
altitude = input('What altitude will this be tested at? (meters above sea level):')

#calculate ambient pressure using altitude
#calculate motor mass, burn time, impulse total, and p_exit from motor class and Estes info


# if nozzle_type == 'bell' or 'Bell' or 'bell nozzle' or 'Bell nozzle':
        #input exit_area and assign it as a variable
        #create a bell nozzle subclass of the motor class (using all variables)
        #return nozzle thrust estimate as well as other calculated rocket data
# elif nozzle_type == 'aerospike' or 'Aerospike' or 'aerospike nozzle' or 'Aerospike nozzle':
        #input p_exit_centerbody and p_base and assign them as variables
        #create an Aerospike nozzle subclass of the motor class (using all variables)
        #return nozzle thrust estimate as well as other calculated rocket data
