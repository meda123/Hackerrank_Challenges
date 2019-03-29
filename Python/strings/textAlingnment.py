# https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bsubdomains%5D%5B%5D=py-strings&badge_type=python

'''
Input:
A single line containing the thickness of value for the logo

Outout:
Out the desired logo
'''

def gen_logo(thickness):
    c = "H"

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Bottom Cone
    for i in range(thickness):
        print(
            (
                (c * (thickness - i - 1)).rjust(thickness)
                + c
                + (c * (thickness - i - 1)).ljust(thickness)
            ).rjust(thickness * 6)
        )


if __name__ == "__main__":
    thickness = int(input())
    gen_logo(thickness)
