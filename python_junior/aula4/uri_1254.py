import re

tag_pattern = re.compile(r"<[A-Za-z0-9\\\s/=]+>")

while True:
    try:
        word_to_replace = input()
        int_to_replace = input()
        text = input()

        valid_tags = re.findall(tag_pattern, text)

        insensitive_pattern = re.compile(re.escape(word_to_replace),
                                         re.IGNORECASE)

        for old_tag in valid_tags:
            new_tag = insensitive_pattern.sub(int_to_replace, old_tag)
            text = re.sub(old_tag, new_tag, text, 1)

        print(text)
    except:
        break
