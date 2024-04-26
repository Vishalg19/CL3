import Pyro4

def main():
    uri = input("Enter the URI of the server object: ")  # Assume you've got the URI from the server output
    string_concatenator = Pyro4.Proxy(uri)  # Get a proxy to the remote object

    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    result = string_concatenator.concatenate(str1, str2)
    print("The concatenated string is:", result)

if __name__ == '__main__':
    main()
