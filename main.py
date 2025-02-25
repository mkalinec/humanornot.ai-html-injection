def fix_url(url):
    """Ensures the URL is properly formatted by replacing '//' with '////', but keeping 'http://' or 'https://'."""
    if url.startswith("http://") or url.startswith("https://"):
        return url.replace("//", "////", 1)  # Only replace the second occurrence of //
    return url.replace("//", "////")  # Replace all if not a full URL

def get_html(choice):
    """Generates HTML based on the chosen option using match-case."""
    match choice:
        case "1":
            text = input("Enter the text you want to make big: ")
            return f"&lth1&gt{text}&lt/h1&gt"
        case "2":
            text = input("Enter the text you want to make small: ")
            return f"&ltspan style='font-size: 8px;'&gt{text}&lt/span&gt"
        case "3":
            text = input("Enter the text you want to make bold: ")
            return f"&ltb&gt{text}&lt/b&gt"
        case "4":
            text = input("Enter the text you want to make italic: ")
            return f"&lti&gt{text}&lt/i&gt"
        case "5":
            img_url = input("Enter the direct link to the image: ")
            fixed_url = fix_url(img_url)
            return f"&ltimg src='{fixed_url}' alt='Image'&gt"
        case "6":
            video_url = input("Enter the direct link to the video: ")
            fixed_url = fix_url(video_url)
            return f"&ltvideo controls&gt&ltsource src='{fixed_url}' type='video/mp4'&gtYour browser does not support the video tag.&lt/video&gt"
        case "7":
            link_url = input("Enter the URL of the link: ")
            fixed_url = fix_url(link_url)
            link_text = input("Enter the text for the link: ")
            return f"&lta href='{fixed_url}' target='_blank'&gt{link_text}&lt/a&gt"
        case "8":
            js_code = input("Enter the JavaScript code (without `<script>` tags): ")
            return f"&ltscript&gt{js_code}&lt/script&gt"
        case "9":
            custom_html = input("Enter your custom HTML code: ")
            return custom_html.replace("<", "&lt").replace(">", "&gt")
        case _:
            return None

def generate_html():
    print("Choose options for HTML code generation (separate multiple choices with commas):")
    print("1. Make text big")
    print("2. Make text small")
    print("3. Make text bold")
    print("4. Make text italic")
    print("5. Insert an image")
    print("6. Insert a video")
    print("7. Insert a link")
    print("8. Insert JavaScript")
    print("9. Insert custom HTML")

    choices = input("Enter the numbers of your choices, separated by commas (e.g., 1,3,5): ").split(",")

    final_html = ""
    for choice in choices:
        choice = choice.strip()
        html_part = get_html(choice)
        if html_part:
            final_html += html_part + "\n"

    print("\nGenerated HTML Code:")
    print(final_html.strip())

# Run the function
generate_html()
