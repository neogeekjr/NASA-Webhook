
# Discord NASA APOD Webhook

Uses [NASA's](https://api.nasa.gov/) APOD API to get a daily space photo and send it to a Discord webhook


## Installation and running

Install 

```bash
git clone https://github.com/neogeekjr/NASA-Webhook.git
```
Edit Config

`config.json`
```json
{
    "Version":1.00,
    "NASA_API_Key":"<ADD YOUR API KEY HERE>",
    "Webhook_URL":"<ADD YOUR WEBHOOK HERE>"
}
```

Then add to a cron job of your choosing 
