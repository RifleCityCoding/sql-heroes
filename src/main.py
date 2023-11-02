from database.db_connection import execute_modify, execute_query

def select_hero_profile(user_input):
    query = """
        SELECT 
            h.id, h.name, h.about_me, h.biography, at.name AS ability_name
        FROM
            heroes h
        LEFT JOIN
            abilities a ON h.id = a.hero_id
        LEFT JOIN
            ability_types at ON a.ability_type_id = at.id
        WHERE
            h.name = %s OR h.id = %s
    """
    returned_items = execute_query(query, (user_input, user_input))

    if returned_items:
        hero_id = returned_items[0][0]
        hero_name = returned_items[0][1]
        about_me = returned_items[0][2]
        biography = returned_items[0][3]
        
        print(f"Hero ID: {hero_id}")
        print(f"Name: {hero_name}")
        print(f"About Me: {about_me}")
        print(f"Biography: {biography}")
        
        print("Abilities:")
        for item in returned_items:
            ability_name = item[4]
            print(f"- {ability_name}")
    else:
        print(f"No hero found with the name or ID: {user_input}")


user_input = input("Enter the name or ID of the hero you want to retrieve: ")

# select_hero_profile(user_input)



def create_hero_profile():
   
    hero_name = input("Enter the name of the hero: ")
    about_me = input("Enter a short description (about me) for the hero: ")
    biography = input("Enter the hero's biography: ")

    hero_query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        RETURNING id
    """
    hero_id = execute_modify(hero_query, (hero_name, about_me, biography))

    if hero_id:
        hero_id = hero_id[0][0]
    print(f"Hero profile for '{hero_name}' created successfully!\n")

    ability_name = input("Enter an ability name for the hero (or press Enter to skip): ")
    if ability_name:
            ability_type_query = """
                INSERT INTO ability_types (name)
                VALUES (%s)
                RETURNING id
            """
            ability_type_id = execute_modify(ability_type_query, (ability_name,))

            if ability_type_id:
                ability_type_id = ability_type_id[0][0]
                insert_ability_query = """
                    INSERT INTO abilities (hero_id, ability_type_id)
                    VALUES (%s, %s)
                """
                execute_modify(insert_ability_query, (hero_id, ability_type_id))

    print(f"Hero ability for '{hero_name}' added successfully!")

# create_hero_profile()

from database.db_connection import execute_modify, execute_query

def delete_hero(hero_name):
    check_hero_query = "SELECT id FROM heroes WHERE name = %s"
    hero_id = execute_query(check_hero_query, (hero_name,))

    if hero_id:
        hero_id = hero_id[0][0]
        delete_abilities_query = "DELETE FROM abilities WHERE hero_id = %s"
        execute_modify(delete_abilities_query, (hero_id,))
        delete_hero_query = "DELETE FROM heroes WHERE id = %s"
        execute_modify(delete_hero_query, (hero_id,))
        print(f"Hero profile for '{hero_name}' and associated abilities have been deleted.")
    else:
        print(f"No hero found with the name '{hero_name}'.")

delete_hero_name = input("Enter the name of the hero you want to delete: ")

delete_hero(delete_hero_name)
