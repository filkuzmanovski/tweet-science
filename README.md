# Tweet Science

Tweet science is a simple application allowing you to mine data from Twitter.

  - Work in Progress
  - D3 Integration Coming Soon
  - Eventual integration with Spotify/Luigi


  ## Environment

  ### Autoenv

  I use **autoenv** to automatically activate the conda environment.

  Install it easily:

  ##### Mac OS X Using Homebrew

  ```
  $ brew install autoenv
  $ echo "source $(brew --prefix autoenv)/activate.sh" >> ~/.bash_profile

  ```

  ##### Using git

  ```
  $ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
  $ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
  ```

  Head over to the autoenv repository for further configuration instructions

  [Autoenv Github Repo]: https://github.com/kennethreitz/autoenv	"autoenv"

  ### Safely storing API Credentials

  To use the Twitter API and safely store the credentials, I export the 4 variables to my ZSH profile.

  Open Terminal

  ```
  nano ~/.zshrc
  export TWITTER_CONSUMER_KEY="Your Consumer Key"
  export TWITTER_CONSUMER_SECRET="Your Consumer Secret"
  export TWITTER_TOKEN="Your Access Token"
  export TWITTER_TOKEN_SECRET="Your Token Secret"
  ```


### Version
1.0
