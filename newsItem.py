class newsItem:
    newsID=''
    title=''
    time=''
    date=''
    description=''
    sourceId=''
    author=''
    pic_url=''
    origin_url=''
    categoryId=''

    def __init__(self, title,complete_title,time,date,sourceId,description,origin_url,categoryId,author,pic_url):
        self.title = title
        self.complete_title=complete_title
        self.date=date
        self.time=time
        self.description=description
        self.sourceId=sourceId
        self.origin_url=origin_url
        self.categoryId=categoryId  # instance variable unique to each instance
        self.author=author
        self.pic_url=pic_url
