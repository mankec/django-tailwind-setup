# Django with Tailwind setup

## Getting started

Clone a project and add new origin so you can push changes to your own repo.
```bash
git clone git@github.com:mankec/jekyll-tailwind-setup.git my-new-repo
cd my-new-repo
git remote rm origin
git remote add origin your-git-ssh-url
```

Install Django and activate your virtual environment. I used `pipenv`. You can use whatever you want.
```bash
sudo apt update
sudo apt install pipx
pipx install pipenv

pipenv install
pipenv shell
```

Install node packages.
```bash
npm i
```

Start a server.
```bash
python manage.py runserver
```

In second terminal keep running build process so you can see new style changes on page reload.
```bash
npm run watch:css
```

#### Perhaps you are looking for auto reload? Then [this](https://django-tailwind.readthedocs.io/en/latest/installation.html) might be a right thing for you.
