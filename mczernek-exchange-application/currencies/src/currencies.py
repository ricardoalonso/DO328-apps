import logging
import opentracing as ot
from flask import Flask, jsonify, request, g
from flask_cors import CORS
from jaeger_client import Config

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

config = Config(
    service_name='currencies',
    validate=True,
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
        'propagation': 'b3'
    }
)
tracer = config.initialize_tracer()


app = Flask(__name__)
CORS(app)


@app.before_request
def start_span():
    headers_dict = {key: value for key, value in request.headers.items()}
    context = tracer.extract(ot.Format.HTTP_HEADERS, headers_dict)
    span_name = f"{request.method}:currencies"
    scope = tracer.start_active_span(span_name, child_of=context)
    scope.span.set_tag(ot.tags.HTTP_URL, request.url)
    scope.span.set_tag(ot.tags.HTTP_METHOD, request.method)
    g.scope = scope



@app.after_request
def close_span(response):
    g.scope.span.set_tag(ot.tags.HTTP_STATUS_CODE, response.status_code)
    g.scope.close()
    return response


@app.route('/')
def currenciesList():
    return jsonify('EUR', 'USD')
