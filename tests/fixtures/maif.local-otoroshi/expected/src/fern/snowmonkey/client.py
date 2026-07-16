

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.done import Done
from ..types.outage import Outage
from ..types.snow_monkey_config import SnowMonkeyConfig
from .raw_client import AsyncRawSnowmonkeyClient, RawSnowmonkeyClient


OMIT = typing.cast(typing.Any, ...)


class SnowmonkeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnowmonkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnowmonkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnowmonkeyClient
        """
        return self._raw_client

    def start_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Start the Snow Monkey

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.start_snow_monkey()
        """
        _response = self._raw_client.start_snow_monkey(request_options=request_options)
        return _response.data

    def stop_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Stop the Snow Monkey

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.stop_snow_monkey()
        """
        _response = self._raw_client.stop_snow_monkey(request_options=request_options)
        return _response.data

    def get_snow_monkey_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> SnowMonkeyConfig:
        """
        Get current Snow Monkey config

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.get_snow_monkey_config()
        """
        _response = self._raw_client.get_snow_monkey_config(request_options=request_options)
        return _response.data

    def update_snow_monkey(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnowMonkeyConfig:
        """
        Update current Snow Monkey config

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.update_snow_monkey(
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.update_snow_monkey(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def patch_snow_monkey(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnowMonkeyConfig:
        """
        Update current Snow Monkey config

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.patch_snow_monkey(
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.patch_snow_monkey(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Outage]:
        """
        Get all current Snow Monkey ourages

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Outage]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.get_snow_monkey_outages()
        """
        _response = self._raw_client.get_snow_monkey_outages(request_options=request_options)
        return _response.data

    def reset_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Reset Snow Monkey Outages for the day

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.reset_snow_monkey()
        """
        _response = self._raw_client.reset_snow_monkey(request_options=request_options)
        return _response.data


class AsyncSnowmonkeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnowmonkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnowmonkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnowmonkeyClient
        """
        return self._raw_client

    async def start_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Start the Snow Monkey

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.start_snow_monkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.start_snow_monkey(request_options=request_options)
        return _response.data

    async def stop_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Stop the Snow Monkey

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.stop_snow_monkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_snow_monkey(request_options=request_options)
        return _response.data

    async def get_snow_monkey_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SnowMonkeyConfig:
        """
        Get current Snow Monkey config

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.get_snow_monkey_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_snow_monkey_config(request_options=request_options)
        return _response.data

    async def update_snow_monkey(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnowMonkeyConfig:
        """
        Update current Snow Monkey config

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.update_snow_monkey(
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_snow_monkey(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def patch_snow_monkey(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnowMonkeyConfig:
        """
        Update current Snow Monkey config

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.patch_snow_monkey(
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_snow_monkey(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Outage]:
        """
        Get all current Snow Monkey ourages

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Outage]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.get_snow_monkey_outages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_snow_monkey_outages(request_options=request_options)
        return _response.data

    async def reset_snow_monkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> Done:
        """
        Reset Snow Monkey Outages for the day

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.reset_snow_monkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_snow_monkey(request_options=request_options)
        return _response.data
