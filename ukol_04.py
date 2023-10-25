def valid_phone_number(phone_number):
    # Ověření, že číslo má správný formát
    if phone_number.startswith("+420") and (len(phone_number) == 13):
        return True
    elif (not phone_number.startswith("+420")) and (len(phone_number) == 9):
        return True
    else:
        return False

def calculate_message_cost(message):
    # Spočítání cenu zprávy na základě počtu znaků
    message_length = len(message)
    cost = (message_length // 180 + 1) * 3  # Cena za každých započatých 180 znaků
    return cost

def main():
    phone_number = input("Zadejte telefonní číslo: ")
    if valid_phone_number(phone_number):
        message = input("Zadejte zprávu: ")
        cost = calculate_message_cost(message)
        print(f"Cena zprávy je {cost} Kč.")
    else:
        print("Chybný formát telefonního čísla.")


if __name__ == "__main__":
    main()