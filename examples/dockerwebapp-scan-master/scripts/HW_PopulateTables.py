"""
Populate tables with random data
sudo pip install barnum - for random data
"""
import barnum
import re
import random

# Create random data for manufacturer - Ready
def createManufacturerData(numberValues, lastIndex):
    valuesList = list()
    phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    for i in range(numberValues):
        address = barnum.create_city_state_zip()
        phone = phonePattern.search(barnum.create_phone()).groups()
        # Create list with all the values for the MANUFACTURER table
        valuesList.append([
            lastIndex + i,                      # MAN_CODE attribute
            barnum.create_company_name(),       # MAN_COMPANY
            barnum.create_street(),             # MAN_STREET
            address[1],                         # MAN_CITY
            address[2],                         # MAN_STATE
            int(address[0]),                         # MAN_ZIP
            int(phone[0]),                           # MAN_AREACODE
            phone[1]+"-"+phone[2],              # MAN_PHONE
            ((barnum.create_cc_number())[1])[0] # MAN_ACCNUM
        ])
    return valuesList

# Create random data for brand
def createBrandData(numberValues, lastIndex, lastManIndex):
    availableBrands = ['San Juan Hollyday', 'Yabucoa Bay', 'Coamo Caverns', 'Arecibo Sunshine', 'Grey Humacao']
    availableLevels = ['premium', 'mid-level', 'entry-level']
    valuesList = list()
    for i in range(numberValues):
        valuesList.append([
            lastIndex + i,                        # BRAND_ID
            availableBrands[random.randint(0,4)], # BRAND_NAME
            availableLevels[random.randint(0,2)], # BRAND_LEVEL
            random.randint(1,lastManIndex)        # MAN_CODE
        ])
    return valuesList

# Create random data for MODEL
def createModelData(numberValues, lastIndex, lastBrandIndex):
    availableLevels = ['premium', 'mid-level', 'entry-level']
    valuesList = list()
    for i in range(numberValues):
        valuesList.append([
            lastIndex + i,                           # MODEL_NUM
            random.randint(1,20),                    # MODEL_JETS
            random.randint(1,10),                    # MODEL_MOTORS
            random.randint(50,200),                  # MODEL_HP
            round(random.uniform(200.00,400.00), 2), # MODEL_SRP
            round(random.uniform(200.00,400.00), 2), # MODEL_HWRP
            round(random.uniform(100.00,200.00), 2), # MODEL_WEIGTH
            round(random.uniform(30.00,70.00), 2),   # MODEL_WATCAP
            random.randint(1,10),                    # MODEL_SEATCAP
            random.randint(1,lastBrandIndex),        # BRAND_ID
        ])
    return valuesList

def saveScript(name,sql):
    file = open(name,'w+')
    for i in sql:
        file.write(i+'\n')
    file.close()

if __name__ == "__main__":

    """
    Global variables
    """
    size           = 60 # how many rows do you want to add
    lastIndexMan   = 1  # how many primary keys do you have on manufacturer table
    lastIndexBrand = 1  # how many primary keys do you have on manufacturer table
    lastIndexModel = 1  # how many primary keys do you have on manufacturer table

    """
    Call functions
    """
    val = createManufacturerData(size, lastIndexMan)
    #val = createBrandData(size, lastIndexBrand, 60)
    #val = createModelData(size, 1, 10)

    """
    Create Scripts
    """
    manufacturer = "INSERT INTO MANUFACTURER VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');"
    brand        = "INSERT INTO BRAND VALUES('%s','%s','%s','%s');"
    model        = "INSERT INTO MODEL VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"

    filename = 'InsertData_On_Manufacturer.sql'

    script = list()
    for i in val:
        script.append(manufacturer % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        #script.append(brand % (i[0],i[1],i[2],i[3]))
        #script.append(model % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))

    saveScript(filename, script)
