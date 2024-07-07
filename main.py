def main():
    path = input("Enter the Path to Book")
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        noOfwords = len(words)

    def countChar(file_contents: str):
        bookStr = file_contents.lower()
        char_Count = {}
        for char in bookStr:
            if char.isalpha():
                if char in char_Count:
                    char_Count[char] +=1
                else :
                    char_Count[char] = 1

        return char_Count

    def printReport():
        print(f"------------------ Begin of the report of {path} book ------------------ ")
        print(f"{noOfwords} found in the Document")
        theBook = countChar(file_contents)
        theBook = dict(sorted(theBook.items()))

        for key,value in theBook.items():
            print(f"The {key} char was found {value} times ")


        print(f"----------------- end of the report for the {path}----------------- ")


    printReport()


main()




