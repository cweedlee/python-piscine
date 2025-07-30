import sys

def main() -> int : 
    ### error case
    # check the argv length
    if len(sys.argv) > 2 :
        print("AssertionError: more than one argument is provided") ; return 1 ; 
    elif len(sys.argv) == 1 : 
        return 1 ; 

    val = 0;
    # check the argv is integer
    try:  
        val = int(sys.argv[1])
    except ValueError as e: 
        print("AssertionError: argument is not an integer") ; return 1 ; 

    ### check
    # check if it's odd or even
    if (val % 2) :
        print("I'm Odd.");
    else :
        print("I'm Even.");
    return 0;


if __name__ == "__main__":
    main()
