"""
15. Process User Activity Logs
Concepts: list comprehension, dictionary access
📌 Task:
Given a list of dictionaries representing users:
Extract only active users
Return a list of usernames
"""

inp_user_list: list = [
    {"user": "Aman", "active": True},
    {"user": "Asif", "active": False},
    {"user": "Diwan", "active": True},
    {"user": "Bilal", "active": False}
      ]

active_user_list = [user["user"] for user in inp_user_list if user["active"] == True]
print(active_user_list)


# chatgpt Score 9/10 and optimized code

def get_active_users(users: list[dict]) -> list[str]:
    """
    Returns a list of usernames for active users.
    """
    return [user["user"] for user in users if user.get("active")]


if __name__ == "__main__":
    inp_user_list = [
        {"user": "Aman", "active": True},
        {"user": "Asif", "active": False},
        {"user": "Diwan", "active": True},
        {"user": "Bilal", "active": False}
    ]

    print(get_active_users(inp_user_list))
