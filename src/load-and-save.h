#pragma once

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include "simulator.h"

namespace BS {

    class GenomeFileHandler {
    
    private:
        std::ofstream   m_savefile;

        void writeGenome(Genome &genome);

    public:
    //    GenomeFileHandler();
        void loadGenomes(std::string filename ,std::vector<Genome> *genomes);
        void saveGenomes(unsigned int generation,std::vector<Genome> *genomes);
    };


}