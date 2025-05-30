import json
import os

def generate_variations(keyword):
    words = keyword.strip().replace("-", " ").split()
    if not words:
        return []

    base = " ".join(words)
    variations = set()

    # words variations
    variations.add(base.lower())
    variations.add(base.upper())
    variations.add(base.title())
    variations.add("".join(words))
    variations.add("_".join(words))
    variations.add("-".join(words))
    variations.add("".join([w.capitalize() for w in words]))  # PascalCase
    variations.add(words[0].lower() + "".join(w.capitalize() for w in words[1:]))  # camelCase

    # add prefix
    base_no_space = "".join(words).lower()
    suffixes = ["_official", "_exchange", ".com", ".io"]
    prefixes = ["@", "#"]

    for suffix in suffixes:
        variations.add(base_no_space + suffix)
    for prefix in prefixes:
        variations.add(prefix + base_no_space)

    return list(variations)

def main():
    input_file = 'keywords.txt'
    output_txt = 'variations.txt'
    output_json = 'variations.json'

    if not os.path.exists(input_file):
        print(f"File {input_file} not found.")
        return

    all_variations = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        keywords = [line.strip() for line in file if line.strip()]

    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        for keyword in keywords:
            variations = generate_variations(keyword)
            all_variations[keyword] = variations
            for variant in variations:
                txt_file.write(variant + '\n')
            txt_file.write('\n')  

    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(all_variations, json_file, indent=4, ensure_ascii=False)

    print(f"Saved result as '{output_txt}' and '{output_json}'.")

if __name__ == "__main__":
    main()
