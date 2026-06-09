class Logger:

    @staticmethod
    def log_error(line, error):

        with open(
            "errors.log",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"{line} -> {error}\n"
            )