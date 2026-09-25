

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAnalyticalClient, RawAnalyticalClient


OMIT = typing.cast(typing.Any, ...)


class AnalyticalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticalClient
        """
        return self._raw_client

    def listanalyticalfields(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.listanalyticalfields()
        """
        _response = self._raw_client.listanalyticalfields(request_options=request_options)
        return _response.data

    def getanalyticalfieldvalues(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.getanalyticalfieldvalues(
            id="id",
        )
        """
        _response = self._raw_client.getanalyticalfieldvalues(id, request_options=request_options)
        return _response.data

    def listexpensecategories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.listexpensecategories()
        """
        _response = self._raw_client.listexpensecategories(request_options=request_options)
        return _response.data

    def listcostcenters(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.listcostcenters()
        """
        _response = self._raw_client.listcostcenters(request_options=request_options)
        return _response.data

    def createcostcenter(
        self, *, name: str, code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        name : str

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.createcostcenter(
            name="name",
        )
        """
        _response = self._raw_client.createcostcenter(name=name, code=code, request_options=request_options)
        return _response.data

    def updatecostcenter(
        self, *, name: str, code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        name : str

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.updatecostcenter(
            name="name",
        )
        """
        _response = self._raw_client.updatecostcenter(name=name, code=code, request_options=request_options)
        return _response.data

    def deletecostcenter(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.deletecostcenter()
        """
        _response = self._raw_client.deletecostcenter(request_options=request_options)
        return _response.data

    def get_analytical_field_values(
        self, *, field_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve analytical field values.

        Parameters
        ----------
        field_id : typing.Optional[str]
            Analytical field ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Get analytical field values successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytical.get_analytical_field_values()
        """
        _response = self._raw_client.get_analytical_field_values(field_id=field_id, request_options=request_options)
        return _response.data


class AsyncAnalyticalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticalClient
        """
        return self._raw_client

    async def listanalyticalfields(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.listanalyticalfields()


        asyncio.run(main())
        """
        _response = await self._raw_client.listanalyticalfields(request_options=request_options)
        return _response.data

    async def getanalyticalfieldvalues(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.getanalyticalfieldvalues(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getanalyticalfieldvalues(id, request_options=request_options)
        return _response.data

    async def listexpensecategories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.listexpensecategories()


        asyncio.run(main())
        """
        _response = await self._raw_client.listexpensecategories(request_options=request_options)
        return _response.data

    async def listcostcenters(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.listcostcenters()


        asyncio.run(main())
        """
        _response = await self._raw_client.listcostcenters(request_options=request_options)
        return _response.data

    async def createcostcenter(
        self, *, name: str, code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        name : str

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.createcostcenter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createcostcenter(name=name, code=code, request_options=request_options)
        return _response.data

    async def updatecostcenter(
        self, *, name: str, code: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        name : str

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.updatecostcenter(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatecostcenter(name=name, code=code, request_options=request_options)
        return _response.data

    async def deletecostcenter(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.deletecostcenter()


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecostcenter(request_options=request_options)
        return _response.data

    async def get_analytical_field_values(
        self, *, field_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieve analytical field values.

        Parameters
        ----------
        field_id : typing.Optional[str]
            Analytical field ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Get analytical field values successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytical.get_analytical_field_values()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_analytical_field_values(
            field_id=field_id, request_options=request_options
        )
        return _response.data
