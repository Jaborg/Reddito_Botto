# Use a base image with Python installed
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the bot script and requirements file into the container
COPY app/ ./app
COPY requirements.txt .
COPY Makefile .

# Install dependencies
RUN python3 -m venv env
RUN env/bin/python3 -m pip install --upgrade pip
RUN env/bin/pip3 install -r requirements.txt

# Set environment variables
ENV CLIENT_ID=$CLIENT_ID
ENV CLIENT_SECRET=$CLIENT_SECRET
ENV USERNAME=$REDDIT_USERNAME
ENV PASSWORD=$PASSWORD
ENV USER_AGENT="MyBotName by /u/YourRedditUsername"

# Command to run your bot script
CMD ["make", "run_app"]
