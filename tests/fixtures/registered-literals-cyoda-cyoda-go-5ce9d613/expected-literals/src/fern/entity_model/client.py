

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entity_model_action_result_dto import EntityModelActionResultDto
from ..types.entity_model_dto import EntityModelDto
from .raw_client import AsyncRawEntityModelClient, RawEntityModelClient
from .types.export_metadata_request_converter import ExportMetadataRequestConverter
from .types.import_entity_model_request_converter import ImportEntityModelRequestConverter
from .types.import_entity_model_request_data_format import ImportEntityModelRequestDataFormat
from .types.set_entity_model_change_level_request_change_level import SetEntityModelChangeLevelRequestChangeLevel


OMIT = typing.cast(typing.Any, ...)


class EntityModelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntityModelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntityModelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntityModelClient
        """
        return self._raw_client

    def get_available_entity_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> EntityModelDto:
        """

        Retrieves a list of all available entity models in the system.

        Each model in the response includes its identifier, name, version,
        current state (LOCKED/UNLOCKED), and last modification timestamp.

        Paging and searching are not yet supported.


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelDto
            List of available entity models

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.get_available_entity_models()
        """
        _response = self._raw_client.get_available_entity_models(request_options=request_options)
        return _response.data

    def export_metadata(
        self,
        converter: ExportMetadataRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """

        Exports an entity model's metadata in the specified format.

        Path Parameters:
        - converter: The format to export to (e.g., JSON_SCHEMA, SIMPLE_VIEW)
        - entityName: The name of the entity model to export
        - modelVersion: The version number of the model

        The response format depends on the chosen converter:
        - JSON_SCHEMA: Returns a JSON Schema representation
        - SIMPLE_VIEW: Returns a simplified view of the model structure


        Parameters
        ----------
        converter : ExportMetadataRequestConverter
            The type converter to use

        entity_name : str
            The model name of the entity

        model_version : int
            The model version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successfully exported model metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.export_metadata(
            converter="JSON_SCHEMA",
            entity_name="nobel-prize",
            model_version=1,
        )
        """
        _response = self._raw_client.export_metadata(
            converter, entity_name, model_version, request_options=request_options
        )
        return _response.data

    def import_entity_model(
        self,
        data_format: ImportEntityModelRequestDataFormat,
        converter: ImportEntityModelRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """

        Imports or updates an entity model from the provided data.

        Path Parameters:
        - dataFormat: The format of the input data (e.g., JSON, XML)
        - converter: The type converter to use for processing the data (SAMPLE_DATA, JSON_SCHEMA, SIMPLE_VIEW)
        - entityName: The name for the entity model
        - modelVersion: The version number for the model

        Returns the UUID of the created/updated entity model.


        Parameters
        ----------
        data_format : ImportEntityModelRequestDataFormat
            The format of the input data

        converter : ImportEntityModelRequestConverter
            The type converter to use for processing the data

        entity_name : str
            The model name of the entity

        model_version : int
            The version number for the model

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Model successfully imported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.import_entity_model(
            data_format="JSON",
            converter="SAMPLE_DATA",
            entity_name="nobel-prize",
            model_version=1,
            request={
                "category": "physics",
                "laureates": [
                    {
                        "firstname": "John",
                        "surname": "Hopfield",
                        "id": "1037",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                    {
                        "firstname": "Geoffrey",
                        "surname": "Hinton",
                        "id": "1038",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                ],
                "year": "2024",
            },
        )
        """
        _response = self._raw_client.import_entity_model(
            data_format, converter, entity_name, model_version, request=request, request_options=request_options
        )
        return _response.data

    def validate_entity_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityModelActionResultDto:
        """
        Validates a JSON payload against the entity model's discovered schema. Returns whether the data conforms to the model.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Validation result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.validate_entity_model(
            entity_name="entityName",
            model_version=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.validate_entity_model(
            entity_name, model_version, request=request, request_options=request_options
        )
        return _response.data

    def delete_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Deletes an entity model if it meets deletion criteria.

        Requirements for deletion:
        - Model must be in UNLOCKED state
        - No entities can reference this model in the database

        Path Parameters:
        - entityName: The name of the entity model to delete
        - modelVersion: The version number of the model

        Returns a confirmation message upon successful deletion.

        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Confirmation of successful deletion

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.delete_entity_model(
            entity_name="nobel-prize",
            model_version=1,
        )
        """
        _response = self._raw_client.delete_entity_model(entity_name, model_version, request_options=request_options)
        return _response.data

    def set_entity_model_change_level(
        self,
        entity_name: str,
        model_version: int,
        change_level: SetEntityModelChangeLevelRequestChangeLevel,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityModelActionResultDto:
        """

        Sets or updates the allowed change level for a locked entity model.

        Path Parameters:
        - entityName: The name of the entity model
        - modelVersion: The version number of the model
        - changeLevel: The desired change level (ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL) or null to disallow changes

        Change levels are hierarchical - allowing a specific level automatically allows all less impactful levels:
        1. ARRAY_LENGTH: Only permits increases in UniTypeArray width
        2. ARRAY_ELEMENTS: Allows MultiTypeArray changes without new types
        3. TYPE: Permits modifications to existing types
        4. STRUCTURAL: Allows fundamental model changes

        Note: Setting a change level is only meaningful for locked models. An unlocked model always allows all changes.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        change_level : SetEntityModelChangeLevelRequestChangeLevel

            The allowed change level for the model.
            Set to null to disallow all changes.
            Valid values: ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Change level successfully updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.set_entity_model_change_level(
            entity_name="nobel-prize",
            model_version=1,
            change_level="ARRAY_LENGTH",
        )
        """
        _response = self._raw_client.set_entity_model_change_level(
            entity_name, model_version, change_level, request_options=request_options
        )
        return _response.data

    def lock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Locks an entity model to prevent further modifications.

        Path Parameters:
        - entityName: The name of the entity model to lock
        - modelVersion: The version number of the model

        Returns a confirmation message upon successful locking.
        Once locked, a model cannot be modified unless explicitly unlocked or a change level is set.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Model successfully locked

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.lock_entity_model(
            entity_name="nobel-prize",
            model_version=1,
        )
        """
        _response = self._raw_client.lock_entity_model(entity_name, model_version, request_options=request_options)
        return _response.data

    def unlock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Attempts to unlock a locked entity model.

        Requirements for unlocking:
        - No entities can reference this model in the database
        - Model must be in LOCKED state

        Path Parameters:
        - entityName: The name of the entity model to unlock
        - modelVersion: The version number of the model

        The operation will fail if there are any entities in the database using this model.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Model successfully unlocked

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model.unlock_entity_model(
            entity_name="nobel-prize",
            model_version=1,
        )
        """
        _response = self._raw_client.unlock_entity_model(entity_name, model_version, request_options=request_options)
        return _response.data


class AsyncEntityModelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntityModelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntityModelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntityModelClient
        """
        return self._raw_client

    async def get_available_entity_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelDto:
        """

        Retrieves a list of all available entity models in the system.

        Each model in the response includes its identifier, name, version,
        current state (LOCKED/UNLOCKED), and last modification timestamp.

        Paging and searching are not yet supported.


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelDto
            List of available entity models

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.get_available_entity_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_available_entity_models(request_options=request_options)
        return _response.data

    async def export_metadata(
        self,
        converter: ExportMetadataRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """

        Exports an entity model's metadata in the specified format.

        Path Parameters:
        - converter: The format to export to (e.g., JSON_SCHEMA, SIMPLE_VIEW)
        - entityName: The name of the entity model to export
        - modelVersion: The version number of the model

        The response format depends on the chosen converter:
        - JSON_SCHEMA: Returns a JSON Schema representation
        - SIMPLE_VIEW: Returns a simplified view of the model structure


        Parameters
        ----------
        converter : ExportMetadataRequestConverter
            The type converter to use

        entity_name : str
            The model name of the entity

        model_version : int
            The model version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successfully exported model metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.export_metadata(
                converter="JSON_SCHEMA",
                entity_name="nobel-prize",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_metadata(
            converter, entity_name, model_version, request_options=request_options
        )
        return _response.data

    async def import_entity_model(
        self,
        data_format: ImportEntityModelRequestDataFormat,
        converter: ImportEntityModelRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """

        Imports or updates an entity model from the provided data.

        Path Parameters:
        - dataFormat: The format of the input data (e.g., JSON, XML)
        - converter: The type converter to use for processing the data (SAMPLE_DATA, JSON_SCHEMA, SIMPLE_VIEW)
        - entityName: The name for the entity model
        - modelVersion: The version number for the model

        Returns the UUID of the created/updated entity model.


        Parameters
        ----------
        data_format : ImportEntityModelRequestDataFormat
            The format of the input data

        converter : ImportEntityModelRequestConverter
            The type converter to use for processing the data

        entity_name : str
            The model name of the entity

        model_version : int
            The version number for the model

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Model successfully imported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.import_entity_model(
                data_format="JSON",
                converter="SAMPLE_DATA",
                entity_name="nobel-prize",
                model_version=1,
                request={
                    "category": "physics",
                    "laureates": [
                        {
                            "firstname": "John",
                            "surname": "Hopfield",
                            "id": "1037",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                        {
                            "firstname": "Geoffrey",
                            "surname": "Hinton",
                            "id": "1038",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                    ],
                    "year": "2024",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_entity_model(
            data_format, converter, entity_name, model_version, request=request, request_options=request_options
        )
        return _response.data

    async def validate_entity_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityModelActionResultDto:
        """
        Validates a JSON payload against the entity model's discovered schema. Returns whether the data conforms to the model.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Validation result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.validate_entity_model(
                entity_name="entityName",
                model_version=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_entity_model(
            entity_name, model_version, request=request, request_options=request_options
        )
        return _response.data

    async def delete_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Deletes an entity model if it meets deletion criteria.

        Requirements for deletion:
        - Model must be in UNLOCKED state
        - No entities can reference this model in the database

        Path Parameters:
        - entityName: The name of the entity model to delete
        - modelVersion: The version number of the model

        Returns a confirmation message upon successful deletion.

        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Confirmation of successful deletion

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.delete_entity_model(
                entity_name="nobel-prize",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_entity_model(
            entity_name, model_version, request_options=request_options
        )
        return _response.data

    async def set_entity_model_change_level(
        self,
        entity_name: str,
        model_version: int,
        change_level: SetEntityModelChangeLevelRequestChangeLevel,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityModelActionResultDto:
        """

        Sets or updates the allowed change level for a locked entity model.

        Path Parameters:
        - entityName: The name of the entity model
        - modelVersion: The version number of the model
        - changeLevel: The desired change level (ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL) or null to disallow changes

        Change levels are hierarchical - allowing a specific level automatically allows all less impactful levels:
        1. ARRAY_LENGTH: Only permits increases in UniTypeArray width
        2. ARRAY_ELEMENTS: Allows MultiTypeArray changes without new types
        3. TYPE: Permits modifications to existing types
        4. STRUCTURAL: Allows fundamental model changes

        Note: Setting a change level is only meaningful for locked models. An unlocked model always allows all changes.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        change_level : SetEntityModelChangeLevelRequestChangeLevel

            The allowed change level for the model.
            Set to null to disallow all changes.
            Valid values: ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Change level successfully updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.set_entity_model_change_level(
                entity_name="nobel-prize",
                model_version=1,
                change_level="ARRAY_LENGTH",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_entity_model_change_level(
            entity_name, model_version, change_level, request_options=request_options
        )
        return _response.data

    async def lock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Locks an entity model to prevent further modifications.

        Path Parameters:
        - entityName: The name of the entity model to lock
        - modelVersion: The version number of the model

        Returns a confirmation message upon successful locking.
        Once locked, a model cannot be modified unless explicitly unlocked or a change level is set.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Model successfully locked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.lock_entity_model(
                entity_name="nobel-prize",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lock_entity_model(
            entity_name, model_version, request_options=request_options
        )
        return _response.data

    async def unlock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityModelActionResultDto:
        """

        Attempts to unlock a locked entity model.

        Requirements for unlocking:
        - No entities can reference this model in the database
        - Model must be in LOCKED state

        Path Parameters:
        - entityName: The name of the entity model to unlock
        - modelVersion: The version number of the model

        The operation will fail if there are any entities in the database using this model.


        Parameters
        ----------
        entity_name : str
            The model name of the entity

        model_version : int
            The version number of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityModelActionResultDto
            Model successfully unlocked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model.unlock_entity_model(
                entity_name="nobel-prize",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlock_entity_model(
            entity_name, model_version, request_options=request_options
        )
        return _response.data
