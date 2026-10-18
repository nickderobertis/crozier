

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key_response_output import ApiKeyResponseOutput
from ..types.create_secret_body import CreateSecretBody
from ..types.delete_secrets_body import DeleteSecretsBody
from ..types.legacy_api_keys_response_output import LegacyApiKeysResponseOutput
from ..types.pgsodium_config_response_output import PgsodiumConfigResponseOutput
from ..types.secret_response_output import SecretResponseOutput
from .raw_client import AsyncRawSecretsClient, RawSecretsClient
from .types.create_api_key_body_type import CreateApiKeyBodyType


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

    def v1get_project_api_keys(
        self, ref: str, *, reveal: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKeyResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1get_project_api_keys(
            ref="abcdefghijklmnopqrst",
            reveal="true",
        )
        """
        _response = self._raw_client.v1get_project_api_keys(ref, reveal=reveal, request_options=request_options)
        return _response.data

    def v1create_project_api_key(
        self,
        ref: str,
        *,
        type: CreateApiKeyBodyType,
        name: str,
        reveal: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        secret_jwt_template: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        type : CreateApiKeyBodyType

        name : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        description : typing.Optional[str]

        secret_jwt_template : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        from fern.secrets import CreateApiKeyBodyType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1create_project_api_key(
            ref="abcdefghijklmnopqrst",
            reveal="true",
            type=CreateApiKeyBodyType.SECRET,
            name="ci_secret_key",
            description="CI deploy key",
        )
        """
        _response = self._raw_client.v1create_project_api_key(
            ref,
            type=type,
            name=name,
            reveal=reveal,
            description=description,
            secret_jwt_template=secret_jwt_template,
            request_options=request_options,
        )
        return _response.data

    def v1get_project_legacy_api_keys(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LegacyApiKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LegacyApiKeysResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1get_project_legacy_api_keys(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_legacy_api_keys(ref, request_options=request_options)
        return _response.data

    def v1update_project_legacy_api_keys(
        self, ref: str, *, enabled: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LegacyApiKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        enabled : str
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LegacyApiKeysResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1update_project_legacy_api_keys(
            ref="abcdefghijklmnopqrst",
            enabled="true",
        )
        """
        _response = self._raw_client.v1update_project_legacy_api_keys(
            ref, enabled=enabled, request_options=request_options
        )
        return _response.data

    def v1get_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1get_project_api_key(
            ref="abcdefghijklmnopqrst",
            id="22222222-2222-4222-8222-222222222222",
            reveal="true",
        )
        """
        _response = self._raw_client.v1get_project_api_key(ref, id, reveal=reveal, request_options=request_options)
        return _response.data

    def v1delete_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        was_compromised: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string, true or false

        was_compromised : typing.Optional[str]
            Boolean string, true or false

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1delete_project_api_key(
            ref="abcdefghijklmnopqrst",
            id="22222222-2222-4222-8222-222222222222",
            reason="rotating_key",
        )
        """
        _response = self._raw_client.v1delete_project_api_key(
            ref, id, reveal=reveal, was_compromised=was_compromised, reason=reason, request_options=request_options
        )
        return _response.data

    def v1update_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        secret_jwt_template: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        name : typing.Optional[str]

        description : typing.Optional[str]

        secret_jwt_template : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1update_project_api_key(
            ref="abcdefghijklmnopqrst",
            id="22222222-2222-4222-8222-222222222222",
            reveal="true",
            name="ci_secret_key_rotated",
            description="Rotated after March release",
        )
        """
        _response = self._raw_client.v1update_project_api_key(
            ref,
            id,
            reveal=reveal,
            name=name,
            description=description,
            secret_jwt_template=secret_jwt_template,
            request_options=request_options,
        )
        return _response.data

    def v1get_pgsodium_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PgsodiumConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PgsodiumConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1get_pgsodium_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_pgsodium_config(ref, request_options=request_options)
        return _response.data

    def v1update_pgsodium_config(
        self, ref: str, *, root_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PgsodiumConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        root_key : str
            The pgsodium root key: 32 bytes, hex-encoded (64 characters).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PgsodiumConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1update_pgsodium_config(
            ref="abcdefghijklmnopqrst",
            root_key="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        )
        """
        _response = self._raw_client.v1update_pgsodium_config(ref, root_key=root_key, request_options=request_options)
        return _response.data

    def v1list_all_secrets(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SecretResponseOutput]:
        """
        Returns all secrets you've previously added to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SecretResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1list_all_secrets(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_secrets(ref, request_options=request_options)
        return _response.data

    def v1bulk_create_secrets(
        self, ref: str, *, request: CreateSecretBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Creates multiple secrets and adds them to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request : CreateSecretBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import CreateSecretBodyItem, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.v1bulk_create_secrets(
            ref="abcdefghijklmnopqrst",
            request=[
                CreateSecretBodyItem(
                    name="OPENAI_API_KEY",
                    value="sk-example-secret",
                ),
                CreateSecretBodyItem(
                    name="STRIPE_WEBHOOK_SECRET",
                    value="whsec_example",
                ),
            ],
        )
        """
        _response = self._raw_client.v1bulk_create_secrets(ref, request=request, request_options=request_options)
        return _response.data

    def v1bulk_delete_secrets(
        self, ref: str, *, request: DeleteSecretsBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all secrets with the given names from the specified project

        Parameters
        ----------
        ref : str
            Project ref

        request : DeleteSecretsBody

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
        client.secrets.v1bulk_delete_secrets(
            ref="abcdefghijklmnopqrst",
            request=["OPENAI_API_KEY"],
        )
        """
        _response = self._raw_client.v1bulk_delete_secrets(ref, request=request, request_options=request_options)
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

    async def v1get_project_api_keys(
        self, ref: str, *, reveal: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKeyResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1get_project_api_keys(
                ref="abcdefghijklmnopqrst",
                reveal="true",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_api_keys(ref, reveal=reveal, request_options=request_options)
        return _response.data

    async def v1create_project_api_key(
        self,
        ref: str,
        *,
        type: CreateApiKeyBodyType,
        name: str,
        reveal: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        secret_jwt_template: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        type : CreateApiKeyBodyType

        name : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        description : typing.Optional[str]

        secret_jwt_template : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern.secrets import CreateApiKeyBodyType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1create_project_api_key(
                ref="abcdefghijklmnopqrst",
                reveal="true",
                type=CreateApiKeyBodyType.SECRET,
                name="ci_secret_key",
                description="CI deploy key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_project_api_key(
            ref,
            type=type,
            name=name,
            reveal=reveal,
            description=description,
            secret_jwt_template=secret_jwt_template,
            request_options=request_options,
        )
        return _response.data

    async def v1get_project_legacy_api_keys(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LegacyApiKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LegacyApiKeysResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1get_project_legacy_api_keys(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_legacy_api_keys(ref, request_options=request_options)
        return _response.data

    async def v1update_project_legacy_api_keys(
        self, ref: str, *, enabled: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LegacyApiKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        enabled : str
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LegacyApiKeysResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1update_project_legacy_api_keys(
                ref="abcdefghijklmnopqrst",
                enabled="true",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_project_legacy_api_keys(
            ref, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def v1get_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1get_project_api_key(
                ref="abcdefghijklmnopqrst",
                id="22222222-2222-4222-8222-222222222222",
                reveal="true",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_api_key(
            ref, id, reveal=reveal, request_options=request_options
        )
        return _response.data

    async def v1delete_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        was_compromised: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string, true or false

        was_compromised : typing.Optional[str]
            Boolean string, true or false

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1delete_project_api_key(
                ref="abcdefghijklmnopqrst",
                id="22222222-2222-4222-8222-222222222222",
                reason="rotating_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_project_api_key(
            ref, id, reveal=reveal, was_compromised=was_compromised, reason=reason, request_options=request_options
        )
        return _response.data

    async def v1update_project_api_key(
        self,
        ref: str,
        id: str,
        *,
        reveal: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        secret_jwt_template: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        reveal : typing.Optional[str]
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        name : typing.Optional[str]

        description : typing.Optional[str]

        secret_jwt_template : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1update_project_api_key(
                ref="abcdefghijklmnopqrst",
                id="22222222-2222-4222-8222-222222222222",
                reveal="true",
                name="ci_secret_key_rotated",
                description="Rotated after March release",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_project_api_key(
            ref,
            id,
            reveal=reveal,
            name=name,
            description=description,
            secret_jwt_template=secret_jwt_template,
            request_options=request_options,
        )
        return _response.data

    async def v1get_pgsodium_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PgsodiumConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PgsodiumConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1get_pgsodium_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_pgsodium_config(ref, request_options=request_options)
        return _response.data

    async def v1update_pgsodium_config(
        self, ref: str, *, root_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PgsodiumConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        root_key : str
            The pgsodium root key: 32 bytes, hex-encoded (64 characters).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PgsodiumConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1update_pgsodium_config(
                ref="abcdefghijklmnopqrst",
                root_key="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_pgsodium_config(
            ref, root_key=root_key, request_options=request_options
        )
        return _response.data

    async def v1list_all_secrets(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SecretResponseOutput]:
        """
        Returns all secrets you've previously added to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SecretResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1list_all_secrets(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_secrets(ref, request_options=request_options)
        return _response.data

    async def v1bulk_create_secrets(
        self, ref: str, *, request: CreateSecretBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Creates multiple secrets and adds them to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request : CreateSecretBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateSecretBodyItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.v1bulk_create_secrets(
                ref="abcdefghijklmnopqrst",
                request=[
                    CreateSecretBodyItem(
                        name="OPENAI_API_KEY",
                        value="sk-example-secret",
                    ),
                    CreateSecretBodyItem(
                        name="STRIPE_WEBHOOK_SECRET",
                        value="whsec_example",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1bulk_create_secrets(ref, request=request, request_options=request_options)
        return _response.data

    async def v1bulk_delete_secrets(
        self, ref: str, *, request: DeleteSecretsBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all secrets with the given names from the specified project

        Parameters
        ----------
        ref : str
            Project ref

        request : DeleteSecretsBody

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
            await client.secrets.v1bulk_delete_secrets(
                ref="abcdefghijklmnopqrst",
                request=["OPENAI_API_KEY"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1bulk_delete_secrets(ref, request=request, request_options=request_options)
        return _response.data
