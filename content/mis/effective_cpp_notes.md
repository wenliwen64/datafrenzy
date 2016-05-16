Title: Effective C++ Notes
Date: 2016-03-27 18:16
Slug: effective-cpp-notes
Author: Liwen Wen

# Log
---
1. 2016-03-26: Item21, dont try to return object reference when you have to return an object

2. 2016-03-27: Item13, use objects to manage resources: `std::auto_ptr<Investment>` or `std::tr1::shared_ptr<Investment>` last one is preffered for its normal copy behaviour 

3. 2016-03-28: Item20,  prefere pass-by-reference-to-const to pass-by-value; the former is better over the latter because it is efficient(vector<pointers> copy will copy all of the objects they are pointing to) and avoid slicing problem(only copy base classes); pass-by-value is better for built-in types(even user-defined object is small).

4. 2016-03-29: Item27, minimizing casting, static_cast and dynamic_cast(performance poor, up and down), static_cast can only to down or implicit conversion. prefer c++ style.

5. 2016-03-30: Item2, prefer consts, enums, and inlines to `#define`s. Or prefert compiler to pre-processor. Reasons: 1. Hard to track it down; 2. in-class definition is not allowed except the integer/char/bool types. Instead you can do like `const double CostEstimate::FudgeFactor = 1.35`; 3. define an enum in class is also okay as the size of an array. 4. Prefer `inline` to `#define` thing.

6. 2016-03-31: Item20, issues you need to consider in type/class design.

7. 2016-04-01: Item7, declare destructor virtual in polymorphic base classes: Always make base class destructor virtual. STL classes(string, vector things) have no virtual destructor though, so never derive from them. Also, you always can implement pure virtual function in abstract base classes in spite of you still have to implement them in derived classes but sometime you may use the abstract class' implementation. 

8. 2016-04-18: Item 15: provide acccess to raw resources in resources managing classes: implicit conversion function using `operator FontHandle() const` to convert `Font` toi `handle` type; Diamond problem which stems from multiple inheritance, we can do like `class transmitter: virtual public device` and `class reciever: virtual public device` to ensure there is only one base class object in `modem` class which is defined as `class modem : public transmitter, public  receiver`, check [this](http://www.cprogramming.com/tutorial/virtual_inheritance.html) for more. `++i` is more efficient thant `i++`; long double > double > float > unsigned long int > long int > unsigned int > int > char

9.
