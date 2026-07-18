

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUtilityRoutesClient, RawUtilityRoutesClient


class UtilityRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUtilityRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUtilityRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUtilityRoutesClient
        """
        return self._raw_client

    def utils_delay_random(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delay the response by 1 to 10 seconds randomly

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_delay_random()
        """
        _response = self._raw_client.utils_delay_random(request_options=request_options)
        return _response.data

    def utils_delay(self, seconds: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delay the response by the specified number of seconds

        Parameters
        ----------
        seconds : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_delay(
            seconds=1,
        )
        """
        _response = self._raw_client.utils_delay(seconds, request_options=request_options)
        return _response.data

    def utils_number(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random number

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_number()
        """
        _response = self._raw_client.utils_number(request_options=request_options)
        return _response.data

    def utils_number_max(self, max: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random number up to the specified maximum

        Parameters
        ----------
        max : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_number_max(
            max=1,
        )
        """
        _response = self._raw_client.utils_number_max(max, request_options=request_options)
        return _response.data

    def utils_status(self, code: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a response with the specified status code

        Parameters
        ----------
        code : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_status(
            code=1,
        )
        """
        _response = self._raw_client.utils_status(code, request_options=request_options)
        return _response.data

    def utils_uuid(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random UUID

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_uuid()
        """
        _response = self._raw_client.utils_uuid(request_options=request_options)
        return _response.data

    def utils_uuid_from(self, input: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a UUID generated from the input string

        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_uuid_from(
            input="input",
        )
        """
        _response = self._raw_client.utils_uuid_from(input, request_options=request_options)
        return _response.data

    def utils_word(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random word

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_word()
        """
        _response = self._raw_client.utils_word(request_options=request_options)
        return _response.data

    def utils_words(self, count: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a number of random words

        Parameters
        ----------
        count : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.utility_routes.utils_words(
            count=1,
        )
        """
        _response = self._raw_client.utils_words(count, request_options=request_options)
        return _response.data


class AsyncUtilityRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUtilityRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUtilityRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUtilityRoutesClient
        """
        return self._raw_client

    async def utils_delay_random(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delay the response by 1 to 10 seconds randomly

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_delay_random()


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_delay_random(request_options=request_options)
        return _response.data

    async def utils_delay(self, seconds: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delay the response by the specified number of seconds

        Parameters
        ----------
        seconds : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_delay(
                seconds=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_delay(seconds, request_options=request_options)
        return _response.data

    async def utils_number(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random number

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_number()


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_number(request_options=request_options)
        return _response.data

    async def utils_number_max(self, max: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random number up to the specified maximum

        Parameters
        ----------
        max : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_number_max(
                max=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_number_max(max, request_options=request_options)
        return _response.data

    async def utils_status(self, code: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a response with the specified status code

        Parameters
        ----------
        code : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_status(
                code=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_status(code, request_options=request_options)
        return _response.data

    async def utils_uuid(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random UUID

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_uuid()


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_uuid(request_options=request_options)
        return _response.data

    async def utils_uuid_from(self, input: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a UUID generated from the input string

        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_uuid_from(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_uuid_from(input, request_options=request_options)
        return _response.data

    async def utils_word(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a random word

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_word()


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_word(request_options=request_options)
        return _response.data

    async def utils_words(self, count: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a number of random words

        Parameters
        ----------
        count : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Vanilla text/plain response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.utility_routes.utils_words(
                count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.utils_words(count, request_options=request_options)
        return _response.data
