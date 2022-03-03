
![alt text](https://pbs.twimg.com/profile_banners/1348714168782827524/1646140988/1500x500)
![Active](https://img.shields.io/badge/development%20status-active-green) ![license](https://img.shields.io/badge/license-gpl3-blue)

A python based siren detector that uses volume data from audio sinks to determine if a siren has gone off.

Data is sent to [Twitter](https://twitter.com/UkraineAlert) and [Telegram](https://t.co/oAoK13twYY)

Created by Aurora Knish from [Aurora Intel](https://twitter.com/AuroraIntel)


## Appendix

- [Info about helping:](#info-about-helping-)
  * [Contributing](#contributing)
  * [Required libraries](#required-libraries)
- [Road map and Recent additions:](#road-map-and-recent-additions-)
  * [Roadmap](#roadmap)
  * [Recent additions:](#recent-additions-)




## Info about helping:
### Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


### Required libraries

To run this project, you will need to get the following libraries

```
pip install sounddevice numpy datetime pytz tweepy telepot
```

You will also need to get API keys from Telegram and Twitter:

[Twitter API keys](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwji85Swyqn2AhUOQkEAHQd0DFQQFnoECAQQAQ&url=https%3A%2F%2Fdeveloper.twitter.com%2Fen%2Fdocs%2Ftwitter-api%2Fgetting-started%2Fgetting-access-to-the-twitter-api&usg=AOvVaw3rl-dk4Y3VvM4lwRfsMUbl)

[Telegram API keys](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjonqW3yqn2AhUUWsAKHeUwBZ8QFnoECAYQAQ&url=https%3A%2F%2Fcore.telegram.org%2F&usg=AOvVaw00WR4l6PW_bRSqM5hCaKEf)
## Road map and Recent additions:
### Roadmap
```
:soon: - To be done
:wavy_dash: - Being worked on now
:x: - Cancelled or pushed off
:heavy_check_mark: - Done
```

- Ability to detect if a stream goes down and switch to an alternate :soon:

- Add more towns :wavy_dash:
  - Kyiviy Rih :wavy_dash:
  - Dnipro :soon:

### Recent additions:

- Released code to GitHub
- Tweaked code to better support newer streams

