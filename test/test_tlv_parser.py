import unittest

from src.tlv_parser import Tlv_Parser
from data.gtpu_tlv_data import gtpu_dict

class Test_Tlv_Parser(unittest.TestCase):
    
    def setUp(self):
        tlv_str = '01 0D 00 24 00 08 00 04 00 00 00 01 00 01 00 04 00 00 00 02 00 67 00 04 00 00 00 03 00 07 00 08 02 03 07 06 05 04 0A 0B'
        self.parser = Tlv_Parser(tlv_str, gtpu_dict)

    def tearDown(self):
        pass

    def test_list_to_type(self):
        input_list = ['00', '0D'] 
        input_type = self.parser.list_to_type(input_list)
        
        self.assertEqual(0xd, input_type)

    def test_list_to_len(self):
        input_list = ['00', '04']
        input_len = self.parser.list_to_len(input_list)

        self.assertEqual(4, input_len)

    def test_parse_tlv(self):
        self.parser.parse_tlv_str()



if __name__ == '__main__':
    unittest.main()
