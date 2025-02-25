def fix_url(url):
    """Ensures the URL is properly formatted by replacing '//' with '////', but keeping 'http://' or 'https://'."""
    if url.startswith("http://") or url.startswith("https://"):
        return url.replace("//", "////", 1)  # Only replace the second occurrence of //
    return url.replace("//", "////")  # Replace all if not a full URL

def generate_html():
    print("Choose an option for HTML code generation:")
    print("1. Make text big")
    print("2. Make text small")
    print("3. Make text bold")
    print("4. Make text italic")
    print("5. Insert an image")
    print("6. Insert a video")
    print("7. Insert a link")
    print("8. Insert JavaScript")
    print("9. Insert custom HTML")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        text = input("Enter the text you want to make big: ")
        html_code = f"&lth1&gt{text}&lt/h1&gt"
    elif choice == "2":
        text = input("Enter the text you want to make small: ")
        html_code = f"&ltspan style='font-size: 8px;'&gt{text}&lt/span&gt"
    elif choice == "3":
        text = input("Enter the text you want to make bold: ")
        html_code = f"&ltb&gt{text}&lt/b&gt"
    elif choice == "4":
        text = input("Enter the text you want to make italic: ")
        html_code = f"&lti&gt{text}&lt/i&gt"
    elif choice == "5":
        img_url = input("Enter the direct link to the image: ")
        fixed_url = fix_url(img_url)
        html_code = f"&ltimg src='{fixed_url}' alt='Image'&gt"
    elif choice == "6":
        video_url = input("Enter the direct link to the video: ")
        fixed_url = fix_url(video_url)
        html_code = f"&ltvideo controls&gt&ltsource src='{fixed_url}' type='video/mp4'&gtYour browser does not support the video tag.&lt/video&gt"
    elif choice == "7":
        link_url = input("Enter the URL of the link: ")
        fixed_url = fix_url(link_url)
        link_text = input("Enter the text for the link: ")
        html_code = f"&lta href='{fixed_url}' target='_blank'&gt{link_text}&lt/a&gt"
    elif choice == "8":
        js_code = input("Enter the JavaScript code (without `<script>` tags): ")
        html_code = f"&ltscript&gt{js_code}&lt/script&gt"
    elif choice == "9":
        custom_html = input("Enter your custom HTML code: ")
        html_code = custom_html.replace("<", "&lt").replace(">", "&gt")
    else:
        html_code = "Invalid choice. Please choose a valid option."

    print("\nGenerated HTML Code:")
    print(html_code)

# Run the function
generate_html()
