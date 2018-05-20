# random-bmp-generator
Contains scripts to generate image bitmaps with random RGB values

## Requirements
This code runs on **Python3**.

You need to use `pip install` to install the following dependencies before our scripts work.

```
pip install requests, Pillow
```

## Running
You can generate the bmp image by running the `generate_random_bmp.py` file on the console as follows:

```
python generate_random_bmp.py
```



## Troubleshooting
If there are any errors when retrieving the random integers from the [https://www.random.org/](https://www.random.org/) web server, your quota might have run out. Running the bmp generator program once uses up approximately 400,000 bits of the 1,000,000 bit quota allocated to your IP Address. To wait for it to be topped-up, wait till midnight on UTC.