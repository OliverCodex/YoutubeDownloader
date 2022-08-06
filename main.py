from download import Download
from utils import Text

class main:
    def __init__(self, default_path):
        url, path = Text.main(default_path)

        Download(url, path)

        input("Press enter to rerun script:\n>>")

        main(r"C:\Users\olive\Music\test")
        
if __name__ == "__main__":
    main(r"C:\Users\olive\Music\test")