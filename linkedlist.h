#ifndef SINGLYLINKEDLIST
#define SINGLYLINKEDLIST
    template <class Item>
    class SinglyLinkedList{
        public:
            SinglyLinkedList();
            ~SinglyLinkedList();

            //adds to front of list
            void addToHead(Item entry);

            //adds to back of list
            void addToTail(Item entry);

            //removes from head of list
            //returns removed datum
            //if list is empty, return NULL
            Item removeFromHead();

            //removes from tail of list
            //returns removed datum
            //if list is empty, return NULL
            Item removeFromTail();

            //prints the list 
            //NOTE: only works for basic data types
            void printList() const;

            //returns list size
            unsigned int getSize() const;

        private:
            struct SNode {
                Item datum;
                SNode* next;
            };

            SNode* head;
            SNode* tail;
            unsigned int size;
    };
#endif

#ifndef DOUBLYLINKEDLIST
#define DOUBLYLINKEDLIST
    template <class Item>
    class DoublyLinkedList{
        public:
            DoublyLinkedList();
            ~DoublyLinkedList();

            //adds to front of list
            void addToHead(Item entry);

            //adds to back of list
            void addToTail(Item entry);

            //removes from head of list
            //returns removed datum
            //if list is empty, return NULL
            Item removeFromHead();

            //removes from tail of list
            //returns removed datum
            //if list is empty, return NULL
            Item removeFromTail();

            //prints the list 
            //NOTE: only works for basic data types
            void printList() const;

            //returns list size
            unsigned int getSize() const;

        private:
            struct DNode{
                Item datum;
                DNode* next;
                DNode* previous;
            };

            DNode* head;
            DNode* tail;
            unsigned int size;
    };
#endif