import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        my_request = requests.get(url, timeout=3)
        if my_request.status_code not in [requests.codes.ok]:
            return None
        return my_request.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


class News:
    def get_url(selector):
        url = selector.css("head link[rel=canonical]::attr(href)").get()
        self.url = url
        
        
    def get_title(selector):
        title = selector.css(".tec--article__header__title::text").get()
        self.title = title
    
    
    def get_timestamp(selector):
        timestamp = selector.css(".tec--timestamp__item time::attr(datetime)").get()
        self.timstamp = timestamp
        
    
    def get_summary(selector):
        summary = selector.css("div.tec--article__body > p:nth-child(1) *::text").getall()
        self.summary = ''.join(summary)
    
    
    def get_writer(selector):
        selectors = [
            ".tec--timestamp:nth-child(1) a::text",
            ".tec--author__info p:first-child::text",
            ".tec--author__info p:first-child a::text",
        ]
        selected = []
        for curr_selector in selectors:
            selected_writer = selector.css(curr_selector).get()
            if selected_writer is not None:
                selected.append(selected_writer.strip())
            if selected_writer is None:
                selected.append(None)
        writer = [item for item in selected if item]
        if len(writer) == 0:
            return None
        self.writer = writer[0]
    

    def get_shares_count(selector):
        shares = selector.css(".tec--toolbar div:first-child::text").get()
        if shares is None or not ("Compartilharam") in shares:
            return 0
        shares_count = re.findall(r"\s(\d*)\s(...*)", shares)
        self.shares_count = int(shares_count[0][0])


    def get_comments_count(selector):
        comments = selector.css("#js-comments-btn::attr(data-count)").get()
        if comments is None:
            return 0
        self.comments_count = int(comments)


    def get_sources(selector):
        sources = selector.css(".z--mb-16 .tec--badge::text").getall()
        self.sources = [item.strip() for item in sources]
    
        
    def get_categories(selector):
        categories = selector.css("#js-categories a::text").getall()
        self.cotegories = [item.strip() for item in categories]

# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    
    news = News()
    
    news.get_url(selector)
    news.get_title(selector)
    news.get_timestamp(selector)
    news.get_writer(selector)
    news.get_shares_count(selector)
    news.get_comments_count(selector)
    news.get_sources(selector)
    news.get_categories(selector)
    
    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
