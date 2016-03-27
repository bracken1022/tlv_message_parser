

class Tlv_Parser(object):
    TLV_T_L_LEN = 4
    TLV_LEN_FOUR = 4
    TLV_LEN_EIGHT = 8
    TLV_LEN_TWELEVE = 12
    
    def __init__(self, input_str, data):
        self.tlv_str = input_str
        self.data = data

    def list_to_type(self, input_list):
        return int(''.join(input_list), 16)

    def list_to_len(self, input_list):
        return int(''.join(input_list), 16)

    def parse_tlv_str(self):
        tlv_str = self.tlv_str.replace('\n', '')
        tlv_list = tlv_str.split(' ')

        return self.parse_tlv_list(tlv_list, len(tlv_list))

    def parse_tlv_list(self, tlv_list, length):
        if length == 0:
            return 

        tlv_t = self.list_to_type(tlv_list[0:2])
        tlv_l = self.list_to_len(tlv_list[2:4])

        if self.TLV_LEN_FOUR == tlv_l:
            newlen = length - self.TLV_LEN_EIGHT
            tlv_v = tlv_list[self.TLV_T_L_LEN:self.TLV_T_L_LEN+tlv_l]
            tlv_start = tlv_list[self.TLV_LEN_EIGHT::]
        elif self.TLV_LEN_EIGHT == tlv_l:
            newlen = length - self.TLV_LEN_TWELEVE
            tlv_v = tlv_list[self.TLV_T_L_LEN:self.TLV_T_L_LEN+tlv_l]
            tlv_start = tlv_list[self.TLV_LEN_TWELEVE::]
        else:
            tlv_v = tlv_list[self.TLV_T_L_LEN:length]
            newlen = length - self.TLV_T_L_LEN
            tlv_start = tlv_v

        print self.data[tlv_t], tlv_l, tlv_v
        return self.parse_tlv_list(tlv_start, newlen)
