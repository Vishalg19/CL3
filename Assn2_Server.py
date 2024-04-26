import Pyro4

@Pyro4.expose
class StringConcatenator(object):
    def concatenate(self, str1, str2):
        """Concatenates two strings."""
        return str1 + str2

def main():
    # Start the Pyro daemon
    daemon = Pyro4.Daemon()  # Make a Pyro daemon
    uri = daemon.register(StringConcatenator)  # Register the greeting maker as a Pyro object
    
    print("Ready. Object uri =", uri)  # Print the URI so we can use it in the client later
    daemon.requestLoop()  # Start the event loop of the server to wait for calls

if __name__ == '__main__':
    main()
