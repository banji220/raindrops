import unittest
from raindrops import convert

class RainDropTest(unittest.TestCase):
    def test_the_sound_for_number_1_is_1(self):
        self.assertEqual(convert(1), 1)
    
    def test_the_sound_for_number_4_is_4(self):
        self.assertEqual(convert(4), 4)
    
    def test_the_sound_four_number_3_is_Pling(self):
        self.assertEqual(convert(3), "Pling")
        
    def test_the_sound_four_number_5_is_Plang(self):
        self.assertEqual(convert(5), "Plang")
        
    def test_the_sound_four_number_7_is_Plong(self):
        self.assertEqual(convert(7), "Plong")
    
    def test_the_sound_four_number_15_is_PlingPlang(self):
        self.assertEqual(convert(15), "PlingPlang")
    
    def test_the_sound_four_number_21_is_PlingPlong(self):
        self.assertEqual(convert(21), "PlingPlong")
        
    def test_the_sound_four_number_105_is_PlingPlangPlong(self):
        self.assertEqual(convert(105), "PlingPlangPlong")
        
    def test_2_to_the_power_3_does_not_make_a_raindrop_sound_as_3_is_the_exponent_not_the_base(self):
        self.assertEqual(convert(8), "8")
    

if __name__ == "__main__":
    unittest.main()