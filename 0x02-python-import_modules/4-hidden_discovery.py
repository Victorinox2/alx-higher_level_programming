#!/usr/bin/python3

# File: 4-hidden_discovery.py
# Auth: Victorinox2

if __name__ == "__main__":
    """prints all the names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
