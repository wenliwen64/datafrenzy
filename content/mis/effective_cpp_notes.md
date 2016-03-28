Title: Effective C++ Notes
Date: 2016-03-27 18:16
Slug: effective-cpp-notes
Author: Liwen Wen

# Log
---
1. 2016-03-26: Item21, dont try to return object reference when you have to return an object

2. 2016-03-27: Item13, use objects to manage resources: `std::auto_ptr<Investment>` or `std::tr1::shared_ptr<Investment>` last one is preffered for its normal copy behaviour 

3. 2016-03-28: Item20,  prefere pass-by-reference-to-const to pass-by-value; the former is better over the latter because it is efficient(vector<pointers> copy will copy all of the objects they are pointing to) and avoid slicing problem(only copy base classes); pass-by-value is better for built-in types(even user-defined object is small).
