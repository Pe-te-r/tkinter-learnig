import psycopg2
import tabulate
import pyperclip as clip
import argparse
from cryptography.fernet import Fernet, InvalidToken


class Encryption:
    def __init__(self, secret, key="Wi9gXP2pznwrmiab1vqYFY7i4O_vKtLHNoWwpD_Uiwo="):
        self.key = (key + secret).encode("utf-8")
        self.cipher = Fernet(self.key)

    def encrypting(self, data):
        self.data = data.encode("utf-8")
        self.encrypted = self.cipher.encrypt(self.data)
        return self.encrypted.decode("utf-8")

    def decrypting(self, data):
        try:
            self.data = data.encode("utf-8")
            self.decrypted = self.cipher.decrypt(self.data)
            return self.decrypted.decode("utf-8")
        except InvalidToken:
            pass


class Database:
    def __init__(
        self, dbname, user="phantom", password="phantom8526", host="localhost"
    ) -> None:
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host
        )
        self.cur = self.conn.cursor()
        self.encryptor = Encryption("peter")

    def fetchAll(self, table="passwords"):
          self.cur.execute(f"SELECT name,passwords FROM {table}")
          data = self.cur.fetchall()

          new_list = []
          for value in data:
            value = list(value)
            value[1] = self.encryptor.decrypting(value[1])
            value = tuple(value)
            new_list.append(value)
#         new_list = []
#         for value in data:
#             value = list(value)
#             value[1] = self.encryptor.decrypting(value[1])
#             value = tuple(value)
#             new_list.append(value)
#         table = tabulate.tabulate(
#             new_list, headers=["url", "password"], tablefmt="grid"
#         )
          return new_list

    def count(self, table="passwords"):
        self.cur.execute(f"SELECT name,passwords FROM {table}")
        data = self.cur.fetchall()
        return len(data)

    def insertData(self, name, password):
        try:
            encryptedPassword = self.encryptor.encrypting(password)
            self.cur.execute(
                "insert into passwords (name,passwords) values (%s, %s)",
                (name, encryptedPassword),
            )
            self.conn.commit()
            print("one row inserted")
        except Exception as e:
            print(f"error occured. Row not added {e}")
            self.conn.rollback()

    def fetchOne(self, name, table="passwords"):
        sql = f"select name, passwords from {table} where name=%s"
        self.cur.execute(sql, (name,))
        data = self.cur.fetchone()
        if not data:
            return None
        data = list(data)
        data[1] = self.encryptor.decrypting(data[1])
        return data

    def updateData(self, changeThis, changeTo, table="passwords", what="name"):
        try:
            self.cur.execute(
                f"update {table} set {what}=%s where {what}=%s", (changeTo, changeThis)
            )
            self.conn.commit()
            print("one item updated")
        except Exception:
            self.conn.rollback()

    def deleteData(self, where, what="name", table="passwords"):
        try:
            self.cur.execute(f"delete from {table} where {what}=%s", (where,))
            self.conn.commit()
            print("one row deleted")

        except Exception:
            print("no such hostname(error occured)")
            self.conn.rollback()

    def close_connections(self):
        self.cur.close()
        self.conn.close()


# def main():
#     database = Database("passwords")

#     parser = argparse.ArgumentParser(description="Password manager")

#     group = parser.add_mutually_exclusive_group()

#     group.add_argument("--add", action="store_true", help="Add an entry.")
#     group.add_argument("--print", action="store_true", help="Print all entries.")
#     group.add_argument(
#         "--delete", action="store_true", help="Delete an entry by hostname."
#     )
#     group.add_argument(
#         "--update",
#         action="store_true",
#         help="update details from the database to new details",
#     )
#     group.add_argument(
#         "--copy", action="store_true", help="copy passwords to system clipboard"
#     )

#     parser.add_argument("-host", "--hostname", help="The hostname or URL.")
#     parser.add_argument(
#         "-pass", "--password", help="The password (required for adding entries)."
#     )
#     parser.add_argument(
#         "-value", "--new_value", help="Stores the value that will be changed to)."
#     )

#     args = parser.parse_args()

#     hostname = args.hostname
#     password = args.password
#     new_value = args.new_value

#     if args.add:
#         if not args.password:
#             raise ValueError("Password is required for adding entries.")

#         database.insertData(hostname.strip(), password.strip())

#     elif args.print:
#         print(database.fetchAll())
#     elif args.delete:
#         database.deleteData(hostname.strip())
#     elif args.update:
#         database.updateData(hostname.strip(), new_value.strip())
#     elif args.copy:
#         data = database.fetchOne(hostname.strip())
#         if data is None:
#             print("deosn't exists")
#             exit()
#         clip.copy(data[1])
#         print("copied to clipboard")
#     else:
#         parser.error("Invalid command. Please use -a, --print, or --delete.")

#     database.close_connections()
