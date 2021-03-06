// header files
// THIS FILE IS AUTOMATICALLY GENERATED BY param.py
// ANY CHANGES WILL BE OVERWRITTEN AT COMPILE TIME

void cHydrosphereModel::SetDefaultConfig() {

  // common section
  bathymetry_path = "../data/topo_grids";
  BathymetrySuffix = "Ma_smooth.xyz";
  verbose = false;
  output_path = "output/";
  paraview_panorama_vts_flag = true;
  debug = false;
  velocity_w_file = "../data/w_surface.txt";
  velocity_v_file = "../data/v_surface.txt";
  temperature_file = "../data/SurfaceTemperature_NASA.xyz";
  precipitation_file = "../data/SurfacePrecipitation_NASA.xyz";
  salinity_file = "../data/SurfaceSalinity_NASA.xyz";
  temperature_curve_file = "../data/Lenton_etal_COPSE_time_temp.txt";
  pole_temperature_file = "../data/pole_temperature.txt";
  reconstruction_script_path = "../reconstruction/reconstruct_atom_data.py";
  use_earthbyte_reconstruction = false;
  use_NASA_velocity = false;
  sun = 0;
  NASATemperature = 0;
  t_paleo_max = 10.0;
  t_paleo = 0.0;
  time_start = 0;
  time_end = 0;
  time_step = 10;
  omega = 7.292e-05;

  // hydrosphere section
  input_path = "output";
  velocity_iter_max_2D = 2;
  pressure_iter_max_2D = 10;
  velocity_iter_max = 2;
  pressure_iter_max = 2;
  checkpoint = 2;
  buoyancy = 1.0;
  L_hyd = 200.0;
  re = 10.0;
  sc = 1.7329;
  pr = 6.957;
  g = 9.8066;
  cp_w = 4182.0;
  p_0 = 1013.25;
  t_0 = 273.15;
  c_0 = 34.6;
  u_0 = 0.24;
  r_0_water = 997.0;
  r_air = 1.2041;
  t_land = 0.0;
  t_average = 15.4;
  t_equator = 1.1025;
  t_pole = 0.993;
}