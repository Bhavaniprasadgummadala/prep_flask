from database import insert_user, get_users, delete_user, update_user, get_user_by_id

while True:
    print("Enter the options")
    print("1. Insert User")
    print("2. Get Users")
    print("3. Delete User")
    print("4. Update User")
    print("5. Get User by ID")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        insert_user(name, email)
        print("User inserted successfully.")

    elif option == 2:
        users = get_users()
        if users:
            print("Users:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        else:
            print("No users found.")

    elif option == 3:
        user_id = int(input("Enter user ID to delete: "))
        delete_user(user_id)
        print(f"User with ID {user_id} deleted successfully.")

    elif option == 4:
        user_id = int(input("Enter user ID to update: "))
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        update_user(user_id, name, email)
        print(f"User with ID {user_id} updated successfully.")

    elif option == 5:
        user_id = int(input("Enter user ID to retrieve: "))
        user = get_user_by_id(user_id)
        if user:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        else:
            print(f"No user found with ID {user_id}.")

    elif option == 6:
        print("Exiting the program")
        break

    else:
        print("Invalid option. Please try again.")
