

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.counter import Counter
from ..types.keycloak_config import KeycloakConfig
from ..types.secret import Secret
from .raw_client import AsyncRawConfigClient, RawConfigClient


OMIT = typing.cast(typing.Any, ...)


class ConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigClient
        """
        return self._raw_client

    def get_features_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Get features configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.get_features_configuration()
        """
        _response = self._raw_client.get_features_configuration(request_options=request_options)
        return _response.data

    def get_keycloak_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> KeycloakConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeycloakConfig
            Get current configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.get_keycloak_config()
        """
        _response = self._raw_client.get_keycloak_config(request_options=request_options)
        return _response.data

    def get_secrets(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Secret]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Secrets to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Secrets to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Secret]
            List of found Secrets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.get_secrets()
        """
        _response = self._raw_client.get_secrets(page=page, size=size, request_options=request_options)
        return _response.data

    def create_secret(
        self,
        *,
        description: str,
        name: str,
        ca_cert_pem: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        token: typing.Optional[str] = OMIT,
        token_header: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Secret:
        """
        Parameters
        ----------
        description : str
            Description of this Secret

        name : str
            Unique distinct name of Secret

        ca_cert_pem : typing.Optional[str]

        id : typing.Optional[str]
            Unique identifier of Secret

        password : typing.Optional[str]

        token : typing.Optional[str]

        token_header : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Secret
            Created Secret

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.create_secret(
            description="description",
            name="name",
        )
        """
        _response = self._raw_client.create_secret(
            description=description,
            name=name,
            ca_cert_pem=ca_cert_pem,
            id=id,
            password=password,
            token=token,
            token_header=token_header,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def get_secrets_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of Secrets in datastore

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.get_secrets_counter()
        """
        _response = self._raw_client.get_secrets_counter(request_options=request_options)
        return _response.data

    def get_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Secret:
        """
        Retrieve a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Secret
            Found Secret

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.config.get_secret(
            id="id",
        )
        """
        _response = self._raw_client.get_secret(id, request_options=request_options)
        return _response.data

    def update_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Update a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

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
        client.config.update_secret(
            id="id",
        )
        """
        _response = self._raw_client.update_secret(id, request_options=request_options)
        return _response.data

    def delete_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

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
        client.config.delete_secret(
            id="id",
        )
        """
        _response = self._raw_client.delete_secret(id, request_options=request_options)
        return _response.data


class AsyncConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigClient
        """
        return self._raw_client

    async def get_features_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Get features configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.get_features_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_features_configuration(request_options=request_options)
        return _response.data

    async def get_keycloak_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> KeycloakConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeycloakConfig
            Get current configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.get_keycloak_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_keycloak_config(request_options=request_options)
        return _response.data

    async def get_secrets(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Secret]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Secrets to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Secrets to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Secret]
            List of found Secrets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.get_secrets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secrets(page=page, size=size, request_options=request_options)
        return _response.data

    async def create_secret(
        self,
        *,
        description: str,
        name: str,
        ca_cert_pem: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        token: typing.Optional[str] = OMIT,
        token_header: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Secret:
        """
        Parameters
        ----------
        description : str
            Description of this Secret

        name : str
            Unique distinct name of Secret

        ca_cert_pem : typing.Optional[str]

        id : typing.Optional[str]
            Unique identifier of Secret

        password : typing.Optional[str]

        token : typing.Optional[str]

        token_header : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Secret
            Created Secret

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.create_secret(
                description="description",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_secret(
            description=description,
            name=name,
            ca_cert_pem=ca_cert_pem,
            id=id,
            password=password,
            token=token,
            token_header=token_header,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def get_secrets_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of Secrets in datastore

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.get_secrets_counter()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secrets_counter(request_options=request_options)
        return _response.data

    async def get_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Secret:
        """
        Retrieve a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Secret
            Found Secret

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.config.get_secret(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secret(id, request_options=request_options)
        return _response.data

    async def update_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Update a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

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
            await client.config.update_secret(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_secret(id, request_options=request_options)
        return _response.data

    async def delete_secret(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a Secret

        Parameters
        ----------
        id : str
            Unique identifier of Secret to manage

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
            await client.config.delete_secret(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_secret(id, request_options=request_options)
        return _response.data
