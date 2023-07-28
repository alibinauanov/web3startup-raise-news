with open("output_file.txt", "w", encoding="utf-8") as file:
    import requests
    from bs4 import BeautifulSoup

    url = "https://cryptonews.com/news/futureverse-raises-54-million-fuel-expansion-of-diversified-metaverse-platform.htm"  # Replace this with the URL of the website you want to scrape
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to fetch the content. Status code: {response.status_code}")

    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <p> tags without a class name
    paragraphs_without_class = soup.find_all("p", class_=False)

    # Extract the text content of each <p> tag
    main_content = [p.get_text() for p in paragraphs_without_class]

    # Print or use the extracted content
    for paragraph in main_content:
        file.write(paragraph + "\n")