from hashlib import md5,sha1
import os

def md5_check(file_path):
    md5_value=md5()
    sha1_value=sha1()
    md5_str=''
    sha1_str=''
    with open(file_path,'rb') as f:
        while True:
            data=f.read(1024)
            if not data:
                break
            md5_value.update(data)
            sha1_value.update(data)
            md5_str =md5_value.hexdigest()
            sha1_str=sha1_value.hexdigest()
    return md5_str,sha1_str


def copy_file(file_path):
    #先复制文件，避免源文件损坏,存放同级目录下
    new_file_name=os.path.split(file_path)[0]+'\\'+'copy_'+os.path.split(file_path)[1]
    print(new_file_name)
    # fw = open(new_file_name, 'w')
    # flag=True
    try:
        with open(file_path,'rb') as fr,open(new_file_name, 'wb') as fw:
            while True:
                data=fr.read(1024)
                if not data:
                    break
                fw.write(data)
        print('复制完毕')
        flag=True
        return flag,new_file_name
    except Exception:
        print('读写失败 ')
        flag=False
        return flag,new_file_name

def change_md5(file_path):
    flag,new_file_name=copy_file(file_path)
    if flag:
        m=open(new_file_name,'a')
        m.write('@@@@')
        m.close()
        md5_str, sha1_str=md5_check(new_file_name)
        return new_file_name,md5_str,sha1_str
    else:
        print('复制失败')


def mycopy(old_file, new_file):
    """此函数的功以实现复制文件
    src_file : 源文件名
    dst_file : 目标文件名
    """
    try:
        with open(file=old_file,mode= "rb") as fr,open(file=new_file,mode= 'wb') as fw:  # fr读文件
            while True:
                data = fr.read(4096)
                if not data:
                    break
                fw.write(data)
    except OSError as s:
        print("打开读文件失败")
        print(s.args)
        return False
    except:
        print("可能U盘被拔出...")
    return True

# s = r'D:\音乐\说散就散.mp3'
# d = r'D:\音乐\c说散就散.mp3'
# if mycopy(s, d):
#     print("复制文件成功")
# else:
#     print("复制文件失败")

