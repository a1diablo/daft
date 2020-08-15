from daftlistings import Daft, RentType
import os

daft = Daft()
daft.set_listing_type(RentType.APARTMENT_TO_SHARE)
listings = daft.search(fetch_all=False)

os.remove('dataset.csv')
with open('dataset.csv', 'a+', encoding='utf-8') as f:
    for i, listing in enumerate(listings):
        print(f'Listing {i + 1}/{len(listings)}')
        if listing.price:
            trimmed_description = listing.description.replace(
                ",", " ").replace("\n", " ")if listing.description else ""
            f.write(
                f'{listing.formalised_address.replace(",", " ")}, {listing.price}, {trimmed_description}\n')
