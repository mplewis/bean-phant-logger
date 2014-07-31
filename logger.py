#!/usr/bin/env python3

import config

import time
from datetime import datetime

import serial
from phant import Phant


def read_and_store(bean_serial, phant_endpoint):
    print('Requesting...')
    bean.write(b'\n')
    raw_data = bean.readline()
    data = raw_data.decode('utf-8').rstrip('\r\n')

    if len(data) == 0:
        print('Bean timed out.\n')
        return False

    data_split = data.split('\t')
    print('    %s' % datetime.now())
    for num, field in enumerate(config.DATA_FIELDS):
        print('    %s: %s' % (field, data_split[num]))

    print('Sending...')
    phant.log(*data_split)

    print('Done!\n')
    return True

print('Data destination: %s' % config.PUBLIC_KEY)
print('Data fields: %s' % str(config.DATA_FIELDS))
phant = Phant(config.PUBLIC_KEY, *config.DATA_FIELDS,
              private_key=config.PRIVATE_KEY)
bean = serial.Serial(config.BEAN_SERIAL_PATH,
                     timeout=config.BEAN_REQ_TIMEOUT_SECS)

last_run = None

while True:
    now = datetime.now()

    if last_run:
        since_last_run = (now - last_run).total_seconds()

    if not last_run or since_last_run >= config.INTERVAL_SECS:
        success = read_and_store(bean, phant)
        if success:
            last_run = now

    else:
        until_next_run = config.INTERVAL_SECS - since_last_run
        time.sleep(until_next_run)
