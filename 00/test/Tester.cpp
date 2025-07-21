#include "Tester.hpp"
bool fileExists(const std::string& filename) {
    std::ifstream   file(filename);
    return file.good(); // Checks if the stream is in a good state (e.g., file opened successfully)
}


Tester::Tester(): _task_len(9) {
    
}

std::string getResultFromCommand (std::string cmd) {
    std::string result;
    FILE* stream;
    const int maxBuffer = 256; 
    char buffer[maxBuffer];
    cmd.append(" 2>&1");
    
    stream = popen(cmd.c_str(), "r"); //커맨드 실행, 파이프 연결, fd 반환
    if (stream) {
        while (fgets(buffer, maxBuffer, stream) != NULL) result.append(buffer);
        pclose(stream);
    }
    return result;
}

bool checkFileType(std::string &filename, std::string &type) {
    std::string temp = filename;
    try {
        size_t end = temp.length();
        size_t start = temp.find('.');
        while (start != std::string::npos && start != 0){
            temp = temp.substr(start+1, end - start);
            start = temp.find('.');
        }
    } catch (std::exception &e){
        return false;
    }
    // DEBUG
    // std::cout <<"CHECKING:: "<< filename <<" " << type  << " "<<(filename == type)<< std::endl;
    return (std::strncmp(temp.c_str(), type.c_str(), type.length()) == 0);
}



Tester::Tester(int task_len): _task_len(task_len) {
    std::string filetype = "py";
    _filenames = new std::string[task_len];

    // file check, if every file is ok
    std::cout << " ### CHECKING FOLDERS ... ###"<< std::endl;
    try {
        std::string foldername, filename;
        for (int i = 0; i < _task_len; i++){
            foldername = "ex0" + std::to_string(i);
            filename = getResultFromCommand(("ls ../"+ foldername));
            
            std::cout << foldername + "/" + filename << "exist" << std::endl;
            assert(checkFileType(filename,filetype) == true);
            
            _filenames[i] = (foldername + "/" + filename);
        }
    } catch (std::exception e) {
        std::cerr << "FILE NOT VALID" <<std::endl;
        std::cerr << "ERROR :: " << e.what() << std::endl;
    }

    // allocating single tester into class
    singleTester[0] = testerEx00;
    singleTester[1] = testerEx01;
    singleTester[2] = testerEx02;
    singleTester[3] = testerEx03;
    singleTester[4] = testerEx04;
    singleTester[5] = testerEx05;
    singleTester[6] = testerEx06;
    singleTester[7] = testerEx07;
    singleTester[8] = testerEx08;
    singleTester[9] = testerEx09;
}

Tester::~Tester(){};

void Tester::run(){
    for (int code = 0; code < _task_len ; code++) {
        std::string result, answer;
        
        result = getResultFromCommand(("python3 ../" + _filenames[code]));
        std::cout << "***************************************" <<std::endl;
        std::cout << "RESULT " << (code) << "\n" << result  << "\n" << std::endl;
        
        std::cout << "ANSWER " << (code) << "\n";
        _successLog[code] = singleTester[code](result);
        std::cout << std::endl;
        std::cout << "STATUS"<< code <<" :: " << (_successLog[code] ? "\033[32mSUCCESS" : "\033[31mFAIL") << "\033[0m\n\n" << std::endl;
    }
    
}