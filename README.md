# SatVision: Real-time Data Acquisition

- Experiments, workflows, and tests to acquire a real-time feed of medium resolution satellite images from Sentinel-2 (ESA), Landsat-8 (NASA), and Resourcesat (ISRO) satellites.
- Pluggable interface for use with web or native applications built with any framework.

## High-level Steps for Use

- Register an API user token with [SentinelHub](https://www.sentinel-hub.com/).
- Edit [token_manager.py](./SentinelHub/token_manager.py) to set up the token and other credentials.
- Define callables to render HTTP POST requests from the API endpoint (reference: [landsat8_l2.py](./SentinelHub/landsat8_l2.py)).
