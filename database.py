import MySQLdb as dbc
import MySQLdb.cursors
from config import Config

def get_connection():
    return dbc.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        passwd=Config.MYSQL_PASSWORD,
        db=Config.MYSQL_DATABASE,
        charset="utf8mb4",
        cursorclass=MySQLdb.cursors.DictCursor,
        autocommit=False,
        ssl={"ca": 
                Config.MYSQL_SSL_CA
        },
        ssl_mode="VERIFY_CA"
    )
