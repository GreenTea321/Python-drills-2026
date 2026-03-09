fighter = {"name": "Rolento", "style": "Bojutsu"}

for key, value in fighter.items():
    # .items() pulls the pair out together.
    # 'key' gets "name", 'value' gets "Rolento".

    print(f"{key} is {value}")
    # An f-string. The 'f' prefix lets you inject
    # variables directly inside curly braces.