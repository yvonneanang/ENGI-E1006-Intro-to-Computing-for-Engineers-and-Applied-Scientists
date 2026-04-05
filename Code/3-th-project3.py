# Take Home 3 - Project 3
#By Yvonne Anang

def read_markets(filename):
    
    read_file = open(filename, "r")
    zipcodes_to_list_of_farmers_market_tuples = {}    
    towns_to_sets_of_zipcodes = {}
    
    for line in read_file:
        list_of_farmers_market = line.strip().split("#")
        farmers_market = tuple(list_of_farmers_market[:5])
    #creates dictionary of zipcodes_to_list_of_farmers_market_tuples
        zipcode = farmers_market[4]
        list_of_farmers_market_tuples = []
        if zipcode in zipcodes_to_list_of_farmers_market_tuples:
            zipcodes_to_list_of_farmers_market_tuples[zipcode].append(farmers_market)
        else:
            list_of_farmers_market_tuples.append(farmers_market)
            zipcodes_to_list_of_farmers_market_tuples[zipcode] = list_of_farmers_market_tuples
        
    #creates dictionary of towns_to_sets_of_zipcodes
        town = farmers_market[3]
        sets_of_zipcodes = set()
        if town in towns_to_sets_of_zipcodes:
            towns_to_sets_of_zipcodes[town].add(zipcode)
        else:
            sets_of_zipcodes.add(zipcode)
            towns_to_sets_of_zipcodes[town] = sets_of_zipcodes
    
    return zipcodes_to_list_of_farmers_market_tuples, towns_to_sets_of_zipcodes 

    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """


def print_market(market):
    name_of_market = market[1]
    street_address = market[2]
    town = market[3]
    state_and_zipcode = market[0] + " " + market[4]
    return "{}\n{}\n{}, {}\n". format(name_of_market, street_address, town, state_and_zipcode)
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """


if __name__ == "__main__":
    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        while True:
            user_input = input("Please enter a zip code or a town name:>>>")
            if user_input == "quit":
                break
            elif user_input.isdigit() == True and user_input in zip_to_market:
                counter = 0
                while counter < len(zip_to_market[user_input]):
                    print (print_market(zip_to_market[user_input][counter]))
                    counter += 1
            elif user_input in town_to_zips:
                for zipcode in town_to_zips[user_input]:
                    for market_tuple in zip_to_market[zipcode]:
                        if market_tuple[3] == user_input:
                            print (print_market(market_tuple))
            else:
                print ("Not found.")
    
    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
        
    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").
