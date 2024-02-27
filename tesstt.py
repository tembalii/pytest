import dill
import dill as securedill

import dill as pickle
from dill import load, loads

def lambda_handler(event, context):

    tainted = event['exploit_code']
    s = "encoded-data"
    b = bytearray().extend(map(ord,string))
    
    # ruleid: tainted-dill-aws-lambda
    dill.load_module(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    dill.load_module_asdict(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    dill.temp.load(tainted)
    # ruleid: tainted-dill-aws-lambda
    dill.temp.loadIO(tainted)
    # ruleid: tainted-dill-aws-lambda
    dill.temp.load_source(tainted)
    # ruleid: tainted-dill-aws-lambda
    dill.temp.loadIO_source(tainted)

    # ruleid: tainted-dill-aws-lambda
    unpickler = dill.Unpickler(tainted)
    unpickler.load()

    # ok: tainted-dill-aws-lambda
    dill.load_module(filename=s)
    # ok: tainted-dill-aws-lambda
    dill.load_module_asdict(filename=s)
    # ok: tainted-dill-aws-lambda
    dill.temp.load(s)
    # ok: tainted-dill-aws-lambda
    dill.temp.loadIO(s)
    # ok: tainted-dill-aws-lambda
    dill.temp.load_source(s)
    # ok: tainted-dill-aws-lambda
    dill.temp.loadIO_source(s)

    # ok: tainted-dill-aws-lambda
    unpickler = dill.Unpickler(s)
    unpickler.load()

    # ruleid: tainted-dill-aws-lambda
    pickle.load_module(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    pickle.load_module_asdict(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    pickle.temp.load(tainted)
    # ruleid: tainted-dill-aws-lambda
    pickle.temp.loadIO(tainted)
    # ruleid: tainted-dill-aws-lambda
    pickle.temp.load_source(tainted)
    # ruleid: tainted-dill-aws-lambda
    pickle.temp.loadIO_source(tainted)

    # ruleid: tainted-dill-aws-lambda
    unpickler = pickle.Unpickler(tainted)
    unpickler.load()

    # ok: tainted-dill-aws-lambda
    pickle.load_module(filename=s)
    # ok: tainted-dill-aws-lambda
    pickle.load_module_asdict(filename=s)
    # ok: tainted-dill-aws-lambda
    pickle.temp.load(s)
    # ok: tainted-dill-aws-lambda
    pickle.temp.loadIO(s)
    # ok: tainted-dill-aws-lambda
    pickle.temp.load_source(s)
    # ok: tainted-dill-aws-lambda
    pickle.temp.loadIO_source(s)

    # ok: tainted-dill-aws-lambda
    unpickler = pickle.Unpickler(s)
    unpickler.load()

    # ruleid: tainted-dill-aws-lambda
    securedill.load_module(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    securedill.load_module_asdict(filename=tainted)
    # ruleid: tainted-dill-aws-lambda
    securedill.temp.load(tainted)
    # ruleid: tainted-dill-aws-lambda
    securedill.temp.loadIO(tainted)
    # ruleid: tainted-dill-aws-lambda
    securedill.temp.load_source(tainted)
    # ruleid: tainted-dill-aws-lambda
    securedill.temp.loadIO_source(tainted)

    # ruleid: tainted-dill-aws-lambda
    unpickler = securedill.Unpickler(tainted)
    unpickler.load()

    # ok: tainted-dill-aws-lambda
    securedill.load_module(filename=s)
    # ok: tainted-dill-aws-lambda
    securedill.load_module_asdict(filename=s)
    # ok: tainted-dill-aws-lambda
    securedill.temp.load(s)
    # ok: tainted-dill-aws-lambda
    securedill.temp.loadIO(s)
    # ok: tainted-dill-aws-lambda
    securedill.temp.load_source(s)
    # ok: tainted-dill-aws-lambda
    securedill.temp.loadIO_source(s)

    # ok: tainted-dill-aws-lambda
    unpickler = securedill.Unpickler(s)
    unpickler.load()

