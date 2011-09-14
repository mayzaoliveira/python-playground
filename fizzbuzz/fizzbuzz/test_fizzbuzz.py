from fizzbuzz import fizzbuzz

import unittest


class FizzBuzzTestCase(unittest.TestCase):

    def test_quando_o_numero_e_divisivel_por_3_deve_retornar_fizz(self):
        self.assertEqual('fizz',fizzbuzz(3))

    def test_quando_o_numero_e_divisivel_por_5_deve_retornar_buzz(self):
        assert 'buzz' == fizzbuzz(5)

    def test_quando_numero_nao_e_divisivel_por_3_e_nem_5_deve_retornar_o_numero(self):
        assert 11 == fizzbuzz(11)

    def teste_quando_numero_e_divisivel_por_3_e_por_5_deve_retornar_fizzbuzz(self):
        assert 'fizzbuzz' == fizzbuzz(15)

unittest.main()
