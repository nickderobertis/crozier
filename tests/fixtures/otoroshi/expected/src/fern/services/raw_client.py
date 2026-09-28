

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
from ..types.any import Any
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.done import Done
from ..types.error_response import ErrorResponse
from ..types.error_template_list import ErrorTemplateList
from ..types.health_check_event_list import HealthCheckEventList
from ..types.live_stats import LiveStats
from ..types.otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
from ..types.otoroshi_models_error_template import OtoroshiModelsErrorTemplate
from ..types.otoroshi_models_service_descriptor import OtoroshiModelsServiceDescriptor
from ..types.otoroshi_models_service_descriptor_auth_config_ref import OtoroshiModelsServiceDescriptorAuthConfigRef
from ..types.otoroshi_models_service_descriptor_client_validator_ref import (
    OtoroshiModelsServiceDescriptorClientValidatorRef,
)
from ..types.otoroshi_models_service_descriptor_issue_cert_ca import OtoroshiModelsServiceDescriptorIssueCertCa
from ..types.otoroshi_models_service_descriptor_matching_root import OtoroshiModelsServiceDescriptorMatchingRoot
from ..types.otoroshi_models_target import OtoroshiModelsTarget
from ..types.otoroshi_models_target_ip_address import OtoroshiModelsTargetIpAddress
from ..types.otoroshi_models_target_protocol import OtoroshiModelsTargetProtocol
from ..types.targets_list import TargetsList
from ..types.unknown import Unknown
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    def otoroshi_controllers_adminapi_services_controller_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ErrorTemplateList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ErrorTemplateList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplateList,
                    parse_obj_as(
                        type_=ErrorTemplateList,
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

    def otoroshi_controllers_adminapi_services_controller_create_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsErrorTemplate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="POST",
            json={
                "template50x": template50x,
                "templateMaintenance": template_maintenance,
                "templateBuild": template_build,
                "serviceId": service_id,
                "_loc": loc,
                "metadata": metadata,
                "messages": messages,
                "name": name,
                "template40x": template40x,
                "tags": tags,
                "description": description,
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
                    OtoroshiModelsErrorTemplate,
                    parse_obj_as(
                        type_=OtoroshiModelsErrorTemplate,
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

    def otoroshi_controllers_adminapi_services_controller_update_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsErrorTemplate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="PUT",
            json={
                "template50x": template50x,
                "templateMaintenance": template_maintenance,
                "templateBuild": template_build,
                "serviceId": service_id,
                "_loc": loc,
                "metadata": metadata,
                "messages": messages,
                "name": name,
                "template40x": template40x,
                "tags": tags,
                "description": description,
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
                    OtoroshiModelsErrorTemplate,
                    parse_obj_as(
                        type_=OtoroshiModelsErrorTemplate,
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

    def otoroshi_controllers_adminapi_services_controller_delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    def otoroshi_controllers_adminapi_services_controller_service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TargetsList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TargetsList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TargetsList,
                    parse_obj_as(
                        type_=TargetsList,
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

    def otoroshi_controllers_adminapi_services_controller_service_add_target(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsTarget]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsTarget]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="POST",
            json={
                "tags": tags,
                "host": host,
                "weight": weight,
                "metadata": metadata,
                "protocol": protocol,
                "predicate": predicate,
                "ipAddress": convert_and_respect_annotation_metadata(
                    object_=ip_address, annotation=OtoroshiModelsTargetIpAddress, direction="write"
                ),
                "mtlsConfig": mtls_config,
                "scheme": scheme,
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
                    OtoroshiModelsTarget,
                    parse_obj_as(
                        type_=OtoroshiModelsTarget,
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

    def otoroshi_controllers_adminapi_services_controller_service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    def otoroshi_controllers_adminapi_services_controller_update_service_targets(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsTarget]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsTarget]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="PATCH",
            json={
                "tags": tags,
                "host": host,
                "weight": weight,
                "metadata": metadata,
                "protocol": protocol,
                "predicate": predicate,
                "ipAddress": convert_and_respect_annotation_metadata(
                    object_=ip_address, annotation=OtoroshiModelsTargetIpAddress, direction="write"
                ),
                "mtlsConfig": mtls_config,
                "scheme": scheme,
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
                    OtoroshiModelsTarget,
                    parse_obj_as(
                        type_=OtoroshiModelsTarget,
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

    def otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LiveStats]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LiveStats]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/live",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LiveStats,
                    parse_obj_as(
                        type_=LiveStats,
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

    def otoroshi_controllers_adminapi_analytics_controller_service_stats(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Unknown]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/stats",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    def otoroshi_controllers_adminapi_analytics_controller_service_events(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Unknown]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    def otoroshi_controllers_adminapi_analytics_controller_service_status(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Unknown]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    def otoroshi_controllers_adminapi_services_controller_service_health(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[HealthCheckEventList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HealthCheckEventList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthCheckEventList,
                    parse_obj_as(
                        type_=HealthCheckEventList,
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

    def otoroshi_controllers_adminapi_analytics_controller_service_response_time(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Unknown]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    def otoroshi_controllers_adminapi_canary_controller_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Any]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/canary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Any,
                    parse_obj_as(
                        type_=Any,
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

    def otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/canary",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    def otoroshi_controllers_adminapi_services_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsServiceDescriptor], direction="write"
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

    def otoroshi_controllers_adminapi_services_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsServiceDescriptor], direction="write"
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

    def otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
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
            "api/services/_bulk",
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

    def otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
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
            "api/services/_bulk",
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

    def otoroshi_controllers_adminapi_services_controller_convert_as_route(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}/route",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def otoroshi_controllers_adminapi_services_controller_import_as_route(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}/route",
            method="POST",
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    def otoroshi_controllers_adminapi_services_controller_update_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id_)}",
            method="PUT",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    def otoroshi_controllers_adminapi_services_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    def otoroshi_controllers_adminapi_services_controller_patch_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    def otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OtoroshiModelsServiceDescriptor]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OtoroshiModelsServiceDescriptor]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiModelsServiceDescriptor],
                    parse_obj_as(
                        type_=typing.List[OtoroshiModelsServiceDescriptor],
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

    def otoroshi_controllers_adminapi_services_controller_create_action(
        self,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services",
            method="POST",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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


class AsyncRawServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    async def otoroshi_controllers_adminapi_services_controller_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ErrorTemplateList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ErrorTemplateList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplateList,
                    parse_obj_as(
                        type_=ErrorTemplateList,
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

    async def otoroshi_controllers_adminapi_services_controller_create_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsErrorTemplate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="POST",
            json={
                "template50x": template50x,
                "templateMaintenance": template_maintenance,
                "templateBuild": template_build,
                "serviceId": service_id,
                "_loc": loc,
                "metadata": metadata,
                "messages": messages,
                "name": name,
                "template40x": template40x,
                "tags": tags,
                "description": description,
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
                    OtoroshiModelsErrorTemplate,
                    parse_obj_as(
                        type_=OtoroshiModelsErrorTemplate,
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

    async def otoroshi_controllers_adminapi_services_controller_update_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsErrorTemplate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="PUT",
            json={
                "template50x": template50x,
                "templateMaintenance": template_maintenance,
                "templateBuild": template_build,
                "serviceId": service_id,
                "_loc": loc,
                "metadata": metadata,
                "messages": messages,
                "name": name,
                "template40x": template40x,
                "tags": tags,
                "description": description,
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
                    OtoroshiModelsErrorTemplate,
                    parse_obj_as(
                        type_=OtoroshiModelsErrorTemplate,
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

    async def otoroshi_controllers_adminapi_services_controller_delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    async def otoroshi_controllers_adminapi_services_controller_service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TargetsList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TargetsList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TargetsList,
                    parse_obj_as(
                        type_=TargetsList,
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

    async def otoroshi_controllers_adminapi_services_controller_service_add_target(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsTarget]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsTarget]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="POST",
            json={
                "tags": tags,
                "host": host,
                "weight": weight,
                "metadata": metadata,
                "protocol": protocol,
                "predicate": predicate,
                "ipAddress": convert_and_respect_annotation_metadata(
                    object_=ip_address, annotation=OtoroshiModelsTargetIpAddress, direction="write"
                ),
                "mtlsConfig": mtls_config,
                "scheme": scheme,
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
                    OtoroshiModelsTarget,
                    parse_obj_as(
                        type_=OtoroshiModelsTarget,
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

    async def otoroshi_controllers_adminapi_services_controller_service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    async def otoroshi_controllers_adminapi_services_controller_update_service_targets(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsTarget]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsTarget]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="PATCH",
            json={
                "tags": tags,
                "host": host,
                "weight": weight,
                "metadata": metadata,
                "protocol": protocol,
                "predicate": predicate,
                "ipAddress": convert_and_respect_annotation_metadata(
                    object_=ip_address, annotation=OtoroshiModelsTargetIpAddress, direction="write"
                ),
                "mtlsConfig": mtls_config,
                "scheme": scheme,
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
                    OtoroshiModelsTarget,
                    parse_obj_as(
                        type_=OtoroshiModelsTarget,
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

    async def otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LiveStats]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LiveStats]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/live",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LiveStats,
                    parse_obj_as(
                        type_=LiveStats,
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

    async def otoroshi_controllers_adminapi_analytics_controller_service_stats(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Unknown]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/stats",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    async def otoroshi_controllers_adminapi_analytics_controller_service_events(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Unknown]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    async def otoroshi_controllers_adminapi_analytics_controller_service_status(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Unknown]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    async def otoroshi_controllers_adminapi_services_controller_service_health(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HealthCheckEventList]:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HealthCheckEventList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthCheckEventList,
                    parse_obj_as(
                        type_=HealthCheckEventList,
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

    async def otoroshi_controllers_adminapi_analytics_controller_service_response_time(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Unknown]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Unknown]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Unknown,
                    parse_obj_as(
                        type_=Unknown,
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

    async def otoroshi_controllers_adminapi_canary_controller_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Any]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Any]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/canary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Any,
                    parse_obj_as(
                        type_=Any,
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

    async def otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/canary",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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

    async def otoroshi_controllers_adminapi_services_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsServiceDescriptor], direction="write"
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

    async def otoroshi_controllers_adminapi_services_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiModelsServiceDescriptor], direction="write"
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

    async def otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
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
            "api/services/_bulk",
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

    async def otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
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
            "api/services/_bulk",
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

    async def otoroshi_controllers_adminapi_services_controller_convert_as_route(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}/route",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def otoroshi_controllers_adminapi_services_controller_import_as_route(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}/route",
            method="POST",
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    async def otoroshi_controllers_adminapi_services_controller_update_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id_)}",
            method="PUT",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    async def otoroshi_controllers_adminapi_services_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    async def otoroshi_controllers_adminapi_services_controller_patch_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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

    async def otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OtoroshiModelsServiceDescriptor]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OtoroshiModelsServiceDescriptor]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiModelsServiceDescriptor],
                    parse_obj_as(
                        type_=typing.List[OtoroshiModelsServiceDescriptor],
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

    async def otoroshi_controllers_adminapi_services_controller_create_action(
        self,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsServiceDescriptor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services",
            method="POST",
            json={
                "buildMode": build_mode,
                "hosts": hosts,
                "privateApp": private_app,
                "localScheme": local_scheme,
                "authConfigRef": convert_and_respect_annotation_metadata(
                    object_=auth_config_ref, annotation=OtoroshiModelsServiceDescriptorAuthConfigRef, direction="write"
                ),
                "issueCertCA": convert_and_respect_annotation_metadata(
                    object_=issue_cert_ca, annotation=OtoroshiModelsServiceDescriptorIssueCertCa, direction="write"
                ),
                "root": root,
                "name": name,
                "additionalHeaders": additional_headers,
                "domain": domain,
                "clientConfig": client_config,
                "matchingRoot": convert_and_respect_annotation_metadata(
                    object_=matching_root, annotation=OtoroshiModelsServiceDescriptorMatchingRoot, direction="write"
                ),
                "forceHttps": force_https,
                "localHost": local_host,
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "healthCheck": health_check,
                "strictlyPrivate": strictly_private,
                "detectApiKeySooner": detect_api_key_sooner,
                "allowHttp10": allow_http10,
                "subdomain": subdomain,
                "paths": paths,
                "stripPath": strip_path,
                "secComAlgoChallengeOtoToBack": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_oto_to_back, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "apiKeyConstraints": api_key_constraints,
                "env": env,
                "xForwardedHeaders": x_forwarded_headers,
                "transformerRefs": transformer_refs,
                "enabled": enabled,
                "gzip": gzip,
                "sendInfoToken": send_info_token,
                "tcpUdpTunneling": tcp_udp_tunneling,
                "removeHeadersOut": remove_headers_out,
                "useAkkaHttpClient": use_akka_http_client,
                "maintenanceMode": maintenance_mode,
                "id": id,
                "removeHeadersIn": remove_headers_in,
                "logAnalyticsOnServer": log_analytics_on_server,
                "secComAlgoInfoToken": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_info_token, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "userFacing": user_facing,
                "transformerConfig": transformer_config,
                "clientValidatorRef": convert_and_respect_annotation_metadata(
                    object_=client_validator_ref,
                    annotation=OtoroshiModelsServiceDescriptorClientValidatorRef,
                    direction="write",
                ),
                "securityExcludedPatterns": security_excluded_patterns,
                "ipFiltering": ip_filtering,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[OtoroshiModelsTarget], direction="write"
                ),
                "redirection": redirection,
                "tags": tags,
                "restrictions": restrictions,
                "overrideHost": override_host,
                "accessValidator": access_validator,
                "sendStateChallenge": send_state_challenge,
                "chaosConfig": chaos_config,
                "secComInfoTokenVersion": sec_com_info_token_version,
                "additionalHeadersOut": additional_headers_out,
                "secComHeaders": sec_com_headers,
                "matchingHeaders": matching_headers,
                "secComAlgoChallengeBackToOto": convert_and_respect_annotation_metadata(
                    object_=sec_com_algo_challenge_back_to_oto, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "secComUseSameAlgo": sec_com_use_same_algo,
                "useNewWSClient": use_new_ws_client,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "redirectToLocal": redirect_to_local,
                "enforceSecureCommunication": enforce_secure_communication,
                "missingOnlyHeadersOut": missing_only_headers_out,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=OtoroshiModelsAlgoSettings, direction="write"
                ),
                "handleLegacyDomain": handle_legacy_domain,
                "canary": canary,
                "_loc": loc,
                "plugins": plugins,
                "secComTtl": sec_com_ttl,
                "description": description,
                "secComVersion": sec_com_version,
                "preRouting": pre_routing,
                "groups": groups,
                "readOnly": read_only,
                "privatePatterns": private_patterns,
                "targetsLoadBalancing": targets_load_balancing,
                "cors": cors,
                "metadata": metadata,
                "publicPatterns": public_patterns,
                "api": api,
                "missingOnlyHeadersIn": missing_only_headers_in,
                "issueCert": issue_cert,
                "headersVerification": headers_verification,
                "jwtVerifier": jwt_verifier,
                "letsEncrypt": lets_encrypt,
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
                    OtoroshiModelsServiceDescriptor,
                    parse_obj_as(
                        type_=OtoroshiModelsServiceDescriptor,
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
