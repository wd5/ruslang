/* 
 * File:   main.cpp
 * Author: Victor
 *
 * Created on January 31, 2012, 10:24 PM
 */

#include <cstdlib>
#include <boost/program_options.hpp>

using namespace std;
namespace po = boost::program_options;

/*
 * 
 */
int main(int argc, char** argv) 
{
    po::options_description desc("Allowed options") ;
    desc.add_options()
            ("help", "produce help message")
            ("inputfile,i", po::value<string>()->default_value("empty.txt"), "set input file")
            ("outputfile,o", po::value<string>(), "set output file")
            ("paramfile,p", po::value<string>(), "set parameters file")
            ("ifcodepage","input file codepage")
            ("commandfile",po::value<string>(),"file containing XML formated command to execute and parameters")
    
    
    ;        
           
    po::variables_map vm ;
    po::store(po::parse_command_line(argc,argv,desc),vm) ;
    po::notify(vm) ;
    
    if (vm.count("help")) 
    {
        cout << desc << "\n";
        return 1;
    }
    
    if (vm.count("inputfile")) 
    {
        cout << "Input file:" << vm["inputfile"].as<string>() << endl ;
    }
    
    if (vm.count("commandfile")) 
    {
        cout << "Command file:" << vm["commandfile"].as<string>() << endl ;
    }
    
    
    return 0;
}

