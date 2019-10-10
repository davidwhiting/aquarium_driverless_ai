import h2oai_client
import numpy as np
import pandas as pd
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters

#ip = '35.175.227.14'
ip = '35.175.227.14'
address = 'http://' + ip + ':12345'
username = 'training'
password = 'training'

h2oai = Client(address = address
               , username = username
               , password = password)

