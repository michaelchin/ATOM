# Given a parameter definition, generates necessary C++, Python and XML bindings
# coding=utf-8


def main():
    # read the input definition

    # name, description, datatype, default
    PARAMS = {
        'common': [
            ( 'bathymetry_path', '', 'string', '../data/Paleotopography_bathymetry/Golonka_rev210' ),
            ( 'BathymetrySuffix', '', 'string', 'Ma_Golonka.xyz' ),
#            ( 'verbose', '', 'bool', False ),
            ( 'verbose', '', 'bool', True ),
            ( 'output_path', 'directory where model outputs should be placed ( must end in / )', 'string', 'output' ),
        ],

        'atmosphere': [
            ( 'velocity_iter_max', '', 'int', 2 ),
            ( 'pressure_iter_max', '', 'int', 2 ),
            ( 'velocity_iter_max_2D', '', 'int', 2 ),
            ( 'pressure_iter_max_2D', '', 'int', 2 ),

            ( 'coriolis', 'coriolis force', 'double', 1.0 ),
            ( 'centrifugal', 'centrifugal force', 'double', 1.0 ),
            ( 'WaterVapour', 'water vapour', 'double', 1.0 ),
            ( 'buoyancy', 'buoyancy', 'double', 1.0 ),
            ( 'CO2', 'CO2', 'double', 1.0 ),

            ( 'epsres', 'accuracy of relative and absolute errors', 'double', 0.00001 ),

            ( 'sun', 'while no variable sun position wanted', 'int', 0 ),
            ( 'NASATemperature', 'surface temperature given by NASA', 'int', 1 ),
            ( 'RadiationModel', 'surface temperature computation by a radiation model', 'int', 3 ),
            ( 'IceShield', 'compute ice shields? computation of ice shield following the theorie by Milankowitsch', 'int', 0 ),

            ( 'declination', 'position of sun axis, today 23,4°, 21.12.: -23,4°, am 21.3. und 23.9.: 0°, 21.6.: +23,4°, in between sin form', 'int', 0 ),
            ( 'sun_position_lat', 'position of sun j = 120 means 30°S, j = 60 means 30°N', 'int', 60 ),
            ( 'sun_position_lon', 'position of sun k = 180 means 0° or 180° E ( Greenwich, zero meridian  )', 'int', 180 ),

            ( 'Ma_max', 'parabolic temperature distribution 300 Ma ( from Ruddiman )', 'int', 300 ),
            ( 'Ma_max_half', 'half of time scale', 'int', 150 ),

            ( 'L_atm', 'extension of the atmosphere shell in m, 20000 m / 40 steps = 500 m', 'double', 20000. ),

            ( 'dt', 'time step coincides with the CFL condition', 'double', 0.0001 ),

            ( 'dr', 'compares to 500 m hight, 0.0005 * 40 = .02 * 1000 km = 20 km', 'double', 0.025 ),

            ( 'ik', 'solar constant in W/m2', 'double', 1366. ),
            ( 'ik_equator', 'solar short wave radiation on the surface of the earth, Ik / 4', 'double', 341.5 ),
            ( 'ik_pole', 'solar short wave radiation at the poles, an approximation for the singularity at the poles', 'double', 60. ),

            ( 'sigma', 'Stefan-Boltzmann constant W/( m²*K4 )', 'double', 5.670280e-8 ),

            ( 'albedo_pole', 'albedo around the poles', 'double', 0.7 ),
            ( 'albedo_equator', 'albedo around the equator', 'double', 0.15 ),

            ( 'epsilon_equator', 'emissivity and absorptivity caused by other gases than water vapour / ( by Häckel )', 'double', 0.594 ),
            ( 'epsilon_tropopause', 'emissivity and absorptivity caused by other gases than water vapour in the tropopause', 'double', 0.001 ),
            ( 'epsilon_pole', 'emissivity and absorptivity caused by other gases than water vapour at the poles', 'double', 0.5 ),
            ( 'epsilon_extra', 'capability of emissions in the atmosphere, 2D approach', 'double', 0.71 ),

            ( 'radiation_ocean', 'increase of radiation at equator in W/m²', 'double', 40.0 ),
            ( 'radiation_pole', 'negative amount of radiation at poles in W/m²', 'double', -40.0 ),
            ( 'radiation_equator', 'positive amount of radiation at equator in W/m²', 'double', 100.0 ),

            ( 're', 'Reynolds number: ratio viscous to inertia forces, Re = u * L / nue', 'double', 1000. ),
            ( 'ec', 'Eckert number: ratio kinetic energy to enthalpy, Ec = u² / cp T', 'double', 0.00044 ),
            ( 'sc_WaterVapour', 'Schmidt number of water vapour, Sc = nue / D', 'double', 0.6 ),
            ( 'sc_CO2', 'Schmidt number of CO2', 'double', 0.96 ),
            ( 'pr', 'Prandtl number of air for laminar flows', 'double', 0.7179 ),
            ( 'g', 'gravitational acceleration of the earth', 'double', 9.8066 ),
            ( 'omega', 'rotation number of the earth', 'double', 7.29e-5 ),
            ( 'ep', 'ratio of the gas constants of dry air to water vapour [ / ]', 'double', 0.623 ),
            ( 'hp', 'water vapour pressure at T = 0°C: E = 6.1 hPa', 'double', 6.1078 ),
            ( 'R_Air', 'specific gas constant of air in J/( kg*K )', 'double', 287.1 ),
            ( 'r_air', 'density of dry air in kg/m³ at 20°C', 'double', 1.2041 ),
            ( 'R_WaterVapour', 'specific gas constant of water vapour in J/( kg*K )', 'double', 461.6 ),
            ( 'r_water_vapour', 'density of saturated water vapour in kg/m³ at 10°C', 'double', 0.0094),
            ( 'R_co2', 'specific gas constant of CO2 in J/( kg*4.5K )', 'double', 188.91 ),
            ( 'lv', 'specific latent Evaporation heat ( Condensation heat ) in J/kg', 'double', 2.52e6 ),
            ( 'ls', 'specific latent vaporisation heat ( sublimation heat ) in J/kg', 'double', 2.83e6 ),
            ( 'cp_l', 'specific heat capacity of dry air at constant pressure and 20°C in J/( kg K )', 'double', 1005. ),
            ( 'lamda', 'heat transfer coefficient of air in W/m² K )', 'double', 0.0262 ),
            ( 'r_water', 'density of water in kg/m³ at 20°C', 'double', 1000.0 ),
            ( 'r_co2', 'density of CO2 in kg/m³ at 25°C', 'double', 0.0019767 ),
            ( 'gam', 'constant slope of temperature    gam = 0.65 K/100 m', 'double', 0.65 ),

            ( 'u_0', 'maximum value of velocity in 15 m/s compares to 54 km/h', 'double', 15.0 ),
            ( 'p_0', 'pressure at sea level in hPa', 'double', 1013.25 ),
            ( 't_0', 'temperature in K compare to 0°C', 'double', 273.15 ),
            ( 'c_0', 'maximum value of water vapour in kg / kg', 'double', 0.035 ),
            ( 'co2_0', 'maximum value of CO2 in ppm at preindustrial times', 'double', 280.0 ),

            ( 'ua', 'initial velocity component in r-direction', 'double', 0.0 ),
            ( 'va', 'initial velocity component in theta-direction', 'double', 0.0 ),
            ( 'wa', 'initial velocity component in phi-direction', 'double', 0.0 ),
            ( 'pa', 'initial value for the pressure field', 'double', 0.0 ),
            ( 'ca', 'value 0.04 stands for the maximum value of 40 g/kg water vapour', 'double', 0.0 ),
            ( 'ta', 'initial value for the temperature field, 1.0 compares to 0° C compares to 273.15 K', 'double', 1.0 ),
            ( 'coa', 'initial value of co2 = 1.0 compares to 280 ppm in pre-industrial times', 'double', 1.0 ),

            ( 't_cretaceous_max', 'maximum add of mean temperature in °C during cretaceous times', 'double', 10.0 ),
            ( 't_cretaceous', 'value at modern times', 'double', 0.0 ),

            ( 't_average', 'mean temperature of the modern earth', 'double', 15.0 ),
            ( 't_equator', 'temperature t_0 = 1.11 compares to 30.0° C compares to 303.15 K', 'double', 1.11 ),
            ( 't_pole', 'temperature at the poles t_pole = 0.927 compares to -20.0°C compares to 253.15 K', 'double', 0.927 ),
            ( 't_tropopause', 'temperature in the tropopause, t = 0.798 compares to -55°C compares to 218.15 K', 'double', 0.798 ),
#            ( 't_land', 'temperature increase on land by 1°C ( 1°C compares to t_land = 0.003661 )', 'double', 0.003661 ),
            ( 't_land', 'temperature increase on land by 1°C ( 1°C compares to t_land = 0.003661 )', 'double', 0.0 ),

#            ( 'c_tropopause', 'minimum water vapour at tropopause c_tropopause = 0.001 compares to 0.001 kg/kg', 'double', 0.0 ),
            ( 'c_tropopause', 'minimum water vapour at tropopause c_tropopause = 0.001 compares to 0.001 kg/kg', 'double', 0.001 ),
            ( 'c_land', 'water vapour reduction on land ( 50% of the saturation value )', 'double', 0.5 ),
           ( 'c_ocean', 'water vapour reduction on sea surface ( 50% of the saturation value )', 'double', 0.5 ),
#           ( 'c_land', 'water vapour reduction on land ( 50% of the saturation value )', 'double', 0.45 ),
#            ( 'c_ocean', 'water vapour reduction on sea surface ( 50% of the saturation value )', 'double', 0.45 ),

            ( 'co2_average', 'rate of CO2 at preindustrial times', 'double', 372.0 ),
            ( 'co2_equator', 'maximum rate of CO2 at sea level at equator, 1. compares to 330 ppm', 'double', 330.0 ),
            ( 'co2_tropopause', 'minimum rate CO2 at tropopause 0 ppm', 'double', 0.0 ),
            ( 'co2_pole', 'maximum rate of CO2 of the sea surface at poles', 'double', 305.0 ),
            ( 'co2_cretaceous', 'value at modern times', 'double', 0.0 ),
            ( 'co2_vegetation', 'value compares to 100/600Gt per year on the global surface by vegetation', 'double', 3.0 ),
            ( 'co2_ocean', 'value compares to 0.6/600Gt per year on the sea surface', 'double', 0.0 ),
            ( 'co2_land', 'value compares to 0.2/600Gt per year on land', 'double', 3.0 ),
        ],

        'hydrosphere': [
            ( 'input_path', 'directory where Atmosphere output can be read (must end in /)', 'string', 'output' ),
            ( 'velocity_iter_max', '', 'int', 2 ),
            ( 'pressure_iter_max', '', 'int', 2 ),
            ( 'velocity_iter_max_2D', '', 'int', 2 ),
            ( 'pressure_iter_max_2D', '', 'int', 2 ),

            ( 'coriolis', 'computation with Coriolis force', 'double', 1.0 ),
            ( 'centrifugal', 'computation with centrifugal force', 'double', 1.0 ),
            ( 'buoyancy', 'computation with buoyancy', 'double', 1.0 ),

            ( 'L_hyd', 'extension of the hydrosphere shell in m, assumption of maximum depth of sea 6000 m compares to 40 steps times 150 m', 'double', 6000.0 ),

            ( 'dt', 'time step coincides with the CFL condition', 'double', 0.0001 ),

            ( 'dr', 'compares to 150m depth', 'double', 0.0005 ),

            ( 're', 'Reynolds numberc_0', 'double', 1000.0 ),
            ( 'ec', 'Eckert number', 'double', 0.0001 ),
            ( 'sc', 'Schmidt number for salt water', 'double', 10.0 ),
            ( 'pr', 'Prandtl number for water', 'double', 6.957 ),
            ( 'g', 'gravitational acceleration of the earth', 'double', 9.8066 ),
            ( 'cp_w', 'specific heat capacity of water at constant pressure and 20°C in J/( kg K )', 'double', 4182.0 ),
            ( 'omega', 'rotation number of the earth', 'double', 7.29e-5 ),

            ( 'p_0', 'pressure at sea level in hPa', 'double', 1013.25 ),
            ( 't_0', 'temperature in K compares to 0°C', 'double', 273.15 ),
            ( 'c_0', 'rate of salt in psu at temperature t_0', 'double', 34.6 ),
            ( 'u_0', 'maximum value of velocity in m/s', 'double', 0.45 ),
            ( 'r_0_water', 'reference density of salt water in kg/m3', 'double', 1026.0 ),

            ( 'epsres', 'accuracy for relative and absolute errors0,988571429', 'double', 0.0005 ),

            ( 'ua', 'initial velocity component in r-direction', 'double', 0.0 ),
            ( 'va', 'initial velocity component in theta-direction', 'double', 0.0 ),
            ( 'wa', 'initial velocity component in phi-direction', 'double', 0.0 ),
            ( 'pa', 'initial value for the pressure field', 'double', 0.0 ),
            ( 'ta', 'compares to 4°C', 'double', 1.01464 ),
            ( 'ca', 'c = 1.01156 compares to a salinity of 35.0 psu, mean value, ca corresponds to ta = 1.01464  ( = 4°C )', 'double', 1.01156 ),

            ( 'ca_max', 'c = 1.0983 compares to a salinity of 38.00 psu  used for deep flow initialization', 'double', 1.0983 ),

            ( 't_cretaceous_max', 'maximum add of mean temperature during cretaceous', 'double', 10.0 ),

            ( 'r0', 'Earth\'s radius is r_earth = 6731 km compares to 6.731 [ / ]', 'double', 1.0 ),
            ( 'the0', 'North Pole', 'double', 0.0 ),
            ( 'phi0', 'zero meridian in Greenwich', 'double', 0.0 ),

            ( 't_average', 'mean temperature of the modern earth', 'double', 15.0 ),
            ( 't_equator', 'temperature t_0 = 1.1355 compares to 37° C compares to 310 K', 'double', 1.1355 ),
            ( 't_pole', 'compares to 4°C, threshhold temperature for the Boussinesq-approximation concerning bouyancy effect', 'double', 1.0146 ),
        ]
    }

    XML_READ_FUNCS = {
        "string": "FillStringWithElement",
        "double": "FillDoubleWithElement",
        "int": "FillIntWithElement",
        "bool": "FillBoolWithElement"
    }



    def write_cpp_defaults ( filename, classname, sections ):
        with open ( filename, 'w' ) as f:
            f.write ( "// header files\n" )
            f.write ( "// THIS FILE IS AUTOMATICALLY GENERATED BY param.py\n" )
            f.write ( "// ANY CHANGES WILL BE OVERWRITTEN AT COMPILE TIME\n" )
            f.write ( "\n" )
            f.write ( "void %s::SetDefaultConfig() {\n" % classname )

            for section in sections:
                f.write ( '\n  // %s section\n' % section )

                for slug, desc, ctype, default in PARAMS[section]:
                    rhs = default
                    if ctype == 'string':
                        rhs = '"%s"' % default
                    elif ctype == 'bool':
                        if default:
                            rhs = 'true'
                        else:
                            rhs = 'false'

                    f.write ( '  %s = %s;\n' % ( slug, rhs ) )

            f.write ( "}" )




    def write_cpp_load_config ( filename, classname, sections ):
        with open ( filename, 'w' ) as f:
            f.write ( "// config files\n" )
            f.write ( "// THIS FILE IS AUTOMATICALLY GENERATED BY param.py\n" )
            f.write ( "// ANY CHANGES WILL BE OVERWRITTEN AT COMPILE TIME\n" )
            f.write ( "\n" )

            for section in sections:
                f.write ( '\n  // %s section\n' % section )
                element_var_name = 'elem_%s' % section
                f.write ( '\n  if (%s ) {\n' % ( element_var_name ) )

                for slug, desc, ctype, default in PARAMS [ section ]:
                    func_name = XML_READ_FUNCS [ ctype ]
                    f.write ( '    Config::%s(%s, "%s", %s );\n' % ( func_name, element_var_name, slug, slug ) )
                f.write ( "  }\n" )




    def write_cpp_headers ( filename, sections ):
        with open ( filename, 'w' ) as f:
            f.write ( "// header files\n" )
            f.write ( "// THIS FILE IS AUTOMATICALLY GENERATED BY param.py\n" )
            f.write ( "// ANY CHANGES WILL BE OVERWRITTEN AT COMPILE TIME\n" )
            f.write ( "\n" )

            for section in sections:
                f.write ( '\n// %s section\n' % section )

                for slug, desc, ctype, default in PARAMS [ section ]:
                    f.write('%s %s;\n' % ( ctype, slug ) )




    def write_pxi ( input_filename, output_filename, substitutions ):
        data = open ( input_filename, 'rb' ).read()

        indent = '    '

        for key, classname, sections in substitutions:
            rep = ''
            for section in sections:
                rep += '%s# %s section\n' % ( indent, section )

                for slug, desc, ctype, default in PARAMS[section]:
                    rep += '%sproperty %s:\n' % ( indent, slug )
                    rep += '%s    def __get__(%s self ):\n' % ( indent, classname )
                    rep += '%s        self._check_alive()\n' % indent
                    rep += '%s        return self._thisptr.%s\n' % ( indent, slug )
                    rep += '%s\n' % indent
                    rep += '%s    def __set__(%s self, value ):\n' % ( indent, classname )
                    rep += '%s        self._check_alive()\n' % indent
                    rep += '%s        self._thisptr.%s = <%s> value\n' % ( indent, slug, ctype )
                    rep += '%s\n' % indent

            data = data.replace ( '{{ %s }}' % key, rep )

        with open ( output_filename, 'w' ) as f:
            f.write ( """# pxi files\n""" )
            f.write ( data )




    def write_pxd ( filename, model, sections ):
        with open ( filename, 'w' ) as f:
            # Sadly, Cython docs are incorrect on usage of 'include', so we must include a whole lot of boilerplate
            f.write ( """# pxd files\n""" )
            f.write ( """# THIS FILE IS AUTOMATICALLY GENERATED BY param.py
# ANY CHANGES WILL BE OVERWRITTEN AT COMPILE TIME
cdef extern from "c%sModel.h":
    cppclass c%sModel:
        c%sModel() except +  # NB! std::bad_alloc will be converted to MemoryError
        void LoadConfig ( const char *filename )
        void Run()
        void RunTimeSlice ( int time_slice )
""" % ( model, model, model ) )

            for section in sections:
                f.write ( '        # %s section\n' % section )

                for slug, desc, ctype, default in PARAMS [ section ]:
                    f.write ( '        %s %s\n' % ( ctype, slug ) )




    def write_config_xml ( filename, sections ):
        with open ( filename, 'w' ) as f:
            f.write ( """<!-- THIS FILE IS GENERATED AUTOMATICALLY BY param.py. DO NOT EDIT. -->""" )

            f.write ( '<atom>' )

            for section in sections:
                f.write ( '    <%s>\n' % section )

                for slug, desc, ctype, default in PARAMS [ section ]:
                    if ctype == 'bool':
                        default = str ( default ).lower()  # Python uses True/False, C++, uses true/false

                    f.write ( '        <%s>%s</%s>  <!-- %s (%s ) -->\n' % ( slug, default, slug, desc, ctype ) )

                f.write ( '    </%s>\n' % section )
            f.write ( '</atom>' )



    atmosphere_sections = [ 'common', 'atmosphere' ]
    hydrosphere_sections = [ 'common', 'hydrosphere' ]


    for filename, classname, sections in [
        ( 'atmosphere/cAtmosphereDefaults.cpp.inc', 'cAtmosphereModel', atmosphere_sections ),
        ( 'hydrosphere/cHydrosphereDefaults.cpp.inc', 'cHydrosphereModel', hydrosphere_sections )
    ]:
        write_cpp_defaults ( filename, classname, sections )



    for filename, classname, sections in [
        ( 'atmosphere/AtmosphereLoadConfig.cpp.inc', 'cAtmosphereModel', atmosphere_sections ),
        ( 'hydrosphere/HydrosphereLoadConfig.cpp.inc', 'cHydrosphereModel', hydrosphere_sections )
    ]:
        write_cpp_load_config ( filename, classname, sections )



    for filename, sections in [
        ( 'atmosphere/AtmosphereParams.h.inc', atmosphere_sections ),
        ( 'hydrosphere/HydrosphereParams.h.inc', hydrosphere_sections )
    ]:
        write_cpp_headers ( filename, sections )



    write_pxi ('python/pyatom.pyx.template', 'python/pyatom.pyx', [
        ( 'atmosphere_params', 'Atmosphere', atmosphere_sections ),
        ( 'hydrosphere_params', 'Hydrosphere', hydrosphere_sections ) ]
    )



    for filename, model, sections in [
        ( 'python/atmosphere_pxd.pxi', 'Atmosphere', atmosphere_sections ),
        ( 'python/hydrosphere_pxd.pxi', 'Hydrosphere', hydrosphere_sections )
    ]:
        write_pxd ( filename, model, sections )


    for  filename, sections in [
        ( 'python/config_atm.xml', atmosphere_sections ),
        ( 'python/config_hyd.xml', hydrosphere_sections )
    ]:
        write_config_xml ( filename, sections )


    for  filename, sections in [
        ( 'examples/config_atm.xml', atmosphere_sections ),
        ( 'examples/config_hyd.xml', hydrosphere_sections )
    ]:
        write_config_xml ( filename, sections )


    for  filename, sections in [
        ( 'benchmark/config_atm.xml', atmosphere_sections ),
        ( 'benchmark/config_hyd.xml', hydrosphere_sections )
    ]:
        write_config_xml ( filename, sections )




if __name__ == '__main__':
    main()
