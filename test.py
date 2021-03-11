
def print_versions():
    import platform
    print("Platform Version:",platform.python_version())

    import sys
    print("Sys Version:",sys.version)
    print("Sys Version:",sys.version.replace("\n"," - "))

#print_versions()
