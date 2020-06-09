

- Clone this repository with "git clone https://github.com/sasili-adetunji/delta.git"
- run `cd delta`
- Install Virtual environement by running pip install virtualenv. This helps in isolating python packages from every project. This makes projects with conflicting dependecies to coeexist peacefully
- Create a vitual env
- Activate virtual environment source venv/bin/activate
- Edit the `.env-sample` file and save it as `.env`
- Grab api key from https://newsapi.org/
- Install the dependencies by running `pip install -r requirements.txt`
- Start the app by running `python app.py`
- Navigate to `http://localhost:5000/api/news` and send a post json request 
