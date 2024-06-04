import redis


class Museum:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
        self.current_admin = None

    def _get_admins_key(self):
        return 'museum:admins'

    def add_admin(self, admin_id, password):
        admin_key = self._get_admins_key()
        if self.redis.hexists(admin_key, admin_id):
            print("Admin is already exists")
            return
        self.redis.hset(admin_key, admin_id, password)
        print("Admin added")

    def login(self, admin_id, password):
        admin_key = self._get_admins_key()
        admin_password = self.redis.hget(admin_key, admin_id)

        if admin_password and password == admin_password:
            print("Login success")
            self.current_admin = admin_id
            return
        else:
            print("Incorrect login or password")

    def add_exhibit(self, exhibit_id, exhibit_data):
        if not self._check_login():
            return

        exhibit_key = self._get_exhibit_key(exhibit_id)

        if self.redis.exists(exhibit_key):
            print("Exhibit is already exists")
            return

        data = {
            'admin': self.current_admin,
            'name': exhibit_data.get('name', ''),
            'description': exhibit_data.get('description', '')
        }
        self.redis.hset(exhibit_key, mapping=data)

        exhibit_people_key = self._get_exhibit_related_people_key(exhibit_id)

        people = exhibit_data.get('people', [])
        self.redis.sadd(exhibit_people_key, *people)

        for person_id in people:
            person_exhibits_key = self._get_person_exhibits(person_id)
            print(person_exhibits_key)
            self.redis.sadd(person_exhibits_key, exhibit_id)

        print("Data added")

    def _get_person_key(self, person_id):
        return f'museum:people:{person_id}'

    def _get_person_exhibits(self, person_id):
        return self._get_person_key(person_id) + ':related_exhibits'

    def _get_exhibit_related_people_key(self, exhibit_id):
        return self._get_exhibit_key(exhibit_id) + ':related_people'

    def _get_exhibit_key(self, exhibit_id):
        return f'museum:exhibits:{exhibit_id}'

    def _check_login(self):
        if self.current_admin is None:
            print("Login needed")
            return False
        return True

    def delete_exhibit(self, exhibit_id):
        if not self._check_login():
            return

        exhibit_key = self._get_exhibit_key(exhibit_id)

        if not self.redis.exists(exhibit_key):
            print("Exhibit not found")
            return

        self.redis.delete(exhibit_key)
        exhibit_people_key = self._get_exhibit_related_people_key(exhibit_id)
        people = self.redis.smembers(exhibit_people_key)
        self.redis.delete(exhibit_people_key)

        for person_id in people:
            person_exhibits_key = self._get_person_exhibits(person_id)
            self.redis.srem(person_exhibits_key, exhibit_id)

        print("Exhibit data deleted")

    def view_exhibit_info(self, exhibit_id):
        if not self._check_login():
            return

        exhibit_key = self._get_exhibit_key(exhibit_id)

        if not self.redis.exists(exhibit_key):
            print("Exhibit not found")
            return

        exhibit_data = self.redis.hgetall(exhibit_key)
        print(f'Exhibit {exhibit_id} information:')
        print(f'\t\t Name: {exhibit_data.get("name", "unknown")}')
        print(f'\t\t Description: {exhibit_data.get("description", "unknown")}')
        exhibit_people_key = self._get_exhibit_related_people_key(exhibit_id)

        people = self.redis.smembers(exhibit_people_key)
        if people:
            print("People info: ", *people)

    def view_all_exhibits(self):
        if not self._check_login():
            return
        pattern_key = self._get_exhibit_key("*")
        exhibit_key = self.redis.keys(pattern=pattern_key)
        for key in exhibit_key:
            exhibit_id = key.split(":")[-1]

            if exhibit_id.isdigit():
                print(f"{exhibit_id} data")
                self.view_exhibit_info(exhibit_id)

    def update_exhibit(self, exhibit_id, data):
        if not self._check_login():
            return

        exhibit_key = self._get_exhibit_key(exhibit_id)

        if not self.redis.exists(exhibit_key):
            print("Exhibit not found")
            return

        exhibit_data = self.redis.hgetall(exhibit_key)

        for key in data:
            if data[key] and key != "people":
                exhibit_data[key] = data[key]
        print(exhibit_data)

        self.redis.hset(exhibit_key, mapping=exhibit_data)

        if data["people"]:
            exhibit_people_key = self._get_exhibit_related_people_key(exhibit_id)
            for person in data["people"]:
                if not self.redis.sismember(exhibit_people_key, person):
                    self.redis.sadd(exhibit_people_key, person)

                    person_exhibits_key = self._get_person_exhibits(person)
                    self.redis.srem(person_exhibits_key, exhibit_id)

    def view_people_related_to_exhibit(self, exhibit_id):
        if not self._check_login():
            return

        exhibit_key = self._get_exhibit_key(exhibit_id)

        if not self.redis.exists(exhibit_key):
            print("Exhibit not found")
            return

        exhibit_people_key = self._get_exhibit_related_people_key(exhibit_id)
        related_people = self.redis.smembers(exhibit_people_key)
        print(f"Related people to {exhibit_id}: ", related_people)

    def view_exhibits_related_to_person(self, person_id):
        if not self._check_login():
            return

        person_exhibit_key = self._get_person_exhibits(person_id)

        if not self.redis.type(person_exhibit_key):
            print("Person not found")
            return

        related_exhibits = self.redis.smembers(person_exhibit_key)
        if related_exhibits:
            print("Related exhibits: ", related_exhibits)

    def view_exhibits_by_description(self, word):
        if not self._check_login():
            return
        pattern_key = self._get_exhibit_key("*")
        exhibit_key = self.redis.keys(pattern=pattern_key)
        for key in exhibit_key:
            exhibit_id = key.split(":")[-1]

            if exhibit_id.isdigit():
                exhibit_key = self._get_exhibit_key(exhibit_id)
                exhibit_data = self.redis.hgetall(exhibit_key)

                if word in exhibit_data['description'].lower():
                    self.view_exhibit_info(exhibit_id)


