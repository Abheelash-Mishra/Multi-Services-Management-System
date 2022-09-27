import mysql.connector

def help():
    print("""
              Type 1 to All Available Services
              Type 2 to Search for a Specific Service
              """)

def show():
    def all_help():
        print("""
                 Type 1 to View all Available services in Computer Service
                 Type 2 to View all Available Services in catering
                 Type 3 to View all Available Services in Furniture
                 Type 4 to View all Available Services in construction
                 Type 5 to Roll back to main menu
                 Type 6 to View Help Menu 
                 """)

    def cs():
        cur.execute("select * from comp_serv")
        data = cur.fetchall()
        for content in data:
            print(content)

    def restaurant():
        cur.execute("select * from catering")
        data = cur.fetchall()
        for content in data:
            print(content)

    def furni():
        cur.execute("select * from furni_traders")
        data = cur.fetchall()
        for content in data:
            print(content)
    def const():
        cur.execute("select * from construction")
        data = cur.fetchall()
        for content in data:
            print(content)

    error_count = -1
    if error_count == -1 or error_count == 2:
        all_help()
    in1 = int(input("Show all service listing in: "))
    if in1 == 1:
        cs()
    elif in1 == 2:
        restaurant()
    elif in1 == 3:
        furni()
    elif in1 == 4:
        const()
    elif in1 == 5:
        init()
    elif in1 == 6:
        all_help()
    else:
        print("Enter a Valid Option")
        error_count += 1
        show()


