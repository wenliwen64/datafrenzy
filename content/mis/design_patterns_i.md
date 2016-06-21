Title: Design Patterns Study Notes I 
Date: 2015-11-27 21:22
Modified: 2015-11-27 21:22
Slug: design-patterns-study-notes-i
Status: draft
Authors: Liwen Wen

[TOC]

# Chapter 1: Introduction

* Differences between experienced software designer and novice:
    1. Do not to solve every problem from first principles;
    2. 

* A pattern has four essential elements:
  
   1. Pattern name;

   2. The problems describing when to apply the pattern;

   3. The solution describing the elements that make up the design, relationships, responsibilities and collaborations

   4. The consequences(a system's flexibility, extensibility or portability) are the results and trade-offs of applying the pattern. 

* Design pattern definition in this book: descriptions of communicating objects and classes that are customized to solve a general design problems in a particular context. 

* Model/View/Controller(MVC) pattern

* Dynamic binding: the run-time association of a request to an object and one of its operations

* Polymorphism: it lets a client object make few assumptions about other objects beyond supporting a particular interface. 

* Principles in object-oriented design: 

   1. Program to an interface , not an implementation;

   2. Favor object composition over class inheritance;

   notes: interface: what users see; implementation: all the dirty work you do. 

# Headsup design pattern:

1. Design principle I: identify aspects of your application that vary and separate them from what stays the same.(Pull duck behaviour(quak and fly) out of duck classes, so basically you define interface variables in your base class and instantiate or initialize the specific one in your subclasses, here, `FlyBehaviour` and `QuackBehaviour` are interface not implementation).

2. Design principle II: program to an interface, not an implementation.

3. Design principle III: favor composition more than inheritance. 

4. Page 32 for summary of Chapter 1;

Chapter II: Observer pattern

Chapter III: Decorating your objects(decoration pattern)

Chapter IV: Factory method pattern and abstract factory pattern(create pizza method for only one object and ingredient factory class for a set of objects)

Chapter V: Command pattern(abstract a command and let cutstomer implement concrete command for execution)

Chapter VI: Adapter pattern(create an adapter object to do the job); Facade pattern(Just like our StMaker class, encapsulate all of other classes' operations)

Chapter VII: Algorithm template 

Chapter VIII: Create state objects' interface;

Chapter IX: Singleton Pattern(how to maintain one instance)

Chapter X: Iterator and composite, about the collectives  

Chapter XI: Proxy pattern.(icon, imageproxy to derive from it and plot thing)
