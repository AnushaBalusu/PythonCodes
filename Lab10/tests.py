""" 
file: tests.py
description: Verify the LinkedHashTable class implementation
"""

__author__ = [ "anusha_balusu", "pankhuri_roy" ]

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set: # uses the iter method
        print( word, end=" " )
    print()

def test0():
    '''
    Example test method provided
    :return: None
    '''
    table = LinkedHashTable( 100 )
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print_set( table )

    print( "'to' in table?", table.contains( "to" ) )
    table.remove( "to" )
    print( "'to' in table?", table.contains( "to" ) )

    print_set( table )

def test1():
    '''
    Test that adds few integers to the hash table. And then deletes one and checks it's presence in the table
    :return: None
    '''
    table = LinkedHashTable( 100 )
    table.add("0")
    table.add("1")
    table.add("2")
    table.add("3")
    table.add("4")

    print_set( table )

    print( "4 in table?", table.contains("4") )
    table.remove("4")
    print( "4 in table?", table.contains("4") )

    print_set( table )

def test2():
    '''
    Test that adds few words, and then random words and deleted and the table is printed again.
    :return: None
    '''
    table = LinkedHashTable( 3 )
    table.add( "Hello" )
    table.add( "it's" )
    table.add( "me" )
    table.add( "I" )
    table.add( "was" )
    table.add( "wondering" )

    print_set( table )

    table.add( "if" )
    table.add( "after" )
    table.add( "all" )
    table.add( "these" )
    table.add( "years" )
    table.add( "you'd" )
    table.add( "like" )
    table.add( "to" )
    table.add( "meet" )

    print_set( table )

    table.remove( "I" )
    table.remove( "years" )

    print_set( table )

def test3():
    '''
    Test that adds some words and some numbers as strings. Then some of them are deleted and the table is shown
    :return: None
    '''
    table = LinkedHashTable( 1 )
    table.add( "Hello" )
    table.add( "1" )
    table.add( "from" )
    table.add( "2" )
    table.add( "the" )
    table.add( "3" )
    table.add( "other" )
    table.add( "4" )
    table.add( "side!" )
    table.add( "5" )

    print_set( table )

    table.remove( "1" )
    table.remove( "3" )
    table.remove( "5" )

    print_set( table )

if __name__ == '__main__':
    print("First test")
    test0()
    print("Second test")
    test1()
    print("Third test")
    test2()
    print("Fourth test")
    test3()

