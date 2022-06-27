#Import your dependencies
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape_all():
    #Setup your executable path and chrome browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere_data": hemisphere_scrape(browser)
    }

     # Stop webdriver and return data
    browser.quit()
    return data   

# ### Article Scraping
def mars_news(browser):

    #setup the url for nasa
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

     # Add try/except for error handling
    try:

        slide_elem = news_soup.select_one('div.list_text')
        #slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        #remove print here and move to function return statment
        #news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        
        #remove print here and move to function return statment
        #news_p

    except AttributeError:
        return None, None   

    return news_title, news_p



# ### Image Scraping - Feature Images

def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button. The 1 index stimpulates that we want our browser to click the second button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    #With the new page loaded onto our automated browser, 
    #it needs to be parsed so we can continue and scrape the full-size image URL. In the next empty cell, type the following:
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:

        # Find the relative image url
        #An img tag is nested within this HTML, so we've included it.
        #.get('src') pulls the link to the image.
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        #img_url_rel

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    #img_url

    return img_url


def mars_facts():

    try:
        # use 'read_html" to scrape the facts table into a dataframe    
        # ### Pull a table with Mars Facts From Another Webpage
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    #Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    #df

    # Pandas also has a way to easily convert our DataFrame back into HTML-ready code using the .to_html() function. 
    #Add this line to the next cell in your notebook and then run the code.
    #df.to_html()

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")



def hemisphere_scrape(browser):
    # Set the executable path and initialize the chrome browser in splinter
    ##executable_path = {'executable_path': ChromeDriverManager().install()}
    ##browser = Browser('chrome', **executable_path)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
 
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

  # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Parse the html with beautifulsoup
    html = browser.html
    hemi_soup = soup(html, 'html.parser')

    # Locate links for each of the 4 hemispheres
    hemi_links = hemi_soup.find_all('h3')

    #loop through each hemisphere link and capture the title and Sample jpeg
    for hemi in hemi_links:
        # Navigate and click the link of the hemisphere
        img_page = browser.find_by_text(hemi.text)
        img_page.click()
        html= browser.html
        img_soup = soup(html, 'html.parser')
        # Scrape the image link
        img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])
        # Scrape the title
        title = img_soup.find('h2', class_='title').text
        # Define and append to the dictionary
        hemisphere = {'img_url': img_url,'title': title}
        hemisphere_image_urls.append(hemisphere)
        browser.back()
    return hemisphere_image_urls

  


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
    


