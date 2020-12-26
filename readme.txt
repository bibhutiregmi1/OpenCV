## process to heroku deployment

git init, add, commit

#Login into heroku. this will open a browser where you can give your credentials
heroku login

#Create a project for heroku deployment. Make sure to give a unique name.Name must start with a letter, end with a letter or digit and can only contain lowercase letters, digits, and dashes.
heroku create opencvtextdetect

# login into the heroku container
heroku container:login

# push the code to the heroku container
heroku container:push web
