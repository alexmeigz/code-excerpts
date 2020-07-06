#include "queue.h"
#include <iostream>

template <class Item>
Queue<Item>::Queue(){
}

template <class Item>
Queue<Item>::~Queue(){
}

template <class Item>
void Queue<Item>::enqueue(Item data){
    contents.push_back(data);
}

template <class Item>
Item Queue<Item>::dequeue(){
    if(contents.size()){
        Item temp = contents[0];
        contents.erase(contents.begin());
        return temp;
    }
    return NULL;
}
        
template <class Item>
int Queue<Item>::size() const{
    return contents.size();
}

template <class Item>
void Queue<Item>::printQueue() const{
    std::cout << "----- PRINTING QUEUE -----" << std::endl;
    for(auto i = contents.begin(); i < contents.end(); i++){
        std::cout << "Element: " << *i << std::endl;
    }
    std::cout << "----- END OF QUEUE -----" << std::endl;
}