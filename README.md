# DetaLog

DetaLog is a Python package that provides a logging handler for sending logs to a [PingBack](https://github.com/MaximilianHeidenreich/PingBack) events crawler. This can be useful for aggregating logs from multiple sources into a central place, and analyzing them to gain insights about your application or system.

## Installation

You can install DetaLog via pip:

```
pip install detalog
```

## Usage

Here's an example of how to use DetaLog in your Python code:

```python
import logging
from detalog import PingBackHandler

app_url = "https://my-pingback-events-crawler.com"
api_key = "my-api-key"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = PingBackHandler(app_url, api_key, project="my-project", channel="my-channel")
handler.setLevel(logging.INFO)

logger.addHandler(handler)

logger.info("Hello, world!")

logger.debug("Hello, world!", extra={"channel": "debug-channel", "project": "my-project-2"})
```

In this example, we create a logger with the name `__name__`, which is the name of the current module. We set its logging level to `INFO`, which means it will log messages at the `INFO` level or above. We also create a `PingBackHandler` instance, passing in the URL of the PingBack events crawler, an API key for authentication, and optional `project` and `channel` parameters to specify the destination of the logs. We set the handler's logging level to `INFO` as well, so it will only handle messages at that level or above.

Finally, we add the handler to the logger, and log an `INFO` message with the text "Hello, world!". This message will be sent to the PingBack events crawler via the handler's `emit` method, in the form of a JSON payload.

## License

DetaLog is licensed under the MIT License. See LICENSE for details.
