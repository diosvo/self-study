"""
Join Function
"""

words = ["Hey!", "Subscribe", "to", "DV!"]

# Manual way

sentence = ""
for word in words:
    sentence += word + " "

# Join Function

sentence = " ".join(words)
