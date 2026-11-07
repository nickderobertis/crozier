

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInstructionClient, RawInstructionClient
from .types.instruction import Instruction


OMIT = typing.cast(typing.Any, ...)


class InstructionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInstructionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInstructionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInstructionClient
        """
        return self._raw_client

    def get_instruction(
        self, instruction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Instruction:
        """
        Retrieve an instruction via it's ID

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.instruction.get_instruction(
            instruction_id="InstructionID",
        )
        """
        _response = self._raw_client.get_instruction(instruction_id, request_options=request_options)
        return _response.data

    def update_instruction(
        self,
        instruction_id: str,
        *,
        sequence: int,
        description: str,
        media_id: str,
        entity_id: str,
        entity_type: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Instruction:
        """
        Update an instruction

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

        sequence : int
            Sequence position of the instruction

        description : str
            instruction content

        media_id : str
            mediaID associated to the instruction

        entity_id : str
            entity ID the instruction belongs to

        entity_type : str

        id : typing.Optional[str]
            ID of the instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.instruction.update_instruction(
            instruction_id="InstructionID",
            sequence=1,
            description="This is the text of an instruction",
            media_id="23582396-12a3-425b-a597-8a22052823da",
            entity_id="6c4e174f-e760-4a4d-af6e-d1d5849b0fe1",
            entity_type="recipe",
        )
        """
        _response = self._raw_client.update_instruction(
            instruction_id,
            sequence=sequence,
            description=description,
            media_id=media_id,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def delete_instruction(
        self, instruction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an instruction

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

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
        client.instruction.delete_instruction(
            instruction_id="InstructionID",
        )
        """
        _response = self._raw_client.delete_instruction(instruction_id, request_options=request_options)
        return _response.data

    def create_instruction(
        self,
        recipe_id: str,
        *,
        sequence: int,
        description: str,
        media_id: str,
        entity_id: str,
        entity_type: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Instruction:
        """
        Creates an instruction for a recipe.

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        sequence : int
            Sequence position of the instruction

        description : str
            instruction content

        media_id : str
            mediaID associated to the instruction

        entity_id : str
            entity ID the instruction belongs to

        entity_type : str

        id : typing.Optional[str]
            ID of the instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.instruction.create_instruction(
            recipe_id="RecipeID",
            sequence=1,
            description="This is the text of an instruction",
            media_id="23582396-12a3-425b-a597-8a22052823da",
            entity_id="6c4e174f-e760-4a4d-af6e-d1d5849b0fe1",
            entity_type="recipe",
        )
        """
        _response = self._raw_client.create_instruction(
            recipe_id,
            sequence=sequence,
            description=description,
            media_id=media_id,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            request_options=request_options,
        )
        return _response.data


class AsyncInstructionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInstructionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInstructionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInstructionClient
        """
        return self._raw_client

    async def get_instruction(
        self, instruction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Instruction:
        """
        Retrieve an instruction via it's ID

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.instruction.get_instruction(
                instruction_id="InstructionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_instruction(instruction_id, request_options=request_options)
        return _response.data

    async def update_instruction(
        self,
        instruction_id: str,
        *,
        sequence: int,
        description: str,
        media_id: str,
        entity_id: str,
        entity_type: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Instruction:
        """
        Update an instruction

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

        sequence : int
            Sequence position of the instruction

        description : str
            instruction content

        media_id : str
            mediaID associated to the instruction

        entity_id : str
            entity ID the instruction belongs to

        entity_type : str

        id : typing.Optional[str]
            ID of the instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.instruction.update_instruction(
                instruction_id="InstructionID",
                sequence=1,
                description="This is the text of an instruction",
                media_id="23582396-12a3-425b-a597-8a22052823da",
                entity_id="6c4e174f-e760-4a4d-af6e-d1d5849b0fe1",
                entity_type="recipe",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_instruction(
            instruction_id,
            sequence=sequence,
            description=description,
            media_id=media_id,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def delete_instruction(
        self, instruction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an instruction

        Parameters
        ----------
        instruction_id : str
            ID of an instruction

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
            await client.instruction.delete_instruction(
                instruction_id="InstructionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_instruction(instruction_id, request_options=request_options)
        return _response.data

    async def create_instruction(
        self,
        recipe_id: str,
        *,
        sequence: int,
        description: str,
        media_id: str,
        entity_id: str,
        entity_type: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Instruction:
        """
        Creates an instruction for a recipe.

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        sequence : int
            Sequence position of the instruction

        description : str
            instruction content

        media_id : str
            mediaID associated to the instruction

        entity_id : str
            entity ID the instruction belongs to

        entity_type : str

        id : typing.Optional[str]
            ID of the instruction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Instruction
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.instruction.create_instruction(
                recipe_id="RecipeID",
                sequence=1,
                description="This is the text of an instruction",
                media_id="23582396-12a3-425b-a597-8a22052823da",
                entity_id="6c4e174f-e760-4a4d-af6e-d1d5849b0fe1",
                entity_type="recipe",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_instruction(
            recipe_id,
            sequence=sequence,
            description=description,
            media_id=media_id,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            request_options=request_options,
        )
        return _response.data
