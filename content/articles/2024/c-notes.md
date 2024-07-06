---
title: "Some notes on C(PP)"
publishDate: '2024-07-06T14:20:00+05:30'
categories: Programming
tags:
- Programming
slug: c-notes
---

This is a compilation of threads from my twitter about some C/C++ quirks I encountered
when building a compiler.

1. Float literals can be written in hex as well. The e character for exponent 
   is replaced with p in hex. `0x5ea.bfp-5f` is a valid float literal. Also, 
   it's a hexa decimal, so characters after the decimal are in 1/16ths and not 1/10ths.
2. Strings AND character literals take unicode characters, with a `\uXXXX` 
   specifier for unicode codepoints in hex. If the character doesn't fit in a 
   byte, you get a compiler error
```c
void main() {
    char c = '\u021f'; // clang: Character too large for enclosing character literal type
}
```
3. K&R style function definitions are deprecated, but still compile. All the 
   three below are legal (didn't know no names are a C2x extension)
```c
void foo(a, b)
int a;
char *b; // clang: deprecation warning but will compile
{
    // code 
}

void bar(int a, char *b) {
    // code
}

void baz(int, char*) { // clang: C2x extension warning
    // code
}
```
4. `auto`. `auto` is a relic of the old B days, when declarations were either 
   `auto` (scoped), `extern` or `static`. `auto` is C's appendix: completely 
   vestigal but has to be supported for backward compatiability. Unlike C++, 
   auto IS NOT automatic type inferencing in C.
5. `_Noreturn` is used when a function does not return at all; it either jumps 
   out via longjmp (akin to an exception), loops infinitely or quits. Not the 
   same as a void function (which returns nothing, but does return after execution). 
   More [here](https://en.cppreference.com/w/c/language/_Noreturn)
6. Inline struct declarations in C11 are treated as postfix expressions rather 
   than primary expressions. Also, the type for such expressions is compulsary, 
   and is represented in the typecast format, but is not a typecast.
```c
struct Point { int x, y; };
...
norm((Point){5, 2});
```
7. If you want your variables to be extra constant / extra volatile, you can 
   simply write const/volatile as many times as you want. 
   (works for restrict/atomic too)
```c
int main() {
    volatile volatile voaltile int c = 5; // clang: Duplicate specifier warning
}
```
Notwithstanding compiler warnings, the following is perfectly legal C code 
8. `static` can be used in array declarations in function arguments to imply 
   atleast that many elements will be present in the array passed to the 
   function. For example,
```c
void foo(int A[static 100]) { ... }
```
will have atleast 100 elements in A.
9. While we're on arrays, the size expression for arrays takes an assignment 
   expression. This means you can do weird stuff, like
```c
int c=2;
int a[c=5+3];
int b[c+=5];
```
Here, len(a) = 8 and len(b) = 13 
10. Even more on arrays: `char arr[const]` is equivalent to char *const arr, 
    and `arr[*]` (or `arr[n]`) denote variable length arrays in C. These only 
    work within function declarations and are non-binding for VLAs. For example,
```c
int foo(int n, int a[n])
int foo(int n, int a[*])
```
are the same, which can be confusing! 

11. Function declarations are local to scope

t1.c:
```c
int foo(int k) {
  int bar(int, int);
  return bar(k, 2);
}

void main() {
  printf("%d %d\n", foo(5), bar(2, 1));
}
```

t2.c:
```c
int bar(int a, int b) {
  return a+b;
}
```

`clang t1.c t2.c -o exec && ./exec` won't compile. Surprisingly, this behaviour 
varies across compilers. clang gives an error always, even if the C standard 
is changed (probably has to do something with how clang resolves references).
GCC compiles without complaining, but gives a warning (`-Wimplicit-function-declaration`)

12. Declarations without variable names are legal and merit only a warning 
13. More on float literals: p is a power of 2 and not 16, and p is compulsory to provide for hexfloats.

```c
float f;
f = 0x3.2f // wrong
f = 0x3.2p1f // correct
f = 0xA.p2f // f = 40.f 
```
14. new(loc) allows you to point the heap memory allocator to prereserved space,
    which can also be on the stack:

```c
char loc[1000];
Object *o = new(loc) Object();
```

Creates o at loc (if it’s <1000 bytes, I guess? probably UB otherwise)

15. Static polymorphism is a thing [in C++](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern):

```c++
template <class C>
class base {
    void interface () {
        static_cast<C*>(this)->impl();
    }
}

class derived: public base<derived> {
    void impl() {
        // logic here
    }
}
```

This gives you compile-time polymorphism without a vtable :D 

16. Static alloc is much faster than a malloc. don’t alloc/free objects when 
    latency is critical, instead use a fixed-size ring buffer initialised 
    statically with objects that your producer populates and consumer copies 
    out of


## Puzzles

This is a good one. What are the values in a and b after this code runs?

```c
int a[3] = {2, 3, 4};
int *b = a;
*(b++) += 100;
```

Your answer should be in the format a={...}, *b=..

{{% spoiler prompt="Ans: " %}}
Ans: a = {102, 3, 4}, *b=a[1].
b++ increments b, but returns the original value of b, so that line is equivalent 
to a[0] += 100. b is incremented and points to a[1] now. Note that that f += c 
is not equivalent to f = f + c if you're making a compiler.
{{%/ spoiler %}} 

Another one: What does the following code do?

```c++
void comma(std::vector<int>& A) {
  for (int i=0; i<A.size()-1; i++) {
    cout << A[i] << ",";
  }
  if (A.size() > 0) cout << A[A.size()-1] << endl;
}

void main() {
  std::vector<int> A;
  comma(A);
}
```

1. prints nothing
2. segfaults
3. prints "\n"
4. doesn't compile

{{% spoiler prompt="Ans: " %}} 
Ans: 2. A tricky q! A.size() is of type size_t, which is unsigned, so A.size()-1
underflows to 2^64-1. 0 is less than this value, so we enter the loop, causing a segfault.
The compiler gives a warning when comparing int and size_t, and this is why you should follow it.
{{%/ spoiler %}} 


Last one: 

```c++
std::string("012345").replace(0, 5, "abcde");
std::string("012345").replace(0, 2, "abcde");
```

Gives what pair of strings?

1. "abcde5" and "ab2345"
2. "01234a" and "01abcd"
3. "abcde5" and "abcde2345"
4. "abcde5" and "abc345"

{{% spoiler prompt="Ans: " %}} 
"abcde5" and "abcde2345". replace is modelled as a delete and insert operation, 
rather than a range-based replacement (replace(0,2,"abcde",0,2) gives "ab2345"). 
Most sources (cppreference included) don't say this clearly.
{{%/ spoiler %}} 
