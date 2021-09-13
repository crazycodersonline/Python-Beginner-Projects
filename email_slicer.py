email = input("ENter email:")

username = email[:email.index('@')]
domain = email[email.index('@')+1 : ]

print(f"Username :{username}, domain:{domain}")