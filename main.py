from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(str(input())))
print(get_mask_account(str(input())))
