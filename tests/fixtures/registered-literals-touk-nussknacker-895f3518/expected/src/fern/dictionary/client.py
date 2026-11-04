

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dict_dto import DictDto
from ..types.dict_entry import DictEntry
from .raw_client import AsyncRawDictionaryClient, RawDictionaryClient


OMIT = typing.cast(typing.Any, ...)


class DictionaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDictionaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDictionaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDictionaryClient
        """
        return self._raw_client

    def get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
        self, processing_type: str, dict_id: str, *, key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DictEntry:
        """
        Parameters
        ----------
        processing_type : str

        dict_id : str

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DictEntry


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
            processing_type="processingType",
            dict_id="dictId",
            key="key",
        )
        """
        _response = self._raw_client.get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
            processing_type, dict_id, key=key, request_options=request_options
        )
        return _response.data

    def get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
        self, processing_type: str, dict_id: str, *, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DictEntry]:
        """
        Parameters
        ----------
        processing_type : str

        dict_id : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DictEntry]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
            processing_type="processingType",
            dict_id="dictId",
            label="label",
        )
        """
        _response = self._raw_client.get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
            processing_type, dict_id, label=label, request_options=request_options
        )
        return _response.data

    def post_api_processdefinitiondata_processingtype_dicts(
        self,
        processing_type: str,
        *,
        expected_type: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DictDto]:
        """
        Parameters
        ----------
        processing_type : str

        expected_type : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DictDto]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dictionary.post_api_processdefinitiondata_processingtype_dicts(
            processing_type="processingType",
            expected_type={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_processdefinitiondata_processingtype_dicts(
            processing_type, expected_type=expected_type, request_options=request_options
        )
        return _response.data


class AsyncDictionaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDictionaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDictionaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDictionaryClient
        """
        return self._raw_client

    async def get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
        self, processing_type: str, dict_id: str, *, key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DictEntry:
        """
        Parameters
        ----------
        processing_type : str

        dict_id : str

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DictEntry


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
                processing_type="processingType",
                dict_id="dictId",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processdefinitiondata_processingtype_dicts_dictid_entrybykey(
            processing_type, dict_id, key=key, request_options=request_options
        )
        return _response.data

    async def get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
        self, processing_type: str, dict_id: str, *, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DictEntry]:
        """
        Parameters
        ----------
        processing_type : str

        dict_id : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DictEntry]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dictionary.get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
                processing_type="processingType",
                dict_id="dictId",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processdefinitiondata_processingtype_dicts_dictid_entry(
            processing_type, dict_id, label=label, request_options=request_options
        )
        return _response.data

    async def post_api_processdefinitiondata_processingtype_dicts(
        self,
        processing_type: str,
        *,
        expected_type: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DictDto]:
        """
        Parameters
        ----------
        processing_type : str

        expected_type : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DictDto]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dictionary.post_api_processdefinitiondata_processingtype_dicts(
                processing_type="processingType",
                expected_type={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_processdefinitiondata_processingtype_dicts(
            processing_type, expected_type=expected_type, request_options=request_options
        )
        return _response.data
