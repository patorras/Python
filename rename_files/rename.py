import os



def main():

    #change directory
    os.chdir('J:\Scenes\Devon')

    #grabs the folder name
    folder = os.path.basename(str(os.getcwd()))

    #runs trhoug all the files in the folder
    for f in os.listdir():
        #renames the files
        os.rename(f, folder + " - " + f)
        print(folder + " - " + f)


if __name__ == '__main__':
    main()
