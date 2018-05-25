## Niagara tensorflow_model_server seg-fault example

1. Run the server:
```bash
bash ./server/run_server.sh
```
It will appear successful.

2. In another terminal (on the same login node), send data to the server by running the `test.py`
```bash
python ./client/test.py
```

The python import can take a few seconds.  As soon as the client sends some data to the server, the server will segfault.

### An example successful run on (non-Niagara) machines:







