#ifndef STACK
#define STACK
    #include <vector>

    template <class Item>
    class Stack{
        public:
            Stack();
            ~Stack();

            //adds to top of stack
            void push(Item data);

            //removes top of stack
            //returns removed datum
            //if stack is empty, return NULL
            Item pop();

            //returns stack size
            int size() const;

            //prints the list 
            //NOTE: only works for basic data types
            void printStack() const;

        private:
            std::vector<Item> contents;
    };
#endif