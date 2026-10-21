

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBorrowersClient, RawBorrowersClient
from .types.one_fd12f73a7dc29d90f19d587c1c24d15response import OneFd12F73A7Dc29D90F19D587C1C24D15Response


OMIT = typing.cast(typing.Any, ...)


class BorrowersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBorrowersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBorrowersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBorrowersClient
        """
        return self._raw_client

    def _8dfafa734b74b320d90079f9c6b9def4(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )
        client.borrowers._8dfafa734b74b320d90079f9c6b9def4()
        """
        _response = self._raw_client._8dfafa734b74b320d90079f9c6b9def4(request_options=request_options)
        return _response.data

    def _1fd12f73a7dc29d90f19d587c1c24d15(
        self,
        *,
        firstname: str,
        lastname: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OneFd12F73A7Dc29D90F19D587C1C24D15Response:
        """
        Creates a new borrower in the system

        Parameters
        ----------
        firstname : str

        lastname : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneFd12F73A7Dc29D90F19D587C1C24D15Response
            Borrower created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.borrowers._1fd12f73a7dc29d90f19d587c1c24d15(
            firstname="John",
        )
        """
        _response = self._raw_client._1fd12f73a7dc29d90f19d587c1c24d15(
            firstname=firstname, lastname=lastname, email=email, request_options=request_options
        )
        return _response.data


class AsyncBorrowersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBorrowersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBorrowersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBorrowersClient
        """
        return self._raw_client

    async def _8dfafa734b74b320d90079f9c6b9def4(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.borrowers._8dfafa734b74b320d90079f9c6b9def4()


        asyncio.run(main())
        """
        _response = await self._raw_client._8dfafa734b74b320d90079f9c6b9def4(request_options=request_options)
        return _response.data

    async def _1fd12f73a7dc29d90f19d587c1c24d15(
        self,
        *,
        firstname: str,
        lastname: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OneFd12F73A7Dc29D90F19D587C1C24D15Response:
        """
        Creates a new borrower in the system

        Parameters
        ----------
        firstname : str

        lastname : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OneFd12F73A7Dc29D90F19D587C1C24D15Response
            Borrower created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.borrowers._1fd12f73a7dc29d90f19d587c1c24d15(
                firstname="John",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client._1fd12f73a7dc29d90f19d587c1c24d15(
            firstname=firstname, lastname=lastname, email=email, request_options=request_options
        )
        return _response.data
