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

13. `Map::insert()` takes O(N) time as well as `Map::erase()`, this is where I made a mistake in homework4.

14. To count a string's length, use `std::string::size()` which measure how many characters in the string(no `'\0'` included); `strlen(const char*)` counts number of chars until null terminator.

15. `int main(int argc, char** argv)` is equal to `int main(int argc, char* argv[])`, so `argv[1]` will take out the second string passed to the main function.

16. How to write `sprintf`-like code in c++?

        :::c++
        std::ifstream ifile("blah.txt");
        std::string line;
        while(!getline(ifile, line)){
            std::istringstream is(line);
            if(!(is >> string1 >> string2 >> string3))
                std::cout << "bad formatted line" << std::endl;
            int int_dec = std::stoi(string1.c_str(), nullptr, 10); 
            //int int_hex = std::stoi(string1.c_str(), nullptr, 16); 
            //int int_bin = std::stoi(string1.c_str(), nullptr, 2); 

            double do = std::atof(string2.c_str());
            float  fl = std::stof(string3.c_str());
        }

17. A complete example:

        :::c++
        #include <fstream>
        #include <sstream>
        #include <iostream>
        #include <string>
        #include <cassert>
        #include <iomanip>
        int main(){
            std::ifstream ifile("fio_file_input.txt");
            if(!ifile)
                std::cout <<  "so Bad!" << std::endl;
            std::string line;
            int int_dec;
            double dou, fl;
            while(getline(ifile, line)){
                std::cout << line << " happy!" << std::endl;
                std::istringstream is(line);
                std::string string1, string2, string3;

                if(!(is >> string1 >> string2 >> string3))
                    std::cout << "bad formatted line" << std::endl;
                int int_dec = std::stoi(string1.c_str(), nullptr, 10);
                //int int_hex = std::stoi(string1.c_str(), nullptr, 16);
                //int int_bin = std::stoi(string1.c_str(), nullptr, 2);

                dou = std::stod(string2.c_str());
                fl = std::stod(string3.c_str());

                std::cout << int_dec << " " << std::setprecision(13) << dou << " " << std::setprecision(13) << fl << std::endl;
            }
            //assert((dou+fl) == (323224.3 + 4343.43545465)); 
        }  
