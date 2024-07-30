from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

print(get_mask_card_number(str(input())))
print(get_mask_account(str(input())))
print(mask_account_card(str(input())))