from openai import OpenAI

client = OpenAI(
    organization='org-5j0BXHEz8F5nFzu8xksebwcm',
    project='proj_oGsPKgX5WKQ5wGpsq8j2AjTA',
)


def get_chat_completion(model, messages):
    """Funkcja do uzyskania odpowiedzi od modelu ChatGPT."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response
    except Exception as e:
        print(f"Error while calling OpenAI API: {e}")
        return None


def read_article_from_file(file_path):
    """Funkcja do odczytywania artykułu z pliku."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def process_article_with_openai(article_text):
    """Funkcja do przetwarzania treści artykułu za pomocą API OpenAI."""
    response = get_chat_completion(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
             "content": f"Please generate a concise HTML document for the following article. The HTML should include the "
                        f"following titles: 'Sztuczna inteligencja: wpływ i wyzwania', 'Wyzwania etyczne i społeczne', "
                        f"'Automatyzacja i przyszłość rynku pracy'. The content should be organized under these titles with "
                        f"consolidated paragraphs to reduce the overall number of paragraphs. Additionally, include <img> tags "
                        f"where appropriate, each with 'src' set to 'image_placeholder.jpg', an 'alt' attribute with a detailed "
                        f"description of the image, and a caption below each image using a <figcaption> tag. Ensure that no new "
                        f"paragraph is started after an image; images should be inline with the text without creating new paragraphs:\n\n"
                        f"{article_text}"}
        ],
    )

    if response and response.choices:
        raw_content = response.choices[0].message.content

        # Usuwanie niepożądanych elementów z początku
        cleaned_content = raw_content.replace(
            "Here's the revised article with <img> tags inserted at appropriate places:", ""
        ).replace(
            "Here's a complete HTML document for the provided article on artificial intelligence and its impact, challenges, "
            "and future:\n\n html", ""
            ).strip()

        # Usuwanie linii zawierających tylko myślniki
        cleaned_content = '\n'.join(line for line in cleaned_content.split('\n') if line.strip() != '---')

        # Usuwanie pustych linii na początku i końcu
        cleaned_content = cleaned_content.strip()

        # Znajdowanie początku treści
        start_index = cleaned_content.find('<h1>')
        if start_index != -1:
            cleaned_content = cleaned_content[start_index:]

        # Znajdowanie końca ostatniego akapitu
        end_index = cleaned_content.rfind('</p>')
        if end_index != -1:
            cleaned_content = cleaned_content[:end_index + 4]  # +4 to include the </p> tag itself

        # Dodanie dodatkowego akapitu na końcu
        additional_paragraph = (
            "<p>Nasza zdolność do adaptacji i innowacji zdecyduje o tym, jak AI wpłynie na przyszłość ludzkości. "
            "Wspólnie możemy kształtować tę przyszłość, wykorzystując AI dla dobra wszystkich.</p>"
        )

        return cleaned_content + additional_paragraph
    else:
        return "No valid response received from OpenAI API."


def save_to_html(content, file_path):
    """Funkcja do zapisywania treści jako plik HTML."""
    with open(file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(content)

# Ścieżka do pliku z artykułem
file_path = 'artykul.txt'

# Odczytuje artykuł
article_text = read_article_from_file(file_path)

# Przetwarza artykuł
processed_article = process_article_with_openai(article_text)

# Zapisz przetworzony artykuł jako HTML
html_file_path = 'artykul.html'
save_to_html(processed_article, html_file_path)

if __name__ == '__main__':

    print("Koniec pracy programu")