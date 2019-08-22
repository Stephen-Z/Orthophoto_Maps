import gdal
from PIL import Image
# import exifread
import pyexiv2

if __name__ == '__main__':
    file_path1 = './testData/20180213_064947.tiff'
    file_path2 = '../Data/DJI_0386.JPG'
    file_path3 = './20181018_160439_346.TIFF'
    file_path4 = './testData/20190619_131032_R.tif'
    file_path5 = './testData/sample dir/20190822/flir/20190822_113709_574.TIFF'

    # ## GDAL
    # hDataset = gdal.Open(file_path1, gdal.GA_ReadOnly)
    # hDriver = hDataset.GetDriver()
    # print("Driver: %s/%s" % (hDriver.ShortName, hDriver.LongName))


    # ## exifread
    # # Open image file for reading (binary mode)
    # f = open(file_path4, 'rb')
    #
    # # Return Exif tags
    # tags = exifread.process_file(f)
    #
    # for tag in tags.keys():
    #    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
    #        print("Key: %s, value %s" % (tag, tags[tag]))

    ### pyexiv2
    metadata = pyexiv2.ImageMetadata(file_path5)
    metadata.read()
    print(metadata.exif_keys)
    # print(metadata.xmp_keys)

    latitude = metadata['Exif.GPSInfo.GPSLatitude']
    latitudeValue = latitude.raw_value.split('/')
    latitudeDeg = int(latitudeValue[0])
    latitudeMin = int(latitudeValue[1].split(' ')[1])
    latitudeSec = int(latitudeValue[2].split(' ')[1]) / 1000
    lat = latitudeDeg + latitudeMin/60 + latitudeSec/3600

    longitude = metadata['Exif.GPSInfo.GPSLongitude']
    longitudeValue = longitude.raw_value.split('/')
    longitudeDeg = int(longitudeValue[0])
    longitudeMin = int(longitudeValue[1].split(' ')[1])
    longitudeSec = int(longitudeValue[2].split(' ')[1]) / 1000
    lon = longitudeDeg + longitudeMin/60 + longitudeSec/3600

    altitude = metadata['Exif.GPSInfo.GPSAltitude']
    altitudeValue = altitude.raw_value.split('/')
    alt = int(altitudeValue[0])/int(altitudeValue[1])

    focalLength = metadata['Exif.Photo.FocalLength']
    sensorWidth = metadata['Exif.Photo.FocalPlaneXResolution']  # row
    sensorWidthValue = sensorWidth.raw_value

    print('GPS info: ', lat, " ", lon, " ", alt)
    print('Focal Length: ', focalLength.value, 'mm')
    print('Sensor Width(Row): ', int(sensorWidthValue[0:5])-10000)
