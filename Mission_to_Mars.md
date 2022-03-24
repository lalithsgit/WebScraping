```python
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
```


```python
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
```

## Visit the NASA mars news site


```python
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
```




    True




```python
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
```


```python
slide_elem.find('div', class_='content_title')
```




    <div class="content_title">NASA's Mars Reconnaissance Orbiter Undergoes Memory Update</div>




```python
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
```




    "NASA's Mars Reconnaissance Orbiter Undergoes Memory Update"




```python
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
```




    'Other orbiters will continue relaying data from Mars surface missions for a two-week period.'



## JPL Space Images Featured Image


```python
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
```


```python
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
```


```python
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup
```




    <html class="fancybox-margin fancybox-lock"><head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet"/>
    <!-- <link rel="stylesheet" type="text/css" href="css/font.css"> -->
    <link href="css/app.css" rel="stylesheet" type="text/css"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
    <title>Space Image</title>
    <style type="text/css">.fancybox-margin{margin-right:0px;}</style></head>
    <body>
    <div class="header">
    <nav class="navbar navbar-expand-lg">
    <a class="navbar-brand" href="#"><img id="logo" src="image/nasa.png"/><span class="logo">Jet Propulsion Laboratory</span>
    <span class="logo1">California Institute of Technology</span></a>
    <button aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbarNav" data-toggle="collapse" type="button">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
    <ul class="navbar-nav">
    <li class="nav-item active">
    <a class="nav-link" href="#"><i aria-hidden="true" class="fa fa-bars"></i>   MENU   <i aria-hidden="true" class="fa fa-search"></i></a>
    </li>
    </ul>
    </div>
    </nav>
    <div class="floating_text_area">
    <h2 class="brand_title">FEATURED IMAGE</h2>
    <h1 class="media_feature_title">Dusty Space Cloud</h1>
    <br/>
    <a class="showimg fancybox-thumbs" href="image/featured/mars3.jpg" target="_blank"> <button class="btn btn-outline-light"> FULL IMAGE</button></a>
    </div>
    <img class="headerimage fade-in" src="image/featured/mars3.jpg"/></div>
    <div class="search sticky">
    <div class="col-md-12">
    <div class="row">
    <div class="col-md-6">
    <input name="Search" placeholder="Search" type="text"/>
    </div>
    <div class="col-md-6">
    <select aria-label="Default select example" class="form-select" id="options">
    <option onchange="0" selected="">Mars</option>
    <!-- <option data-filter="sun" class="button">Mars</option> -->
    <option class="button" data-filter="Sun">Sun</option>
    <option class="button" data-filter="earth">Earth</option>
    <option class="button" data-filter="ida">Ida</option>
    <option class="button" data-filter="jupiter">Jupiter</option>
    <option class="button" data-filter="venus">Venus</option>
    </select>
    </div>
    </div>
    </div>
    </div>
    <div class="container mt-5">
    <div class="col-md-12">
    <div class="row">
    <div class="col-md-6">
    <h1>Images</h1>
    </div>
    <div class="col-md-6" id="icon">
    <div class="icon2"></div>
    <div class="icon1"></div>
    </div>
    </div>
    </div>
    <!-- first div -->
    <div class="div1" id="filter">
    <div class="thmbgroup"><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae7.jpg"/><p class="thumbcontent">January 1, 2020<br/>Icaria Fossae7</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Proctor Crater Dunes 7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Proctor Crater Dunes 7.jpg"/><p class="thumbcontent">December 31, 2020<br/>Proctor Crater Dunes</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae7.jpg"/><p class="thumbcontent">December 31, 2020<br/>Icaria Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Proctor Crater Dunes 7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Proctor Crater Dunes 7.jpg"/><p class="thumbcontent">December 29, 2020<br/>Proctor Crater Dunes</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Proctor Crater Dunes 7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Proctor Crater Dunes 7.jpg"/><p class="thumbcontent">December 28, 2020<br/>roctor Crater Dunes</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae7.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae7.jpg"/><p class="thumbcontent">December 22, 2020<br/>Icaria Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae.jpg"/><p class="thumbcontent">December 21, 2020<br/>Icaria Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Ariadnes Colles4.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Ariadnes Colles4.jpg"/><p class="thumbcontent">December 18, 2020<br/>Ariadnes Colles</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Niger Vallis.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Niger Vallis.jpg"/><p class="thumbcontent">December 17, 2020<br/>Niger Vallis</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Proctor Crater Dunes.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Proctor Crater Dunes.jpg"/><p class="thumbcontent">December 16, 2020<br/>Proctor Crater Dunes</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Niger Vallis.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Niger Vallis.jpg"/><p class="thumbcontent">December 15, 2020<br/>Niger Vallis</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Daedalia Planum.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Daedalia Planum.jpg"/><p class="thumbcontent">December 11, 2020<br/>Daedalia Planum</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Sirenum Fossae.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Sirenum Fossae.jpg"/><p class="thumbcontent">November,11, 2020<br/>Sirenum Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Ariadnes Colles4.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Ariadnes Colles4.jpg"/><p class="thumbcontent">November,13, 2020<br/>Ariadnes Colles</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/South Polar Cap.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/South Polar Cap.jpg"/><p class="thumbcontent">November,14, 2020<br/>South Polar Cap</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Daedalia Planum.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Daedalia Planum.jpg"/><p class="thumbcontent">November,17, 2020<br/>Daedalia Planum</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Ariadnes Colles3.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Ariadnes Colles3.jpg"/><p class="thumbcontent">November,11, 2020<br/>Ariadnes Colles</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Atlantis Chaos.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Atlantis Chaos.jpg"/><p class="thumbcontent">November,09, 2020<br/>Atlantis Chaos</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Daedalia Planum.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Daedalia Planum.jpg"/><p class="thumbcontent">January 1, 2020<br/>Daedalia Planum</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae.jpg"/><p class="thumbcontent">January 1, 2020<br/>Icaria Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Niger Vallis.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Niger Vallis.jpg"/><p class="thumbcontent">January 1, 2020<br/>Niger Vallis</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Proctor Crater Dunes.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Proctor Crater Dunes.jpg"/><p class="thumbcontent">January 1, 2020<br/>Proctor Crater Dunes</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Reull Vallis.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Reull Vallis.jpg"/><p class="thumbcontent">January 1, 2020<br/>Reull Vallis</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Ariadnes Colles3.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Ariadnes Colles3.jpg"/><p class="thumbcontent">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Sirenum Fossae.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Sirenum Fossae.jpg"/><p class="thumbcontent">January 1, 2020<br/>Sirenum Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/South Polar Cap.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/South Polar Cap.jpg"/><p class="thumbcontent">January 1, 2020<br/>South Polar Cap</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Niger Vallis.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Niger Vallis.jpg"/><p class="thumbcontent">January 1, 2020<br/>Niger Vallis</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Daedalia Planum.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Daedalia Planum.jpg"/><p class="thumbcontent">January 1, 2020<br/>Daedalia Planum</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Icaria Fossae.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Icaria Fossae.jpg"/><p class="thumbcontent">January 1, 2020<br/>Icaria Fossae</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Ariadnes Colles4.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Ariadnes Colles4.jpg"/><p class="thumbcontent">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/South Polar Cap.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/South Polar Cap.jpg"/><p class="thumbcontent">January 1, 2020<br/>South Polar Cap</p></div></a><a class="fancybox-thumbs" data-fancybox-group="thumb" href="image/mars/Daedalia Planum.jpg"><div class="thmb"><img alt="" class="thumbimg" src="image/mars/Daedalia Planum.jpg"/><p class="thumbcontent">January 1, 2020<br/>Daedalia Planum</p></div></a></div>
    </div>
    <!-- first div ends -->
    <!-- second div starts -->
    <div class="col-md-12 grid-margin" id="column">
    <ul class="post-list">
    <li class="post-heading"></li>
    </ul>
    </div>
    <!-- second div starts -->
    </div>
    <div class="first imgcontainer mt-3">
    <div class="col-md-12">
    <div class="row">
    <div class="col-md-3">
    <img id="pic" src=""/>
    </div>
    </div>
    </div>
    </div>
    <!-- end -->
    <div class="module_gallery container">
    <div class="col-md-12">
    <div class="row">
    <div class="col-md-6">
    <div class="card">
    <img alt="Card image cap" class="card-img-top" src="https://www.jpl.nasa.gov/assets/images/content/tmp/images/jpl_photojournal(3x1).jpg"/>
    <div class="card-body">
    <h5 class="card-title">JPL Photojournal</h5>
    <p class="card-text">Access to the full library of publicly released images from various Solar System exploration programs</p>
    </div>
    </div>
    </div>
    <div class="col-md-6">
    <div class="card">
    <img alt="Card image cap" class="card-img-top" src="https://www.jpl.nasa.gov/assets/images/content/tmp/images/nasa_images(3x1).jpg"/>
    <div class="card-body">
    <h5 class="card-title">Great images in NASA</h5>
    <p class="card-text">A selection of the best-known images from a half-century of exploration and discovery</p>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="multi_teaser">
    <div class="container">
    <h1>You Might Also Like</h1>
    <div class="col-md-12 mt-5">
    <div class="row">
    <div class="col-md-4">
    <div class="card">
    <img alt="Card image cap" class="card-img-top" src="https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA24304---CatScanMars-16-640x350.gif"/>
    <div class="card-body">
    <p class="card-text">Access to the full library of publicly released images from various Solar System exploration programs</p>
    </div>
    </div>
    </div>
    <div class="col-md-4">
    <div class="card">
    <img alt="Card image cap" class="card-img-top" src="https://imagecache.jpl.nasa.gov/images/640x350/PIA23491-16-640x350.jpg"/>
    <div class="card-body">
    <p class="card-text">Access to the full library of publicly released images from various Solar System exploration programs</p>
    </div>
    </div>
    </div>
    <div class="col-md-4">
    <div class="card">
    <img alt="Card image cap" class="card-img-top" src="https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA23180-16-640x350.gif"/>
    <div class="card-body">
    <p class="card-text">Access to the full library of publicly released images from various Solar System exploration programs</p>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="footer">
    <div class="container">
    <div class="col-md-12">
    <div class="row">
    <div class="col-md-3">
    <h4>About JPL</h4>
    <ul>
    <li>About JPL</li>
    <li>JPL Vision</li>
    <li>Executive Council</li>
    <li>History</li>
    </ul>
    </div>
    <div class="col-md-3">
    <h4>Education</h4>
    <ul>
    <li>Intern</li>
    <li>Learn</li>
    <li>Teach</li>
    <li>News</li>
    </ul>
    </div>
    <div class="col-md-3">
    <h4>Our Sites</h4>
    <ul>
    <li>Asteroid Watch</li>
    <li>Basics of Spaceflight</li>
    <li>Cassini - Mission to Saturn</li>
    <li>Climate Kids</li>
    </ul>
    </div>
    <div class="col-md-3">
    <h4>Galleries</h4>
    <ul>
    <li>JPL Space Images</li>
    <li>Videos</li>
    <li>Infographics</li>
    <li>Photojournal</li>
    </ul>
    </div>
    </div>
    </div>
    </div>
    </div>
    <!--<div class="showFullimage">
    	<button class="btn btn-outline-light hideimage" onclick=hideimage()> Close</button>
    	<img class="fullimage fade-in" src="">
    </div>-->
    <!-- <script src="js/jquery.easeScroll.js"></script>  -->
    <script src="js/jquery-3.5.1.min.js"></script>
    <!-- <script src="js/jquery-3.2.1.slim.min.js"></script> -->
    <script src="js/demo.js"></script>
    <!-- <script src="js/app.js"></script> -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="js/fancyBox/jquery.fancybox.pack.js?v=2.1.5" type="text/javascript"></script>
    <link href="js/fancyBox/jquery.fancybox.css?v=2.1.5" media="screen" rel="stylesheet" type="text/css"/>
    <link href="js/fancyBox/helpers/jquery.fancybox-thumbs.css?v=1.0.7" rel="stylesheet" type="text/css"/>
    <script src="js/fancyBox/helpers/jquery.fancybox-thumbs.js?v=1.0.7" type="text/javascript"></script>
    <div class="fancybox-overlay fancybox-overlay-fixed" style="width: auto; height: auto; display: block;"><div class="fancybox-wrap fancybox-desktop fancybox-type-image" style="width: 670px; height: 380px; position: absolute; top: 110px; left: 65px; opacity: 0.10174; overflow: hidden;" tabindex="-1"><div class="fancybox-skin" style="padding: 15px; width: auto; height: auto;"><div class="fancybox-outer"><div class="fancybox-inner" style="overflow: visible; width: 640px; height: 350px;"><img alt="" class="fancybox-image" src="image/featured/mars3.jpg"/></div></div></div></div></div></body></html>




