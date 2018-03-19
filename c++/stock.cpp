#include "stock.h"
#include "utils.h"

using namespace std;
Stocks::Stocks() {
    currentItems.reserve(10);
    transactions.reserve(10);
    string header = "Transaction type | item | count | time";
    transactions.push_back(header);
}
void Stocks::add_item(item *item1) {
    date timer = std::time(nullptr);
    item1->time_added = timer;
    currentItems.push_back(*item1);
    string log = "Add   |  " + item1->name + "  |  "
                 + to_string(item1->item_count) + "  |  "  + to_string(item1->time_added);
    transactions.push_back(log);
}

void Stocks::print_items() {
    cout<<"Name   |   Time   |   Item count   |   Stock code\n";
    for (auto & element : currentItems) {
        cout<< element.name << " | "
            << element.time_added << " | "
            << element.item_count << " | "
            << element.stock_code << endl;
    }
}

void Stocks::delete_item(const string &name) {
    int i = 0;
    bool exists = false;
    for(auto & element: currentItems) {
        if (element.name == name) {
            exists = true;
            currentItems.erase(currentItems.begin() + i);
            time_t current_time = time(nullptr);
            string log ="Delete |  " + element.name + " |           | " + to_string(current_time);
            transactions.push_back(log);
            break;
        }
        i += 1;
    }
    if(!exists) cout<<"Item doesn't exist in stock";
}

void Stocks::receive_item(const string &name, number &addition) {
    bool exists = false;
    for(auto & element: currentItems) {
        if(element.name == name) {
            exists = true;
            element.item_count += addition;
            time_t current_time = time(nullptr);
            string log ="Receive   |  " + element.name +
                    to_string(element.item_count) + "  |  " + to_string(element.item_count)
            + " at " + to_string(current_time);
            transactions.push_back(log);
            break;
        }
    }

    if(!exists) cout<<"Item does not exist in stock";
}

void Stocks::send_item(const string &name, number &subtraction) {
    bool exists = false;
    for(auto & element: currentItems) {
        if(element.name == name) {
            exists = true;
            //TODO: try to figure out why the if statement is like so
            if (element.item_count - subtraction > element.item_count) {
                cout<<"Impossible operation. Trying to send more than you have";
                return;
            }
            element.item_count -= subtraction;
            time_t current_time = time(nullptr);
            string log ="Send   |  "  + element.name + " | " + to_string(element.item_count)
                                   + " | " + to_string(current_time);
            transactions.push_back(log);
            break;
        }
    }
    if(!exists) {
        cout<<"Item does not exist in stock";
    }
}

void Stocks::execute(const string &c) {
    vector<string> tokens = split(c, ' ');
    if(tokens[0] == "add") {
        item new_item = {tokens[1], get_stock_count() + 1, static_cast<number>(stoi(tokens[2]))};
        add_item(&new_item);

    } else if(tokens[0] == "delete") {
        delete_item(tokens[1]);

    } else if(tokens[0] == "print") {
        print_items();

    } else if(tokens[0] == "receive"){
        auto adds = stoi(tokens[2]);
        receive_item(tokens[1], reinterpret_cast<number &>(adds));

    } else if(tokens[0] == "send") {
        auto subs = stoi(tokens[2]);
        send_item(tokens[1], reinterpret_cast<number &>(subs));

    } else if(tokens[0] == "transactions") {
        display_transaction_log();
    }
    else cout<<"Unknown command";
}






