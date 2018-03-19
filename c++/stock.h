//
// Created by Gfred on 3/18/2018.
//
#ifndef STOCK_MANAGEMENT_STOCK_H
#define STOCK_MANAGEMENT_STOCK_H
#include <iostream>
#include <vector>
#include<ctime>
using namespace std;
typedef unsigned int number;
typedef std::time_t date;

struct item {
    string name;
    number stock_code;
    number item_count;
    date time_added;
};

class Stocks {
public:
    Stocks();
    number get_stock_count() { return currentItems.size(); }
    void add_item(item *item);
    void delete_item(const string &code);
    void receive_item(const string &name, number &addition);
    void send_item(const string &name, number &subtraction);
    void print_items();
    void display_transaction_log() { for(auto & element: transactions) { cout<<element << endl; } }
    void execute(const string &c);

private:
    vector<item> currentItems;
    vector<string> transactions;
};
#endif //STOCK_MANAGEMENT_STOCK_H
