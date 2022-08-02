import requests

def get_page_num():
    content = requests.get("https://jsonmock.hackerrank.com/api/articles").json()
    return content['total_pages']

def bindingArticles(author):
    all_titles = []
    total_pages = get_page_num()
    print(total_pages)
    for page in range(total_pages):
        content = requests.get(f"https://jsonmock.hackerrank.com/api/articles?author={author}&page={page}").json()
        for title in content['data']:
            if title['title'] is not None and title['title'] != '':
                all_titles.append(title['title'])
            elif title['story_title'] is not None and title['story_title'] != '':
                all_titles.append(title['story_title'])
            else:
                continue
    print(all_titles)
    return all_titles    

bindingArticles('epaga')