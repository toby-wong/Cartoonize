# Cartoonize Web API

### Taking It To Production
Comments have been left in cartoonize_api.py where a possible implementation for user accounts and authentication would be. This could be done via a database accessible by the API or have the user be only able to access the API through the frontend client. Currently, there is framework for requests to be made to a server/client, but no implementation of the server/client.

Possible measures that could be taken when upscaling the service could be to utilise threading to allow multiple requests to be made at the same time (i.e. additional users). The cartoonise function would also require optimising to reduce server resources; one such implementation would be to hand off the image to the local machine and then 'cartoonise' with local machine resources. This was reflected in my implementation with the 'cartoonise' functions being accessed as a library and stored separately to the API. 

A Flask server could be used to handle both requests and to store the images. Timers could also be used to periodically delete old images from the server.

### How to use
```console
$ pip install -r requirements.txt
$ python cartoonize_api.py
```

