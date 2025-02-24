# humanornot.ai HTML Injection

This simple Python script generates HTML code from text input. It works on **humanornot.ai**, allowing you to manipulate displayed text using HTML tags.

## Features
- **Big text** (`<h1>`)
- **Small text** (`<span style="font-size: 8px;">`) – smaller than `<h6>`
- **Bold text** (`<b>`)
- **Italic text** (`<i>`)
- **Insert images** (`<img>`) – supports direct image URLs
- **Insert videos** (`<video>`) – supports direct video URLs

## How to Use
1. Run the `main.py` script
2. Choose an option
3. Enter your text or media URL
4. The script generates HTML code, which you can use on **humanornot.ai**

## URL Handling
The script ensures that URLs are correctly formatted:
- If the URL starts with `http://` or `https://`, it is left unchanged.
- If the URL contains `//`, it replaces the **second occurrence** with `////` to prevent formatting issues.

## Example
If you enter "Hello" and choose **big text**, the output will be:
```html
&lth1&gtHello&lt/h1&gt
