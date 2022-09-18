from constants import Constants

class Test():
    __word = 'DIGNO'
    __attempt = 0

    def try_attempt(self, word):
        colors = []

        if self.__word[0] != word[0]:
            if word[0] in self.__word:
                colors.append(Constants.YELLOW)
            else:
                colors.append(Constants.GRAY)
        else:
            colors.append(Constants.GREEN)
        if self.__word[1] != word[1]:
            if word[1] in self.__word:
                colors.append(Constants.YELLOW)
            else:
                colors.append(Constants.GRAY)
        else:
            colors.append(Constants.GREEN)
        if self.__word[2] != word[2]:
            if word[2] in self.__word:
                colors.append(Constants.YELLOW)
            else:
                colors.append(Constants.GRAY)
        else:
            colors.append(Constants.GREEN)
        if self.__word[3] != word[3]:
            if word[3] in self.__word:
                colors.append(Constants.YELLOW)
            else:
                colors.append(Constants.GRAY)
        else:
            colors.append(Constants.GREEN)
        if self.__word[4] != word[4]:
            if word[4] in self.__word:
                colors.append(Constants.YELLOW)
            else:
                colors.append(Constants.GRAY)
        else:
            colors.append(Constants.GREEN)

        self.__attempt += 1

        return colors