

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScopeClient, RawScopeClient
from .types.sign_confirm_response import SignConfirmResponse
from .types.sign_delete_response import SignDeleteResponse
from .types.sign_request_response import SignRequestResponse
from .types.sign_retrieve_response import SignRetrieveResponse


class ScopeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScopeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScopeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScopeClient
        """
        return self._raw_client

    def sign_request(
        self, *, test: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SignRequestResponse:
        """
        scope verification request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        test : typing.Optional[int]
            test only mode, using test issuer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignRequestResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_request()
        """
        _response = self._raw_client.sign_request(test=test, request_options=request_options)
        return _response.data

    def sign_retrieve(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SignRetrieveResponse]:
        """
        get the status / current content of a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SignRetrieveResponse]
            Successful response (JWT)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_retrieve(
            job="job",
        )
        """
        _response = self._raw_client.sign_retrieve(job, request_options=request_options)
        return _response.data

    def sign_confirm(self, job: str, *, request_options: typing.Optional[RequestOptions] = None) -> SignConfirmResponse:
        """
        this is a scope confirmation

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignConfirmResponse
            Successfully confirmed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_confirm(
            job="job",
        )
        """
        _response = self._raw_client.sign_confirm(job, request_options=request_options)
        return _response.data

    def sign_update(self, job: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        authority updates a JWT with its signature
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_update(
            job="job",
        )
        """
        _response = self._raw_client.sign_update(job, request_options=request_options)
        return _response.data

    def sign_delete(self, job: str, *, request_options: typing.Optional[RequestOptions] = None) -> SignDeleteResponse:
        """
        delete a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignDeleteResponse
            Successfully deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_delete(
            job="job",
        )
        """
        _response = self._raw_client.sign_delete(job, request_options=request_options)
        return _response.data

    def sign_retrieve_head(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        HEAD to get the status of a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scope.sign_retrieve_head(
            job="job",
        )
        """
        _response = self._raw_client.sign_retrieve_head(job, request_options=request_options)
        return _response.headers


class AsyncScopeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScopeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScopeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScopeClient
        """
        return self._raw_client

    async def sign_request(
        self, *, test: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SignRequestResponse:
        """
        scope verification request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        test : typing.Optional[int]
            test only mode, using test issuer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignRequestResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scope.sign_request()


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_request(test=test, request_options=request_options)
        return _response.data

    async def sign_retrieve(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[SignRetrieveResponse]:
        """
        get the status / current content of a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SignRetrieveResponse]
            Successful response (JWT)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scope.sign_retrieve(
                job="job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_retrieve(job, request_options=request_options)
        return _response.data

    async def sign_confirm(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SignConfirmResponse:
        """
        this is a scope confirmation

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignConfirmResponse
            Successfully confirmed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scope.sign_confirm(
                job="job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_confirm(job, request_options=request_options)
        return _response.data

    async def sign_update(self, job: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        authority updates a JWT with its signature
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        job : str
            Job ID (20 chars)

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
            await client.scope.sign_update(
                job="job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_update(job, request_options=request_options)
        return _response.data

    async def sign_delete(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SignDeleteResponse:
        """
        delete a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignDeleteResponse
            Successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scope.sign_delete(
                job="job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_delete(job, request_options=request_options)
        return _response.data

    async def sign_retrieve_head(
        self, job: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        HEAD to get the status of a verification job

        Parameters
        ----------
        job : str
            Job ID (20 chars)

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
            await client.scope.sign_retrieve_head(
                job="job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_retrieve_head(job, request_options=request_options)
        return _response.headers
