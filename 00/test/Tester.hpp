#ifndef TESTER_HPP
# define TESTER_HPP

#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <cstdlib> // getenv
#include <stdlib.h>
#include <cassert>

bool testerEx00(std::string result);
bool testerEx01(std::string result);
bool testerEx02(std::string result);
bool testerEx03(std::string result);
bool testerEx04(std::string result);
bool testerEx05(std::string result);
bool testerEx06(std::string result);
bool testerEx07(std::string result);
bool testerEx08(std::string result);
bool testerEx09(std::string result);


class Tester {
    public: 
        void run();
        void run(int level);
        ~Tester();
        Tester(int task_len);
        Tester();
    private:
        const int _task_len;
        std::string *_filenames;
        int _successLog[10] = {0, };
        Tester &operator= (const Tester &copy);
        Tester(const Tester &copy);
        bool (*singleTester[10])(std::string result);
        
    };

#endif