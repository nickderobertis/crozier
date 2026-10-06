

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.category import Category
from ..types.pet import Pet
from ..types.pet_status import PetStatus
from ..types.tag import Tag
from .raw_client import AsyncRawPetClient, RawPetClient
from .types.find_pets_by_status_request_status import FindPetsByStatusRequestStatus


OMIT = typing.cast(typing.Any, ...)


class PetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPetClient
        """
        return self._raw_client

    def add_pet(
        self,
        *,
        name: str,
        photo_urls: typing.Sequence[str],
        id: typing.Optional[int] = OMIT,
        category: typing.Optional[Category] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        status: typing.Optional[PetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Add a new pet to the store.

        Parameters
        ----------
        name : str

        photo_urls : typing.Sequence[str]

        id : typing.Optional[int]

        category : typing.Optional[Category]

        tags : typing.Optional[typing.Sequence[Tag]]

        status : typing.Optional[PetStatus]
            pet status in the store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.add_pet(
            name="doggie",
            photo_urls=["photoUrls"],
        )
        """
        _response = self._raw_client.add_pet(
            name=name,
            photo_urls=photo_urls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def update_pet(
        self,
        *,
        name: str,
        photo_urls: typing.Sequence[str],
        id: typing.Optional[int] = OMIT,
        category: typing.Optional[Category] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        status: typing.Optional[PetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Update an existing pet by Id.

        Parameters
        ----------
        name : str

        photo_urls : typing.Sequence[str]

        id : typing.Optional[int]

        category : typing.Optional[Category]

        tags : typing.Optional[typing.Sequence[Tag]]

        status : typing.Optional[PetStatus]
            pet status in the store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.update_pet(
            name="doggie",
            photo_urls=["photoUrls"],
        )
        """
        _response = self._raw_client.update_pet(
            name=name,
            photo_urls=photo_urls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def find_pets_by_status(
        self, *, status: FindPetsByStatusRequestStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Pet]:
        """
        Multiple status values can be provided with comma separated strings.

        Parameters
        ----------
        status : FindPetsByStatusRequestStatus
            Status values that need to be considered for filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pet]
            successful operation

        Examples
        --------
        from fern.pet import FindPetsByStatusRequestStatus

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.find_pets_by_status(
            status=FindPetsByStatusRequestStatus.AVAILABLE,
        )
        """
        _response = self._raw_client.find_pets_by_status(status=status, request_options=request_options)
        return _response.data

    def find_pets_by_tags(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Pet]:
        """
        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tags to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pet]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.find_pets_by_tags(
            tags=["tags"],
        )
        """
        _response = self._raw_client.find_pets_by_tags(tags=tags, request_options=request_options)
        return _response.data

    def get_pet_by_id(self, pet_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Pet:
        """
        Returns a single pet.

        Parameters
        ----------
        pet_id : int
            ID of pet to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.get_pet_by_id(
            pet_id=1000000,
        )
        """
        _response = self._raw_client.get_pet_by_id(pet_id, request_options=request_options)
        return _response.data

    def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Updates a pet resource based on the form data.

        Parameters
        ----------
        pet_id : int
            ID of pet that needs to be updated

        name : typing.Optional[str]
            Name of pet that needs to be updated

        status : typing.Optional[str]
            Status of pet that needs to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.update_pet_with_form(
            pet_id=1000000,
        )
        """
        _response = self._raw_client.update_pet_with_form(
            pet_id, name=name, status=status, request_options=request_options
        )
        return _response.data

    def delete_pet(self, pet_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a pet.

        Parameters
        ----------
        pet_id : int
            Pet id to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.pet.delete_pet(
            pet_id=1000000,
        )
        """
        _response = self._raw_client.delete_pet(pet_id, request_options=request_options)
        return _response.data

    def upload_file(
        self,
        pet_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        additional_metadata: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload image of the pet.

        Parameters
        ----------
        pet_id : int
            ID of pet to update

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        additional_metadata : typing.Optional[str]
            Additional Metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = self._raw_client.upload_file(
            pet_id, request=request, additional_metadata=additional_metadata, request_options=request_options
        )
        return _response.data


class AsyncPetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPetClient
        """
        return self._raw_client

    async def add_pet(
        self,
        *,
        name: str,
        photo_urls: typing.Sequence[str],
        id: typing.Optional[int] = OMIT,
        category: typing.Optional[Category] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        status: typing.Optional[PetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Add a new pet to the store.

        Parameters
        ----------
        name : str

        photo_urls : typing.Sequence[str]

        id : typing.Optional[int]

        category : typing.Optional[Category]

        tags : typing.Optional[typing.Sequence[Tag]]

        status : typing.Optional[PetStatus]
            pet status in the store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.add_pet(
                name="doggie",
                photo_urls=["photoUrls"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_pet(
            name=name,
            photo_urls=photo_urls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def update_pet(
        self,
        *,
        name: str,
        photo_urls: typing.Sequence[str],
        id: typing.Optional[int] = OMIT,
        category: typing.Optional[Category] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        status: typing.Optional[PetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Update an existing pet by Id.

        Parameters
        ----------
        name : str

        photo_urls : typing.Sequence[str]

        id : typing.Optional[int]

        category : typing.Optional[Category]

        tags : typing.Optional[typing.Sequence[Tag]]

        status : typing.Optional[PetStatus]
            pet status in the store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.update_pet(
                name="doggie",
                photo_urls=["photoUrls"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pet(
            name=name,
            photo_urls=photo_urls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def find_pets_by_status(
        self, *, status: FindPetsByStatusRequestStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Pet]:
        """
        Multiple status values can be provided with comma separated strings.

        Parameters
        ----------
        status : FindPetsByStatusRequestStatus
            Status values that need to be considered for filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pet]
            successful operation

        Examples
        --------
        import asyncio

        from fern.pet import FindPetsByStatusRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.find_pets_by_status(
                status=FindPetsByStatusRequestStatus.AVAILABLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_pets_by_status(status=status, request_options=request_options)
        return _response.data

    async def find_pets_by_tags(
        self,
        *,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Pet]:
        """
        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        Parameters
        ----------
        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tags to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pet]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.find_pets_by_tags(
                tags=["tags"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_pets_by_tags(tags=tags, request_options=request_options)
        return _response.data

    async def get_pet_by_id(self, pet_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Pet:
        """
        Returns a single pet.

        Parameters
        ----------
        pet_id : int
            ID of pet to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.get_pet_by_id(
                pet_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pet_by_id(pet_id, request_options=request_options)
        return _response.data

    async def update_pet_with_form(
        self,
        pet_id: int,
        *,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pet:
        """
        Updates a pet resource based on the form data.

        Parameters
        ----------
        pet_id : int
            ID of pet that needs to be updated

        name : typing.Optional[str]
            Name of pet that needs to be updated

        status : typing.Optional[str]
            Status of pet that needs to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pet
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.update_pet_with_form(
                pet_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pet_with_form(
            pet_id, name=name, status=status, request_options=request_options
        )
        return _response.data

    async def delete_pet(self, pet_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a pet.

        Parameters
        ----------
        pet_id : int
            Pet id to delete

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pet.delete_pet(
                pet_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_pet(pet_id, request_options=request_options)
        return _response.data

    async def upload_file(
        self,
        pet_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        additional_metadata: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload image of the pet.

        Parameters
        ----------
        pet_id : int
            ID of pet to update

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        additional_metadata : typing.Optional[str]
            Additional Metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = await self._raw_client.upload_file(
            pet_id, request=request, additional_metadata=additional_metadata, request_options=request_options
        )
        return _response.data
