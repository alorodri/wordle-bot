

class Test():
    __word = 'PERRA'
    __attempt = 0

    def try_attempt(self, word):
        if self.__attempt == 6:
            return 'LOST GAME'

        result = ''

        if self.__word[0] != word[0]:
            result += '.'
        else:
            result += word[0]
        if self.__word[1] != word[1]:
            result += '.'
        else:
            result += word[1]
        if self.__word[2] != word[2]:
            result += '.'
        else:
            result += word[2]
        if self.__word[3] != word[3]:
            result += '.'
        else:
            result += word[3]
        if self.__word[4] != word[4]:
            result += '.'
        else:
            result += word[4]

        self.__attempt += 1

        return result