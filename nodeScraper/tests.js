const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();
const port = 8000;

const today = new Date();
const formattedDate = today.toLocaleDateString('en-GB', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
}).replace(/\//g, '-');

// const { Builder, By, Key, until } = require('selenium-webdriver');
// const chrome = require('selenium-webdriver/chrome');

// // Set up Chrome options (headless mode)
// const chromeOptions = new chrome.Options();
// chromeOptions.addArguments('--headless'); // Run in headless mode (no GUI)

// // Create a WebDriver instance with Chrome
// const driver = new Builder()
//   .forBrowser('chrome')
//   .setChromeOptions(chromeOptions)
//   .build();


app.get('/', async (req, res) => {
    try {
        let team1 = "Rouen"
        let team2 = "Monaco"
        
        team1 = team1.toLowerCase().replace(' ', '-');
        team2 = team2.toLowerCase().replace(' ', '-');
        
        // Replace the URL with the website you want to scrape
        const url = `https://www.mightytips.com/football-predictions/${team1}-vs-${team2}-prediction-${formattedDate}/`;
        console.log(url);
        // Fetch HTML content from the website
        const response = await axios.get(url);
        
        // Load the HTML content into Cheerio for easy manipulation
        const $ = cheerio.load(response.data);
        
        // Extract the data you need using Cheerio selectors
        const predictions = [];
        const main = $('.mtl-prediction-main2__name').text()
        predictions.push(main)
        const additional = $('.mtl-prediction-additional__name').each((index, element) => {
            // console.log($(element).text());
            predictions.push($(element).text());
        });;
        console.log(predictions);
    } catch (error) {
        res.status(500).send(`Internal Server Error: ${error}`);
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});