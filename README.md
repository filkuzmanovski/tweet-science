# Tweet Science

Tweet science is a simple application allowing you to mine data from Twitter.

  - Work in Progress
  - D3 Integration Coming Soon
  - Eventual integration with Spotify/Luigi


  ## Environment

  ### Conda

  Conda alongside autoenv is a suitable workflow to manage a python project for a particular version of python with all modules, rather than installing everything globally. Its an efficient and easy alternative to using virtualenv and so far conda environments are yet to fail me.
  Head over to [conda](http://conda.pydata.org/docs/install/quick.html) docs to install and configure your conda environment.


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

  Head over to the [autoenv](https://github.com/kennethreitz/autoenv) repository for further configuration instructions


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
