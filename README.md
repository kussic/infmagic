# infmagic.py
 _Takes a list of IPs as input and outputs the associated CIDRs based on WHOIS information. Primary useful for OSINT work, made out of frustration due to the lack of similar tools available._

```
██╗███╗   ██╗███████╗███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗
██║████╗  ██║██╔════╝████╗ ████║██╔══██╗██╔════╝ ██║██╔════╝
██║██╔██╗ ██║█████╗  ██╔████╔██║███████║██║  ███╗██║██║
██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══██║██║   ██║██║██║
██║██║ ╚████║██║     ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╗
╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝
        Version: 0.2 Codename: "Oblivious Bison"

What:
        Takes a list of IPs as input and outputs the associated CIDRs based on WHOIS information.

Dependencies:
        ipwhois & docopt (both can be pip installed)

Usage:
        infmagic.py [-h] [-c OUTPUT1] [-s OUTPUT2] -i INPUT


Options:
  -h --help           show this
  -c --csv OUTPUT1   save output as CSV
  -s --sql OUTPUT2    save output as SQLite (TODO!)
  -i INPUT            list of IPs to use
```

So seriously this was created due to pure frustration, please someone! Make something better! - I am serious...
