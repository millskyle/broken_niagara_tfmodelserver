from __future__ import print_function

import numpy as np
import time
# This is a placeholder for a Google-internal import.

from grpc.beta import implementations
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from tensorflow.python.saved_model import signature_constants

import logging


class Predictor(object):
    """ Talks to a tensorflow-model-server on a remote host using gRPC.

    Example Usage:

    P = Predictor("localhost", 9000)
    for i in range(100):
        data = np.random.rand(100,2)
        result = P.do(data)

    """

    def __init__(self, host, port, model_name='holey_sheets', input_node='coords_in'):
        self.__host = host
        self.__port = int(port)
        self.__input_node = input_node
        self.__model_name = model_name
        self.__channel = implementations.insecure_channel(host, int(port))
        self.__stub = prediction_service_pb2.beta_create_PredictionService_stub(self.__channel)


        self.__request = predict_pb2.PredictRequest()
        self.__request.model_spec.name = self.__model_name
        self.__request.model_spec.signature_name = 'Predict'
        self.__count = 1.
        self.disabled = False

    def reset(self):
        self.__count = 1.
    def increment_count(self, d):
        self.__count += d

    @property
    def host(self):
        return self.__host

    @property
    def count(self):
        return self.__count


    def do(self, data):
        self.__request.inputs[self.__input_node].CopyFrom(
             tf.contrib.util.make_tensor_proto(data, shape=data.shape, dtype=tf.float32))
        fails = 0
        while True:
            try:
                val = self.__stub.Predict(self.__request, 1.0)
                fails = 0
                return val.outputs['tile_output'].float_val[0]  # 10 secs timeout
            except:
                logging.warning("Communication to {} failed {} times.".format(self.__host, fails))
                fails += 1
                time.sleep(0.5)
                if fails > 10:
                    self.disabled = True
                    return None





