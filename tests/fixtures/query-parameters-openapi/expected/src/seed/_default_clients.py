

import typing

import httpx

SDK_DEFAULT_TIMEOUT = 60

try:
    import httpx_aiohttp
except ImportError:

    class DefaultAioHttpClient(httpx.AsyncClient):
        def __init__(self, **kwargs: typing.Any) -> None:
            raise RuntimeError(
                "To use the aiohttp client, install the aiohttp extra: "
                "pip install fern_query-parameters-openapi[aiohttp]"
            )

else:

    class DefaultAioHttpClient(httpx_aiohttp.HttpxAiohttpClient):
        def __init__(self, **kwargs: typing.Any) -> None:
            kwargs.setdefault("timeout", SDK_DEFAULT_TIMEOUT)
            kwargs.setdefault("follow_redirects", True)
            super().__init__(**kwargs)


class DefaultAsyncHttpxClient(httpx.AsyncClient):
    def __init__(self, **kwargs: typing.Any) -> None:
        kwargs.setdefault("timeout", SDK_DEFAULT_TIMEOUT)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)
