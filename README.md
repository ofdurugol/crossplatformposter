# Cross-Platform Poster
For trial, this particular instance posts submissions from reddit to an Instagram account.

"Controller.py" is the main controller of the other scripts.
All of the files need to be downloaded and should be run without changing the hierarchy of the files to run properly.
reqs.txt includes the python libraries in a notepad to install them easily.

TO USE:
Edit InstagramPoster.py and change the username and password.
Run Controller.py


What it does?

1) 'RedditPull_v3' goes to www.reddit.com/r/dankmemes and takes the image source code of the first hot post, converts it into png and saves it into "assets/hot.png". It also saves the title of the post to the "assets/title.txt".

2) 'MakeImgSquare' takes "hot.png" and adds white space around it to make it 1:1 if it's not square, and saves it again to "assets/hot.png". This is done because most social media platforms work better or require 1:1 image for best viewing.

3) 'InstagramPoster' opens the instagram account in mobile view and posts the image with the caption from "assets/title.txt" and the image from "assets/hot.png".


NOTE: Use an interpreter other than conda, a standard python virtual environment should do. Conda repos do not have 'pyautoit' library yet and installing with 'pip install' in conda created problems with package in my case with Python==3.11.2
