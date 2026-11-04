

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.named_ref import NamedRef
from ..types.predicate_dto import PredicateDto
from ..types.transform_response import TransformResponse
from .raw_client import AsyncRawTransformsClient, RawTransformsClient


OMIT = typing.cast(typing.Any, ...)


class TransformsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransformsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransformsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransformsClient
        """
        return self._raw_client

    def returns_all_available_transformations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransformResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransformResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transforms.returns_all_available_transformations()
        """
        _response = self._raw_client.returns_all_available_transformations(request_options=request_options)
        return _response.data

    def creates_new_transform(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        predicate: typing.Optional[PredicateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        predicate : typing.Optional[PredicateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transforms.creates_new_transform(
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.creates_new_transform(
            name=name,
            type=type,
            schema=schema,
            description=description,
            vaults=vaults,
            config=config,
            predicate=predicate,
            request_options=request_options,
        )
        return _response.data

    def returns_a_transform_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransformResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransformResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transforms.returns_a_transform_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_transform_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_transform(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        predicate: typing.Optional[PredicateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransformResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        predicate : typing.Optional[PredicateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransformResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transforms.updates_an_existing_transform(
            id=1000000,
            name="name",
            type="type",
            schema="schema",
        )
        """
        _response = self._raw_client.updates_an_existing_transform(
            id,
            name=name,
            type=type,
            schema=schema,
            description=description,
            vaults=vaults,
            config=config,
            predicate=predicate,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_transform(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
        client.transforms.deletes_an_existing_transform(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_transform(id, request_options=request_options)
        return _response.data


class AsyncTransformsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransformsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransformsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransformsClient
        """
        return self._raw_client

    async def returns_all_available_transformations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransformResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransformResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transforms.returns_all_available_transformations()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_transformations(request_options=request_options)
        return _response.data

    async def creates_new_transform(
        self,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        predicate: typing.Optional[PredicateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        predicate : typing.Optional[PredicateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transforms.creates_new_transform(
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_transform(
            name=name,
            type=type,
            schema=schema,
            description=description,
            vaults=vaults,
            config=config,
            predicate=predicate,
            request_options=request_options,
        )
        return _response.data

    async def returns_a_transform_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransformResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransformResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transforms.returns_a_transform_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_transform_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_transform(
        self,
        id: int,
        *,
        name: str,
        type: str,
        schema: str,
        description: typing.Optional[str] = OMIT,
        vaults: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        predicate: typing.Optional[PredicateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransformResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : str

        schema : str

        description : typing.Optional[str]

        vaults : typing.Optional[typing.Sequence[NamedRef]]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        predicate : typing.Optional[PredicateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransformResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transforms.updates_an_existing_transform(
                id=1000000,
                name="name",
                type="type",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_transform(
            id,
            name=name,
            type=type,
            schema=schema,
            description=description,
            vaults=vaults,
            config=config,
            predicate=predicate,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_transform(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
            await client.transforms.deletes_an_existing_transform(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_transform(id, request_options=request_options)
        return _response.data
