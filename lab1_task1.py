import redis


class ShoppingCart:
    def __init__(self):
        self.server = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        self.current_user = None

    def add_user(self, user, password):
        if self.server.hexists('users', user):
            print("User exists")
            return
        self.server.hset('users', user, password)

    def login(self, user, password):
        real_password = self.server.hget('users', user)
        if real_password and password == real_password:
            print("Ok")
            self.current_user = user
        else:
            print("Wrong password or user name")

    def add_item(self, item_id, quantity=1):
        key = self._get_user_item_key(item_id)
        if self.server.exists(key):
            print("Item is already in the cart")
            self.server.hincrby(key, 'quantity', quantity)
        else:
            self.server.hset(key, mapping={'id': item_id, "quantity": quantity})

    def __str__(self):
        return f'current user: {self.current_user}'

    def show_cart(self):
        # keys = self.server.key(f'{self.current_user}')
        pattern = self._get_user_item_key('*')
        keys = self.server.keys(pattern)
        print(keys)
        if keys:
            for key in keys:
                data = self.server.hgetall(key)
                print(f"item id: {data['id']} -- {data['quantity']}")
        else:
            print("No items")

    def _get_user_item_key(self, item_id):
        return f'{self.current_user}:{item_id}'

    def delete_item(self, item_id):
        key = self._get_user_item_key(item_id)
        if self.server.exists(key):
            self.server.delete(key)
            print("Item is deleted")
        else:
            print("No item in the cart")

    def clear_cart(self):
        pattern = self._get_user_item_key('*')
        keys = self.server.keys(pattern)

        if keys:
            for key in keys:
                self.server.delete(key)
            print(f"Cart is cleared")
        else:
            print("No items to clear")

    def search_item(self, item_id):
        key = self._get_user_item_key(item_id)
        data = self.server.hgetall(key)

        if data:
            print(f"Info: item id: {data['id']} -- {data['quantity']}")
        else:
            print("Item is not found")

    def update_item(self, item_id, new_quantity):
        key = self._get_user_item_key(item_id)
        if self.server.exists(key):
            self.server.hset(key, 'quantity', new_quantity)
            print('Item quantity is updated')
        else:
            print('There is no item in the cart')


shopping_cart = ShoppingCart()
while True:

    print("Chose the option: ")
    print("1. Add user")
    print("2. Login user")
    print("3. Add item to the cart")
    print("4. Print current user")
    print("5. Show cart items")
    print("6. Delete cart item")
    print("7. Clear cart")
    print("8. Search cart item")
    print("9. Update item")
    print("Exit")

    command = input("Chose the option: ")

    if command == 'exit':
        break

    if command == '1':
        user = input('user name: ')
        password = input('password: ')
        shopping_cart.add_user(user, password)

    elif command == '2':
        user = input('user name: ')
        password = input('password: ')
        shopping_cart.login(user, password)

    elif command == '3':
        item_id = input('enter the cart item id: ')
        quantity = input('enter the quantity: ')

        shopping_cart.add_item(item_id, quantity)
    elif command == '4':
        print(shopping_cart)
    elif command == '5':
        shopping_cart.show_cart()
    elif command == '6':
        item_id = input('enter the cart item id: ')
        shopping_cart.delete_item(item_id)
    elif command == '7':
        shopping_cart.clear_cart()
    elif command == '8':
        item_id = input('enter the cart item id: ')
        shopping_cart.search_item(item_id)
    elif command == '9':
        item_id = input('enter the cart item id: ')
        quantity = input('enter the quantity: ')
        shopping_cart.update_item(item_id, quantity)
