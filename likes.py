def likes(users):
    if len(users) == 0: return "no one likes this"
    elif len(users) == 1: return f"{users[0]} likes this"
    elif len(users) == 2: return f"{users[0]} and {users[1]} like this"
    elif len(users) == 3: return f"{users[0]}, {users[1]} and {users[2]} like this"
    elif len(users) >= 4: return f"{users[0]}, {users[1]} and {len(users) - 2} others like this"
