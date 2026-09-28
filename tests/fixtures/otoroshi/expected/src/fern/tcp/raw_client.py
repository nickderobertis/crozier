

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
from ..types.empty import Empty
from ..types.error_response import ErrorResponse
from ..types.otoroshi_tcp_tcp_rule import OtoroshiTcpTcpRule
from ..types.otoroshi_tcp_tcp_service import OtoroshiTcpTcpService
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTcpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/services/_template",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/_template",
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/services/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiTcpTcpService], direction="write"
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/services/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiTcpTcpService], direction="write"
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
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
            "api/tcp/services/_bulk",
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
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
            "api/tcp/services/_bulk",
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id_)}",
            method="PUT",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OtoroshiTcpTcpService]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OtoroshiTcpTcpService]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiTcpTcpService],
                    parse_obj_as(
                        type_=typing.List[OtoroshiTcpTcpService],
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

    def otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tcp/services",
            method="POST",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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


class AsyncRawTcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/services/_template",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    async def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/_template",
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/services/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiTcpTcpService], direction="write"
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/services/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiTcpTcpService], direction="write"
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
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
            "api/tcp/services/_bulk",
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
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
            "api/tcp/services/_bulk",
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id_)}",
            method="PUT",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/tcp/services/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OtoroshiTcpTcpService]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OtoroshiTcpTcpService]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiTcpTcpService],
                    parse_obj_as(
                        type_=typing.List[OtoroshiTcpTcpService],
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

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiTcpTcpService]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tcp/services",
            method="POST",
            json={
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "port": port,
                "tags": tags,
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[OtoroshiTcpTcpRule], direction="write"
                ),
                "clientAuth": client_auth,
                "interface": interface,
                "sni": sni,
                "id": id,
                "_loc": loc,
                "name": name,
                "tls": tls,
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
                    OtoroshiTcpTcpService,
                    parse_obj_as(
                        type_=OtoroshiTcpTcpService,
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
