

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mscid import Mscid
from ..types.response_item_vocabulary_term import ResponseItemVocabularyTerm
from ..types.response_page_vocabulary_term import ResponsePageVocabularyTerm
from ..types.response_success_vocabulary_term import ResponseSuccessVocabularyTerm
from ..types.uri import Uri
from ..types.vocabulary_term_applies_item import VocabularyTermAppliesItem
from .raw_client import AsyncRawLocationClient, RawLocationClient


OMIT = typing.cast(typing.Any, ...)


class LocationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationClient
        """
        return self._raw_client

    def list_all_registered_location_url_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageVocabularyTerm:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageVocabularyTerm
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.location.list_all_registered_location_url_types()
        """
        _response = self._raw_client.list_all_registered_location_url_types(request_options=request_options)
        return _response.data

    def submit_a_new_location_url_type(
        self,
        *,
        id: str,
        label: str,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessVocabularyTerm:
        """
        Parameters
        ----------
        id : str
            String used to identify this term in records.

        label : str
            Human-readable descriptor for this term.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessVocabularyTerm
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.location.submit_a_new_location_url_type(
            label="label",
            id="id",
        )
        """
        _response = self._raw_client.submit_a_new_location_url_type(
            id=id, label=label, mscid=mscid, uri=uri, applies=applies, request_options=request_options
        )
        return _response.data

    def retrieve_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemVocabularyTerm:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemVocabularyTerm
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.location.retrieve_an_existing_location_url_type_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_location_url_type_record(
            int_, request_options=request_options
        )
        return _response.data

    def modify_an_existing_location_url_type_record(
        self,
        int_: int,
        *,
        label: str,
        id: typing.Optional[str] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessVocabularyTerm:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        label : str
            Human-readable descriptor for this term.

        id : typing.Optional[str]
            String used to identify this term in records.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessVocabularyTerm
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.location.modify_an_existing_location_url_type_record(
            int_=1,
            label="label",
        )
        """
        _response = self._raw_client.modify_an_existing_location_url_type_record(
            int_, label=label, id=id, mscid=mscid, uri=uri, applies=applies, request_options=request_options
        )
        return _response.data

    def remove_an_existing_location_url_type_record(
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
        client.location.remove_an_existing_location_url_type_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_location_url_type_record(int_, request_options=request_options)
        return _response.data


class AsyncLocationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationClient
        """
        return self._raw_client

    async def list_all_registered_location_url_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageVocabularyTerm:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageVocabularyTerm
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
            await client.location.list_all_registered_location_url_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registered_location_url_types(request_options=request_options)
        return _response.data

    async def submit_a_new_location_url_type(
        self,
        *,
        id: str,
        label: str,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessVocabularyTerm:
        """
        Parameters
        ----------
        id : str
            String used to identify this term in records.

        label : str
            Human-readable descriptor for this term.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessVocabularyTerm
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
            await client.location.submit_a_new_location_url_type(
                label="label",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_location_url_type(
            id=id, label=label, mscid=mscid, uri=uri, applies=applies, request_options=request_options
        )
        return _response.data

    async def retrieve_an_existing_location_url_type_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemVocabularyTerm:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemVocabularyTerm
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
            await client.location.retrieve_an_existing_location_url_type_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_location_url_type_record(
            int_, request_options=request_options
        )
        return _response.data

    async def modify_an_existing_location_url_type_record(
        self,
        int_: int,
        *,
        label: str,
        id: typing.Optional[str] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        applies: typing.Optional[typing.Sequence[VocabularyTermAppliesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessVocabularyTerm:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        label : str
            Human-readable descriptor for this term.

        id : typing.Optional[str]
            String used to identify this term in records.

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        applies : typing.Optional[typing.Sequence[VocabularyTermAppliesItem]]
            Entities for which this term may be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessVocabularyTerm
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
            await client.location.modify_an_existing_location_url_type_record(
                int_=1,
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_location_url_type_record(
            int_, label=label, id=id, mscid=mscid, uri=uri, applies=applies, request_options=request_options
        )
        return _response.data

    async def remove_an_existing_location_url_type_record(
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
            await client.location.remove_an_existing_location_url_type_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_location_url_type_record(
            int_, request_options=request_options
        )
        return _response.data
