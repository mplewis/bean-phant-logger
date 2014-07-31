# Bean-to-Phant Logger

Use the [LightBlue Bean](http://punchthrough.com/bean/) to log data over time.

Save your data to Sparkfun's [free IoT storage service](https://data.sparkfun.com/) running [Phant](http://phant.io/).

[Punch Through Design](http://punchthrough.com) has a data stream that uses a Bean with an attached light sensor. [Check it out live!](https://data.sparkfun.com/streams/4JJ8xKpVNEHqo4lKlx29)

# Setup

1. Copy `sample_config.py` to `config.py`.
2. Edit `config.py`, setting your public/private keys and your desired logging interval.
3. Install the Python script's requirements with `pip3 install -r requirements.txt`.
4. Connect to your Bean with the Bean Loader App.
5. Program your Bean with `logger_sketch/logger_sketch.ino`.
6. Use your Bean as a Virtual Serial device by right-clicking on it and selecting the menu option. It'll look like this when you're done:

![Bean as Virtual Serial menu](http://i.imgur.com/dKpgldI.png =512x)

# Usage

1. Run the script with `python3 logger.py`.
2. Watch data flow into your Sparkfun data stream!

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time. You can also tweet me at [mplewis](http://twitter.com/mplewis) or email me at [matt@mplewis.com](mailto:matt@mplewis.com).

# License

Copyright (c) 2014 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).
