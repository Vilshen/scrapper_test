 1. Был произведен сбор цитат, их авторов и тегов, которыми они были отмечены
 2. Сайт **https://quotes.toscrape.com/**
 3. С помощью модуля `requests` был получен HTML страниц сайта. Из него, с помощью библиотеки BeautifulSoup, были собраны все `div` элементы с классом `quote`. В них текст цитаты был в элементе `span` с классом `text`; теги в атрибуте `content` элемента `meta`; автор в элементе `small` с классом `author`. 
 4. BeautifulSoup имеет прямой и простой синтакс, и имел достаточный функционал для данной задачи.