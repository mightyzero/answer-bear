#!/usr/bin/env python
import os
from concurrent import futures

from answer_bear.routes import app
from illumination.build_model import ModelBuilder

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    # Kick off scraper agent in a background thread
    # Need to run this first, because once the server runs it won't stop
    model_builder = ModelBuilder()
    with futures.ThreadPoolExecutor() as executor:
        executor.submit(model_builder.build_model())
        executor.submit(app.run(host='0.0.0.0', port=port))
