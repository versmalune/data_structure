def pyramid(height):
        for i in range(height):
            print(" " * (height - i - 1), end = "")
            print("*" * (2 * i + 1))


pyramid(1)
print("")
pyramid(3)
print("")
pyramid(5)
print("")

"""

  *
 ***
*****

    *
   ***
  *****
 *******
*********
"""
