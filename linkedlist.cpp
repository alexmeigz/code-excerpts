#include "linkedlist.h"
#include <iostream>

// ------------------------------- SINGLY LINKED LIST -------------------------------

template<class Item>
SinglyLinkedList<Item>::SinglyLinkedList(){
    head = NULL;
    tail = NULL;
    size = 0;
}

template <class Item>
SinglyLinkedList<Item>::~SinglyLinkedList(){
    SNode* traverse = head;
    while(traverse){
        SNode* temp = traverse;
        traverse = traverse->next;
        delete temp;
    }
}
            
template <class Item>
void SinglyLinkedList<Item>::addToHead(Item entry){
    ++size;
    head = new SNode{entry, head};
    if(!tail){
        tail = head;
    }   
}

template <class Item>
void SinglyLinkedList<Item>::addToTail(Item entry){
    ++size;
    SNode* previous = tail;
    tail = new SNode{entry, NULL};
    if(previous){
        previous->next = tail;
    } 
    if(!head){
        head = tail;
    }
}
            
template <class Item>
Item SinglyLinkedList<Item>::removeFromHead(){
    if(size){
        SNode* temp = head;
        Item returnval = temp->datum;
        head = head->next;
        delete temp;
        if(tail == temp){
            tail = NULL;
        }
        --size;
        return returnval;
    }
    return NULL;
}

template <class Item>
Item SinglyLinkedList<Item>::removeFromTail(){
    if(size){
        SNode* traverse = head;
        SNode* previous = NULL;
        while(traverse->next){
            previous = traverse;
            traverse = traverse->next;
        }
        Item returnval = tail->datum;
        delete tail;
        if(previous){
            previous->next = NULL;
        } 
        tail = previous;
        if(!tail){
            head = NULL;
        }
        --size;
        return returnval;
    }
    return NULL;
}

template <class Item>
void SinglyLinkedList<Item>::printList() const{
    SNode* traverse = head;
    while(traverse){
        std::cout << "[" << traverse->datum << "] -> ";
        traverse = traverse->next;
    }
    std::cout << "NULL" << std::endl; 
}

template <class Item>
unsigned int SinglyLinkedList<Item>::getSize() const{
    return size;
}

// ------------------------------- DOUBLY LINKED LIST -------------------------------

template<class Item>
DoublyLinkedList<Item>::DoublyLinkedList(){
    head = NULL;
    tail = NULL;
    size = 0;
}

template <class Item>
DoublyLinkedList<Item>::~DoublyLinkedList(){
    DNode* traverse = head;
    while(traverse){
        DNode* temp = traverse;
        traverse = traverse->next;
        delete temp;
    }
}
            
template <class Item>
void DoublyLinkedList<Item>::addToHead(Item entry){
    ++size;
    DNode* temp = head;
    head = new DNode{entry, temp, NULL};
    if(temp){
        temp->previous = head;
    }
    if(!tail){
        tail = head;
    }   
}

template <class Item>
void DoublyLinkedList<Item>::addToTail(Item entry){
    ++size;
    DNode* temp = tail;
    tail = new DNode{entry, NULL, temp};
    if(temp){
        temp->next = tail;
    }  
    if(!head){
        head = tail;
    }
}
            
template <class Item>
Item DoublyLinkedList<Item>::removeFromHead(){
    if(size){
        DNode* temp = head;
        Item returnval = temp->datum;
        head = head->next;
        if(head){
            head->previous = NULL;
        }
        delete temp;
        if(tail == temp){
            tail = NULL;
        }
        --size;
        return returnval;
    }
    return NULL;
}

template <class Item>
Item DoublyLinkedList<Item>::removeFromTail(){
    if(size){
        DNode* temp = tail;
        Item returnval = temp->datum;
        tail = tail->previous;
        if(tail){
            tail->next = NULL;
        }
        delete temp;
        if(head == temp){
            head = NULL;
        }
        --size;
        return returnval;
    }
    return NULL;
}

template <class Item>
void DoublyLinkedList<Item>::printList() const{
    DNode* traverse = head;
    while(traverse){
        std::cout << "[" << traverse->datum << "] -> ";
        traverse = traverse->next;
    }
    std::cout << "NULL" << std::endl; 
}

template <class Item>
unsigned int DoublyLinkedList<Item>::getSize() const{
    return size;
}