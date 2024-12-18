username = "nor"
password = "asd123asD"
server = "pol.database.windows.net"
database = "movie-db"
port = 1433
conn_string = f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+18+for+SQL+Server"