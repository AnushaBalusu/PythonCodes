"""
This is an exercise from:
    http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html
that demonstrates how bitcoin mining works.  It performs only a single
pass of the SHA-256 algorithm to encrypt the first 32 bits of data.

Author: Sean Strout @ RIT CS
Author: <<< ANUSHA BALUSU, PANKHURI ROY>>
"""

# constants
BITS = 32    # working with 32 bits of data

# the initial constants for SHA-256
A0 = 0x6a09e667
B0 = 0xbb67ae85
C0 = 0x3c6ef372
D0 = 0xa54ff53a
E0 = 0x510e527f
F0 = 0x9b05688c
G0 = 0x1f83d9ab
H0 = 0x5be0cd19
K = 0x428a2f98


def padIntTo32Bits(data):
    """
    Takes an integer that can be represented in 32 bits (or less), and returns
    it as a 32 bit binary string of 0's and 1's.], e.g.:

        padIntTo32Bits(11) = '0b00000000000000000000000000001011'
        padIntTo32Bits(0x6a09e667) = '0b01101010000010011110011001100111'

    :param data (int): An integer represented in 32 bits or less
    :pre: data is 32 bits or less
    :return: A 32 bit binary string
    """
    binary_data = bin(data)
    no_of_zeros = 34 - len(binary_data)
    padded_binary = '0b'
    for _ in range(no_of_zeros):
        padded_binary += '0'
    padded_binary += binary_data[2:]
    return padded_binary


def Ma(A, B, C):
    """
    The Ma majority box looks at the bits of A, B, and C. For each position,
    if the majority of the bits are 0, it outputs 0. Otherwise it outputs 1.
    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param B (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param C (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string that stores the result
    """

    result = ''

    for index in range(2, 34):
        counter_zero = 0
        if A[index] is '0':
            counter_zero += 1
        if B[index] is '0':
            counter_zero += 1
        if C[index] is '0':
            counter_zero += 1

        if counter_zero > 1:
            result += '0'
        else:
            result += '1'
    return '0b' + result


def rightShift(data, amount):
    """
    Right shift (rotating) a binary string by an amount, e.g.:

        rightShift('0b01101010000010011110011001100111', 2) ==
                   '0b11011010100000100111100110011001'

    This routine is used internally by Sum0() and Sum1() to
    perform the proper shifts.

    :param data (str): The 32 bit binary string to shift/rotate
    :param amount (int): The amount to shift/rotate
    :return: The resulting 32 bit binary string
    """
    original_str = data[2:]
    shift_data = original_str[len(original_str) - amount:]
    string_after_shift = original_str[0:len(original_str) - amount]
    return '0b' + shift_data + string_after_shift


def Sum0(A):
    """
    Rotates the bits of A to form three rotated versions, and then sums them
    together modulo 2. In other words, if the number of 1 bits is odd, the sum
    is 1; otherwise, it is 0.  The three values in the sum are A rotated right
    by 2 bits, 13 bits, and 22 bits.

    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    result = ''
    shifted_str1 = rightShift(A, 2)
    shifted_str2 = rightShift(A, 13)
    shifted_str3 = rightShift(A, 22)
    for index in range(2, 34):
        counter_one = 0
        if shifted_str1[index] == '1':
            counter_one += 1
        if shifted_str2[index] == '1':
            counter_one += 1
        if shifted_str3[index] == '1':
            counter_one += 1

        if counter_one % 2 != 0:
            result += '1'
        else:
            result += '0'
    return '0b' + result


def Ch(E, F, G):
    """
    The Ch "choose" box chooses output bits based on the value of input E. If
    a bit of E is 1, the output bit is the corresponding bit of F. If a bit
    of E is 0, the output bit is the corresponding bit of G. In this way, the
    bits of F and G are shuffled together based on the value of E.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param F (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param G (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    result = ''
    for counter in range(2, 34):
        if E[counter] == '1':
            result += F[counter]
        else:
            result += G[counter]
    return '0b' + result


def Sum1(E):
    """
    This sum box rotates and sums the bits of E, similar to Sum0 except the
    shifts are 6, 11, and 25 bits.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    result = ''
    shifted_str1 = rightShift(E, 6)
    shifted_str2 = rightShift(E, 11)
    shifted_str3 = rightShift(E, 25)
    for index in range(2, 34):
        counter_one = 0
        if shifted_str1[index] == '1':
            counter_one += 1
        if shifted_str2[index] == '1':
            counter_one += 1
        if shifted_str3[index] == '1':
            counter_one += 1
        if counter_one % 2 != 0:
            result += '1'
        else:
            result += '0'
    return '0b' + result


def trimTo32Bits(val):
    """
    Takes a binary string that may be larger than 32 bits and cut it down to 32
    bits by removing the extra most significant bits, e.g.:

        trim('0b111111110000010001000100001001101') ==
            '0b11111110000010001000100001001101'

    :param val (str): A binary string of 32 or greater bits
    :pre: val is >= 32 bits
    :return: A trimmed 32 bit binary string
    """
    val = val[2:]
    extra_bits = len(val) - 32
    val = val[extra_bits:]
    return '0b' + val


def main():
    """
    The main performs a single pass of SHA-256 on a 32 bit user supplied input
    :return: None
    """

    # 1. Convert the initial values for A,B,C into padded binary strings
    A, B, C = padIntTo32Bits(A0), padIntTo32Bits(B0), padIntTo32Bits(C0)

    # 2. Compute the majority and sum0 boxes
    majority = Ma(A, B, C)
    print('Ma: bin=' + majority, ', hex=' + hex(int(majority, 2)))
    sum0 = Sum0(A)
    print('sum0: bin=' + sum0 + ', hex=' + hex(int(sum0, 2)))

    # 3. Convert the initial values for E,F,G into padded binary strings
    E, F, G = padIntTo32Bits(E0), padIntTo32Bits(F0), padIntTo32Bits(G0)

    # 4. Compute the choose and sum1 boxes
    choose = Ch(E, F, G)
    print('Ch: bin=' + choose, ', hex=' + hex(int(choose, 2)))
    sum1 = Sum1(E)
    print('Sum1: bin=' + sum1, ', hex=' + hex(int(sum1, 2)))

    # 5. Prompt the user for a 32 bit integer, w, to encrypt
    w = int(input('Enter 32 bit input, e.g. 0x02000000:'), 16)

    # 6. Compute the overall sum
    sum = trimTo32Bits(bin(w + K + H0 + int(choose, 2) + int(sum1, 2)))
    print('Sum1: bin=' + sum, ', hex=' + hex(int(sum, 2)))

    # 7. Update to the new values for A-H
    newA = int(trimTo32Bits(bin(int(sum0, 2) + int(majority, 2) + int(sum,2))), 2)
    newB = int(A, 2)
    newC = int(B, 2)
    newD = int(C, 2)
    newE = int(trimTo32Bits(bin(D0 + int(sum,2))), 2)
    newF = int(E, 2)
    newG = int(F, 2)
    newH = int(G, 2)

    # display results
    print("newA:", hex(newA))
    print("newB:", hex(newB))
    print("newC:", hex(newC))
    print("newD:", hex(newD))
    print("newE:", hex(newE))
    print("newF:", hex(newF))
    print("newG:", hex(newG))
    print("newH:", hex(newH))

if __name__ == '__main__':
    main()
