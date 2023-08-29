#!/usr/bin/env pytohn3

def reverse(text):
    while True:
        try:
            if len(text) == 0:
                return text
            else:
                return reverse(text[1:]) + text[0]
        except ValueError:
            print("Illegal input please enter string!!!")
        except Illegal: #your custom error was raised
           print("Meaningful message indicating the source of the error")

# print(reverse())
print(reverse("cat"))
