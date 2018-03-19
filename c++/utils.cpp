//
// Created by Gfred on 3/18/2018.
//
#include "utils.h"

template<typename Out>
void split(const string &s, char delimiter, Out result) {
    stringstream ss(s);
    string item;
    while (std::getline(ss, item, delimiter)) {
        *(result++) = item;
    }
}

vector<string> split(const std::string &s, char delimiter) {
    vector<string> elements;
    split(s, delimiter, std::back_inserter(elements));
    return elements;
}


