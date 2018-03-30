Google Assistant to work with respeakerd
==========

[![Build Status](https://travis-ci.org/respeaker/googleassistant_respeakerd.svg?branch=master)](https://travis-ci.org/respeaker/googleassistant_respeakerd)
[![Pypi](https://img.shields.io/pypi/v/googleassistant_respeakerd.svg)](https://pypi.python.org/pypi/googleassistant_respeakerd)


Adapt google assistant's [gRPC sample app](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/grpc) for working with [respeakerd](https://github.com/respeaker/respeakerd)

## About Google Assisant Service

Please refer to Google Assistant's [documentations](https://developers.google.com/assistant/sdk/guides/service/python/). 

## Setup Guide

### Configure a Developer Project and Account Settings

Please refer to [here](https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account).

### Register the Device Model

Please refer to [here](https://developers.google.com/assistant/sdk/guides/service/python/embed/register-device)

### Install the SDK and Sample Code

In this step, it's a little bit different from the Google's guide. Since we will use the `pydbus` library, which depends on the `gi.repository` library, it's not easy to install `gi.repository` in a python virtual env. But the system of ReSpeaker has this library builtin. So here we're going to skip the python virutal env setup from the Google's guide.

```shell
sudo apt-get install portaudio19-dev libffi-dev libssl-dev
cd ~ && git clone https://github.com/respeaker/googleassistant_respeakerd.git && cd googleassistant_respeakerd
sudo pip install -r requirements.txt
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets /path/to/credentials.json
```

You should see a URL displayed in the terminal:

```
Please visit this URL to authorize this application: https://...
```

Copy the URL and paste it into a browser (this can be done on any machine). The page will ask you to sign in to your Google account. Sign into the Google account that created the developer project in the previous step.

After you approve the permission request from the API, a code will appear in your browser, such as "4/XXXX". Copy and paste this code into the terminal:

```
Enter the authorization code:
```

If authorization was successful, you will see a response similar to the following:

```
credentials saved: /path/to/.config/google-oauthlib-tool/credentials.json
```

If instead you see `InvalidGrantError`, then an invalid code was entered. Try again, taking care to copy and paste the entire code.

### Run the Sample Code

Please refer to [here](https://developers.google.com/assistant/sdk/guides/service/python/embed/run-sample), except that you should replace the `googlesamples-assistant-pushtotalk` command with `googlesamples-assistant-respeakerd`. That is,

```shell
googlesamples-assistant-respeakerd --project-id my-dev-project --device-model-id my-model
```

### Known Limits

- Can not be interrupted (waked) when the assistant's speaking something
