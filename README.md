# Mission-to-Mars

## Project Overview
To add functionality to the current web app, the purpose of this project is to add four high resolution images of Mar's hemispheres through web scraping. This should be accomplished through using BeautifulSoup and Splinter to scrape the images and title's of those images, store the scraped data on a Mongo database, use a web applciation to display the data and alter the web app to accommodate these images. 

## Resources
- Software: Jupyter Notebook, Visual Studio, Flask, Mongo database

## Results

### Deliverable 1 and 2 : Scrape Full-Resolution Mars Hemisphere Images and Titles and Update the Web App with Mar's Images and Titles

Using BeautifulSoup and Splinter, the code is updated to retrieve full-resolution image URL's of Mars’s hemispheres along with the titles of those images, where they are added to the mars Mongo database and the index.html contains code to display the images and titles.

![web1](https://user-images.githubusercontent.com/87085239/176810689-fb927659-24b7-41c7-9806-75df351baefb.jpg)

![web2](https://user-images.githubusercontent.com/87085239/176810724-9e6dbe14-e144-443b-b407-8cccfde66806.jpg)


### Deliverable 3 : Add Bootstrap 3 Components

The following bootstrap components were added:
- Use the Bootstrap 3 grid system examples to update your index.html file so your website is mobile-responsive. Use the DevTools to test the responsiveness of your website.
    - By adding content="width=device-width, initial-scale=1.0" to the head section, the webpage will adjust to the width of the mobile device. 
- Add two other Bootstrap 3 components
    - The title was changed to bold.
    - The scrap button fill color and border was changed.
    - An image was added to the backgroud of the jumbotron by calling an image from a style.css file. 
    - The mar hemisphere images were changed to the size col-xs-6.

## Summary

The final web app provides the end-user with the ability to scrap different sites that will bring in the latest Mars article, updated featured mars image, planet facts, and high res images of the hemispheres. 






