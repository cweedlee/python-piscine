#include <ctime>
#include <string>
#include <iostream>

bool testerEx00(std::string result) {
    std::string answer = "['Hello', 'World!']\n('Hello', 'France!')\n{'Hello', 'Paris!'}\n{'Hello': '42Paris!'}\n";
    std::cout << answer << std::endl;
    return answer.compare(result) == 0;
}

bool testerEx01(std::string result) {
    clock_t nowtime =  clock();
    std::string answer = "Seconds since January 1, 1970: ";
    std::cout << answer << nowtime << std::endl;
    if (std::strncmp(result.c_str(), answer.c_str(), answer.length())) {
        return false;
    }
    return true;
}

bool testerEx02(std::string result){return false;};
bool testerEx03(std::string result){return false;};
bool testerEx04(std::string result){return false;};
bool testerEx05(std::string result){return false;};
bool testerEx06(std::string result){return false;};
bool testerEx07(std::string result){return false;};
bool testerEx08(std::string result){return false;};
bool testerEx09(std::string result){return false;};