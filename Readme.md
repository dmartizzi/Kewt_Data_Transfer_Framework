Deployment of three simple services in a Docker network:
- sender: generates an array of random numbers and sends a post request to the listener.
- listener: exposes a POST endpoint and connects to the db service. 
- db: persistent storage for data sent to the listener.