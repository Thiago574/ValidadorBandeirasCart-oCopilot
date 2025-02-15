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

# Example usage:
card_number = 4111111111111111
print(validate_credit_card(card_number))  # Output: Visa

