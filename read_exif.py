import datetime
from PIL import Image
import piexif
from os.path import join


class Exif:

    def __init__(self, path):
        self.img = Image.open(path)

    # EXIF 相機 設備
    def device(self, exif):
        exif_device = exif['0th'][272].decode("utf-8")
        return exif_device

    # EXIF 拍照 時間
    def date_time(self, exif):
        exif_datetime = exif['Exif'][36868].decode("utf-8")
        # print(exif_datetime)
        return exif_datetime

    """   
    計算 時差
    :Args:
        date_time (datetime) 
        hours (float) = 0
    :Returns:
        update_datetime(datetime)     
    """

    def time_difference(self, date_time, hours):
        time_difference = datetime.timedelta(hours=hours)
        update_datetime = date_time + time_difference
        return update_datetime

    # 回傳 exif info
    def exif_info(self, hours=0):
        try:
            exif = piexif.load(self.img.info['exif'])
            device = self.device(exif)
            date_time = self.date_time(exif)
            # datetime_date_time is datetime Object
            # 轉型後 計算時差
            now_date_time = datetime.datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S")
            update_date_time = self.time_difference(now_date_time, hours)
            # 轉換自定格式
            date_time = datetime.datetime.strftime(update_date_time, "%Y%m%d_%H%M%S")
            return date_time + "_" + device

        except:
            return None


if __name__ == '__main__':
    path = join('C:/', 'no.PNG')
    # path = join('C:/', 'iphone.JPG')
    # path = join('C:/', 'sony.JPG')

    file_name = Exif(path).exif_info()
    if file_name != None:
        print('非空 %s' % file_name)
    else:
        print('空 %s' % file_name)
