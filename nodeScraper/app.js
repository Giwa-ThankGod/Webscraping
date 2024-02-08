const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

const router = express.Router();

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Use body-parser middleware to parse incoming requests with JSON or form data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

const today = new Date();
const formattedDate = today.toLocaleDateString('en-CA', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
});

// Define the web scraper function
const scrapeFreesupertips = async (team1, team2) => {

    team1 = team1.toLowerCase().replace(' ', '-');
    team2 = team2.toLowerCase().replace(' ', '-');

    try {
        // Replace the URL with the website you want to scrape
        const url = `https://www.freesupertips.com/predictions/${team1}-vs-${team2}-predictions-betting-tips-match-previews/`;
        
        // Fetch HTML content from the website
        const response = await axios.get(url);
        
        // Load the HTML content into Cheerio for easy manipulation
        const $ = cheerio.load(response.data);
        
        // Extract the data you need using Cheerio selectors
        const predictions = [];
        const pageTitle = $('.IndividualTipPrediction h4').each((index, element) => {
            $(element).each((index, value) => {
                // console.log($(value).text());
                predictions.push($(value).text());
            });;
        });;
      
        return {"title": "Freesupertips", "predictions": predictions};
    } catch (error) {
        return {"title": "Freesupertips", "predictions": null}
    }
};

const scrapemrfixitstips = async (team1, team2) => {

    team1 = team1.toLowerCase().replace(' ', '-');
    team2 = team2.toLowerCase().replace(' ', '-');

    try {
        // Replace the URL with the website you want to scrape
        const url = `https://mrfixitstips.co.uk/previews/${team1}-vs-${team2}-prediction-and-betting-tips/`;
        
        // Fetch HTML content from the website
        const response = await axios.get(url);
        
        // Load the HTML content into Cheerio for easy manipulation
        const $ = cheerio.load(response.data);
        
        // Extract the data you need using Cheerio selectors
        const predictions = [];
        const pageTitle = $('.row.alt_colors').each((index, element) => {
            $(element).each((index, value) => {
                // console.log($(value).find('.col-md-6').find('strong').text());
                predictions.push($(value).find('.col-md-6').find('strong').text());
            });;
        });;
        return {"title": "Mrfixitstips", "predictions": predictions};
    } catch (error) {
        return {"title": "Mrfixitstips", "predictions": null}
    }
};

const scrapethehardtackle = async (team1, team2) => {

    team1 = team1.toLowerCase().replace(' ', '-');
    team2 = team2.toLowerCase().replace(' ', '-');

    try {
        // Replace the URL with the website you want to scrape
        const url = `https://thehardtackle.com/round-up/${formattedDate}/${team1}-vs-${team2}-preview-and-prediction/`;

        // Fetch HTML content from the website
        const response = await axios.get(url);
        
        // Load the HTML content into Cheerio for easy manipulation
        const $ = cheerio.load(response.data);
        
        // Extract the data you need using Cheerio selectors
        const predictions = [];
        const pageTitle = $('.content-inner').each((index, element) => {
            $(element).each((index, value) => {
                // console.log($(value).find('h4').text());
                predictions.push($(value).find('h4')[-1].text());
            });;
        });;
        return {"title": "Thehardtackle", "predictions": predictions};
    } catch (error) {
        return {"title": "Thehardtackle", "predictions": null}
    }
};


const scrapemightytips = async (team1, team2) => {

    const today = new Date();
    const mightytipsDate = today.toLocaleDateString('en-GB', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    }).replace(/\//g, '-');

    team1 = team1.toLowerCase().split(' ')[0];
    team2 = team2.toLowerCase().split(' ')[0];

    try {
        // Replace the URL with the website you want to scrape
        const url = `https://www.mightytips.com/football-predictions/${team1}-vs-${team2}-prediction-${mightytipsDate}/`;

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
        return {"title": "Mightytips", "predictions": predictions};
    } catch (error) {
        return {"title": "Mightytips", "predictions": null}
    }
};

const scrapescores24 = async (team1, team2) => {

    const today = new Date();
    const scores24Date = today.toLocaleDateString('en-GB', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    }).replace(/\//g, '-');

    team1 = team1.toLowerCase().replace(' ', '-');
    team2 = team2.toLowerCase().replace(' ', '-');

    try {
        // Replace the URL with the website you want to scrape
        const url = `https://scores24.live/en/soccer/m-${scores24Date}-${team1}-${team2}-prediction/`;
        console.log(url);
        // Fetch HTML content from the website
        const response = await axios.get(url);
        
        // Load the HTML content into Cheerio for easy manipulation
        const $ = cheerio.load(response.data);
        
        // Extract the data you need using Cheerio selectors
        const predictions = [];
        const main = $('.sc-10cwpmp-2').text()
        predictions.push(main)
        // const additional = $('.mtl-prediction-additional__name').each((index, element) => {
        //     // console.log($(element).text());
        //     predictions.push($(element).text());
        // });;
        return {"title": "Scores24", "predictions": predictions};
    } catch (error) {
        return {"title": "Scores24", "predictions": null}
    }
};

app.get('/', async (req, res) => {
  data = null
  res.render('index', {data});
});

router.post('/', async (req, res) => {
  try {
    // Get team names from query parameters
    let { team1, team2 } = req.body;

    // Check if both team names are provided
    if (!team1 || !team2) {
      return res.status(400).send('Both team1 and team2 parameters are required.');
    }

    // Call the web scraper function with the provided team names
    const freesupertips = await scrapeFreesupertips(team1, team2);
    const mrfixitstips = await scrapemrfixitstips(team1, team2);
    const thehardtackle = await scrapethehardtackle(team1, team2);
    const mightytips = await scrapemightytips(team1, team2);
    const scores24 = await scrapescores24(team1, team2);
    
    const data = {
        team1: team1,
        team2: team2,
        predictions: [freesupertips, mrfixitstips, thehardtackle, mightytips, scores24]
    };
    console.log(mightytips);
    res.render('index', {data});
  } catch (error) {
    // console.error(error);
    res.status(500).send(`Internal Server Error: ${error}`);
  }
});
app.use('/prediction', router)

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
