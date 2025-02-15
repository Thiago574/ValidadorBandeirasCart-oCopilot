# Validação de Cartão de Crédito e Identificação de Bandeira

Este repositório contém um script em Python que valida números de cartões de crédito e identifica a bandeira (Visa, MasterCard, etc.) com base nos prefixos e comprimentos dos números dos cartões.

## Funcionalidades

- Validação de números de cartões de crédito.
- Identificação da bandeira do cartão com base nos prefixos e comprimentos conhecidos.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório ou baixe o arquivo `validate_credit_card.py`.
3. Execute o script com um número de cartão de crédito para verificar sua validade e identificar a bandeira.

## Exemplo de Uso

```python
def validate_credit_card(number):
    card_info = {
        "American Express": {"prefixes": ["34", "37"], "lengths": [15]},
        "Diners Club - Carte Blanche": {"prefixes": ["300", "301", "302", "303", "304", "305"], "lengths": [14]},
        "Diners Club - International": {"prefixes": ["36"], "lengths": [14]},
        "MasterCard": {"prefixes": ["51", "52", "53", "54", "55"] + [str(i) for i in range(222100, 272100)], "lengths": [16]},
        "Visa": {"prefixes": ["4"], "lengths": [13, 16, 19]},
        "Visa Electron": {"prefixes": ["4026", "417500", "4508", "4844", "4913", "4917"], "lengths": [16]}
    }

    number_str = str(number)
    number_length = len(number_str)

    for brand, info in card_info.items():
        if number_length in info["lengths"]:
            for prefix in info["prefixes"]:
                if number_str.startswith(prefix):
                    return brand
    return "Unknown"

# Exemplo de uso:
card_number = 4111111111111111
print(validate_credit_card(card_number))  # Saída: Visa
