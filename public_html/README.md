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
- Deleting files doesn't really work. After deletion they show up again sometimes. Overwriting files does work though, which is why just copying everything in every time is a good idea.
- After running touch on run.fcgi the updates should go live in ~30 seconds or so. If it takes more than a minute or two it's probably a problem with the update.
- When putting links to other pages use absolute paths with a slash on the end (e.g. /projects/new_project/). Leaving off the slash ends up putting run.fcgi in the middle of the displayed url about half the time, and relative paths don't work for the most part.
