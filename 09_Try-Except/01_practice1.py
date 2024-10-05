# Multiple files open & try-except

def openFiles(filename1,filename2,filename3):
    try:
        with(
            open(filename1,"r") as f1,
            open(filename2,"r") as f2,
            open(filename3,"r") as f3,
        ):
            print(f1.read(),f2.read(),f3.read())
            
    except FileNotFoundError:
        print("File doesn't exists!")
        return
    else:
        print("Files Exists.")
        return
    finally:
        print("Thanks!")

def main():  
    openFiles("09_Try-Except/file1.txt","09_Try-Except/file2.txt","09_Try-Except/file3.txt")
    
main()