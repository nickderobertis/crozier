

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.scoped_secret_result_body import ScopedSecretResultBody
from ..types.secret_filter_body import SecretFilterBody
from ..types.secret_scope import SecretScope
from ..types.secret_type import SecretType
from .raw_client import AsyncRawSecretsClient, RawSecretsClient


OMIT = typing.cast(typing.Any, ...)


class SecretsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSecretsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSecretsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSecretsClient
        """
        return self._raw_client

    def get_api_v1secrets(
        self, *, plan_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScopedSecretResultBody]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.get_api_v1secrets()
        """
        _response = self._raw_client.get_api_v1secrets(plan_id=plan_id, request_options=request_options)
        return _response.data

    def post_api_v1secrets(
        self,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        type: typing.Optional[SecretType] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopedSecretResultBody:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        type : typing.Optional[SecretType]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopedSecretResultBody
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.post_api_v1secrets()
        """
        _response = self._raw_client.post_api_v1secrets(
            plan_id=plan_id,
            filters=filters,
            notes=notes,
            scope=scope,
            secret_name=secret_name,
            type=type,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def put_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopedSecretResultBody:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopedSecretResultBody
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.put_api_v1secrets_secret_id(
            secret_id="secretId",
        )
        """
        _response = self._raw_client.put_api_v1secrets_secret_id(
            secret_id,
            plan_id=plan_id,
            filters=filters,
            notes=notes,
            scope=scope,
            secret_name=secret_name,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        scope: typing.Optional[SecretScope] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        scope : typing.Optional[SecretScope]

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
        client.secrets.delete_api_v1secrets_secret_id(
            secret_id="secretId",
        )
        """
        _response = self._raw_client.delete_api_v1secrets_secret_id(
            secret_id, plan_id=plan_id, scope=scope, request_options=request_options
        )
        return _response.data


class AsyncSecretsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSecretsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSecretsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSecretsClient
        """
        return self._raw_client

    async def get_api_v1secrets(
        self, *, plan_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScopedSecretResultBody]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.get_api_v1secrets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1secrets(plan_id=plan_id, request_options=request_options)
        return _response.data

    async def post_api_v1secrets(
        self,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        type: typing.Optional[SecretType] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopedSecretResultBody:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        type : typing.Optional[SecretType]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopedSecretResultBody
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.post_api_v1secrets()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1secrets(
            plan_id=plan_id,
            filters=filters,
            notes=notes,
            scope=scope,
            secret_name=secret_name,
            type=type,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def put_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScopedSecretResultBody:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScopedSecretResultBody
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.put_api_v1secrets_secret_id(
                secret_id="secretId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1secrets_secret_id(
            secret_id,
            plan_id=plan_id,
            filters=filters,
            notes=notes,
            scope=scope,
            secret_name=secret_name,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        scope: typing.Optional[SecretScope] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        scope : typing.Optional[SecretScope]

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
            await client.secrets.delete_api_v1secrets_secret_id(
                secret_id="secretId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1secrets_secret_id(
            secret_id, plan_id=plan_id, scope=scope, request_options=request_options
        )
        return _response.data