def search():
    in2 = input("Enter Your Search parameter: ")
    in2.lower()
    query = in2.split()

    #Global DataSets
    ds2 = ["rating", "star", "best", "quality"]
    ds3 = ["chennai", "mumbai", "bombay", "banglore", "delhi", "bengal"]

    #Global Variables:
    global area
    area = ""
    global rating
    global exe
    exe = ""


    # Computer Search Matches and related Datasets
    ds1 = ["computer", "comp", "repair", "service"]

    # Computer Related Flags
    computer_service = 0
    cs_rating = [0, 0]
    cs_location_flag = 0
    cs_type_flag = 0
    cs_types = ["desktop", 'laptop', 'comp_acc']
    cs_type = ""


    # Furniture Data Sets:
    ds4 = ["wood", "furniture", "furnitures", "table", "cupboard", "cabinets"]

    #Furniture Flags
    furniture = 0
    furniture_rating = [0, 0]
    furniture_location_flag = 0
    furniture_type_flag = 0
    furniture_types = ["indoor", "outdoor"]
    furniture_type = ""


    # Construction Data Sets
    ds5 = ["construction", "building", "build","houses", "homes", "home", "homes","factory", "factories", "industry", "industrial","commercial","office","mall","theater","complex","shop"]
    # Construction Flags
    construction = 0
    construction_rating = [0, 0]
    construction_location_flag = 0
    construction_type_flag = 0
    construction_types = [["houses", "homes", "home", "homes"], ["factory", "factories", "industry", "industrial"],["commercial","office","mall","theater","complex","shop"]]
    construction_type = ""


    # Caterers Data Sets:
    ds6 = ["food","eat","delivery","swiggy","zomato","ubereats"]

    # Caterers Flags
    catering = 0
    catering_rating = [0, 0]
    catering_location_flag = 0
    catering_type_flag = 0
    catering_types = ["nonveg", "veg"]
    catering_type = ""

    # Traverse
    for term in query:

        # Computer Related
        if term in ds1:
            computer_service += 1
        # Check if rating is included in search parameters
        if term in ds2:
            computer_service += 1
            cs_rating[0] += 1
            # Check if rating number is included in search parameter
            if term == ds2[1]:
                location = int(query.index(term))
                for index in range(-2, 3):
                    try:
                        rating = int(query[location + index])
                        cs_rating[1] = rating
                        cs_rating[0] += 1

                    except:
                        pass
        # Check if location is included in search parameter
        if term in ds3:
            area += term
            cs_location_flag += 1

        # Check if Type is included in search parameter
        if term in cs_types:
            cs_type += term
            cs_type_flag += 1

        #################################

        # Furniture Related

        # Check if search is related to furniture
        if term in ds4:
            furniture += 1

        # Check if rating is included in search parameters
        if term in ds2:
            furniture += 1
            furniture_rating[0] += 1
            # Check if rating number is included in search parameter
            if term == ds2[1]:
                location = int(query.index(term))
                for index in range(-2, 3):
                    try:
                        rating = int(query[location + index])
                        furniture_rating[1] = rating
                        furniture_rating[0] += 1
                    except:
                        pass
        # Check if location is included in search parameter
        if term in ds3:
            area += term
            furniture_location_flag += 1
        # Check if type is included in search parameter
        if term in furniture_types:
            furniture_type += term
            furniture_type_flag += 1


        #################################
        # Construction Related

        # Check if search is related to construction
        if term in ds5:
            construction += 1

        # Check if rating is included in search parameters
        if term in ds2:
            construction += 1
            construction_rating[0] += 1
            # Check if rating number is included in search parameter
            if term == ds2[1]:
                location = int(query.index(term))
                for index in range(-2, 3):
                    try:
                        rating = int(query[location + index])
                        construction_rating[1] = rating
                        construction_rating[0] += 1
                    except:
                        pass
        # Check if location is included in search parameter
        if term in ds3:
            area += term
            construction_location_flag += 1
        # Check if type is included in search parameter
        if term in construction_types[0]:
            construction_type += "houses"
            construction_type_flag += 1
        elif term in construction_types[1]:
            construction_type += "industry"
            construction_type_flag += 1
        elif term in construction_types[2]:
            construction_type += "com_build"
            construction_type_flag += 1


        #################################
        # Catering Related

        # Check if search is related to catering
        if term in ds4:
                catering += 1

        # Check if rating is included in search parameters
        if term in ds2:
            catering += 1
            catering_rating[0] += 1
            # Check if rating number is included in search parameter
            if term == ds2[1]:
                location = int(query.index(term))
                for index in range(-2, 3):
                    try:
                        rating = int(query[location + index])
                        catering_rating[1] = rating
                        catering_rating[0] += 1
                    except:
                        pass
        # Check if location is included in search parameter
        if term in ds3:
            area += term
            catering_location_flag += 1
        # Check if type is included in search parameter
        if term in catering_types:
            catering_type += term
            catering_type_flag += 1


    # Query for cs
    if computer_service >= 1:
        exe += "select * from comp_serv"
        if cs_rating[0] >= 1 or cs_location_flag >= 1 or cs_type_flag >= 1:
            exe += " where"
            exe_len = len(exe.split()) - 1
            point = exe.split().index('where')
            if exe_len == point and cs_type_flag >= 1 and cs_type != "":
                exe += " type = '%s'" % (cs_type)
                exe_len = len(exe.split()) - 1
            elif exe_len == point and cs_type_flag >= 1 and cs_type != "":
                exe += " and type = '%s'" % cs_type
                exe_len = len(exe.split()) - 1
            if exe_len == point and cs_rating[0] >= 1 and cs_rating[1] >= 1:
                exe += " ratings = %s" % (cs_rating[1])
                exe_len = len(exe.split()) - 1
            elif exe_len != point and cs_rating[0] >= 1 and cs_rating[1] >= 1:
                exe += " and ratings = %s" % cs_rating[1]
                exe_len = len(exe.split()) - 1
            if exe_len == point and cs_location_flag >= 1:
                exe += " location = '%s'" % area
                exe_len = len(exe.split()) - 1
            elif exe_len != point and cs_location_flag >= 1:
                exe += " and location = '%s'" % area
                exe_len = len(exe.split()) - 1
            if exe_len == point and cs_rating[0] >= 1 and cs_rating[1] is None:
                exe = exe[:-6:] + " order by rating desc"
                exe_len = len(exe.split()) - 1
        cur.execute(exe)
        data = cur.fetchall()
        for content in data:
            print(content)

    # Reject Statement
    if computer_service == 0 and cs_rating == [0, None]:
        print("Enter a Valid Search Parameter")
        search()

    # Query for furniture
    if furniture >= 1:
        exe += "select * from furni_traders"
        if furniture_rating[0] >= 1 or furniture_location_flag >= 1 or furniture_type_flag >= 1:
            exe += " where"
            exe_len = len(exe.split()) - 1
            point = exe.split().index('where')
            if exe_len == point and furniture_type_flag >= 1 and furniture_type != "":
                exe += " type = '%s'" % furniture_type
                exe_len = len(exe.split()) - 1
            elif exe_len == point and furniture_type_flag >= 1 and furniture_type != "":
                exe += " and type = '%s'" % furniture_type
                exe_len = len(exe.split()) - 1
            if exe_len == point and furniture_rating[0] >= 1 and furniture_rating[1] >= 1:
                exe += " ratings = %s" % (furniture_rating[1])
                exe_len = len(exe.split()) - 1
            elif exe_len != point and furniture_rating[0] >= 1 and furniture_rating[1] >= 1:
                exe += " and ratings = %s" % furniture_rating[1]
                exe_len = len(exe.split()) - 1
            if exe_len == point and furniture_location_flag >= 1:
                exe += " location = '%s'" % area
                exe_len = len(exe.split()) - 1
            elif exe_len != point and furniture_location_flag >= 1:
                exe += " and location = '%s'" % area
                exe_len = len(exe.split()) - 1
            if exe_len == point and furniture_rating[0] >= 1 and furniture_rating[1] is None:
                exe = exe[:-6:] + " order by rating desc"
                exe_len = len(exe.split()) - 1
        cur.execute(exe)
        data = cur.fetchall()
        for content in data:
            print(content)

    # Query for construction
    if construction >= 1:
        exe += "select * from construction"
        if construction_rating[0] >= 1 or construction_location_flag >= 1 or construction_type_flag >= 1:
            exe += " where"
            exe_len = len(exe.split()) - 1
            point = exe.split().index('where')
            if exe_len == point and construction_type_flag >= 1 and construction_type != "":
                exe += " type = '%s'" % construction_type
                exe_len = len(exe.split()) - 1
            elif exe_len == point and construction_type_flag >= 1 and construction_type != "":
                exe += " and type = '%s'" % construction_type
                exe_len = len(exe.split()) - 1
            if exe_len == point and construction_rating[0] >= 1 and cs_rating[1] >= 1:
                exe += " ratings = %s" % (construction_rating[1])
                exe_len = len(exe.split()) - 1
            elif exe_len != point and construction_rating[0] >= 1 and construction_rating[1] >= 1:
                exe += " and ratings = %s" % construction_rating[1]
                exe_len = len(exe.split()) - 1
            if exe_len == point and construction_location_flag >= 1:
                exe += " location = '%s'" % area
                exe_len = len(exe.split()) - 1
            elif exe_len != point and construction_location_flag >= 1:
                exe += " and location = '%s'" % area
                exe_len = len(exe.split()) - 1
            if exe_len == point and construction_rating[0] >= 1 and construction_rating[1] is None:
                exe = exe[:-6:] + " order by rating desc"
                exe_len = len(exe.split()) - 1
        cur.execute(exe)
        data = cur.fetchall()
        for content in data:
            print(content)

    # Query for Catering
    if catering >= 1:
        exe += "select * from catering"
        if catering_rating[0] >= 1 or catering_location_flag >= 1 or catering_type_flag >= 1:
            exe += " where"
            exe_len = len(exe.split()) - 1
            point = exe.split().index('where')
            if exe_len == point and catering_type_flag >= 1 and catering_type != "":
                exe += " type = '%s'" % (catering_type)
                exe_len = len(exe.split()) - 1
            elif exe_len == point and catering_type_flag >= 1 and catering_type != "":
                exe += " and type = '%s'" % catering_type
                exe_len = len(exe.split()) - 1
            if exe_len == point and catering_rating[0] >= 1 and catering_rating[1] >= 1:
                exe += " ratings = %s" % (catering_rating[1])
                exe_len = len(exe.split()) - 1
            elif exe_len != point and catering_rating[0] >= 1 and catering_rating[1] >= 1:
                exe += " and ratings = %s" % catering_rating[1]
                exe_len = len(exe.split()) - 1
            if exe_len == point and catering_location_flag >= 1:
                exe += " location = '%s'" % area
                exe_len = len(exe.split()) - 1
            elif exe_len != point and catering_location_flag >= 1:
                exe += " and location = '%s'" % area
                exe_len = len(exe.split()) - 1
            if exe_len == point and catering_rating[0] >= 1 and catering_rating[1] is None:
                exe = exe[:-6:] + " order by rating desc"
                exe_len = len(exe.split()) - 1
        cur.execute(exe)
        data = cur.fetchall()
        for content in data:
            print(content)

def init():
    while True:
        print("Main Menu")
        in1 = int(input("Enter Your choice: "))
        if in1 == 1:
            show()
        elif in1 == 2:
            search()
        else:
            print("Enter a valid Option")
            init()

username=input("Enter your MySQL username: ")
password=input("Enter your MySQL password: ")
database=input("Enter your MySQL database: ")
try:
    db = mysql.connector.connect(host="localhost", user=username, passwd=password, database=database)
    cur = db.cursor()
    availability = 1
except:
    print("An Error Occurred - Try Turning on The MYSQL80 Service")
    availability = 0
if availability == 1:
    init()