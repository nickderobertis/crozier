# Fern Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Fern%2FPython)
[![pypi](https://img.shields.io/pypi/v/fern)](https://pypi.python.org/pypi/fern)

The Fern Python library provides convenient access to the Fern APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install fern
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.send_lower(
    forwarded_proto="v2",
    forwarded_host="v3",
    forwarded_port="v4",
    forwarded="v5",
    real_ip="v6",
    host="v7",
    connection="v8",
    transfer_encoding="v9",
    te="v10",
    trailer="v11",
    upgrade="v12",
    via="v13",
    keep_alive="v14",
    expect="v15",
    date="v16",
    accept="v17",
    accept_encoding="v18",
    accept_charset="v19",
    accept_language="v20",
    referer="v21",
    content_encoding="v22",
    content_md5="v23",
    content_language="v24",
    cache_control="v25",
    pragma="v26",
    proxy_authorization="v27",
    dnt="v28",
    sec_fetch_mode="v29",
    request_id="v30",
    if_match="v31",
    range="v32",
    authorization="v33",
    csrf_token="v34",
    http_method_override="v35",
    set_cookie="v40",
    forwarded_server="v41",
    client_ip="v42",
    true_client_ip="v43",
    original_forwarded_for="v44",
    content_range="v45",
    idempotency_key="v47",
    label="crate",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from fern import AsyncFernApi

client = AsyncFernApi(
    base_url="https://yourhost.com/path/to/api",
)


async def main() -> None:
    await client.send_lower(
        forwarded_proto="v2",
        forwarded_host="v3",
        forwarded_port="v4",
        forwarded="v5",
        real_ip="v6",
        host="v7",
        connection="v8",
        transfer_encoding="v9",
        te="v10",
        trailer="v11",
        upgrade="v12",
        via="v13",
        keep_alive="v14",
        expect="v15",
        date="v16",
        accept="v17",
        accept_encoding="v18",
        accept_charset="v19",
        accept_language="v20",
        referer="v21",
        content_encoding="v22",
        content_md5="v23",
        content_language="v24",
        cache_control="v25",
        pragma="v26",
        proxy_authorization="v27",
        dnt="v28",
        sec_fetch_mode="v29",
        request_id="v30",
        if_match="v31",
        range="v32",
        authorization="v33",
        csrf_token="v34",
        http_method_override="v35",
        set_cookie="v40",
        forwarded_server="v41",
        client_ip="v42",
        true_client_ip="v43",
        original_forwarded_for="v44",
        content_range="v45",
        idempotency_key="v47",
        label="crate",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from fern.core.api_error import ApiError

try:
    client.send_lower(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from fern import FernApi

client = FernApi(...)
response = client.with_raw_response.send_lower(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.send_lower(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from fern import FernApi

client = FernApi(..., timeout=20.0)

# Override timeout for a specific method
client.send_lower(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from fern import FernApi

client = FernApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
