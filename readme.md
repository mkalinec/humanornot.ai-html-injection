# humanornot.ai html injection

This simple Python script generates HTML code from text input, and works on **humanornot.ai** to manipulate displayed text using HTML tags. You can chain multiple HTML modifications in one go.

## Features
- **Big text** using `<h1>`
- **Small text** using `<span style="font-size: 8px;">` (smaller than `<h6>`)
- **Bold text** using `<b>`
- **Italic text** using `<i>`
- **Insert an image** using `<img>`
- **Insert a video** using `<video>` and `<source>`
- **Insert a link** using `<a>`
- **Insert JavaScript** using `<script>`
- **Insert custom HTML** (with automatic escaping)
- **Chaining support**: Combine multiple modifications in one go

## How to Use
1. Run the `main.py` script.
2. Enter the numbers corresponding to the desired HTML modifications, separated by commas (e.g., `1,3,5` for Big Text, Bold, and Insert an Image).
3. For each option, provide the required input (e.g., text or URL).
4. The script outputs the generated HTML code, which you can then use on humanornot.ai.

## Example
If you enter "Hello" for big text, the output will be:
```html
&lth1&gtHello&lt/h1&gt
