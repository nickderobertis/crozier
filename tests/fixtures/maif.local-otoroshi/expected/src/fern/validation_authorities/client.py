

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted import Deleted
from ..types.patch import Patch
from ..types.validation_authority import ValidationAuthority
from .raw_client import AsyncRawValidationAuthoritiesClient, RawValidationAuthoritiesClient


OMIT = typing.cast(typing.Any, ...)


class ValidationAuthoritiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationAuthoritiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValidationAuthoritiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationAuthoritiesClient
        """
        return self._raw_client

    def find_all_client_validators(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ValidationAuthority]:
        """
        Get all validation authoritiess

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ValidationAuthority]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.find_all_client_validators()
        """
        _response = self._raw_client.find_all_client_validators(request_options=request_options)
        return _response.data

    def create_client_validator(
        self,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationAuthority:
        """
        Create one validation authorities

        Parameters
        ----------
        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.create_client_validator(
            always_valid=True,
            bad_ttl=123,
            description="a string value",
            good_ttl=123,
            headers={"key": "value"},
            host="a string value",
            id="a string value",
            method="a string value",
            name="a string value",
            no_cache=True,
            path="a string value",
            timeout=123,
            url="a string value",
        )
        """
        _response = self._raw_client.create_client_validator(
            always_valid=always_valid,
            bad_ttl=bad_ttl,
            description=description,
            good_ttl=good_ttl,
            headers=headers,
            host=host,
            id=id,
            method=method,
            name=name,
            no_cache=no_cache,
            path=path,
            timeout=timeout,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def find_client_validator_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationAuthority:
        """
        Get one validation authorities by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.find_client_validator_by_id(
            id="id",
        )
        """
        _response = self._raw_client.find_client_validator_by_id(id, request_options=request_options)
        return _response.data

    def update_client_validator(
        self,
        id_: str,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationAuthority:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id_ : str
            The validation authorities id

        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.update_client_validator(
            id_="id",
            always_valid=True,
            bad_ttl=123,
            description="a string value",
            good_ttl=123,
            headers={"key": "value"},
            host="a string value",
            id="a string value",
            method="a string value",
            name="a string value",
            no_cache=True,
            path="a string value",
            timeout=123,
            url="a string value",
        )
        """
        _response = self._raw_client.update_client_validator(
            id_,
            always_valid=always_valid,
            bad_ttl=bad_ttl,
            description=description,
            good_ttl=good_ttl,
            headers=headers,
            host=host,
            id=id,
            method=method,
            name=name,
            no_cache=no_cache,
            path=path,
            timeout=timeout,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def delete_client_validator(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.delete_client_validator(
            id="id",
        )
        """
        _response = self._raw_client.delete_client_validator(id, request_options=request_options)
        return _response.data

    def patch_client_validator(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationAuthority:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.validation_authorities.patch_client_validator(
            id="id",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_client_validator(id, request=request, request_options=request_options)
        return _response.data


class AsyncValidationAuthoritiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationAuthoritiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValidationAuthoritiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationAuthoritiesClient
        """
        return self._raw_client

    async def find_all_client_validators(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ValidationAuthority]:
        """
        Get all validation authoritiess

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ValidationAuthority]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.find_all_client_validators()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_client_validators(request_options=request_options)
        return _response.data

    async def create_client_validator(
        self,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationAuthority:
        """
        Create one validation authorities

        Parameters
        ----------
        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.create_client_validator(
                always_valid=True,
                bad_ttl=123,
                description="a string value",
                good_ttl=123,
                headers={"key": "value"},
                host="a string value",
                id="a string value",
                method="a string value",
                name="a string value",
                no_cache=True,
                path="a string value",
                timeout=123,
                url="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_client_validator(
            always_valid=always_valid,
            bad_ttl=bad_ttl,
            description=description,
            good_ttl=good_ttl,
            headers=headers,
            host=host,
            id=id,
            method=method,
            name=name,
            no_cache=no_cache,
            path=path,
            timeout=timeout,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def find_client_validator_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationAuthority:
        """
        Get one validation authorities by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.find_client_validator_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_client_validator_by_id(id, request_options=request_options)
        return _response.data

    async def update_client_validator(
        self,
        id_: str,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationAuthority:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id_ : str
            The validation authorities id

        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.update_client_validator(
                id_="id",
                always_valid=True,
                bad_ttl=123,
                description="a string value",
                good_ttl=123,
                headers={"key": "value"},
                host="a string value",
                id="a string value",
                method="a string value",
                name="a string value",
                no_cache=True,
                path="a string value",
                timeout=123,
                url="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client_validator(
            id_,
            always_valid=always_valid,
            bad_ttl=bad_ttl,
            description=description,
            good_ttl=good_ttl,
            headers=headers,
            host=host,
            id=id,
            method=method,
            name=name,
            no_cache=no_cache,
            path=path,
            timeout=timeout,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def delete_client_validator(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.delete_client_validator(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_client_validator(id, request_options=request_options)
        return _response.data

    async def patch_client_validator(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationAuthority:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationAuthority
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.validation_authorities.patch_client_validator(
                id="id",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_client_validator(id, request=request, request_options=request_options)
        return _response.data
