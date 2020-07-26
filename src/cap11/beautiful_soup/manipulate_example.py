import bs4


with open('example.html') as html_file:
    example_soup = bs4.BeautifulSoup(html_file.read(), features='html.parser')
    elements = example_soup.select('#author')
    print(f'Type of elements is {type(elements)}')
    print(f'Type of elements[0] is {type(elements[0])}')
    print(f'Elements with id="author" {elements}')
    print(str(elements[0]))
    print(f'Text inside {str(elements[0])} is {elements[0].getText()}')
    print(f'All attributes inside {str(elements[0])} {elements[0].attrs}')