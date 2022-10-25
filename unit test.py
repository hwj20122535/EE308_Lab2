import unittest
import EE308_Lab2
text = EE308_Lab2.get_text()
counts1=EE308_Lab2.solve()
class test(unittest.TestCase):

    def test_first_question(self):
        keyWords = ["auto", "break", "case", "char", "const",
                    "continue", "default", "do", "double", "else",
                    "enum", "extern", "float", "for", "goto",
                    "if", "int", "long", "register", "return",
                    "short", "signed", "sizeof", "static", "struct",
                    "switch", "typedef", "union", "unsigned",
                    "void", "volatile", "while", "elseif"]
        self.assertEqual(EE308_Lab2.first_question(), 35)

    def test_second_question(self):
        self.assertEqual(EE308_Lab2.second_question(counts1), [2.3])
    def test_third_question(self):
        self.assertEqual(EE308_Lab2.third_question(), 2)
    def test_fourth_question(self):
        self.assertEqual(EE308_Lab2.fourth_question(), 2)

if __name__ == '__main__':
    unittest.main()