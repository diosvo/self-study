"""
String Formatting with F-Strings
"""

username = "diosvo"
password = 123

# Several approaches

concatenation = "username: " + username + " | password: " + str(password)
operators = "username: %s | password: %d" % (username, password)
formatting = "username: {} | password: {}".format(username, password)

# Best Approach

f_strings = f"username:{username} | password:{password}"
