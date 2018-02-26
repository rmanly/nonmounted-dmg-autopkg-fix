import plistlib, subprocess

cmd = ['/usr/bin/hdiutil', 'info', '-plist']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, _ = process.communicate()
plist = plistlib.readPlistFromString(out)

i = 0
# TODO: account for multiple images in various states
for image in plist['images']:
    for entity in image['system-entities']:
            print entity

# TODO: Eric Holtam mentioned I can just detach the disk# instead of rebooting
