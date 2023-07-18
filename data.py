# get the backup folder paths from environment variable

sql_host = os.environ.get('SQL_HOST')
if sql_host is None or not sql_host:
    sql_host = 'localhost'

# connect to the MySQL database

def dbconnect():
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="password",
        database="fca")


def get_log(start, end):
    db = dbconnect()
    cursor = db.cursor()

    start_date = None
    end_date = None

    end += "23:59:59"

    if start_date is not None and end_date is not None and end_date < start_date:
        raise ValueError("Start Date is < End Date")
