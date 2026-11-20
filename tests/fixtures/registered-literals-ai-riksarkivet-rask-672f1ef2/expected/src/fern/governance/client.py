

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset_governance import DatasetGovernance
from .raw_client import AsyncRawGovernanceClient, RawGovernanceClient


OMIT = typing.cast(typing.Any, ...)


class GovernanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGovernanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGovernanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGovernanceClient
        """
        return self._raw_client

    def set_description(
        self, name: str, *, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Set the dataset's description (an empty string clears it).

        Parameters
        ----------
        name : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.governance.set_description(
            name="name",
            description="description",
        )
        """
        _response = self._raw_client.set_description(name, description=description, request_options=request_options)
        return _response.data

    def get_governance(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        The dataset's curated tags + description with last-writer attribution (who/when per field).

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.governance.get_governance(
            name="name",
        )
        """
        _response = self._raw_client.get_governance(name, request_options=request_options)
        return _response.data

    def add_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Add one governance tag (idempotent — re-adding an existing tag is a no-op re-stamp).

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.governance.add_tag(
            name="name",
            tag="tag",
        )
        """
        _response = self._raw_client.add_tag(name, tag, request_options=request_options)
        return _response.data

    def remove_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Remove one governance tag (idempotent — removing an absent tag is a no-op re-stamp).

        Deliberately unvalidated: removal only filters an existing element out of storage, so any string is
        safe — and it lets a curator purge a non-conforming tag (e.g. an old producer label) that the add
        path would refuse.

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.governance.remove_tag(
            name="name",
            tag="tag",
        )
        """
        _response = self._raw_client.remove_tag(name, tag, request_options=request_options)
        return _response.data


class AsyncGovernanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGovernanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGovernanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGovernanceClient
        """
        return self._raw_client

    async def set_description(
        self, name: str, *, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Set the dataset's description (an empty string clears it).

        Parameters
        ----------
        name : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.governance.set_description(
                name="name",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_description(
            name, description=description, request_options=request_options
        )
        return _response.data

    async def get_governance(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        The dataset's curated tags + description with last-writer attribution (who/when per field).

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.governance.get_governance(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_governance(name, request_options=request_options)
        return _response.data

    async def add_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Add one governance tag (idempotent — re-adding an existing tag is a no-op re-stamp).

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.governance.add_tag(
                name="name",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_tag(name, tag, request_options=request_options)
        return _response.data

    async def remove_tag(
        self, name: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetGovernance:
        """
        Remove one governance tag (idempotent — removing an absent tag is a no-op re-stamp).

        Deliberately unvalidated: removal only filters an existing element out of storage, so any string is
        safe — and it lets a curator purge a non-conforming tag (e.g. an old producer label) that the add
        path would refuse.

        Parameters
        ----------
        name : str

        tag : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetGovernance
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.governance.remove_tag(
                name="name",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_tag(name, tag, request_options=request_options)
        return _response.data
