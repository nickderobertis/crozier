

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCustomPronunciationsClient, RawCustomPronunciationsClient
from .types.bulk_create_pronunciations_response import BulkCreatePronunciationsResponse
from .types.create_pronunciation_response import CreatePronunciationResponse
from .types.delete_pronunciation_response import DeletePronunciationResponse
from .types.get_pronunciation_response import GetPronunciationResponse
from .types.list_pronunciations_request_status import ListPronunciationsRequestStatus
from .types.list_pronunciations_response import ListPronunciationsResponse
from .types.update_pronunciation_response import UpdatePronunciationResponse


OMIT = typing.cast(typing.Any, ...)


class CustomPronunciationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomPronunciationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomPronunciationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomPronunciationsClient
        """
        return self._raw_client

    def list_pronunciations(
        self,
        *,
        language: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        status: typing.Optional[ListPronunciationsRequestStatus] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPronunciationsResponse:
        """
        Retrieve all custom pronunciations for your team, with optional filters.

        Parameters
        ----------
        language : typing.Optional[str]
            Filter by language (e.g., en-us)

        domain : typing.Optional[str]
            Filter by domain (e.g., medical)

        status : typing.Optional[ListPronunciationsRequestStatus]
            Filter by processing status

        active : typing.Optional[bool]
            Filter by active state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPronunciationsResponse
            List of custom pronunciations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.list_pronunciations()
        """
        _response = self._raw_client.list_pronunciations(
            language=language, domain=domain, status=status, active=active, request_options=request_options
        )
        return _response.data

    def create_pronunciation(
        self, *, word: str, audio: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePronunciationResponse:
        """
        Upload a single pronunciation with a reference audio file.

        Parameters
        ----------
        word : str
            The word or phrase (2-100 characters). Letters, accented characters, apostrophes, hyphens, and spaces only.

        audio : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePronunciationResponse
            Pronunciation created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.create_pronunciation(
            word="word",
        )
        """
        _response = self._raw_client.create_pronunciation(word=word, audio=audio, request_options=request_options)
        return _response.data

    def bulk_create_pronunciations(
        self, *, zip: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkCreatePronunciationsResponse:
        """
        Upload multiple pronunciations at once. Each audio file in the ZIP becomes a pronunciation — the filename (without extension) is used as the word.

        Parameters
        ----------
        zip : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkCreatePronunciationsResponse
            Bulk creation result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.bulk_create_pronunciations()
        """
        _response = self._raw_client.bulk_create_pronunciations(zip=zip, request_options=request_options)
        return _response.data

    def get_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPronunciationResponse:
        """
        Retrieve a single custom pronunciation by UUID

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationResponse
            Pronunciation details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.get_pronunciation(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_pronunciation(uuid_, request_options=request_options)
        return _response.data

    def delete_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePronunciationResponse:
        """
        Permanently remove a custom pronunciation. Takes effect immediately.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePronunciationResponse
            Pronunciation deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.delete_pronunciation(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.delete_pronunciation(uuid_, request_options=request_options)
        return _response.data

    def update_pronunciation(
        self, uuid_: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdatePronunciationResponse:
        """
        Enable or disable a pronunciation without deleting it. Inactive pronunciations are not used during synthesis.

        Parameters
        ----------
        uuid_ : str

        active : bool
            Set to false to disable, true to re-enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePronunciationResponse
            Pronunciation updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_pronunciations.update_pronunciation(
            uuid_="uuid",
            active=True,
        )
        """
        _response = self._raw_client.update_pronunciation(uuid_, active=active, request_options=request_options)
        return _response.data


class AsyncCustomPronunciationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomPronunciationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomPronunciationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomPronunciationsClient
        """
        return self._raw_client

    async def list_pronunciations(
        self,
        *,
        language: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        status: typing.Optional[ListPronunciationsRequestStatus] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPronunciationsResponse:
        """
        Retrieve all custom pronunciations for your team, with optional filters.

        Parameters
        ----------
        language : typing.Optional[str]
            Filter by language (e.g., en-us)

        domain : typing.Optional[str]
            Filter by domain (e.g., medical)

        status : typing.Optional[ListPronunciationsRequestStatus]
            Filter by processing status

        active : typing.Optional[bool]
            Filter by active state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPronunciationsResponse
            List of custom pronunciations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.list_pronunciations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pronunciations(
            language=language, domain=domain, status=status, active=active, request_options=request_options
        )
        return _response.data

    async def create_pronunciation(
        self, *, word: str, audio: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePronunciationResponse:
        """
        Upload a single pronunciation with a reference audio file.

        Parameters
        ----------
        word : str
            The word or phrase (2-100 characters). Letters, accented characters, apostrophes, hyphens, and spaces only.

        audio : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePronunciationResponse
            Pronunciation created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.create_pronunciation(
                word="word",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pronunciation(word=word, audio=audio, request_options=request_options)
        return _response.data

    async def bulk_create_pronunciations(
        self, *, zip: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkCreatePronunciationsResponse:
        """
        Upload multiple pronunciations at once. Each audio file in the ZIP becomes a pronunciation — the filename (without extension) is used as the word.

        Parameters
        ----------
        zip : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkCreatePronunciationsResponse
            Bulk creation result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.bulk_create_pronunciations()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_pronunciations(zip=zip, request_options=request_options)
        return _response.data

    async def get_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPronunciationResponse:
        """
        Retrieve a single custom pronunciation by UUID

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationResponse
            Pronunciation details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.get_pronunciation(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pronunciation(uuid_, request_options=request_options)
        return _response.data

    async def delete_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePronunciationResponse:
        """
        Permanently remove a custom pronunciation. Takes effect immediately.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePronunciationResponse
            Pronunciation deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.delete_pronunciation(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_pronunciation(uuid_, request_options=request_options)
        return _response.data

    async def update_pronunciation(
        self, uuid_: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdatePronunciationResponse:
        """
        Enable or disable a pronunciation without deleting it. Inactive pronunciations are not used during synthesis.

        Parameters
        ----------
        uuid_ : str

        active : bool
            Set to false to disable, true to re-enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePronunciationResponse
            Pronunciation updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_pronunciations.update_pronunciation(
                uuid_="uuid",
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pronunciation(uuid_, active=active, request_options=request_options)
        return _response.data
