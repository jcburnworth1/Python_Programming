## Veneer - CodeAcademy
##### Begin classes #####
## Art class for storing works of art and details
class Art():
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return """{artist}. "{title}". {year}, {medium}, {owner}, {location}""".format(artist = self.artist,
                                                                                       title = self.title,
                                                                                       year = self.year,
                                                                                       medium = self.medium,
                                                                                       owner = self.owner.name,
                                                                                       location = self.owner.location)

## Marketplace class for listing, selling, buying, etc.
class Marketplace():
    def __init__(self):
        self.listings = []

    ## Add a new art listing to the marketplace
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    ## Remove a sold art listing from the marketplace
    def remove_listing(self, remove_listing):
        self.listings.remove(remove_listing)

    ## Show current art available for sale
    def show_listings(self):
        print("Current Listings for Veneer: ")
        for listing in self.listings:
            print(listing)

## Create the main marketplace for the art
veneer = Marketplace()

## Print out current listing - Will return nothing
print(veneer.show_listings())

## Client class for buyers and sellers
class Client():
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.location = location
        self.is_museum = is_museum
        self.wallet = wallet

    def __repr__(self):
        return """Client Name: {name}\nLocation: {location}\nMuseum: {museum}""".format(name = self.name,
                                                                                        location = self.location,
                                                                                        museum = self.is_museum)

    ## Sell artwork if seller is the owner
    def sell_artwork(self, artwork, price):
        ## Check ownership
        if artwork.owner.name == self.name:
            ## Add new listing to the marketplace
            new_listing = Listing(artwork, price, self.name)
            veneer.add_listing(new_listing)

    ## Buy artwork is art is for sale and owner is not buyer
    def buy_artwork(self, artwork):
        ## Check ownership
        if artwork.owner.name != self.name:
            ## Check that artwork is actually for sale
            for listing in veneer.listings:
                ## Save off listing for later removal
                if listing.art == artwork:
                    ## Capture listing information for removal after sale
                    art_listing = listing

                    ## Complete sale if buyer has enough funds
                    if self.wallet >= listing.price:
                        ## Exchange the money
                        ## Add to the seller's account
                        artwork.owner.wallet += listing.price

                        ## Remove from the buyer's accounts
                        self.wallet -= listing.price

                        ## Change the owner
                        artwork.owner = self

                        ## Remove the listing from marketplace
                        veneer.remove_listing(art_listing)
                    else:
                        print("Insufficient funds for transactions.")

class Listing():
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{art}: {price}".format(art = self.art, price = self.price)
##### End classes #####

## Create client, Edytta Halprit - Seller
edytta = Client('Edytta Halprit', 'Private Collector', False, 10000000)

## Create client, The MOMA - Buyer
moma = Client('The MOMA', 'New York', True, 100000000)

## Create Artwork - Girl with Mandolin - Owner is Edytta Halprit
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)',
                         'oil on canvas', 1910, edytta)

## Print girl_with_mandolin
print(girl_with_mandolin)

## List Girl with Mandolin for sale
edytta.sell_artwork(girl_with_mandolin, 6000000)

## Check Girl with Mandolin is for sale on veneer marketplace
veneer.show_listings()

## Check account balances
## Seller
print("Seller, {seller}, current waller: {wallet}".format(seller = edytta.name,
                                                          wallet = edytta.wallet))

## Buyer
print("Buyer, {buyer}, current waller: {wallet}".format(buyer = moma.name,
                                                        wallet = moma.wallet))

## Process the purchase
moma.buy_artwork(girl_with_mandolin)

## Check to make sure proper steps have been taken to change owner, remove from listing, and exchanged money
print(girl_with_mandolin)
print(veneer.show_listings())
## Seller
print("Seller, {seller}, current waller: {wallet}".format(seller = edytta.name,
                                                          wallet = edytta.wallet))

## Buyer
print("Buyer, {buyer}, current waller: {wallet}".format(buyer = moma.name,
                                                        wallet = moma.wallet))