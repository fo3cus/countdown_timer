<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fo3cus/countdown_timer">
    <img src="assets/logo.png" alt="Logo" width="216" height="124">
  </a>

<h3 align="center">Countdown Timer</h3>

  <p align="center">
    This is a countdown timer created in Python using Tkinter. <br />
    It will run full screen on execution and display large numbers on a black background.
    <br />
    <br />
    <a href="https://github.com/fo3cus/countdown_timer/issues">Report Bug</a>
    ·
    <a href="https://github.com/fo3cus/countdown_timer/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Countdown Timer Screen Shot][product-screenshot]

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python](https://www.python.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [pygame](https://www.pygame.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

All instructions are based on Ubuntu 20.04.

### Prerequisites

Step 1 — Setting Up Python 3

Ubuntu 20.04 and other versions of Debian Linux ship with Python 3 pre-installed. To make sure that our versions are up-to-date, let’s update and upgrade the system with the apt command to work with Ubuntu’s Advanced Packaging Tool:

```sh
sudo apt update
sudo apt -y upgrade
```

The -y flag will confirm that we are agreeing for all items to be installed, but depending on your version of Linux, you may need to confirm additional prompts as your system updates and upgrades.

Once the process is complete, we can check the version of Python 3 that is installed in the system by typing:

```sh
python3 -V
```

You’ll receive output in the terminal window that will let you know the version number. While this number may vary, the output will be similar to this:

```sh
Output
Python 3.8.10
```

To manage software packages for Python, let’s install pip, a tool that will install and manage programming packages we may want to use in our development projects. You can learn more about modules or packages that you can install with pip by reading “How To Import Modules in Python 3.”

```sh
sudo apt install -y python3-pip
```

Python packages can be installed by typing:

```sh
pip3 install package_name
```

For this project you'll need to install pygame.

```sh
pip3 install pygame
```

Also install the tkinter requirement to the system.

```sh
sudo apt install -y python3-tk
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fo3cus/countdown_timer.git
   ```
2. Install requirements packages
   ```sh
   pip3 install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Run timer4 file from a terminal

```sh
cd <install_path>/countdown_timer/

python3 timer4.py
```

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Create requirements.txt
- [x] Update this README
- [x] Replace alert sound
- [x] Cleanup unnecessary files
- [x] Document/comment the code

See the [open issues](https://github.com/fo3cus/countdown_timer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

James Rollinson - contact@rollinson.nz

Project Link: [https://github.com/fo3cus/countdown_timer](https://github.com/fo3cus/countdown_timer)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/fo3cus/countdown_timer.svg?style=for-the-badge
[contributors-url]: https://github.com/fo3cus/countdown_timer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fo3cus/countdown_timer.svg?style=for-the-badge
[forks-url]: https://github.com/fo3cus/countdown_timer/network/members
[stars-shield]: https://img.shields.io/github/stars/fo3cus/countdown_timer.svg?style=for-the-badge
[stars-url]: https://github.com/fo3cus/countdown_timer/stargazers
[issues-shield]: https://img.shields.io/github/issues/fo3cus/countdown_timer.svg?style=for-the-badge
[issues-url]: https://github.com/fo3cus/countdown_timer/issues
[license-shield]: https://img.shields.io/github/license/fo3cus/countdown_timer.svg?style=for-the-badge
[license-url]: https://github.com/fo3cus/countdown_timer/blob/main/LICENSE.txt
[product-screenshot]: assets/screenshot.png
