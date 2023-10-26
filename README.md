# streamlit_app
Youtube Data Harvesting and Warehousing Project: Aarushi Kumar

Problem Statement: This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on a YouTube channel, stores it in a MongoDB database, migrates it to a SQL data warehouse, and enables users to search for channel details and join tables to view data in the Streamlit app.

The application should have the following features:

- Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.

- Option to store the data in a MongoDB database as a data lake. Ability to collect data for up to 10 different YouTube channels and store them in the data lake by clicking a button. Option to select a channel name and migrate its data from the data lake to a SQL database as tables.
  
- Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.

- YouTube API: You'll need to use the YouTube API to retrieve channel and video data. You can use the Google API client library for Python to make requests to the API.

- Store data in a MongoDB data lake: Once you retrieve the data from the YouTube API, you can store it in a MongoDB data lake. MongoDB is a great choice for a data lake because it can handle unstructured and semi-structured data easily.

- Migrate data to a SQL data warehouse: After you've collected data for multiple channels, you can migrate it to a SQL data warehouse. You can use a SQL database such as MySQL or PostgreSQL for this.

- Query the SQL data warehouse: You can use SQL queries to join the tables in the SQL data warehouse and retrieve data for specific channels based on user input. You can use a Python SQL library such as SQLAlchemy to interact with the SQL database.

- Display data in the Streamlit app: Finally, you can display the retrieved data in the Streamlit app. Overall, this approach involves building a simple UI with Streamlit, retrieving data from the YouTube API, storing it in a MongoDB data lake, migrating it to a SQL data warehouse, querying the data warehouse with SQL, and displaying the data in the Streamlit app.

Important Notes:
- The requirements.txt file stores all the libaries and modules to be installed.
- PKG_CONFIG_PATH, MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS env vars are to be set independently.
- The secrets.toml file establishes the database connection with MYSQL Server: changes to be made in secrets section of streamlit app settings.
- App credentials are personally generated: MongoDB unique client id, Youtube API key and MYSQL db credentials.
- .gitignore ignore this secrets.toml file.
- The versions mentioned in requirements.txt are latest.
- This git profile is connected with Streamlit in order to launch the app - changes are visible real time.
- Url: https://appapp-outmvqvzfxsbmmqcx2vz9d.streamlit.app/

Contributions are welcome! 
