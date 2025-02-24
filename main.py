def generate_html():
    print("Choose an option for HTML code generation:")
    print("1. Make text big")
    print("2. Make text small")
    print("3. Make text bold")
    print("4. Make text italic")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        text = input("Enter the text you want to make big: ")
        html_code = f"&lth1&gt{text}&lt/h1&gt"
    elif choice == "2":
        text = input("Enter the text you want to make small: ")
        html_code = f"&ltspan style&#61;'font-size: 8px;'&gt{text}&lt/span&gt"
    elif choice == "3":
        text = input("Enter the text you want to make bold: ")
        html_code = f"&ltb&gt{text}&lt/b&gt"
    elif choice == "4":
        text = input("Enter the text you want to make italic: ")
        html_code = f"&lti&gt{text}&lt/i&gt"
    else:
        html_code = "Invalid choice. Please choose a valid option."
    
    print("\nGenerated HTML Code:")
    print(html_code)

# Run the function
generate_html()
