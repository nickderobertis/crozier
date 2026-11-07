

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.entity_model_action_result_dto import EntityModelActionResultDto
from ..types.entity_model_dto import EntityModelDto
from .types.export_metadata_request_converter import ExportMetadataRequestConverter
from .types.import_entity_model_request_converter import ImportEntityModelRequestConverter
from .types.import_entity_model_request_data_format import ImportEntityModelRequestDataFormat
from .types.set_entity_model_change_level_request_change_level import SetEntityModelChangeLevelRequestChangeLevel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntityModelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_available_entity_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityModelDto]:
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
        HttpResponse[EntityModelDto]
            List of available entity models
        """
        _response = self._client_wrapper.httpx_client.request(
            "model/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelDto,
                    parse_obj_as(
                        type_=EntityModelDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def export_metadata(
        self,
        converter: ExportMetadataRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Successfully exported model metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/export/{encode_path_param(converter)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def import_entity_model(
        self,
        data_format: ImportEntityModelRequestDataFormat,
        converter: ImportEntityModelRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Model successfully imported
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/import/{encode_path_param(data_format)}/{encode_path_param(converter)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def validate_entity_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityModelActionResultDto]:
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
        HttpResponse[EntityModelActionResultDto]
            Validation result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/validate/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityModelActionResultDto]:
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
        HttpResponse[EntityModelActionResultDto]
            Confirmation of successful deletion
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_entity_model_change_level(
        self,
        entity_name: str,
        model_version: int,
        change_level: SetEntityModelChangeLevelRequestChangeLevel,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityModelActionResultDto]:
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
        HttpResponse[EntityModelActionResultDto]
            Change level successfully updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/changeLevel/{encode_path_param(change_level)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def lock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityModelActionResultDto]:
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
        HttpResponse[EntityModelActionResultDto]
            Model successfully locked
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/lock",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unlock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityModelActionResultDto]:
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
        HttpResponse[EntityModelActionResultDto]
            Model successfully unlocked
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/unlock",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEntityModelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_available_entity_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityModelDto]:
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
        AsyncHttpResponse[EntityModelDto]
            List of available entity models
        """
        _response = await self._client_wrapper.httpx_client.request(
            "model/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelDto,
                    parse_obj_as(
                        type_=EntityModelDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def export_metadata(
        self,
        converter: ExportMetadataRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Successfully exported model metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/export/{encode_path_param(converter)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def import_entity_model(
        self,
        data_format: ImportEntityModelRequestDataFormat,
        converter: ImportEntityModelRequestConverter,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Model successfully imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/import/{encode_path_param(data_format)}/{encode_path_param(converter)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def validate_entity_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityModelActionResultDto]:
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
        AsyncHttpResponse[EntityModelActionResultDto]
            Validation result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/validate/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityModelActionResultDto]:
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
        AsyncHttpResponse[EntityModelActionResultDto]
            Confirmation of successful deletion
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_entity_model_change_level(
        self,
        entity_name: str,
        model_version: int,
        change_level: SetEntityModelChangeLevelRequestChangeLevel,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityModelActionResultDto]:
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
        AsyncHttpResponse[EntityModelActionResultDto]
            Change level successfully updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/changeLevel/{encode_path_param(change_level)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def lock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityModelActionResultDto]:
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
        AsyncHttpResponse[EntityModelActionResultDto]
            Model successfully locked
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/lock",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unlock_entity_model(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityModelActionResultDto]:
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
        AsyncHttpResponse[EntityModelActionResultDto]
            Model successfully unlocked
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/unlock",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityModelActionResultDto,
                    parse_obj_as(
                        type_=EntityModelActionResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
