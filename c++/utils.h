//
// Created by Gfred on 3/18/2018.
//

#ifndef STOCK_MANAGEMENT_UTILS_H
#define STOCK_MANAGEMENT_UTILS_H

#include <string>
#include <sstream>
#include <vector>
#include <iterator>
#include "stock.h"

using namespace std;
template<typename Out>
void split(const string &s, char delimiter, Out result);

vector<string> split(const string &s, char delimiter);

#endif //STOCK_MANAGEMENT_UTILS_H