```python
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
```




    'image/featured/mars3.jpg'




```python
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
```




    'https://spaceimages-mars.com/image/featured/mars3.jpg'



## Mars Facts


```python
# Use `pd.read_html` to pull the data from the Mars-Earth Comparison section
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mars - Earth Comparison</td>
      <td>Mars</td>
      <td>Earth</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Diameter:</td>
      <td>6,779 km</td>
      <td>12,742 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.39 × 10^23 kg</td>
      <td>5.97 × 10^24 kg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Distance from Sun:</td>
      <td>227,943,824 km</td>
      <td>149,598,262 km</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a DataFrame
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mars</th>
      <th>Earth</th>
    </tr>
    <tr>
      <th>Description</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mars - Earth Comparison</th>
      <td>Mars</td>
      <td>Earth</td>
    </tr>
    <tr>
      <th>Diameter:</th>
      <td>6,779 km</td>
      <td>12,742 km</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.39 × 10^23 kg</td>
      <td>5.97 × 10^24 kg</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Distance from Sun:</th>
      <td>227,943,824 km</td>
      <td>149,598,262 km</td>
    </tr>
    <tr>
      <th>Length of Year:</th>
      <td>687 Earth days</td>
      <td>365.24 days</td>
    </tr>
    <tr>
      <th>Temperature:</th>
      <td>-87 to -5 °C</td>
      <td>-88 to 58°C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_html()
```




    '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Mars</th>\n      <th>Earth</th>\n    </tr>\n    <tr>\n      <th>Description</th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Mars - Earth Comparison</th>\n      <td>Mars</td>\n      <td>Earth</td>\n    </tr>\n    <tr>\n      <th>Diameter:</th>\n      <td>6,779 km</td>\n      <td>12,742 km</td>\n    </tr>\n    <tr>\n      <th>Mass:</th>\n      <td>6.39 × 10^23 kg</td>\n      <td>5.97 × 10^24 kg</td>\n    </tr>\n    <tr>\n      <th>Moons:</th>\n      <td>2</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>Distance from Sun:</th>\n      <td>227,943,824 km</td>\n      <td>149,598,262 km</td>\n    </tr>\n    <tr>\n      <th>Length of Year:</th>\n      <td>687 Earth days</td>\n      <td>365.24 days</td>\n    </tr>\n    <tr>\n      <th>Temperature:</th>\n      <td>-87 to -5 °C</td>\n      <td>-88 to 58°C</td>\n    </tr>\n  </tbody>\n</table>'




```python
browser.quit()
```


```python

```
