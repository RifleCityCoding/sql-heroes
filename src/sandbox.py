from database.db_connection import execute_modify, execute_query

def select_all_heroes():
    query = """
        SELECT * from heroes
    """
    try:
        returned_items = execute_query(query)
        if not returned_items:
            print("No heroes found.")
            return None
        
        print("Hello User! Will you let me know what hero is logging in today?")
        for index, item in enumerate(returned_items, start=1):
            print(f"{index}. {item[1]}")

        while True:
                try:
                    choice = int(input("Please use the numbers to select your hero profile:"))
                    if 1 <= choice <= len(returned_items):
                        selected_hero = returned_items[choice - 1]
                        print(f"Welcome to your profile {selected_hero[1]}!")
                        return selected_hero
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"Error: {e}")
        return None

    

select_all_heroes()

def select_ability():
    query = """
        SELECT * from ability_types
    """
    try:
        returned_items = execute_query(query)
        if not returned_items:
            print("No abilities found.")
            return None

        print("Choose an ability:")
        for index, item in enumerate(returned_items, start=1):
            print(f"{index}. {item[1]}")

        while True:
            try:
                choice = int(input("Enter the number of your chosen ability: "))
                if 1 <= choice <= len(returned_items):
                    selected_ability = returned_items[choice - 1]
                    print(f"You have chosen: {selected_ability[1]}")
                    return selected_ability
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"Error: {e}")
        return None

# selected_ability = select_ability()
# if selected_ability:
#     pass


select_ability()