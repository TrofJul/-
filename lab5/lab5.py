import MySQLdb


class Connection:
    def __init__(self, user, password, db, host="localhost"):
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Task:
    def __init__(self, db_connection, title, subject, description):
        self.db_connection = db_connection.connection
        self.title = title
        self.subject = subject
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO tasks (title, subject, description) VALUES(%s, %s, %s);",
                  (self.title, self.subject, self.description))
        self.db_connection.commit()
        c.execute("SELECT * FROM tasks;")
        res = c.fetchall()
        for r in res:
            print(r)

        c.close()


con = Connection("my_user", "my_password", "my_database")
with con:
    task = Task(con, 'Задание2', 'Учеба', 'Сделать еще одно задание')
    task.save()



