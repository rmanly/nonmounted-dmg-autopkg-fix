#!/usr/bin/python

import plistlib
import subprocess

__author__ = 'Ryan Manly'
__copyright__ = 'Copyright (C) 2018 Ryan Manly'
__license__ = 'MIT License'
__version__ = '0.1'


def detach(dev_name):
    """Attempt to detach a dmg based on device name."""

    cmd = ['/usr/bin/hdiutil', 'detach', dev_name]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        print 'Could not detach disk' + dev_name


def get_dev_name(entity):
    """Return the device name for a given entity
    (list) -> string
    
    >>> get_dev_name(entity)
    /dev/disk2
    """
    return entity[0]['dev-entry']


def get_dmg_info():
    """Return output of hdiutil info command
    () -> plist
    """
    cmd = ['/usr/bin/hdiutil', 'info', '-plist']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = process.communicate()
    return plistlib.readPlistFromString(out)


def is_mounted(image):
    """Return whether the image shows a mount point
    (plistlib._InternalDict) -> bool
    >>> is_mounted(image)
    True
    >>> is_mounted(image)
    False
    """
    return 'mount-point' in str(image)


if __name__ == '__main__':
    plist = get_dmg_info()

    for image in plist['images']:
        if is_mounted(image):
            continue
        dev_name = get_dev_name(image['system-entities'])
        # Toyed with the idea of logging, I don't care enough
        # name = dev_name.split('/')[-1]
        detach(dev_name)
