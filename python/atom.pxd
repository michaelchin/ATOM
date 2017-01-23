from libcpp.string cimport string

cdef extern from "cAtmosphereModel.h":
    cppclass cAtmosphereModel:
        cAtmosphereModel() except +  # NB! std::bad_alloc will be converted to MemoryError
        void LoadConfig(const char *filename)
        void Run()
        void RunTimeSlice(int time_slice)

        string output_path

        double coriolis


cdef extern from "cHydrosphereModel.h":
    cppclass cHydrosphereModel:
        cHydrosphereModel() except +  # NB! std::bad_alloc will be converted to MemoryError
        void LoadConfig(const char *filename)
        void Run()
        void RunTimeSlice(int time_slice)

        string output_path
        string input_path
        string bathymetry_path

        double coriolis
