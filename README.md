# Pong

Essa é mais umas das muitas releituras do jogo Pong.
Feito usando Python e a biblioteca curses.
Execute o arquvo `main.py` para jogar.

## Curses

### Linux
O curses já vem incluído por padrão no terminal.

### Windows

É necessário instalar no Windows, usando o pip:
```
pip install windows-curses
```

## Limitações

Decidi usar somente a biblioteca curses, por isso o jogo apresenta uma limitação grave, dois jogadores não conseguem se mover ao mesmo tempo. O motivo, o curses não consegue receber mais de uma entrada ao mesmo tempo.
