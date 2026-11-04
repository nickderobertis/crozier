

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ems import Ems
from ..types.sbi_ls import SbiLs
from .raw_client import AsyncRawEmsClient, RawEmsClient


OMIT = typing.cast(typing.Any, ...)


class EmsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmsClient
        """
        return self._raw_client

    def returns_a_list_of_registered_em_ss(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ems.returns_a_list_of_registered_em_ss()
        """
        _response = self._raw_client.returns_a_list_of_registered_em_ss(request_options=request_options)
        return _response.data

    def adds_a_new_ems(
        self,
        *,
        id: str,
        url: str,
        type: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            EMS' authentication URL - example: http://10.200.64.2:5000/

        type : str
            EMS' type

        name : typing.Optional[str]
            The name for the new EMS

        description : typing.Optional[str]
            A description for the EMS

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ems.adds_a_new_ems(
            id="id",
            url="url",
            type="type",
        )
        """
        _response = self._raw_client.adds_a_new_ems(
            id=id, url=url, type=type, name=name, description=description, request_options=request_options
        )
        return _response.data

    def returns_information_about_the_given_ems(
        self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ems:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ems
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ems.returns_information_about_the_given_ems(
            ems_id="ems_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_ems(ems_id, request_options=request_options)
        return _response.data

    def updates_the_given_ems(self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ems.updates_the_given_ems(
            ems_id="ems_id",
        )
        """
        _response = self._raw_client.updates_the_given_ems(ems_id, request_options=request_options)
        return _response.data

    def deletes_the_given_ems(self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ems.deletes_the_given_ems(
            ems_id="ems_id",
        )
        """
        _response = self._raw_client.deletes_the_given_ems(ems_id, request_options=request_options)
        return _response.data


class AsyncEmsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmsClient
        """
        return self._raw_client

    async def returns_a_list_of_registered_em_ss(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ems.returns_a_list_of_registered_em_ss()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_registered_em_ss(request_options=request_options)
        return _response.data

    async def adds_a_new_ems(
        self,
        *,
        id: str,
        url: str,
        type: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            EMS' authentication URL - example: http://10.200.64.2:5000/

        type : str
            EMS' type

        name : typing.Optional[str]
            The name for the new EMS

        description : typing.Optional[str]
            A description for the EMS

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ems.adds_a_new_ems(
                id="id",
                url="url",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adds_a_new_ems(
            id=id, url=url, type=type, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def returns_information_about_the_given_ems(
        self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ems:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ems
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ems.returns_information_about_the_given_ems(
                ems_id="ems_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_ems(
            ems_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_ems(
        self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ems.updates_the_given_ems(
                ems_id="ems_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_ems(ems_id, request_options=request_options)
        return _response.data

    async def deletes_the_given_ems(
        self, ems_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ems_id : str
            ID of EMS to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ems.deletes_the_given_ems(
                ems_id="ems_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_ems(ems_id, request_options=request_options)
        return _response.data
