# my version

users = ['john', 'joseph', 'mary', 'admin']

for user in users:

    if user != 'admin':
        message1 = f'Welcome {user}'
        print(message1)
    else:
        message2 = f'Welcome Admin'
        print(message2)

# better version
users = ['john', 'joseph', 'mary', 'admin']

for user in users:
    if user == 'admin':
        print('Welcome Admin')
    else:
        print(f'Welcome {user.title()}')

# Best version
for user in users:
    label = 'Admin' if user == 'admin' else user.title()
    print(f'Welcome {label}')

#New Users
new_users = ['joseph', 'tim', 'peter', 'mary']

for new_user in new_users:
    if new_user in users:
        print(f'user {new_user} already registered')
    else:
        print(f'Welcome {new_user}')

#----------------------------------------------------------
# The main improvement is using a set for users,
# because membership checks (in) are O(1) instead of O(n) for a list.
# The original code is fine for small lists, but a set scales better.
users = {'john', 'joseph', 'mary', 'admin'}  # set, not list
new_users = ['joseph', 'tim', 'peter', 'mary']

for new_user in new_users:
    if new_user in users:
        print(f'User {new_user} already registered')
    else:
        print(f'Welcome {new_user}')