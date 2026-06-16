import os

class MarcoTechPacker:
    def __init__(self, A, B):
        self.PackName = A
        self.DirName = B

    def PackingActivity(self):
        try:
            print("--------------------------------------------------------")
            print("----------- MarcoTech Packer Unpacker -----------------")
            print("--------------------------------------------------------")
            print("------------------ Packing Activity --------------------")
            print("--------------------------------------------------------")

            iCountFile = 0

            if os.path.exists(self.DirName) and os.path.isdir(self.DirName):

                print(self.DirName + " is successfully opened")

                with open(self.PackName, "wb") as foobj:

                    for filename in os.listdir(self.DirName):

                        filepath = os.path.join(self.DirName, filename)

                        if not os.path.isfile(filepath):
                            continue

                        FileSize = os.path.getsize(filepath)

                        Header = f"{filename} {FileSize}"
                        Header = Header.ljust(100)

                        foobj.write(Header.encode())

                        with open(filepath, "rb") as fiobj:

                            while True:
                                Buffer = fiobj.read(1024)

                                if not Buffer:
                                    break

                                foobj.write(Buffer)

                        iCountFile += 1

                        print("File Scanned :", filename)
                        print("File size read :", FileSize)
                        print()

                print("Packing activity done")
                print("--------------------------------------------------------")
                print("------------------ Statistical Report ------------------")
                print("Total files Packed :", iCountFile)
                print("--------------------------------------------------------")
                print("--------- Thank you for using our application ----------")
                print("--------------------------------------------------------")

            else:
                print("There is no such directory")

        except Exception as e:
            print(e)


class Packer:
    @staticmethod
    def main():

        DirName = input("Enter the name of Directory that you want to pack: ")

        PackName = input("Enter the name of file that you want to create for packing: ")

        mobj = MarcoTechPacker(PackName, DirName)
        mobj.PackingActivity()


if __name__ == "__main__":
    Packer.main()
