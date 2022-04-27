<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/pkkulhari/sajes">
    <img src="public/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SAJES</h3>

  <p align="center">
    Website for Shree Amar Jyot Education Society, Daman
    <br />
    <a href="https://github.com/pkkulhari/sajes/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://sajes.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/pkkulhari/sajes/issues">Report Bug</a>
    ·
    <a href="https://github.com/pkkulhari/sajes/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://sajes.praveen.ninja/)

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com)
- [JQuery](https://jquery.com)
- Postgres
- Heroku

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To setup a development environment, you are required `Python` with `pip` and `NodeJS` with `npm`

- pip

  ```sh
  pip install --upgrade pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pkkulhari/sajes.git
   ```
2. Change the dir to **sajes**
   ```sh
   cd sajes
   ```
3. rename `.env-example` file to `.env` or create a new one, and change variable
   ```sh
   mv ./.env-example ./.env
   ```
4. Install pip packages

   ```sh
   pip install -r requirements.txt
   ```

5. Run DB migrations
   ```sh
   python manage.py migrate
   ```
6. Finally, start the app by spinning up django dev server
   ```sh
   python manage.py runserver
   ```

Now, the app should listening on http://127.0.0.1:8000/

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: public/images/screenshot.png
