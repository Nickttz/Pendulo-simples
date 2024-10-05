# Simulação de Movimento de Pêndulo

Este código simula o movimento de um pêndulo sob a influência de forças variáveis. O modelo utiliza a seguinte equação diferencial:

### y''(x) = -(a - 2q * cos(2x)) * y(x)

onde:
- y(x) representa a posição do pêndulo,
- a e q são parâmetros que influenciam o comportamento do movimento.

## Condições Iniciais

As condições iniciais para a simulação são:
- y(0) = 1 (posição inicial do pêndulo)
- y'(0) = 0 (velocidade inicial do pêndulo)

## Parâmetros

Os parâmetros a e q podem ser ajustados para explorar diferentes comportamentos do pêndulo. Exemplos de valores usados na simulação incluem:
- (a=1, q=0.5)
- (a=2, q=0.3)
- (a=0.5, q=0.8)
- (a=1.5, q=0.4)
- (a=0.8, q=0.6)

## Tecnologias Utilizadas

- Python
- NumPy
- Matplotlib
- SciPy

## Instalação

Para rodar o código, você precisará ter o Python instalado em seu computador. Você pode instalar as bibliotecas necessárias usando `pip`:

```bash
pip install numpy matplotlib scipy
```

# Gráfico

![Circuito RLC](Imagem.jpg)

