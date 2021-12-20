#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <fstream>
#include "simulator.h"

namespace BS {

 /*   GenomeFileHandler::GenomeFileHandler() {

    }
*/
    void GenomeFileHandler::loadGenomes(std::string filename ,std::vector<Genome> *genomes) {
        
    }

    void GenomeFileHandler::saveGenomes(unsigned int generation,std::vector<Genome> *genomes) {
        std::stringstream filename;
        filename << p.imageDir.c_str() << "/gen-"
                      << std::setfill('0') << std::setw(6) << generation
                      << ".biosim";

        m_savefile.open (filename.str().c_str(),std::ios::out);
        //m_savefile << "Writing this to a file.\n";
        std::size_t total = genomes->size();
        for (std::size_t i = 0; i < total; i++) {
            writeGenome(genomes->at(i));
            m_savefile << std::endl;
        }
        m_savefile.close();
    }

    void GenomeFileHandler::writeGenome(Genome &genome) {
        for (Gene gene : genome) {
            uint32_t n;
            std::memcpy(&n, &gene, sizeof(n));
            m_savefile << std::hex << std::setfill('0') << std::setw(8) << n;
        }
    }
}