

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTermSubstitutionsClient, RawTermSubstitutionsClient
from .types.create_term_substitution_response import CreateTermSubstitutionResponse
from .types.delete_term_substitution_response import DeleteTermSubstitutionResponse
from .types.get_term_substitution_response import GetTermSubstitutionResponse
from .types.list_term_substitutions_response import ListTermSubstitutionsResponse


OMIT = typing.cast(typing.Any, ...)


class TermSubstitutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTermSubstitutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTermSubstitutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTermSubstitutionsClient
        """
        return self._raw_client

    def list_term_substitutions(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTermSubstitutionsResponse:
        """
        List all term substitutions

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTermSubstitutionsResponse
            List of term substitutions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.term_substitutions.list_term_substitutions(
            page=1,
        )
        """
        _response = self._raw_client.list_term_substitutions(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_term_substitution(
        self, *, original_text: str, replacement_text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTermSubstitutionResponse:
        """
        Create a new pronunciation substitution

        Parameters
        ----------
        original_text : str
            Original text to substitute

        replacement_text : str
            Replacement pronunciation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTermSubstitutionResponse
            Term substitution created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.term_substitutions.create_term_substitution(
            original_text="original_text",
            replacement_text="replacement_text",
        )
        """
        _response = self._raw_client.create_term_substitution(
            original_text=original_text, replacement_text=replacement_text, request_options=request_options
        )
        return _response.data

    def get_term_substitution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTermSubstitutionResponse:
        """
        Get term substitution details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTermSubstitutionResponse
            Term substitution details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.term_substitutions.get_term_substitution(
            id=1,
        )
        """
        _response = self._raw_client.get_term_substitution(id, request_options=request_options)
        return _response.data

    def delete_term_substitution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTermSubstitutionResponse:
        """
        Delete a term substitution

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTermSubstitutionResponse
            Term substitution deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.term_substitutions.delete_term_substitution(
            id=1,
        )
        """
        _response = self._raw_client.delete_term_substitution(id, request_options=request_options)
        return _response.data


class AsyncTermSubstitutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTermSubstitutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTermSubstitutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTermSubstitutionsClient
        """
        return self._raw_client

    async def list_term_substitutions(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTermSubstitutionsResponse:
        """
        List all term substitutions

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTermSubstitutionsResponse
            List of term substitutions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.term_substitutions.list_term_substitutions(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_term_substitutions(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_term_substitution(
        self, *, original_text: str, replacement_text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTermSubstitutionResponse:
        """
        Create a new pronunciation substitution

        Parameters
        ----------
        original_text : str
            Original text to substitute

        replacement_text : str
            Replacement pronunciation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTermSubstitutionResponse
            Term substitution created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.term_substitutions.create_term_substitution(
                original_text="original_text",
                replacement_text="replacement_text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_term_substitution(
            original_text=original_text, replacement_text=replacement_text, request_options=request_options
        )
        return _response.data

    async def get_term_substitution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTermSubstitutionResponse:
        """
        Get term substitution details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTermSubstitutionResponse
            Term substitution details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.term_substitutions.get_term_substitution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_term_substitution(id, request_options=request_options)
        return _response.data

    async def delete_term_substitution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTermSubstitutionResponse:
        """
        Delete a term substitution

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTermSubstitutionResponse
            Term substitution deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.term_substitutions.delete_term_substitution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_term_substitution(id, request_options=request_options)
        return _response.data
