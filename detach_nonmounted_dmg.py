import subprocess

cmd = ['/usr/bin/hdiutil', 'info', '-plist']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, _ = process.communicate()
if 'content-hint' in out and not 'mount-point' in out:
    print 'bad'