

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mutable_secret_type import MutableSecretType
from ..types.mutable_secret_value import MutableSecretValue
from ..types.owner import Owner
from .raw_client import AsyncRawSecretsClient, RawSecretsClient
from .types.create_secret_response import CreateSecretResponse
from .types.get_secret_by_id_response import GetSecretByIdResponse
from .types.get_secrets_response import GetSecretsResponse
from .types.update_secret_response import UpdateSecretResponse


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

    def get_secrets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSecretsResponse:
        """
        Retrieve all secrets belonging to the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretsResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.get_secrets()
        """
        _response = self._raw_client.get_secrets(
            page_size=page_size, page_number=page_number, request_options=request_options
        )
        return _response.data

    def create_secret(
        self,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSecretResponse:
        """
        Create a secret

        Parameters
        ----------
        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSecretResponse
            successful operation

        Examples
        --------
        from fern import FernApi, MutableSecretType, Owner

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.create_secret(
            name="My Secret",
            type=MutableSecretType.API_KEY,
            owners=[
                Owner(
                    id="617082258803c70031f85b26",
                    type="USER",
                )
            ],
        )
        """
        _response = self._raw_client.create_secret(
            name=name,
            type=type,
            owners=owners,
            value=value,
            tenant=tenant,
            domain=domain,
            locked_at=locked_at,
            encrypted_fields=encrypted_fields,
            mixed_properties=mixed_properties,
            request_options=request_options,
        )
        return _response.data

    def get_secret_by_id(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSecretByIdResponse:
        """
        Returns a secret with given ID

        Parameters
        ----------
        secret_id : str
            ID of secret to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretByIdResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.get_secret_by_id(
            secret_id="6170a3c465dbff001297f235",
        )
        """
        _response = self._raw_client.get_secret_by_id(secret_id, request_options=request_options)
        return _response.data

    def delete_secret(self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to delete

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
        client.secrets.delete_secret(
            secret_id="6170a3c465dbff001297f235",
        )
        """
        _response = self._raw_client.delete_secret(secret_id, request_options=request_options)
        return _response.data

    def update_secret(
        self,
        secret_id: str,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSecretResponse:
        """
        Update a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to update

        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSecretResponse
            successful operation

        Examples
        --------
        from fern import FernApi, MutableSecretType, Owner

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.secrets.update_secret(
            secret_id="secretId",
            name="My Secret",
            type=MutableSecretType.API_KEY,
            owners=[
                Owner(
                    id="617082258803c70031f85b26",
                    type="USER",
                )
            ],
        )
        """
        _response = self._raw_client.update_secret(
            secret_id,
            name=name,
            type=type,
            owners=owners,
            value=value,
            tenant=tenant,
            domain=domain,
            locked_at=locked_at,
            encrypted_fields=encrypted_fields,
            mixed_properties=mixed_properties,
            request_options=request_options,
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

    async def get_secrets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSecretsResponse:
        """
        Retrieve all secrets belonging to the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretsResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.get_secrets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secrets(
            page_size=page_size, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def create_secret(
        self,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSecretResponse:
        """
        Create a secret

        Parameters
        ----------
        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSecretResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutableSecretType, Owner

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.create_secret(
                name="My Secret",
                type=MutableSecretType.API_KEY,
                owners=[
                    Owner(
                        id="617082258803c70031f85b26",
                        type="USER",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_secret(
            name=name,
            type=type,
            owners=owners,
            value=value,
            tenant=tenant,
            domain=domain,
            locked_at=locked_at,
            encrypted_fields=encrypted_fields,
            mixed_properties=mixed_properties,
            request_options=request_options,
        )
        return _response.data

    async def get_secret_by_id(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSecretByIdResponse:
        """
        Returns a secret with given ID

        Parameters
        ----------
        secret_id : str
            ID of secret to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretByIdResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.get_secret_by_id(
                secret_id="6170a3c465dbff001297f235",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secret_by_id(secret_id, request_options=request_options)
        return _response.data

    async def delete_secret(self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to delete

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
            await client.secrets.delete_secret(
                secret_id="6170a3c465dbff001297f235",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_secret(secret_id, request_options=request_options)
        return _response.data

    async def update_secret(
        self,
        secret_id: str,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSecretResponse:
        """
        Update a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to update

        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSecretResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutableSecretType, Owner

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.secrets.update_secret(
                secret_id="secretId",
                name="My Secret",
                type=MutableSecretType.API_KEY,
                owners=[
                    Owner(
                        id="617082258803c70031f85b26",
                        type="USER",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_secret(
            secret_id,
            name=name,
            type=type,
            owners=owners,
            value=value,
            tenant=tenant,
            domain=domain,
            locked_at=locked_at,
            encrypted_fields=encrypted_fields,
            mixed_properties=mixed_properties,
            request_options=request_options,
        )
        return _response.data
