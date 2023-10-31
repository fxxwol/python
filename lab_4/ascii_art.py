class AsciiArt:
    staticmethod
    def load_ascii_art(file_path):
        ascii_dict = {}
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip().split('@symbol::')
            for item in content[1:]:
                symbol, *lines = item.split('\n')
                ascii_dict[symbol] = [line.strip('^$') for line in lines[0:]]
        return ascii_dict
