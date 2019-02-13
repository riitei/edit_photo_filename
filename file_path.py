import os
import time
from os import listdir
from os.path import isfile, isdir, join
from read_exif_time import ExifTime


class Path:

    def search_file_path(self, path):
        files = listdir(path)
        # 以迴圈處理
        for f in files:
            # 產生檔案的絕對路徑
            fullpath = join(path, f)
            # 判斷目錄
            if isdir(fullpath):
                Path().search_file_path(fullpath)
            else:
                if (os.path.splitext(f)[-1] == ".JPG"):
                    # 使用時間當做檔名
                    photo_time = ExifTime().name_time(fullpath)
                    old_name = fullpath

                    try:
                        new_name = join(path, photo_time + '_Sony.JPG')
                        # 更換檔案名稱
                        print('old_path=> %s' % old_name)
                        print('new_path=> %s' % new_name)
                        os.rename(old_name, new_name)
                    except:
                        new_name = join(path, photo_time + "_" + str(round(time.time() * 1000)) + '_Sony.JPG')
                        print('__=> %s' % new_name)
                        os.rename(old_name, new_name)

            print('----------------------------')


if __name__ == '__main__':
    # mypath = 'C:/iPhone X'
    mypath = 'c:\DCIM'
    p = Path()
    p.search_file_path(join(mypath))
