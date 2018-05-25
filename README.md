## Niagara tensorflow_model_server seg-fault example

### Run the example:

```bash
run_example.sh
```


### or manually:

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
A successful run should result in the client printing a bunch of floating point numbers to the terminal, e.g.

```
-0.00021312199533
-0.000205151736736
-0.000205708667636
-0.000210089609027
-0.000231619924307
-0.000214302912354
-0.000221736729145
-0.000172961503267
-0.000227933749557
-0.000212887302041
-0.000239407643676
-0.000154493376613
-0.00018004141748
-0.000227171927691
-0.000236650928855
-0.000193243846297
-0.000143125653267
...
```
and obviously no segmentation fault from the server.

