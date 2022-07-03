# Spotify Connector

## Getting Started
Before you can start using the spotify API, you need to create an app

### Create a Spotify App
1. Go to the [spotify developer website](https://developer.spotify.com/dashboard/)
2. Log in
3. Click `CREATE AN APP`
4. Give your app a name and description and click `CREATE`

### Set the callback URL
1. From the Spotify dashboard for your app, click `EDIT SETTINGS`
2. Enter a redirect url of `http://localhost:8888/callback` and click `ADD`
3. Click `SAVE`

### Set the environment variables
We're going to use a library called SpotiPy which needs two environment variables setting

To make this easier we're going to use the `dotenv` library to read these from a file called `.env`

1. If you haven't done so already, copy the sample.env file into a file called `.env` by running
```commandline
    cp sample.env .env
```
2. Copy the `client id` and paste it next to the `=` for `SPOTIPY_CLIENT_SECRET` in the `.env` file

## Extension ideas
* Use `progress_ms` and `duration_ms` and a loop to update the display when the next track plays