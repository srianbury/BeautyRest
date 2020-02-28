# BeautyRest
The BeautifulSoup REST-ful API

### Quick Start (node example)
```
fetch('https://beautyrest.herokuapp.com/v1/soup', {
  method: 'POST',
  body: JSON.stringify({ url: 'https://www.google.com' }),
  headers: { 'Content-Type': 'application/json' },
});
```

### Example
[codesandbox](https://codesandbox.io/s/sleepy-shirley-rn0dd)

### Inspiration
I wanted developers (including myself) to be able to use Selenium and BeautifulSoup without having to deal with the selenium issues during
deployment.  With this project you can add web scrapping to your application without worrying about setting up the selenium webdriver.


### New Features
Open to adding new features and adapting for additional requirements, just open an issue.