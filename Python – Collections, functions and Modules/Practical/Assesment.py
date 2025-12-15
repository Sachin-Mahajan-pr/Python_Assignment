from datetime import datetime

# ---------------- IN-MEMORY DATA ----------------
users = {
    "admin": "admin123",
    "rahul": "rahul123",
    "neha": "neha123"
}

posts = []


# ---------------- LOGIN FUNCTION ----------------
def login():
    print("\n===== LOGIN =====")
    attempts = 3

    while attempts > 0:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username == "" or password == "":
            print("Username and password cannot be empty.")
            continue

        if username not in users:
            print("Username does not exist.")
        elif users[username] != password:
            print("Incorrect password.")
        else:
            print(f"\nLogin successful. Welcome {username}")
            return username

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print("Too many failed attempts. Exiting program.")
    exit()


# ---------------- CREATE POST ----------------
def create_post(username):
    print("\n===== CREATE POST =====")

    title = input("Enter Title: ").strip()
    description = input("Enter Description: ").strip()

    if title == "" or description == "":
        print("Title and Description cannot be empty.")
        return

    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)
    print("Post created successfully.")


# ---------------- VIEW ALL POSTS ----------------
def view_posts():
    print("\n===== ALL POSTS =====")

    if not posts:
        print("No posts available.")
        return

    for i, post in enumerate(posts, start=1):
        print(f"""
Post #{i}
-------------------------
Author      : {post['author']}
Title       : {post['title']}
Date        : {post['date']}
Description : {post['description']}
-------------------------
""")


# ---------------- SEARCH POSTS BY USER ----------------
def search_posts_by_user():
    username = input("\nEnter username to search posts: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    found = False
    for post in posts:
        if post["author"].lower() == username.lower():
            found = True
            print(f"""
-------------------------
Author      : {post['author']}
Title       : {post['title']}
Date        : {post['date']}
Description : {post['description']}
-------------------------
""")

    if not found:
        print("No posts found for this user.")


# ---------------- MENU ----------------
def menu(username):
    while True:
        print("""
===== POSTBOARD MENU =====
1. Create Post
2. View All Posts
3. Search Posts by Username
4. Logout
""")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            create_post(username)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_posts_by_user()
        elif choice == "4":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")


# ---------------- MAIN FUNCTION ----------------
def main():
    print("Welcome to PostBoard - Internal Community App")
    user = login()
    menu(user)


main()
