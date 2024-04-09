# estatelookout.ai

**Estate Lookout** is a customer-centric project designed to enhance user experience in the house hunting process. By leveraging Natural Language Processing (NLP) tools such as NLTK and SpaCy, along with other sklearn tools, users can freely describe their desired property features, and the search will be processed and filtered accordingly.


## Table of Contents
  =================
* [Video Demo](#VideoDemo)
* [Dataset](#Dataset)
* [Project Structure](#Project_Structure)
* [Getting Started](#Getting_Started)


## Video Demo
...

## Dataset
- The dataset was obtained by web scraping 1670 House listings from the [allsoppandallsopp.com](https://www.allsoppandallsopp.com/) website, adhering to their terms of service.Subsequent preprocessing and cleaning were conducted to refine the data for analysis.
- The data scraping process is available in the notebook `scrape_data.ipynb`.

## Project Structure
```
estate_lookout/
│
├── app/
│   ├── __init__.py
│   ├── app.py          # Streamlit web application script
│
├── model/
│   ├── listing_model.pkl  # pre-trained on the dataset and joblib serialized file
│   ├── Listing_Model.py   # Python script containing Listing_Model class
│
├── data/
│   ├── estate_data.csv    # Dataset file
│   ├── contact_data.csv   # Contact information file
│   ├── scrape_data.ipynb   # webscraping process
│
├── Dockerfile             # Dockerfile for building the Docker image
├── docker-compose.yml     # Docker Compose configuration file
├── requirements.txt       # Python dependencies file
└── README.md
```

## Contributing

Contributions to Estate Lookout are welcome! Whether you're interested in fixing a bug, adding a new feature, or improving the project documentation, I'd love to have your help.

Feel free to fork the repository, make your changes, and submit a pull request. I appreciate any contributions that help make OmniLightVision better for everyone.

Let's collaborate and make Estate Lookout even better together! 🚀

## Getting Started
  Follow theses steps to set up the environment and run the application.
  
1.Clone the forked repository.
```
git clone https://github.com/NabilYimer/estatelookout.ai.git

cd estatelookout.ai.git
```

2. Run the application.
```
docker-compose up
```

## Author
* ```Nabil Yimer```
