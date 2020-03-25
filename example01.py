import pymysql


def main():
    conn = pymysql.connect(host='120.24.22.101', port=3306, user='root', passwd='lug@r', db='school', charset='utf8')
    print(conn)

if __name__ == '__main__':
    main()