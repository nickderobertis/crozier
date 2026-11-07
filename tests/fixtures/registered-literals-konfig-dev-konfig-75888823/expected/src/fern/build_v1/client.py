

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.build import Build
from ..types.build_id import BuildId
from ..types.build_tag import BuildTag
from .raw_client import AsyncRawBuildV1Client, RawBuildV1Client


OMIT = typing.cast(typing.Any, ...)


class BuildV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBuildV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBuildV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBuildV1Client
        """
        return self._raw_client

    def get_builds(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Build]:
        """
        Returns an array of [builds](https://hathora.dev/docs/concepts/hathora-entities#build) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Build]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build_v1.get_builds(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_builds(app_id, request_options=request_options)
        return _response.data

    def get_build_info(
        self, app_id: AppId, build_id: BuildId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Build:
        """
        Get details for a [build](https://hathora.dev/docs/concepts/hathora-entities#build).

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Build
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build_v1.get_build_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            build_id=1,
        )
        """
        _response = self._raw_client.get_build_info(app_id, build_id, request_options=request_options)
        return _response.data

    def create_build(
        self,
        app_id: AppId,
        *,
        build_tag: typing.Optional[BuildTag] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Build:
        """
        Creates a new [build](https://hathora.dev/docs/concepts/hathora-entities#build). Responds with a `buildId` that you must pass to [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) to build the game server artifact. You can optionally pass in a `buildTag` to associate an external version with a build.

        Parameters
        ----------
        app_id : AppId

        build_tag : typing.Optional[BuildTag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Build


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build_v1.create_build(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.create_build(app_id, build_tag=build_tag, request_options=request_options)
        return _response.data

    def run_build(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Builds a game server artifact from a tarball you provide. Pass in the `buildId` generated from [`CreateBuild()`](https://hathora.dev/api#tag/BuildV1/operation/CreateBuild).

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Ok
        """
        with self._raw_client.run_build(app_id, build_id, file=file, request_options=request_options) as r:
            yield from r.data

    def delete_build(
        self, app_id: AppId, build_id: BuildId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a [build](https://hathora.dev/docs/concepts/hathora-entities#build). All associated metadata is deleted.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.build_v1.delete_build(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            build_id=1,
        )
        """
        _response = self._raw_client.delete_build(app_id, build_id, request_options=request_options)
        return _response.data


class AsyncBuildV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBuildV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBuildV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBuildV1Client
        """
        return self._raw_client

    async def get_builds(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Build]:
        """
        Returns an array of [builds](https://hathora.dev/docs/concepts/hathora-entities#build) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Build]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build_v1.get_builds(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_builds(app_id, request_options=request_options)
        return _response.data

    async def get_build_info(
        self, app_id: AppId, build_id: BuildId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Build:
        """
        Get details for a [build](https://hathora.dev/docs/concepts/hathora-entities#build).

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Build
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build_v1.get_build_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                build_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_build_info(app_id, build_id, request_options=request_options)
        return _response.data

    async def create_build(
        self,
        app_id: AppId,
        *,
        build_tag: typing.Optional[BuildTag] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Build:
        """
        Creates a new [build](https://hathora.dev/docs/concepts/hathora-entities#build). Responds with a `buildId` that you must pass to [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) to build the game server artifact. You can optionally pass in a `buildTag` to associate an external version with a build.

        Parameters
        ----------
        app_id : AppId

        build_tag : typing.Optional[BuildTag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Build


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build_v1.create_build(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_build(app_id, build_tag=build_tag, request_options=request_options)
        return _response.data

    async def run_build(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Builds a game server artifact from a tarball you provide. Pass in the `buildId` generated from [`CreateBuild()`](https://hathora.dev/api#tag/BuildV1/operation/CreateBuild).

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Ok
        """
        async with self._raw_client.run_build(app_id, build_id, file=file, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_build(
        self, app_id: AppId, build_id: BuildId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a [build](https://hathora.dev/docs/concepts/hathora-entities#build). All associated metadata is deleted.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.build_v1.delete_build(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                build_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_build(app_id, build_id, request_options=request_options)
        return _response.data
