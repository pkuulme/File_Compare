import unittest
from Compare import Files
import os

class TestFiles(unittest.TestCase):
    def test_files(self):

        ##Checking if correct files have been selected
        self.assertEqual(Files.first, '/home/peep/Desktop/Python/Project/main_file.xlsx')
        self.assertEqual(Files.second,'/home/peep/Desktop/Python/Project/secondary_file.xlsx')

        ##Checking if the output file has been created
        assert os.path.isfile('/home/peep/Desktop/Python/Project/output.xlsx')




if __name__ == '__main__':
    unittest.main()