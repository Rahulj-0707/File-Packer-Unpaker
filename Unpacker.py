import os

class MarvellousUnpacker:

    def __init__(self, A):
        self.PackName = A

    def UnpackingActivity(self):

        try:
            print("--------------------------------------------------------")
            print("----------- Marvellous Packer Unpacker -----------------")
            print("--------------------------------------------------------")
            print("----------------- UnPacking Activity -------------------")
            print("--------------------------------------------------------")

            iCountFile = 0

            if not os.path.exists(self.PackName):
                print("Unable to access Packed file")
                return

            print("Packed file gets successfully opened")

            with open(self.PackName, "rb") as fiobj:

                while True:

                    HeaderBuffer = fiobj.read(100)

                    if not HeaderBuffer:
                        break

                    Header = HeaderBuffer.decode().strip()

                    if Header == "":
                        break

                    Tokens = Header.split()

                    if len(Tokens) < 2:
                        break

                    FileName = Tokens[0]
                    FileSize = int(Tokens[1])

                    Buffer = fiobj.read(FileSize)

                    with open(FileName, "wb") as foobj:
                        foobj.write(Buffer)

                    print(
                        "File unpack with name :",
                        FileName,
                        "having size",
                        FileSize
                    )

                    iCountFile += 1

            print("--------------------------------------------------------")
            print("------------------ Statistical Report ------------------")
            print("--------------------------------------------------------")
            print("Total number of files unpacked :", iCountFile)
            print("--------------------------------------------------------")
            print("--------- Thank you for using our application ----------")
            print("--------------------------------------------------------")

        except Exception as e:
            print(e)


class Unpacker:

    @staticmethod
    def main():

        PackName = input(
            "Enter the name of file which contains packed data : "
        )

        mobj = MarvellousUnpacker(PackName)
        mobj.UnpackingActivity()


if __name__ == "__main__":
    Unpacker.main()