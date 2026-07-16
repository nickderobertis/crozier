

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attribute import Attribute
from .raw_client import AsyncRawAttributesClient, RawAttributesClient


OMIT = typing.cast(typing.Any, ...)


class AttributesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttributesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttributesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttributesClient
        """
        return self._raw_client

    def fetch_a_list_of_attributes(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Attribute]:
        """
        Without params, it returns a list of Attributes the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Attribute]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attributes.fetch_a_list_of_attributes()
        """
        _response = self._raw_client.fetch_a_list_of_attributes(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_an_attribute(
        self,
        *,
        attribute: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expression: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attribute:
        """
        Parameters
        ----------
        attribute : typing.Optional[str]

        description : typing.Optional[str]

        expression : typing.Optional[str]

        id : typing.Optional[int]

        type : typing.Optional[str]
            String|Number|Boolean

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attribute
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attributes.create_an_attribute()
        """
        _response = self._raw_client.create_an_attribute(
            attribute=attribute,
            description=description,
            expression=expression,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def update_an_attribute(
        self,
        id_: int,
        *,
        attribute: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expression: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attribute:
        """
        Parameters
        ----------
        id_ : int

        attribute : typing.Optional[str]

        description : typing.Optional[str]

        expression : typing.Optional[str]

        id : typing.Optional[int]

        type : typing.Optional[str]
            String|Number|Boolean

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attribute
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attributes.update_an_attribute(
            id_=1,
        )
        """
        _response = self._raw_client.update_an_attribute(
            id_,
            attribute=attribute,
            description=description,
            expression=expression,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_an_attribute(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.attributes.delete_an_attribute(
            id=1,
        )
        """
        _response = self._raw_client.delete_an_attribute(id, request_options=request_options)
        return _response.data


class AsyncAttributesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttributesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttributesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttributesClient
        """
        return self._raw_client

    async def fetch_a_list_of_attributes(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Attribute]:
        """
        Without params, it returns a list of Attributes the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Attribute]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attributes.fetch_a_list_of_attributes()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_attributes(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_an_attribute(
        self,
        *,
        attribute: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expression: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attribute:
        """
        Parameters
        ----------
        attribute : typing.Optional[str]

        description : typing.Optional[str]

        expression : typing.Optional[str]

        id : typing.Optional[int]

        type : typing.Optional[str]
            String|Number|Boolean

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attribute
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attributes.create_an_attribute()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_attribute(
            attribute=attribute,
            description=description,
            expression=expression,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def update_an_attribute(
        self,
        id_: int,
        *,
        attribute: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expression: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attribute:
        """
        Parameters
        ----------
        id_ : int

        attribute : typing.Optional[str]

        description : typing.Optional[str]

        expression : typing.Optional[str]

        id : typing.Optional[int]

        type : typing.Optional[str]
            String|Number|Boolean

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attribute
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attributes.update_an_attribute(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_an_attribute(
            id_,
            attribute=attribute,
            description=description,
            expression=expression,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_an_attribute(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.attributes.delete_an_attribute(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_attribute(id, request_options=request_options)
        return _response.data
