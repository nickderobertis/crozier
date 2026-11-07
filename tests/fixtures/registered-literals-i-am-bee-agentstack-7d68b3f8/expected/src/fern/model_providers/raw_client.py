

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output4 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output5 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
)
from ..types.http_validation_error import HttpValidationError
from ..types.model_capability import ModelCapability
from ..types.model_provider_type import ModelProviderType
from ..types.paginated_result_model_provider import PaginatedResultModelProvider
from ..types.paginated_result_model_with_score import PaginatedResultModelWithScore
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawModelProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_model_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PaginatedResultModelProvider]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultModelProvider]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/model_providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelProvider,
                    parse_obj_as(
                        type_=PaginatedResultModelProvider,
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

    def create_model_provider(
        self,
        *,
        type: ModelProviderType,
        base_url: str,
        api_key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        watsonx_project_id: typing.Optional[str] = OMIT,
        watsonx_space_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4]:
        """
        Parameters
        ----------
        type : ModelProviderType

        base_url : str

        api_key : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        watsonx_project_id : typing.Optional[str]

        watsonx_space_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/model_providers",
            method="POST",
            json={
                "name": name,
                "description": description,
                "type": type,
                "base_url": base_url,
                "watsonx_project_id": watsonx_project_id,
                "watsonx_space_id": watsonx_space_id,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5]:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/model_providers/{encode_path_param(model_provider_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/model_providers/{encode_path_param(model_provider_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def match(
        self,
        *,
        capability: ModelCapability,
        suggested_models: typing.Optional[typing.Sequence[str]] = OMIT,
        score_cutoff: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultModelWithScore]:
        """
        Parameters
        ----------
        capability : ModelCapability

        suggested_models : typing.Optional[typing.Sequence[str]]

        score_cutoff : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultModelWithScore]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/model_providers/match",
            method="POST",
            json={
                "suggested_models": suggested_models,
                "capability": capability,
                "score_cutoff": score_cutoff,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelWithScore,
                    parse_obj_as(
                        type_=PaginatedResultModelWithScore,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawModelProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_model_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PaginatedResultModelProvider]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultModelProvider]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/model_providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelProvider,
                    parse_obj_as(
                        type_=PaginatedResultModelProvider,
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

    async def create_model_provider(
        self,
        *,
        type: ModelProviderType,
        base_url: str,
        api_key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        watsonx_project_id: typing.Optional[str] = OMIT,
        watsonx_space_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4]:
        """
        Parameters
        ----------
        type : ModelProviderType

        base_url : str

        api_key : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        watsonx_project_id : typing.Optional[str]

        watsonx_space_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/model_providers",
            method="POST",
            json={
                "name": name,
                "description": description,
                "type": type,
                "base_url": base_url,
                "watsonx_project_id": watsonx_project_id,
                "watsonx_space_id": watsonx_space_id,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5]:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/model_providers/{encode_path_param(model_provider_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/model_providers/{encode_path_param(model_provider_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def match(
        self,
        *,
        capability: ModelCapability,
        suggested_models: typing.Optional[typing.Sequence[str]] = OMIT,
        score_cutoff: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultModelWithScore]:
        """
        Parameters
        ----------
        capability : ModelCapability

        suggested_models : typing.Optional[typing.Sequence[str]]

        score_cutoff : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultModelWithScore]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/model_providers/match",
            method="POST",
            json={
                "suggested_models": suggested_models,
                "capability": capability,
                "score_cutoff": score_cutoff,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelWithScore,
                    parse_obj_as(
                        type_=PaginatedResultModelWithScore,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
