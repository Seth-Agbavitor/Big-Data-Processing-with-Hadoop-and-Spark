from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol

class LiqourSale(MRJob):
    OUTPUT_PROTOCOL = TextValueProtocol


    def mapper(self, _, line):
        # Split the line by tab delimiter
        fields = line.split('\t')
        # Extract the desired fields
        Date = fields[0]
        Store = fields[1]
        Address = fields[2]
        City = fields[3]
        Zip = fields[4]
        CountyNumber = fields[5]
        County = fields[6]
        Category = fields[7]
        CategoryName = fields[8]
        VendorNumber = fields[9]
        VendorName = fields[10]
        ItemNumber = fields[11]
        ItemDescription = fields[12]
        StateBottleCost = fields[13]
        StateBottleRetail = fields[14]
        BottlesSold = fields[15]
        SaleDollars = fields[16]
        VolumeSoldLiteres = fields[17]
        VolumeSoldGallons = fields[18]
       
        # Emit the extracted fields as key-value pairs
        yield None, (Date, Store, Address, City, Zip, CountyNumber, County, Category, CategoryName, VendorNumber, VendorName, ItemNumber, ItemDescription, StateBottleCost, StateBottleRetail, BottlesSold, SaleDollars, VolumeSoldLiteres, VolumeSoldGallons)

    def reducer(self, _, values):
       
        # Skip the second row
        next(values)
        
        # Emit the values separated by commas
        for fields in values:
            yield None, ','.join(fields)

if __name__ == '__main__':
    LiqourSale.run()
