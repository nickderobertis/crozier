

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shard_detail import ShardDetail
from .raw_client import AsyncRawShardsClient, RawShardsClient
from .types.get_api_shards_response import GetApiShardsResponse
from .types.post_api_shards_response import PostApiShardsResponse
from .types.post_api_shards_upload_response import PostApiShardsUploadResponse


OMIT = typing.cast(typing.Any, ...)


class ShardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShardsClient
        """
        return self._raw_client

    def list_all_shards(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiShardsResponse:
        """
        Get a paginated list of all Crystal shards

        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Number of items per page

        query : typing.Optional[str]
            Search query to filter shards by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shards.list_all_shards()
        """
        _response = self._raw_client.list_all_shards(
            page=page, per_page=per_page, query=query, request_options=request_options
        )
        return _response.data

    def create_a_new_shard(
        self,
        *,
        name: str,
        repository_url: str,
        version: str,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiShardsResponse:
        """
        Publish a new Crystal shard to the registry

        Parameters
        ----------
        name : str

        repository_url : str

        version : str

        description : typing.Optional[str]

        homepage_url : typing.Optional[str]

        documentation_url : typing.Optional[str]

        license : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiShardsResponse
            Shard created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shards.create_a_new_shard(
            name="my-shard",
            repository_url="https://github.com/user/my-shard",
            version="1.0.0",
        )
        """
        _response = self._raw_client.create_a_new_shard(
            name=name,
            repository_url=repository_url,
            version=version,
            description=description,
            homepage_url=homepage_url,
            documentation_url=documentation_url,
            license=license,
            request_options=request_options,
        )
        return _response.data

    def upload_shard_package(
        self,
        *,
        name: str,
        version: str,
        repository_url: str,
        package: core.File,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiShardsUploadResponse:
        """
        Upload a Crystal shard package via multipart form data.
        This endpoint accepts a .tar.gz file along with shard metadata.
        The package is uploaded directly to MinIO storage and a ShardVersion is created.

        **Authentication required:** Include auth_token in Authorization header or as query parameter.
        **Size limit:** Maximum 50 MB per package.

        Parameters
        ----------
        name : str
            Unique shard name (lowercase, alphanumeric with hyphens)

        version : str
            Semantic version number

        repository_url : str
            Git repository URL

        package : core.File
            See core.File for more documentation

        description : typing.Optional[str]
            Brief description of the shard

        homepage_url : typing.Optional[str]
            Project homepage URL

        documentation_url : typing.Optional[str]
            Documentation URL

        license : typing.Optional[str]
            SPDX license identifier

        checksum : typing.Optional[str]
            Optional SHA256 checksum for verification (computed if not provided)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiShardsUploadResponse
            Package uploaded successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shards.upload_shard_package(
            name="name",
            version="version",
            repository_url="repository_url",
        )
        """
        _response = self._raw_client.upload_shard_package(
            name=name,
            version=version,
            repository_url=repository_url,
            package=package,
            description=description,
            homepage_url=homepage_url,
            documentation_url=documentation_url,
            license=license,
            checksum=checksum,
            request_options=request_options,
        )
        return _response.data

    def get_shard_details_by_name_deprecated(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Superseded by /api/shards/{host}/{owner}/{repo}. A shard is identified by
        the repository it comes from, because two shards may share a name on
        different hosts.

        When exactly one shard carries the name, this responds 301 with the
        canonical path in Location. When more than one does, it responds 409
        with the candidate paths rather than guessing which was meant.

        Parameters
        ----------
        name : str
            Shard display name

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
        client.shards.get_shard_details_by_name_deprecated(
            name="name",
        )
        """
        _response = self._raw_client.get_shard_details_by_name_deprecated(name, request_options=request_options)
        return _response.data

    def get_shard_details(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ShardDetail:
        """
        Get a shard by the repository that identifies it, for example
        /api/shards/github.com/kemalcr/kemal.

        Nested namespace paths (host/group/subgroup/repo) are not addressable:
        identity is host/owner/repo.

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShardDetail
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shards.get_shard_details(
            host="github.com",
            owner="kemalcr",
            repo="kemal",
        )
        """
        _response = self._raw_client.get_shard_details(host, owner, repo, request_options=request_options)
        return _response.data


class AsyncShardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShardsClient
        """
        return self._raw_client

    async def list_all_shards(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiShardsResponse:
        """
        Get a paginated list of all Crystal shards

        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Number of items per page

        query : typing.Optional[str]
            Search query to filter shards by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shards.list_all_shards()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_shards(
            page=page, per_page=per_page, query=query, request_options=request_options
        )
        return _response.data

    async def create_a_new_shard(
        self,
        *,
        name: str,
        repository_url: str,
        version: str,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiShardsResponse:
        """
        Publish a new Crystal shard to the registry

        Parameters
        ----------
        name : str

        repository_url : str

        version : str

        description : typing.Optional[str]

        homepage_url : typing.Optional[str]

        documentation_url : typing.Optional[str]

        license : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiShardsResponse
            Shard created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shards.create_a_new_shard(
                name="my-shard",
                repository_url="https://github.com/user/my-shard",
                version="1.0.0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_shard(
            name=name,
            repository_url=repository_url,
            version=version,
            description=description,
            homepage_url=homepage_url,
            documentation_url=documentation_url,
            license=license,
            request_options=request_options,
        )
        return _response.data

    async def upload_shard_package(
        self,
        *,
        name: str,
        version: str,
        repository_url: str,
        package: core.File,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiShardsUploadResponse:
        """
        Upload a Crystal shard package via multipart form data.
        This endpoint accepts a .tar.gz file along with shard metadata.
        The package is uploaded directly to MinIO storage and a ShardVersion is created.

        **Authentication required:** Include auth_token in Authorization header or as query parameter.
        **Size limit:** Maximum 50 MB per package.

        Parameters
        ----------
        name : str
            Unique shard name (lowercase, alphanumeric with hyphens)

        version : str
            Semantic version number

        repository_url : str
            Git repository URL

        package : core.File
            See core.File for more documentation

        description : typing.Optional[str]
            Brief description of the shard

        homepage_url : typing.Optional[str]
            Project homepage URL

        documentation_url : typing.Optional[str]
            Documentation URL

        license : typing.Optional[str]
            SPDX license identifier

        checksum : typing.Optional[str]
            Optional SHA256 checksum for verification (computed if not provided)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiShardsUploadResponse
            Package uploaded successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shards.upload_shard_package(
                name="name",
                version="version",
                repository_url="repository_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_shard_package(
            name=name,
            version=version,
            repository_url=repository_url,
            package=package,
            description=description,
            homepage_url=homepage_url,
            documentation_url=documentation_url,
            license=license,
            checksum=checksum,
            request_options=request_options,
        )
        return _response.data

    async def get_shard_details_by_name_deprecated(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Superseded by /api/shards/{host}/{owner}/{repo}. A shard is identified by
        the repository it comes from, because two shards may share a name on
        different hosts.

        When exactly one shard carries the name, this responds 301 with the
        canonical path in Location. When more than one does, it responds 409
        with the candidate paths rather than guessing which was meant.

        Parameters
        ----------
        name : str
            Shard display name

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
            await client.shards.get_shard_details_by_name_deprecated(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shard_details_by_name_deprecated(name, request_options=request_options)
        return _response.data

    async def get_shard_details(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ShardDetail:
        """
        Get a shard by the repository that identifies it, for example
        /api/shards/github.com/kemalcr/kemal.

        Nested namespace paths (host/group/subgroup/repo) are not addressable:
        identity is host/owner/repo.

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShardDetail
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shards.get_shard_details(
                host="github.com",
                owner="kemalcr",
                repo="kemal",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shard_details(host, owner, repo, request_options=request_options)
        return _response.data
