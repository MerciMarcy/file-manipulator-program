import sys

from file_manipulator import FileManipulator


def main():
    fileManipulator = FileManipulator(sys.argv)
    fileManipulator.execute()


if __name__ == "__main__":
    main()
