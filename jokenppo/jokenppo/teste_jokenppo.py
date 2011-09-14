import unittest

from jokenpo import jokenpo

class TesteJokenpo(unittest.TestCase):
      def test_pedra_empata_com_pedra(self):
            assert 'empate' == jokenpo('pedra', 'pedra')
            
      def test_pedra_ganha_de_tesoura(self):
            assert 'pedra ganha de tesoura' == jokenpo('pedra', 'tesoura')
      
      def test_pedra_ganha_de_tesoura_inverso(self):
            assert 'pedra ganha de tesoura' == jokenpo('tesoura', 'pedra')
      
      def test_tesoura_empata_com_tesoura(self):
            assert 'empate' == jokenpo('tesoura', 'tesoura')
            
      def test_tesoura_ganha_de_papel(self):
            assert 'tesoura ganha de papel' == jokenpo('tesoura', 'papel')
            
      def test_tesoura_ganha_de_papel_inverso(self):
            assert 'tesoura ganha de papel' == jokenpo('papel', 'tesoura')
            
      def test_papel_ganha_de_pedra(self):
            assert 'papel ganha de pedra' == jokenpo('papel', 'pedra')
            
      def test_papel_ganha_de_pedra_inverso(self):
            assert 'papel ganha de pedra' == jokenpo('pedra', 'papel')
                        
unittest.main()