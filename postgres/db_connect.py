import psycopg2


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="postgres",
            user="postgres",
            port=5432,
            password="password")
        while True:
            print("conn")
    except Exception as ex:
        print(ex)
