Pushing updates to the website:

1) Copy files into the server with scp. The easiest way to do this is put everything into a folder called public_html, cd into its parent directory, and copy everything in with

```
scp -r public_html robotics@ssh.ocf.berkeley.edu:~/public_html
```

password is the same as the email.

Or you can manually copy files individually. The root folder of the website (the one that contains flaskyapplication.py) is at robotics@ssh.ocf.berkeley.edu:~/public_html

2) ssh into the server at robotics@ssh.ocf.berkeley.edu and run

```
touch ./public_html/run.fcgi
```

That's it!

Troubleshooting:
A collection of notes on dealing with the server
- Sometimes if someone does something wrong it screws up the symlinks. When this happens, the website will stop updating as expected. This is because the actual website is hosted from /services/http/users/r/robotics on the OCF server, not the /home/r/ro/robotics/public_html folder (aka ~/public_html) folder that things are copied into. Recreate the symlink and everything will work again.
- After running touch on run.fcgi the updates should go live in ~30 seconds or so. If it takes more than a minute or two it's probably a problem with the update.
- When putting links to other pages use absolute paths with a slash on the end (e.g. /projects/new_project/). Leaving off the slash ends up putting run.fcgi in the middle of the displayed url about half the time, and relative paths don't work for the most part.


2016/08/04 update:
A git repo has been created on the server. Now to update the website, just ssh into the server, cd into public_html, then run git pull and you're good! Not sure why I didn't set it up this way to begin with....

2016/08/21 update:
A dynamic page loader has been created! Now, new pages will no longer require changes to flasklyapplication.py as long as
- The file and directory names are in lowercase
- The directory names aren't repeated within the same level (example: having both /templates/foo/bar/ and /templates/foobar/bar/ would be bad. In general just don't repeate directory names, it makes things easier)
- Templates are named the same thing as the directory (example: the template for clubs is /templates/related/clubs/clubs.html)
