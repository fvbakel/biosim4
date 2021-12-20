#pragma once

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include "simulator.h"

namespace BS {

    constexpr std::uint8_t HexCharToInt(char Input)
    {
        return
        ((Input >= 'a') && (Input <= 'f'))
        ? (Input - 87)
        : ((Input >= 'A') && (Input <= 'F'))
        ? (Input - 55)
        : ((Input >= '0') && (Input <= '9'))
        ? (Input - 48)
        : throw std::exception{};
    }

    class GenomeFileHandler {
    
    private:
        std::ofstream   m_savefile;

        void writeGenome(Genome &genome);
        uint32_t parseGeneString(const std::string &geneString);

    public:
    //    GenomeFileHandler();
        void loadGenomes(std::string filename ,std::vector<Genome> *genomes);
        void saveGenomes(unsigned int generation,std::vector<Genome> *genomes);
    };


}