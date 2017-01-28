# Explorer Phat Dashboard

A dashboard for Explorer PHAT (Explorer HAT) to read and control the
inputs, outputs, analogs and motors remotely.

![](http://i.imgur.com/JKqhkmX.gif)

## Requirements

* Raspberry Pi with Explorer PHAT/HAT attached
* [Explorer HAT Python library](https://github.com/pimoroni/explorer-hat)
installed on Raspberry Pi
* [SSH access](https://www.raspberrypi.org/documentation/remote-access/ssh/)
to your Raspberry Pi

## Installation

1. Clone the project:

 ```bash
git clone git@github.com:LowieHuyghe/explorer-phat-dashboard.git
```
2. Move into the new directory:

 ```bash
cd explorer-phat-dashboard
```
3. Setup virtualenv and activate it
4. Install the requirements:

 ```bash
pip install -r requirements.txt
```

5. Make a copy of `config.example.ini` named `config.ini`
6. Fill in `config.ini` to match your configuration


## Run

 ```bash
python dashboard.py
```

> Note: Make sure your virtualenv is active when running the script.

## Troubleshooting

* In case the dashboard has crashed and won't respond:
  - Find the dashboard- and ssh-process and kill them

 ```bash
 > ps aux | grep dashboard.py
 # Copy the process id
 > kill -9 XXXXXX
 > ps aux | grep ssh
 # Copy the process id of the opened ssh session (if one)
 > kill -9 XXXXXX
```
