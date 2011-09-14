import unittest
from bissexto import ano_bissexto

class AnoBissextoTestCase(unittest.TestCase):

    def test_ano_divisivel_por_quatro(self):
          assert ano_bissexto(1732)

    def test_ano_nao_divisivel_por_quatro_nao_e_bissexto(self):
          assert not ano_bissexto(1453)
    
    def test_ano_divisivel_por_quatrocentos_e_bissexto(self):
          assert ano_bissexto(2000)
          
    def test_ano_divisivel_por_cem_nao_e_bisexto(self):
          assert not ano_bissexto(1700)
     
     
unittest.main()
