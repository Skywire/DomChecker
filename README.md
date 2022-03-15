# Dom Checker

Check a Magneto PDP and trigger a notification if the product count is less than expected

## Installation

```
git clone https://github.com/Skywire/DomChecker.git ~/DomChecker
cd DomChecker
[python3 executable] -m pip install -r requirements.txt
```

## Slack Configuration

Ensure your slack bot has chat:write and file:write permissions

## Usage
`[python3 executable] ~/DomChecker/main.py [url] [search class] [min product count] [slack channel] [slack token]`

e.g
`https://example.com/category .product 10 #notifications a-bot-user-slack-token`
