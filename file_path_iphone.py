import os
import time
from os import listdir
from os.path import isfile, isdir, join
from read_exif_time import ExifTime


class Path:

    def search_file_path(self, dir_path):
        files = listdir(dir_path)
        # 以迴圈處理
        for f in files:
            # 產生檔案的絕對路徑
            path = join(dir_path, f)
            # 判斷目錄
            if isdir(path):
                Path().search_file_path(path)
            else:
                # if (os.path.splitext(f)[-1] == ".JPG"):
                # 使用時間當做檔名

                file_type = os.path.splitext(f)[-1]
                # 使用 EXIF 時間為檔案名稱
                new_name = ExifTime().name_time(dir_path) + file_type
                old_name_path = path  # 舊路徑,是檔案路徑
                if new_name == 'No_EXIF' + file_type:
                    # 沒 exif_time
                    # 文件的修改时间
                    create_file_timestamp = os.stat(path).st_mtime
                    localtime = time.localtime(create_file_timestamp)
                    new_name = time.strftime("%Y%m%d%H%M%S", localtime)
                    print('no => %s ' % new_name)

                try:
                    new_name_path = join(dir_path, new_name  + file_type)
                    os.rename(old_name_path, new_name_path)
                except:
                    # 處理檔名重複
                    new_name = new_name + "_" + str(round(time.time() * 1000))
                    new_name_path = join(dir_path, new_name  + file_type)
                    os.rename(old_name_path, new_name_path)
                print('old => %s' % old_name_path)
                print('new => %s' % new_name_path)
                print('----------------------------')


if __name__ == '__main__':
    mypath = 'C:/DCIM'
    p = Path()
    p.search_file_path(mypath)
