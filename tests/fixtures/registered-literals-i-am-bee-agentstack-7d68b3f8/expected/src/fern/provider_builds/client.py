

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.build_configuration import BuildConfiguration
from ..types.build_state import BuildState
from ..types.github_url import GithubUrl
from ..types.on_complete_action import OnCompleteAction
from ..types.paginated_result_provider_build import PaginatedResultProviderBuild
from ..types.provider_build import ProviderBuild
from .raw_client import AsyncRawProviderBuildsClient, RawProviderBuildsClient


OMIT = typing.cast(typing.Any, ...)


class ProviderBuildsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProviderBuildsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProviderBuildsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProviderBuildsClient
        """
        return self._raw_client

    def list_provider_builds(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        status: typing.Optional[BuildState] = None,
        user_owned: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultProviderBuild:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        status : typing.Optional[BuildState]

        user_owned : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultProviderBuild
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.list_provider_builds()
        """
        _response = self._raw_client.list_provider_builds(
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            status=status,
            user_owned=user_owned,
            request_options=request_options,
        )
        return _response.data

    def create_provider_build(
        self,
        *,
        location: GithubUrl,
        on_complete: typing.Optional[OnCompleteAction] = OMIT,
        build_configuration: typing.Optional[BuildConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderBuild:
        """
        Parameters
        ----------
        location : GithubUrl

        on_complete : typing.Optional[OnCompleteAction]

        build_configuration : typing.Optional[BuildConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.create_provider_build(
            location="location",
        )
        """
        _response = self._raw_client.create_provider_build(
            location=location,
            on_complete=on_complete,
            build_configuration=build_configuration,
            request_options=request_options,
        )
        return _response.data

    def preview_provider_build(
        self,
        *,
        location: GithubUrl,
        on_complete: typing.Optional[OnCompleteAction] = OMIT,
        build_configuration: typing.Optional[BuildConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderBuild:
        """
        Parameters
        ----------
        location : GithubUrl

        on_complete : typing.Optional[OnCompleteAction]

        build_configuration : typing.Optional[BuildConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.preview_provider_build(
            location="location",
        )
        """
        _response = self._raw_client.preview_provider_build(
            location=location,
            on_complete=on_complete,
            build_configuration=build_configuration,
            request_options=request_options,
        )
        return _response.data

    def get_provider_build(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ProviderBuild:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.get_provider_build(
            id="id",
        )
        """
        _response = self._raw_client.get_provider_build(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def stream_logs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_builds.stream_logs(
            id="id",
        )
        """
        _response = self._raw_client.stream_logs(id, request_options=request_options)
        return _response.data


class AsyncProviderBuildsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProviderBuildsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProviderBuildsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProviderBuildsClient
        """
        return self._raw_client

    async def list_provider_builds(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        status: typing.Optional[BuildState] = None,
        user_owned: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultProviderBuild:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        status : typing.Optional[BuildState]

        user_owned : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultProviderBuild
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.list_provider_builds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_provider_builds(
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            status=status,
            user_owned=user_owned,
            request_options=request_options,
        )
        return _response.data

    async def create_provider_build(
        self,
        *,
        location: GithubUrl,
        on_complete: typing.Optional[OnCompleteAction] = OMIT,
        build_configuration: typing.Optional[BuildConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderBuild:
        """
        Parameters
        ----------
        location : GithubUrl

        on_complete : typing.Optional[OnCompleteAction]

        build_configuration : typing.Optional[BuildConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.create_provider_build(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_provider_build(
            location=location,
            on_complete=on_complete,
            build_configuration=build_configuration,
            request_options=request_options,
        )
        return _response.data

    async def preview_provider_build(
        self,
        *,
        location: GithubUrl,
        on_complete: typing.Optional[OnCompleteAction] = OMIT,
        build_configuration: typing.Optional[BuildConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderBuild:
        """
        Parameters
        ----------
        location : GithubUrl

        on_complete : typing.Optional[OnCompleteAction]

        build_configuration : typing.Optional[BuildConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.preview_provider_build(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_provider_build(
            location=location,
            on_complete=on_complete,
            build_configuration=build_configuration,
            request_options=request_options,
        )
        return _response.data

    async def get_provider_build(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderBuild:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderBuild
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.get_provider_build(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider_build(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def stream_logs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_builds.stream_logs(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stream_logs(id, request_options=request_options)
        return _response.data
