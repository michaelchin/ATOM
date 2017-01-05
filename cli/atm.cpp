#include <iostream>

#include "cAtmosphereModel.h"

int main(int argc, char **argv) {
    cAtmosphereModel model;

    std::cout << "ATOM atmosphere model\n";
    std::cout << "\n";
    std::cout << "Usage:\n";
    std::cout << "\t" << argv[0] << " [XML configuration path]\n";
    std::cout << "If XML path is not specified, default parameters will be used\n";
    std::cout << "\n";

    if (argc == 2) {
        model.LoadConfig(argv[1]);
    }

    model.Run();
}
