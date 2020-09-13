class AccessDataInterface:

    def read_data(self) -> int:
        # Read data from a file or a database
        pass

class AccessDataFile(AccessDataInterface):
    def __init__(self, path: str, file_name: str):
        self.file_name = file_name
        self.path = path

    def read_data(self) -> str:
        f = open(self.path + self.file_name, 'r')
        word = f.readline()

        return word

class BusinessLogic:
    def __init__(self, data_access: AccessDataInterface):
        self.data_access = data_access

        self.word = self.data_access.read_data()

    def reverse_word(self) -> str:
        
        return self.word[::-1]

class AccessDataMock(AccessDataInterface):
    def __init__(self, data: str):
        self.data = data

    def read_data(self) -> str:
        return self.data

class BusinessLogicTest:
    def __init__(self):
        pass
        
    def test_happy_word(self):
        reversed_word = BusinessLogic(AccessDataMock('happyword')).reverse_word()
        print('Test Reverse of happyword is: ', reversed_word)

        assert(reversed_word == 'drowyppah')

    def test_palindrome_word(self):
        reversed_word = BusinessLogic(AccessDataMock('tattarrattat')).reverse_word()
        print('Test Reverse of tattarrattat is: ', reversed_word)

        assert(reversed_word == 'tattarrattat')

    def test_same_letter_word(self):
        
        reversed_word = BusinessLogic(AccessDataMock('aaaaa')).reverse_word()
        print('Test Reverse of aaaaa is: ', reversed_word)

        assert(reversed_word == 'aaaaa')

    def test_1_letter_word(self):
        reversed_word = BusinessLogic(AccessDataMock('a')).reverse_word()
        print('Test Reverse of a is: ', reversed_word)
        
        assert(reversed_word == 'a')

    def test_empty_word(self):
        reversed_word = BusinessLogic(AccessDataMock('')).reverse_word()
        print('Test Reverse of "" is: ', reversed_word)

        assert(reversed_word == '')

if __name__ == '__main__':

    # Our business logic is reading from a real data source:
    word_reverse = BusinessLogic(AccessDataFile('/home/hamid/projects/training.computerscience.programming.python/oop/', 'data_source.txt'))
    print(word_reverse.reverse_word())

    # Our business logic is reading from a mock data source object:
    tester = BusinessLogicTest()
    tester.test_happy_word()
    tester.test_same_letter_word()
    tester.test_palindrome_word()
    tester.test_1_letter_word()
    tester.test_empty_word()




