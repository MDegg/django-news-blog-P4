# Django News

Django News is a News Blog Web App which can be used to Post articles of interest and to allows other users to read, comment and like each post.
Users are able to register an account with the app and create their own profile using their name, email and choosing a unique usernam. Once registered users can login to the app to allow them to use the like and comment functionality along with add post and choose categories of interest to view blog articles within the chosen category.
#

# User Stories

The user requires certain functionality to enable the app to work as needed.

- Home Page View
- Article Detailed View
- Create Posts
- Login and Logout
- Register
- Comments
- Like Posts
- Edit and Delete Posts

Whilst thinking about the users needs each requirement is added into the user stories within github.

![](static/Media/images/user_stories.JPG)

As the requirements are fulfilled within the app they are moved into the In Progress column.

![](static/Media/images/user_stories_in_progress.JPG)

And finally added to the Complete column once the functionality has been completed.

![](static/Media/images/user_stories_complete.JPG)

# Features

## Navbar

The website has a multi-functional navbar that allows the user to "Add Post", "Choose Category", "Edit Profile", Login and Logout respectively.

![](static/Media/images/navbar_user.JPG)

The Admin user also has an additional button "Add Category". This allows the Admin to add aditional Categories as they see fit.

![](static/Media/images/navbar_admin.JPG)

If a User is not logged in the navbar shows different options "Home", "Register" and "Login".

![](static/Media/images/register_login_navbar.JPG)

## Home Page

The homepage is where all of the posts are shown to the user. They are added to the page showing the most recent post first. The user is able to click the "View Post" button to view the detailed version of the post.

![](static/Media/images/homepage.JPG)

## Login and Register

The user is able to register, login and logout using the navbar navigation buttons. Each creating a new view or form to allow the user to login, logout or register.

![](static/Media/images/register.JPG)

![](static/Media/images/login.JPG)

## Comment

Registered Users are able to comment on each post within the app but only when logged in.

![](static/Media/images/add_new_comment.JPG)
By clicking the Add Comment button the user is directed to the add comment form where they can create their comment and add to the existing post.

![](static/Media/images/add_comment.JPG)

When a user is not logged in they are unable to comment.

![](static/Media/images/comment_not_registered.JPG)

## Like

Registered Users are able to like each post within the app but only when logged in.

![](static/Media/images/like_post.JPG)

When liked the number of likes are added to the number of likes view.

![](static/Media/images/number_of_likes.JPG)

The like button also chnages colour to Red and allows the user to press again to Unlike.

## Post

Registered Users are able to create their own posts within the app but only when logged in. They can do this from the Add Post button within the navbar

![](static/Media/images/navbar_user.JPG)

The user is directed to the Add Post form where they can create their Blog Post. There are 5 sections to the form.

Title - a text field to allow user text input.
Title Tag - a text field to allow user text input.
Category - a dropdown menu to allow the user to choose which category they wish their post to sit within.
Body - Text Editor to allow text input
Image - Allows for user to upload images to their posts

![](static/Media/images/add_post_form.JPG)

The form uses a Text Editor to provide the user with a better UX and also allows for different fonts, Bold Text, Italic Text etc.

![](static/Media/images/text_editor.JPG)

Once the Post has been created the user clicks the "Post" button to upload their post to the home page of the web app.

## Date

Each post is automatically stamped with the date of when the posts were uploaded.

![](static/Media/images/post_view_home.JPG)

## Edit and Delete Post

Registered Users are able to edit or delete their own posts within the app but only when logged in.

![](static/Media/images/edit_delete_post.JPG)

When a user is not registered or logged in they are not shown the "Edit Post" or "Delete Post" buttons.

![](static/Media/images/delete_post_logged_out.JPG)

#

## Testing

- explain testing procedures
  #

## Validation

All of the python code has beenm PEP8 validated using Pythons built in auto validate function and then checked in the PEP8 validator online. Where some of the validation was showing as "line too long" i was unable to rectify without causing bugs within the code. MOdels and Views shown below...

![](static/Media/images/models_pep8.JPG)
![](static/Media/images/views_pep8.JPG)

#

## Bugs

- Mixed up url.py files and settings.py files. This was realised after finding an error within the admin site. Deleted all associated files and started from scratch.
  #

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows:
- Heroku early deployment etc.
  #

## Credits

- [YouTube](https://www.youtube.com/) - Walkthrough videos and Django tutorials.
- [Code Institute](https://learn.codeinstitute.net/) - Django Cheatsheet

## Content

- The text for the Article Details were taken from Wikipedia, The Great Outdoor Magazine, Everything Camping, MCN, Code Magazine,
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

### Media

- The photos used on the home and sign up page are from Google Images

#

## Images

- ![Footer](reference path for required images)
