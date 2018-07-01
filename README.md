# PS3 Update Proxy

Circumvents the update check for PS3's. This will make you able to use PSN with a lower PS3 firmware.

## Installation

Install mitmproxy from [here](https://github.com/mitmproxy/mitmproxy/releases) or from your GNU/Linux distribution.

Clone this git repository somewhere with:

```
git clone https://github.com/rrooij/ps3_update_proxy.git
```

## Running

Run the mitmproxy binary and attach this script

```
./mitmproxy -s tls_passthrough.py -s filereplacer.py
```

Note that the first time starting a game may result in a error. It will work fine if you try again
by restarting the game.

Configure your computer's local IP address as proxy in the PS3, with port 8080.
