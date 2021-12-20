#include <vector>
#include <string>
#include <sstream>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <fstream>
#include "simulator.h"

namespace BS {

 /*   GenomeFileHandler::GenomeFileHandler() {

    }
*/
    uint32_t GenomeFileHandler::parseGeneString(const std::string &geneString) {
        if (geneString.size() == 8 ) {
            return (
                (HexCharToInt(geneString.at(0)) << 28 ) | 
                (HexCharToInt(geneString.at(1)) << 24 ) | 
                (HexCharToInt(geneString.at(2)) << 20 ) | 
                (HexCharToInt(geneString.at(3)) << 16 ) | 
                (HexCharToInt(geneString.at(4)) << 12 ) | 
                (HexCharToInt(geneString.at(5)) <<  8 ) | 
                (HexCharToInt(geneString.at(6)) <<  4 ) | 
                 HexCharToInt(geneString.at(7))
            );
        } else {
            return ((uint32_t) 0);
        }
    }

    void GenomeFileHandler::loadGenomes(std::string filename ,std::vector<Genome> *genomes) {
        genomes->clear();
        std::ifstream infile(filename);
        std::string line;
        while (std::getline(infile, line))
        {
            Genome genome;
            std::istringstream iss(line);
            uint32_t n;
            Gene gene;
            for (std::string::size_type i = 0;i<line.size();i=i+8) {
                std::string geneStr = line.substr(i,8);
                 n = parseGeneString(geneStr);
                std::memcpy(&gene, &n, sizeof(gene));
                genome.push_back(gene);
            }
            if (genome.size() > 0) {
                genomes->push_back(genome);
            }
        }
        infile.close();
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