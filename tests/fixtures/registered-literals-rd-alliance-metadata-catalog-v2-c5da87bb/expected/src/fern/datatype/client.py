

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mscid import Mscid
from ..types.response_item_data_type import ResponseItemDataType
from ..types.response_page_data_type import ResponsePageDataType
from ..types.response_success_data_type import ResponseSuccessDataType
from ..types.uri import Uri
from .raw_client import AsyncRawDatatypeClient, RawDatatypeClient


OMIT = typing.cast(typing.Any, ...)


class DatatypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatatypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatatypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatatypeClient
        """
        return self._raw_client

    def list_all_registered_data_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageDataType:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageDataType
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.datatype.list_all_registered_data_types()
        """
        _response = self._raw_client.list_all_registered_data_types(request_options=request_options)
        return _response.data

    def submit_a_new_data_type(
        self,
        *,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessDataType:
        """
        Parameters
        ----------
        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        id : typing.Optional[str]
            URL identifying this type of data.

        label : typing.Optional[str]
            Descriptor for this type of data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessDataType
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.datatype.submit_a_new_data_type()
        """
        _response = self._raw_client.submit_a_new_data_type(
            mscid=mscid, uri=uri, id=id, label=label, request_options=request_options
        )
        return _response.data

    def retrieve_an_existing_data_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemDataType:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemDataType
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.datatype.retrieve_an_existing_data_type_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_data_type_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_data_type_record(
        self,
        int_: int,
        *,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessDataType:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        id : typing.Optional[str]
            URL identifying this type of data.

        label : typing.Optional[str]
            Descriptor for this type of data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessDataType
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.datatype.modify_an_existing_data_type_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_data_type_record(
            int_, mscid=mscid, uri=uri, id=id, label=label, request_options=request_options
        )
        return _response.data

    def remove_an_existing_data_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

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
        client.datatype.remove_an_existing_data_type_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_data_type_record(int_, request_options=request_options)
        return _response.data


class AsyncDatatypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatatypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatatypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatatypeClient
        """
        return self._raw_client

    async def list_all_registered_data_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageDataType:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageDataType
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.datatype.list_all_registered_data_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registered_data_types(request_options=request_options)
        return _response.data

    async def submit_a_new_data_type(
        self,
        *,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessDataType:
        """
        Parameters
        ----------
        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        id : typing.Optional[str]
            URL identifying this type of data.

        label : typing.Optional[str]
            Descriptor for this type of data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessDataType
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.datatype.submit_a_new_data_type()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_data_type(
            mscid=mscid, uri=uri, id=id, label=label, request_options=request_options
        )
        return _response.data

    async def retrieve_an_existing_data_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemDataType:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemDataType
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.datatype.retrieve_an_existing_data_type_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_data_type_record(int_, request_options=request_options)
        return _response.data

    async def modify_an_existing_data_type_record(
        self,
        int_: int,
        *,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessDataType:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        id : typing.Optional[str]
            URL identifying this type of data.

        label : typing.Optional[str]
            Descriptor for this type of data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessDataType
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.datatype.modify_an_existing_data_type_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_data_type_record(
            int_, mscid=mscid, uri=uri, id=id, label=label, request_options=request_options
        )
        return _response.data

    async def remove_an_existing_data_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

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
            await client.datatype.remove_an_existing_data_type_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_data_type_record(int_, request_options=request_options)
        return _response.data
