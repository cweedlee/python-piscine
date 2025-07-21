#include "Tester.hpp"

int main (int ac, char ** av) {
    int task_len;
    if (ac < 2) {
        task_len = 9;
    } else {
        task_len = atoi(av[1]);
        
    }

    Tester *T = new Tester(task_len);
    T->run();

    delete T;
    return 0;
}