

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subscription_list import SubscriptionList
from .raw_client import AsyncRawRepositoryCredentialsClient, RawRepositoryCredentialsClient


class RepositoryCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRepositoryCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRepositoryCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRepositoryCredentialsClient
        """
        return self._raw_client

    def add_repository(
        self,
        *,
        repository: str,
        autosubscribe: typing.Optional[bool] = None,
        dryrun: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """


        Parameters
        ----------
        repository : str
            full repository to add e.g. docker.io/library/alpine

        autosubscribe : typing.Optional[bool]
            flag to enable/disable auto tag_update activation when new images from a repo are added

        dryrun : typing.Optional[bool]
            flag to return tags in the repository without actually watching the repository, default is false

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Repository and discovered tags added

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.repository_credentials.add_repository(
            repository="repository",
        )
        """
        _response = self._raw_client.add_repository(
            repository=repository,
            autosubscribe=autosubscribe,
            dryrun=dryrun,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data


class AsyncRepositoryCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRepositoryCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRepositoryCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRepositoryCredentialsClient
        """
        return self._raw_client

    async def add_repository(
        self,
        *,
        repository: str,
        autosubscribe: typing.Optional[bool] = None,
        dryrun: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """


        Parameters
        ----------
        repository : str
            full repository to add e.g. docker.io/library/alpine

        autosubscribe : typing.Optional[bool]
            flag to enable/disable auto tag_update activation when new images from a repo are added

        dryrun : typing.Optional[bool]
            flag to return tags in the repository without actually watching the repository, default is false

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Repository and discovered tags added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.repository_credentials.add_repository(
                repository="repository",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_repository(
            repository=repository,
            autosubscribe=autosubscribe,
            dryrun=dryrun,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data
