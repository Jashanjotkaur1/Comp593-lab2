def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full_name' : 'Jashanjot Kaur',
    'student_id': 777200411 ,
    'pizza_toppings' : [
        'PINEAPPLE',
        'BACON',
        'HAM'
    ],
    'movies' : [
        {'title' : 'Pathan',
        'genre' : 'Romantic'},
        {'title' : 'Phir Here Pheri',
        'genre' : 'Comedy' }

    ]}

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title' : 'Star Wars',
                               'genre' : 'Sci-Fi'})
    add_pizza_toppings(about_me, ["TOMATOES", "PANEER"])
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])
    return    

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me Darth {first_name}.")

    print(f"My student ID is {student_id}.")
    return
    
# TODO: Step 5 -  A Function that puts pizza toppings into a list
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    return

# TODO: Step 6 - A Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    [print(f"- {topping}") for topping in about_me["pizza_toppings"]]
    print()
    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    print(f"I like to watch {', '.join(genres)} movies.\n")
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie.get('title', 'Unknown') for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles)}!\n")
    return
    
if __name__ == '__main__':
    main()
