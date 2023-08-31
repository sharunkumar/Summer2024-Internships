import json
from datetime import datetime
import os
import util
import re


def main():

    listings = util.getListingsFromJSON()

    util.checkSchema(listings)
    util.sortListings(listings)

    listings = util.customFilter(listings)

    summer_2024_listings = util.filterSummer(listings)
    util.embedTable(summer_2024_listings, "README.md")

    offseason_listings = util.filterOffSeason(listings)
    util.embedTable(offseason_listings, "README-Off-Season.md", offSeason=True)

if __name__ == "__main__":
    main()
