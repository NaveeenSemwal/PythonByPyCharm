import module
import random
import urllib.request

module.reuse_function()


def download_image(url):
    name = str(random.randrange(1, 1000)) + ".jpg"
    urllib.request.urlretrieve(url, name)


download_image('https://www.bing.com/images/search?view=detailV2&ccid=fmzjN9fR&id=8A8E50B52DF62D58E8479EEBD361F579D40AD91E&thid=OIP.fmzjN9fR9o2Pz_kOeQXlswHaG9&mediaurl=http%3a%2f%2fwww.clker.com%2fcliparts%2ft%2fD%2f6%2fn%2fp%2fP%2fpink-flower-3-hi.png&exph=564&expw=600&q=Flower+clip+art&simid=608045957346427353&selectedIndex=4&ajaxhist=0')

