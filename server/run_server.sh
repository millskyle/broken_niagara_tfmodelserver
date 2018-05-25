#!/bin/bash

tensorflow_model_server --port=9000 --model_name=holey_sheets --model_base_path=$PWD/models/
