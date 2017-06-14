
def extract_filename(url):
    """extract filename from the url
    """
    if '/' in url:
        filename = url.split('/')[-1]
    else:
        raise Exception('not a valid format')

    return filename


def count_frequency(urls):
    mapper = {}

    for url in urls:
        filename = extract_filename(url)

        if filename in mapper:
            mapper[filename] += 1
        else:
            mapper[filename] = 1

    result = sorted(mapper.items(), key=lambda k: k[1], reverse=True) 

    return result


if __name__ == '__main__':


    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "http://www.facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

    res = count_frequency(urls)

    for i in range(3):
        print('{} {}'.format(res[i][0], res[i][1]))
