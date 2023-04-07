<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/antonin-lfv/Bonx_monsters">
    <img src="assets/img/logo_bonx.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Bonx monster</h3>

  <p align="center">
    An awesome game to enjoy in your spare time!
    <br />
    <a href="https://github.com/antonin-lfv/Bonx_monsters/blob/main/ReadMe.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/antonin-lfv/Bonx_monsters">View Demo</a>
    ·
    <a href="https://github.com/antonin-lfv/Bonx_monsters/issues">Report Bug</a>
    ·
    <a href="https://github.com/antonin-lfv/Bonx_monsters/issues">Request Feature</a>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

![Bonx monster home page](https://user-images.githubusercontent.com/63207451/229769113-150f328e-c4e4-4fdf-a9bb-2e89bc8ccb25.png)

Bonx Monster is a game where you collect and own monsters. The objective is to gather all the monsters and raise them to
the highest level. To achieve this, you can have them battle against bosses, explore dungeons, or purchase monster cards
in the store.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section highlights several major tools used in building our project. For a comprehensive list, please refer to
the `requirements.txt` file.

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
* [![Flask][Flask.com]][Flask-url]
* [![Python][Python.com]][Python-url]
* [![SQLAlchemy][SQLAlchemy.com]][SQLAlchemy-url]
* [![Gunicorn][Gunicorn.com]][Gunicorn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install a recent version of Python (3.9 or higher) and pip.

### Installation

_Follow the steps below to set up a local copy of the project and get it running on your local machine._

1. Clone the repo
   ```sh
   git clone https://github.com/antonin-lfv/Bonx_monsters.git
   ```

2. Add the right permissions to the scripts

   ```bash
   chmod +x install_requirements.sh
   chmod +x start_bonx_monster.sh
   chmod +x reset_data.sh
   chmod +x update_bonx_app.sh
   ```

3. Install requirements and dependencies
   ```sh
   ./install_requirements.sh
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->

## Usage

1. To start the game, run the following command:

   ```bash
   ./start_bonx_monster.sh
   ```

_(use `Ctrl + C` to stop the server)_

2. To reset the data, run the following command:

   ```bash
   ./reset_data.sh
   ```

_This will delete all the data in the database (users, monsters, cards, etc.)_

3. To update the game, run the following command:

   ```bash
   ./update_bonx_app.sh
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [ ] Add sorting system during monster selection in battle


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->

## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Antonin - antoninlefevre45@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white

[Bootstrap-url]: https://getbootstrap.com

[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white

[JQuery-url]: https://jquery.com

[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white

[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/

[SQLAlchemy.com]: https://img.shields.io/badge/SQLAlchemy-000000?style=for-the-badge&logo=sqlalchemy&logoColor=white

[SQLAlchemy-url]: https://www.sqlalchemy.org/

[Gunicorn.com]: https://img.shields.io/badge/Gunicorn-000000?style=for-the-badge&logo=gunicorn&logoColor=white

[Gunicorn-url]: https://gunicorn.org/

[Python.com]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white

[Python-url]: https://www.python.org/