

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.animal import Animal
from ..types.enumerations import Enumerations
from ..types.enumerations_colors import EnumerationsColors
from ..types.random_number import RandomNumber
from .raw_client import AsyncRawValidationClient, RawValidationClient
from .types.get_responses_default_response import GetResponsesDefaultResponse
from .types.post_validation_optional_body_response import PostValidationOptionalBodyResponse


OMIT = typing.cast(typing.Any, ...)


class ValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationClient
        """
        return self._raw_client

    def get_validation_numbers_random_number(
        self,
        *,
        max: typing.Optional[float] = None,
        min: typing.Optional[float] = None,
        forbidden: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RandomNumber:
        """
        Parameters
        ----------
        max : typing.Optional[float]

        min : typing.Optional[float]

        forbidden : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RandomNumber
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_validation_numbers_random_number()
        """
        _response = self._raw_client.get_validation_numbers_random_number(
            max=max, min=min, forbidden=forbidden, request_options=request_options
        )
        return _response.data

    def post_validation_enums(
        self,
        *,
        colors: EnumerationsColors,
        star_ratings: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Enumerations:
        """
        Parameters
        ----------
        colors : EnumerationsColors

        star_ratings : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Enumerations
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.post_validation_enums(
            colors="red",
            star_ratings=1.1,
        )
        """
        _response = self._raw_client.post_validation_enums(
            colors=colors, star_ratings=star_ratings, request_options=request_options
        )
        return _response.data

    def post_validation_optional_body(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PostValidationOptionalBodyResponse]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PostValidationOptionalBodyResponse]
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.post_validation_optional_body()
        """
        _response = self._raw_client.post_validation_optional_body(id=id, request_options=request_options)
        return _response.data

    def post_validation_objects_discriminated_union(
        self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None
    ) -> Animal:
        """
        Parameters
        ----------
        request : Animal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Animal
            ok

        Examples
        --------
        from fern import Animal_Cat, FernApi

        client = FernApi()
        client.validation.post_validation_objects_discriminated_union(
            request=Animal_Cat(),
        )
        """
        _response = self._raw_client.post_validation_objects_discriminated_union(
            request=request, request_options=request_options
        )
        return _response.data

    def get_responses500(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_responses500()
        """
        _response = self._raw_client.get_responses500(request_options=request_options)
        return _response.data

    def get_responses_default(
        self, *, status: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetResponsesDefaultResponse:
        """
        Parameters
        ----------
        status : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponsesDefaultResponse
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_responses_default()
        """
        _response = self._raw_client.get_responses_default(status=status, request_options=request_options)
        return _response.data

    def get_responses_empty(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_responses_empty()
        """
        _response = self._raw_client.get_responses_empty(request_options=request_options)
        return _response.data


class AsyncValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationClient
        """
        return self._raw_client

    async def get_validation_numbers_random_number(
        self,
        *,
        max: typing.Optional[float] = None,
        min: typing.Optional[float] = None,
        forbidden: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RandomNumber:
        """
        Parameters
        ----------
        max : typing.Optional[float]

        min : typing.Optional[float]

        forbidden : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RandomNumber
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.get_validation_numbers_random_number()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validation_numbers_random_number(
            max=max, min=min, forbidden=forbidden, request_options=request_options
        )
        return _response.data

    async def post_validation_enums(
        self,
        *,
        colors: EnumerationsColors,
        star_ratings: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Enumerations:
        """
        Parameters
        ----------
        colors : EnumerationsColors

        star_ratings : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Enumerations
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.post_validation_enums(
                colors="red",
                star_ratings=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validation_enums(
            colors=colors, star_ratings=star_ratings, request_options=request_options
        )
        return _response.data

    async def post_validation_optional_body(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PostValidationOptionalBodyResponse]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PostValidationOptionalBodyResponse]
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.post_validation_optional_body()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validation_optional_body(id=id, request_options=request_options)
        return _response.data

    async def post_validation_objects_discriminated_union(
        self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None
    ) -> Animal:
        """
        Parameters
        ----------
        request : Animal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Animal
            ok

        Examples
        --------
        import asyncio

        from fern import Animal_Cat, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.post_validation_objects_discriminated_union(
                request=Animal_Cat(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validation_objects_discriminated_union(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_responses500(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.get_responses500()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_responses500(request_options=request_options)
        return _response.data

    async def get_responses_default(
        self, *, status: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetResponsesDefaultResponse:
        """
        Parameters
        ----------
        status : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponsesDefaultResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.get_responses_default()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_responses_default(status=status, request_options=request_options)
        return _response.data

    async def get_responses_empty(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.get_responses_empty()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_responses_empty(request_options=request_options)
        return _response.data