museum = Museum()

while True:
    print("Select option: ")
    print("1. Sign up")
    print("2. Sign in")
    print("3. Add exhibit")
    print("4. Delete exhibit")
    print("5. View exhibit")
    print("6. View all exhibits")
    print("7. Update exhibits")
    print("8. View people related to exhibit")
    print("9. View exhibits related to the person")
    print("10. View exhibits by description")
    print("0. Exit.")

    command = input("Enter the command: ")
    if command == "exit":
        break

    if command == "1":
        admin_id = int(input("Enter admin id: "))
        password = input("Enter password: ")

        museum.add_admin(admin_id, password)

    elif command == "2":
        admin_id = int(input("Enter admin id: "))
        password = input("Enter password: ")

        museum.login(admin_id, password)

    elif command == "3":
        exhibit_id = int(input("Enter exhibit id: "))
        exhibit_data = {
            'name': input("Enter exhibit name: "),
            'description': input("Enter exhibit description: "),
            'people': input("Enter related people: ").split(',')
        }
        museum.add_exhibit(exhibit_id, exhibit_data)

    elif command == "4":
        exhibit_id = int(input("Enter exhibit id: "))

        museum.delete_exhibit(exhibit_id)

    elif command == "5":
        exhibit_id = int(input("Enter exhibit id: "))
        museum.view_exhibit_info(exhibit_id)

    elif command == "6":
        museum.view_all_exhibits()

    elif command == "7":
        exhibit_id = int(input("Enter exhibit id: "))
        exhibit_data = {
            'name': input("Enter exhibit name: "),
            'description': input("Enter exhibit description: "),
            'people': input("Enter related people: ").split(',')
        }
        museum.update_exhibit(exhibit_id, exhibit_data)

    elif command == "8":
        exhibit_id = int(input("Enter exhibit id: "))
        museum.view_people_related_to_exhibit(exhibit_id)

    elif command == "9":
        person = input("Enter person id: ")
        museum.view_exhibits_related_to_person(person)

    elif command == "10":
        word = input("Enter word for search in description: ").lower()
        museum.view_exhibits_by_description(word)
