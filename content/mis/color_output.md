Title: How to Color Your C++ Output
Date: 2015-11-20 10:15
Slug: how-to-color-cpp-output
Status: draft
Authors: Liwen Wen

How to color your cpp output on your console is depending on the Operating System you are using. Below is the example on Ubuntu/Linux/OS X.

Example:

    :::cpp
    #define RESET   "\033[0m"
    #define BLACK   "\033[30m"      /* Black */
    #define RED     "\033[31m"      /* Red */
    #define GREEN   "\033[32m"      /* Green */
    #define YELLOW  "\033[33m"      /* Yellow */
    #define BLUE    "\033[34m"      /* Blue */
    #define MAGENTA "\033[35m"      /* Magenta */
    #define CYAN    "\033[36m"      /* Cyan */
    #define WHITE   "\033[37m"      /* White */
    #define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
    #define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
    #define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
    #define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
    #define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
    #define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
    #define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
    #define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */ 
    #include ...

    ClassImp(StPhiDownMaker)
    StPhiDownMaker::StPhiDownMaker(std::string par_type):mParticleType(par_type), pdgmass_phi(1.01945), mKCentBin(9), mKPtBin(11){
    std::cout << CYAN << ">>> StPhiDownMaker Constructor v0.01 2015-09-09 " << RESET << std::endl;
    ...
    }
