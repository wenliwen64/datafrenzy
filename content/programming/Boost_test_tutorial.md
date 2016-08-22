Title: Boost Tutorial 
Date: 2016-07-30 14:15
Modified: 2016-07-30 14:15
Category: Programming
Slug: boost-tutorial
Authors: Liwen Wen
Status: draft

[TOC]

## Handy Boost test tools

- BOOST_WARN
- BOOST_CHECK(x != y) (testing continues if test fails)
- BOOST_REQUIRE(x == y) (testing stops if test fails)
- BOOST_CHECK_CLOSE_FRACTION(x, y, tolerance-limit) ( floating point comparison )

## Example:

    :::cpp
    #define BOOST_TEST_MODULE MasterTestSuite
    #include <boost/test/included/unit_test.hpp>
    using boost::unit_test;
    test_suite*
    init_unit_test_suite(int argc, char* argv[]){
        test_suite* ts1 = BOOST_TEST_SUITE("test_suite1");
        ts1->add(BOOST_TEST_CASE(&test_case1));
        ts1->add(BOOST_TEST_CASE(&test_case2));

        test_suite* ts2 = BOOST_TEST_SUITE("test_suite2");
        ts2->add(BOOST_TEST_CASE(&test_case3)); // void function pointer
        ts2->add(BOOST_TEST_CASE(&test_case4));

        framework::master_test_suite().add(ts1);
        framework::master_test_suite().add(ts2);
        return 0;
    }
