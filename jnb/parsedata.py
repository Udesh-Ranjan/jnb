import argparse


class ParseData:
    def __init__(self):
        pass

    @staticmethod
    def parse_data():
        parser = argparse.ArgumentParser(prog='JNB')
        parser.add_argument('-c', '--create',
                            action='extend',
                            help='Empty Jupyter Notebooks to be created',
                            nargs='+',
                            type=str,
                            required=True)

        args = parser.parse_args()

        # if args.create:
        #     for filename in args.create:
        #         print(filename)
        #         with open(f"{filename}", 'w') as file:
        #             file.write("Hmm")

        return args
