import datetime
from PIL import Image
import piexif
from os.path import join


#
#
# path = '/Users/riitei/photo/DSC07410.JPG'
#
#
# img = Image.open(path)
# exif = piexif.load(img.info['exif'])
# print(exif['0th'][306])
# print(exif['Exif'][36867])
# print(exif['Exif'][36868])

# photo_time = str(exif['0th'][306])[2:-1]
# tt = datetime.datetime.strptime(photo_time,"%Y:%m:%d %H:%M:%S")
# new = tt+datetime.timedelta(hours=1)
#
# new_3 = new.strftime("%Y%m%d%H%M%S")
#
# print(new_3)
#

class ExifTime:
    def name_time(self, path):
        # read exif info
        try:
            img = Image.open(path)
            exif = piexif.load(img.info['exif'])
            # read exif time
            exif_time = str(exif['Exif'][36868])[2:-1]
            photo_time = datetime.datetime.strptime(exif_time, "%Y:%m:%d %H:%M:%S")
            new_name = photo_time.strftime("%Y%m%d%H%M%S")
        except:
            new_name = 'No_EXIF'

        return str(new_name)


if __name__ == '__main__':
    path = join('C:/temp', '连拍快照', '20181127_IMG_2879.JPG')
    t = ExifTime().name_time(path)
