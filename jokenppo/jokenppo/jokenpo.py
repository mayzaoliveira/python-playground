def jokenpo(primeira_jogada,segunda_jogada):
      if primeira_jogada == segunda_jogada:
            return 'empate'
            
      ganhador = ''
      perdedor = ''
      
      '''
      ganha_de = {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra',
      }
      
      if ganha_de[primeira_jogada] == segunda_jogada:
            ganhador = primeira_jogada
            perdedor = segunda_jogada
      else:
            ganhador = segunda_jogada
            perdedor = primeira_jogada
            
      
          
      '''
      if primeira_jogada == 'pedra' and segunda_jogada == 'tesoura':
            ganhador = 'pedra'
            perdedor = 'tesoura'
            
      if primeira_jogada == 'tesoura' and segunda_jogada == 'pedra':
            ganhador = 'pedra'
            perdedor = 'tesoura'
            
      if primeira_jogada == 'tesoura' and segunda_jogada == 'papel':
            ganhador = 'tesoura'
            perdedor = 'papel'
            
      if primeira_jogada == 'papel' and segunda_jogada == 'tesoura':
            ganhador = 'tesoura'
            perdedor = 'papel'
            
      if primeira_jogada == 'papel' and segunda_jogada == 'pedra':
            ganhador = 'papel'
            perdedor = 'pedra'
            
      if primeira_jogada == 'pedra' and segunda_jogada == 'papel':
            ganhador = 'papel'
            perdedor = 'pedra'          
      
      return '%s ganha de %s' % (ganhador, perdedor)

if __name__ == "__main__":
      print jokenpo('pedra','pedra')