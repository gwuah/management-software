#include "stock.h"
using namespace std;

Stocks stocks;
int main() {
    cout<<"Stock management system v1.0.0\n";
    cout<<"add [name] [i] - adds i number of name to stock\n"
        <<"delete [name] - deletes name from stock\n"
        <<"print - prints current stock items\n"
        <<"receive [name] [i] - adds i number of items to existing stock\n"
        <<"send [name] [i] - sends i number of items out of stock\n"
        <<"transactions - displays a list of all transactions\n"
        <<"q - exits the program\n\n";

    string c;
    while (true) {
        if(getline(cin, c)) {
            if (c == "q") break;
            stocks.execute(c);
        }
    }
    // you can do file storage stuff here:
    return 0;
}




