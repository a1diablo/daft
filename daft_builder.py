from daftlistings import Daft, RentType

daft = Daft()
daft.set_listing_type(RentType.APARTMENT_TO_SHARE)
listings = daft.search(fetch_all=False)

dataset = ''
for listing in listings:
    dataset += f'{listing.formalised_address.replace(",", " ")}, {listing.price}, {listing.description.replace(",", " ")}\n'

with open('dataset.csv', 'w+') as f:
    f.write(dataset)
