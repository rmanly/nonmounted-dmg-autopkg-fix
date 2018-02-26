import plistlib, subprocess

cmd = ['/usr/bin/hdiutil', 'info', '-plist']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, _ = process.communicate()
plist = plistlib.readPlistFromString(out)

def is_mounted(image):
    '''Return whether the image shows a mount point
    (plistlib._InternalDict) -> bool
    >>> is_mounted(image)
    True
    >>> is_mounted(image)
    False
    '''
    if 'mount-point' in str(image):
        return

def get_dev_name(entity):
    '''Return the base device name for a given entity
    (list) -> string
    
    >>> get_disk(entity)
    /dev/disk2

    '''
    return entity[0]['dev-entry']

def detach(dev_name):
    cmd = ['/usr/bin/hdiutil', 'detach', dev_name]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        print 'Could not detach disk' + dev_name


# TODO: need to check if nothing is mounted first
for image in plist['images']:
    if is_mounted(image):
        continue
    dev_name = get_dev_name(image['system-entities'])
    # Toyed with the idea of logging…I don't care enough
    # name = dev_name.split('/')[-1]
    detach(dev_name)
