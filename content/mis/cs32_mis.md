Title: CS32 Miscellaneous Information
Date: 2016-01-21 23:41
Slug: cs32-miscellaneous-information
Authors: Liwen Wen

[TOC]
# Seasnet Windows Desktop
## On windows:
  
   0. Connect to ucla vpn

   1. Click the Remote Desktop Connection application which is coming with Win8+

   2. Type `remote.seas.ucla.edu`

   3. Enter `seaslab\classlwe` and passcode 

   4. To scp the files, using WinSCP

   5. Host name is `lnxsrv07.seas.ucla.edu` and account `classlwe` and passcode

   6. Drag the file you want to drag

# Tips:

1. Include guard
 
    We need like:

        :::c++
        #ifndef MAP_INCLUDED
        #define MAP_INCLUDED
        #endif

    to prevent double declaration from happening, this is the first thing coming to my mind why asked why we needed it.

2. cyclic declaration

    The typical scenario is like: class has student data member, but student also has class enrolled data member, so you have to declare one first. 

        :::c++
        #include "Foo.h"
        class Foo;

        //You have to #include the header file defining a class when
        //* you declare a data member of that class type
        //* you declare a container (e.g. a vector) of objects of that class type
        //* you create an object of that class type
        //* you use a member of that class type

        class Blah
        {
            //...
            void g(Foo f, Foo& fr, Foo* fp);  // just need to say   class Foo;
            //...
            Foo* m_fp;           // just need to say   class Foo;
            Foo* m_fpa[10];      // just need to say   class Foo;
            vector<Foo*> m_fpv;  // just need to say   class Foo;

            Foo m_f;             // must #include Foo.h
            Foo m_fa[10];        // must #include Foo.h
            vector<Foo> m_fv;    // must #include Foo.h
        };

        void Blah::g(Foo f, Foo& fr, Foo* fp)
        {
            Foo f2(10, 20);      // must #include Foo.h
            f.gleep();           // must #include Foo.h
            fr.gleep();          // must #include Foo.h
            fp->gleep();         // must #include Foo.h
        }

3. delete pointer

    usually, delete pointer will free allocated memory, but the pointer is undefined.

        :::c++
        char* c = new char[5];
        delete [] c; // delete array;

4. initialize class pointer

5. copy and swap
   
        :::c++
        String& String::operator=(const String& rhs){
            if(*this != rhs){
                String tmp(rhs);
                swap(tmp);
            }
            return *this;
        }

6. tips to switch typedef(TODO)

7. pass by reference
    
    Sometime, we dont want to cost space to copy some big object into a fucntion, so we just pass the argument by reference.

8. Constructor: if you don't define ctor for a class, compiler will generate one(no parameter) default constructor for you

9. Virtual function will propagate, but better indicate virtual 

10. "string" , 'char' , double quotes are array of constant characters, single quotes are char, neither of them is string type, 

11. `static` has three usages: 1. static in function; 2. static in class(class-wise, not instance-wise) 3. static in file

12. `Map::insert(const KeyType& key, const ValueType& value)` allows you pass a temporary object to this function. For instance: `map.insert(Coord(40, 20), 43);`. But if you want to pass your temporary object to a non-constant reference, you will get compilation error. Since if you want to pass it to a non-reference, you are implicitly stating that you want to modify the object and return it to its caller. This is completely meaningless.
