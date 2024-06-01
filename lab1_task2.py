import redis


class Leaderboard:
    def __init__(self):
        self.server = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
        self.leaderboard = 'leaderboard'
        self.current_user = 'current_user'
        self.admin = 'admins'

    def create_user(self, username, password):
        if self.server.hexists(self.admin, username):
            print("User already exists.")
            return False
        self.server.hset(self.admin, username, password)
        print("User created successfully.")
        return True

    def login(self, username, password):
        if self.server.hget(self.admin, username) == password:
            print("Login successful.")
            self.server.set(self.current_user, username, 25)
            return True
        else:
            print("Invalid username or password.")
            return False

    def check_login(self):
        return self.server.get(self.current_user)

    def add_score(self, username, score):
        if not self.check_login():
            return False

        if not self.server.zrank(self.leaderboard, username):
            self.server.zadd(self.leaderboard, {username: score})
            print("Record added")
            return True
        else:
            print("Username is already exists")
            return False

    def remove_score(self, username):
        if not self.check_login():
            return False

        if self.server.zrank(self.leaderboard, username):
            self.server.zrem(self.leaderboard, username)
            print("Record deleted")
            return True
        else:
            print("Record doesn't exist")
            return False

    def update_score(self, username, new_score):
        if not self.check_login():
            return False

        if self.server.zrank(self.leaderboard, username):
            self.server.zadd(self.leaderboard, {username: new_score})
            print("Record updated")
            return True
        else:
            print("Record doesn't exist")
            return False

    def clear_leaderboard(self):
        if not self.check_login():
            return False

        if self.server.zcard(self.leaderboard) > 0:
            self.server.delete(self.leaderboard)
            print("Board is cleared")
            return True
        else:
            print("Board is already empty")
            return False

    def search(self, username):
        if not self.check_login():
            return False

        rank = self.server.zrank(self.leaderboard, username)
        if rank is not None:
            score = self.server.zscore(self.leaderboard, username)
            return f"{username} has a score of {score} and is ranked {rank}"
        else:
            return f"{username} is not in the leaderboard"

    def view_leaderboard(self, start=0, end=-1):
        if not self.check_login():
            return False

        leaderboard = self.server.zrevrange(self.leaderboard, start, end, withscores=True)
        for rank, (username, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username}: {score}")


leaderboard = Leaderboard()

while True:
    print("\nMenu:")
    print("1. Create user")
    print("2. Login")
    print("3. Exit")

    option = input("Select option: ")
    if option == "3":
        break
    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        leaderboard.create_user(username, password)
    elif option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if leaderboard.login(username, password):

            while True:
                if not leaderboard.check_login():
                    print("Login expired")
                    break

                print("\nMenu:")
                print("1. Add Score")
                print("2. Remove Score")
                print("3. Update Score")
                print("4. Clear Leaderboard")
                print("5. Search")
                print("6. View Leaderboard")
                print("7. Top 10")
                print("8. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    while True:
                        username = input("Enter username: ")
                        if username == "":
                            break
                        score = float(input("Enter score: "))
                        if not leaderboard.add_score(username, score):
                            break
                elif choice == "2":
                    username = input("Enter username: ")
                    leaderboard.remove_score(username)
                elif choice == "3":
                    username = input("Enter username: ")
                    new_score = float(input("Enter new score: "))
                    leaderboard.update_score(username, new_score)
                elif choice == "4":
                    leaderboard.clear_leaderboard()
                elif choice == "5":
                    username = input("Enter username: ")
                    print(leaderboard.search(username))
                elif choice == "6":
                    leaderboard.view_leaderboard()
                elif choice == "7":
                    leaderboard.view_leaderboard(0, 9)
                elif choice == "8":
                    break
                else:
                    print("Invalid choice. Please try again.")
