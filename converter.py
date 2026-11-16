import zipfile
import os
# zipfile is necessary for handling zip files, os is my way to interact with the OS


# Main function for core logic, need to implement with two parameters, one for in, one for out.
# The for loop allows multiple paths to be zipped together
def create_zip(paths, output_name):
    with zipfile.ZipFile(output_name, "w") as zipf:
        for path in paths:
            if os.path.exists(path):
                zipf.write(path)
            else:
                print(f'{path} does not exist')


def main():
    print(f"Current Working Directory: {os.getcwd()}")

    zip_name = input("Enter a name for your zip file (Ex. 'photos.zip'): ").strip()


    files_to_zip = []
    while True:
        file = input("Enter file name ('done' to exit): ").strip()
        if file == 'done':
            break
        else:
            files_to_zip.append(file)

    create_zip(files_to_zip, zip_name)

if __name__ == "__main__":
    main()