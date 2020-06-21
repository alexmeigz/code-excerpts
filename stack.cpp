#include "stack.h"
#include <iostream>

template <class Item>
Stack<Item>::Stack(){
}

template <class Item>
Stack<Item>::~Stack(){
}

template <class Item>
void Stack<Item>::push(Item data){
    contents.push_back(data);
}

template <class Item>
Item Stack<Item>::pop(){
    if(contents.size()){
        Item temp = contents[contents.size() - 1];
        contents.erase(contents.begin() + contents.size() - 1);
        return temp;
    }
    return NULL;
}
        
template <class Item>
int Stack<Item>::size() const{
    return contents.size();
}

template <class Item>
void Stack<Item>::printStack() const{
    std::cout << "----- PRINTING STACK -----" << std::endl;
    for(auto i = contents.begin(); i < contents.end(); i++){
        std::cout << "Element: " << *i << std::endl;
    }
    std::cout << "----- END OF STACK -----" << std::endl;
}