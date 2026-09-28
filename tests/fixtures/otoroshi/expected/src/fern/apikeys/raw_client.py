

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.error_response import ErrorResponse
from ..types.otoroshi_models_api_key import OtoroshiModelsApiKey
from ..types.otoroshi_models_api_key_valid_until import OtoroshiModelsApiKeyValidUntil
from ..types.otoroshi_models_entity_identifier import OtoroshiModelsEntityIdentifier
from ..types.otoroshi_models_remaining_quotas import OtoroshiModelsRemainingQuotas
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApikeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsApiKey], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsApiKey], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsRemainingQuotas]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsRemainingQuotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsRemainingQuotas,
                    parse_obj_as(
                        type_=OtoroshiModelsRemainingQuotas,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsRemainingQuotas]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsRemainingQuotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsRemainingQuotas,
                    parse_obj_as(
                        type_=OtoroshiModelsRemainingQuotas,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="PUT",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="PATCH",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OtoroshiModelsApiKey]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OtoroshiModelsApiKey]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiModelsApiKey],
                    parse_obj_as(
                        type_=typing.List[OtoroshiModelsApiKey],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_api_keys_controller_create_action(
        self,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="POST",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawApikeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsApiKey], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsApiKey], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys/_bulk",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsRemainingQuotas]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsRemainingQuotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsRemainingQuotas,
                    parse_obj_as(
                        type_=OtoroshiModelsRemainingQuotas,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsRemainingQuotas]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsRemainingQuotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsRemainingQuotas,
                    parse_obj_as(
                        type_=OtoroshiModelsRemainingQuotas,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="PUT",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/apikeys/{encode_path_param(id)}",
            method="PATCH",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OtoroshiModelsApiKey]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OtoroshiModelsApiKey]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiModelsApiKey],
                    parse_obj_as(
                        type_=typing.List[OtoroshiModelsApiKey],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_api_keys_controller_create_action(
        self,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="POST",
            json={
                "dailyQuota": daily_quota,
                "metadata": metadata,
                "throttlingQuota": throttling_quota,
                "constrainedServicesOnly": constrained_services_only,
                "allowClientIdOnly": allow_client_id_only,
                "_loc": loc,
                "restrictions": restrictions,
                "tags": tags,
                "enabled": enabled,
                "readOnly": read_only,
                "clientSecret": client_secret,
                "validUntil": convert_and_respect_annotation_metadata(
                    object_=valid_until, annotation=OtoroshiModelsApiKeyValidUntil, direction="write"
                ),
                "clientName": client_name,
                "monthlyQuota": monthly_quota,
                "description": description,
                "rotation": rotation,
                "authorizedEntities": convert_and_respect_annotation_metadata(
                    object_=authorized_entities,
                    annotation=typing.Sequence[OtoroshiModelsEntityIdentifier],
                    direction="write",
                ),
                "clientId": client_id,
            },
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsApiKey,
                    parse_obj_as(
                        type_=OtoroshiModelsApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
