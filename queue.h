#ifndef QUEUE
#define QUEUE
    #include <vector>

    template <class Item>
    class Queue{
        public:
            Queue();
            ~Queue();

            //adds to end of queue
            void enqueue(Item data);

            //removes front of queue
            //returns removed datum
            //if queue is empty, return NULL
            Item dequeue();

            //returns queue size
            int size() const;

            //prints the queue 
            //NOTE: only works for basic data types
            void printQueue() const;

        private:
            std::vector<Item> contents;
    };
#endif