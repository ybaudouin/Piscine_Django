#!/usr/bin/python3
import os
import sys
import re
import settings

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <file>")
        return
    # Check if the file has the right extension
    regex = re.compile(".*\.template")
    path = sys.argv[1]
    if not regex.match(path):
        return print("wrong extension, (required: .template)")
    # Check if the file exists
    if not os.path.exists(sys.argv[1]):
        print("Error: File does not exist")
        return
    # Check if the template exists
    if not os.path.exists("myCV.template"):
        print("Error: Template does not exist")
        return
    # Read the template and replace the variables
    with open(path, "r") as f:
        template = "".join(f.readlines())
    try:
        # Create the file with the variables replaced
        # by the values in the settings.py file
        file = template.format(**settings.__dict__)
        with open("myCV.html", "w") as f:
            f.write(file)
    # Catch any exception
    except Exception as e:
      return print(f"Error: {e}")
    
if __name__ == '__main__':
    main()