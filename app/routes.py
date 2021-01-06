from app import app


@app.route("/")
def index():
    return "Hello, World!)"


@app.route("/aboutme")
def about_me():
    my_dictionary = dict()
    my_dictionary["title"] = "My Dictionary"
    my_dictionary["first_name"] = "Marisol"
    my_dictionary["last_name"] = "Rodriguez"
    my_dictionary["hobbies"] = "Yarn and bake"
    my_dictionary[" gender"] = "Female"
    my_dictionary["marital_status"] = "Married"
    my_dictionary["Location"] = "Florida"
    return my_dictionary


@app.route("/aboutme2")
def about_me_html():
    title = "My Dictionary"
    first_name = "Marisol"
    last_name = " Rodriguez"
    hobbies = " Crochet and baking"
    gender = "Female"
    marital_status = "Married"
    location = " Florida"
    about_me2 = """<h1 style ="color:red;">Title: %s; </h1><br><hr>
                    <h2 style ="color:blue;">First Name: %s; <br>
                    Last name: %s; <br> 
                    Hobbies: %s; <br>
                    Gender: %s; <br>
                    Marital Status: %s; <br>
                    Location: %s</h2><br>
                    <input type ="text" placeholder="Enter Password" >
                    <button>Submit<button>
                    """ % (
        title,
        first_name,
        last_name,
        hobbies,
        gender,
        marital_status,
        location,
    )
    return about_me2