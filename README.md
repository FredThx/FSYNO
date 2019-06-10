# FSYNO

Synology DownloadStation upload analyser

![/](https://github.com/FredThx/FSYNO/blob/master/images/index.PNG)
![/task_id](https://github.com/FredThx/FSYNO/blob/master/images/file.PNG)
![/total](https://github.com/FredThx/FSYNO/blob/master/images/total.PNG)

## Getting Started

These instructions explain how to install the uploader analyser.
The uploader analyser contain
* a python script to store every hour upload Statistique
* a web server for data analyse

Datas are stored in a json file : ds.json

### Prerequisites

A linux environment with python 3 installed.
(test on raspian and ubuntu on windows 10)

### Installing

#### stat_upload.py

use crontab to execute the script to store upload Statistique every hour

```
sudo crontab -e -u root
add 00 * * * * python #your_path#/stat_upload.py #your path#/ds.json
```

#### web server

synopy : python librairie to use DownloadStation API (https://pypi.org/project/synopy/)

```
pip3 install synopy
```

humanfriendly

```
pip3 ibnstall humanfriendly
```

Copy this folder where you want
Change
* fsyno.service
* fsyno.sh
with the good paths

Enable the service server :

```
sudo systemctl enable #your_path#/fsyno.service
sudo systemctl start fsyno.service
```

## Built With

* [synopy](https://github.com/graingert/synopy) - Python library for the Synology Download Station API
* [Flask](http://flask.pocoo.org/) - web development, one drop at a time

## Author

* FredThx

## Thanks

* [Thomas Grainger](https://github.com/graingert) - for synopy

## License

This project is licensed under CeCILL license : the French open source license.
(please see LICENSE)
