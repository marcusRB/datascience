# Problem 1 - 1.M220P Driver Setup:
## Task: Connection

MFlix will use MongoDB as a storage layer, so for this ticket you'll be required to perform some application setup.

1. First, make sure you've created a user on your Atlas cluster with read and write access to the mflix database.
    - The user name should be m220student and the password should be m220password
    - Don't forget to whitelist your IP address!
2. Copy the connection string. Select that you'd like to connect with the mongo shell, version 3.6 or later - this will give you the srv connection string. Make sure this URI string contains your username and password!

3. Locate the file called dotini_win or dotini_unix (depending on your operating system) and replace the information within with your own srv connection string. The [TEST] URI will be used by the unit tests, while the integration tests will use the [PROD] URI:

```
[PROD]
SECRET_KEY = super_secret_key_you_should_change
MFLIX_DB_URI = mongodb+srv://m220student:m220password@<your-atlas-cluster-address>
MFLIX_NS = sample_mflix

[TEST]
SECRET_KEY = super_secret_testing_key
MFLIX_DB_URI = your_testing_db_uri (can be the same as Atlas, or a local MongoDB database)
MFLIX_NS = sample_mflix
```

    - It's highly suggested you also change the SECRET_KEY to some very long, very random string. While this application is only meant for local use during this course, software has a strange habit of living a long time.
4. Rename dotini_win or dotini_unix to .ini. You can do this by running the following command from the mflix-python directory:

```
mv dotini_unix .ini   # on Unix
ren dotini_win .ini  # on Windows

```

*Note:* Once you rename this file to .ini, it will no longer be visible in Finder or File Explorer. However, it will be visible from Command Prompt or Terminal, so if you need to edit it again, you can open it from there:

```
vi .ini       # on Unix
notepad .ini  # on Windows

```

## Testing and Running the Application

In order to reinforce good development practices, everything asked of you in this course is backed up by unit tests. Reading through the tests for a specific exercise will tell you exactly what is expected.

You can run the unit tests for this ticket by running:

```
pytest -m connection

```

Once the unit tests are passing, run the application with:

```
python run.py
```

Now proceed to the [status page](http://localhost:5000/status) to run the full suite of integration tests and get your validation code.

After passing the relevant tests, what is the validation code for **Connection**?