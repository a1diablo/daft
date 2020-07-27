from daftlistings import Daft

daft = Daft()
listings = daft.search(fetch_all=False)

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
