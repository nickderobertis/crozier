

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
from ..types.otoroshi_next_models_ng_minimal_route import OtoroshiNextModelsNgMinimalRoute
from ..types.otoroshi_next_models_ng_route_composition import OtoroshiNextModelsNgRouteComposition
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRouteCompositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
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
            "api/route-compositions/_form",
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/route-compositions/_openapi",
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
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
            "api/route-compositions/_template",
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/route-compositions/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiNextModelsNgRouteComposition], direction="write"
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/route-compositions/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiNextModelsNgRouteComposition], direction="write"
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
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
            "api/route-compositions/_bulk",
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
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
            "api/route-compositions/_bulk",
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id_)}",
            method="PUT",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OtoroshiNextModelsNgRouteComposition]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OtoroshiNextModelsNgRouteComposition]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/route-compositions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiNextModelsNgRouteComposition],
                    parse_obj_as(
                        type_=typing.List[OtoroshiNextModelsNgRouteComposition],
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

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
        self,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/route-compositions",
            method="POST",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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


class AsyncRawRouteCompositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
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
            "api/route-compositions/_form",
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/route-compositions/_openapi",
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
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
            "api/route-compositions/_template",
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/route-compositions/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiNextModelsNgRouteComposition], direction="write"
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/route-compositions/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiNextModelsNgRouteComposition], direction="write"
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
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
            "api/route-compositions/_bulk",
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
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
            "api/route-compositions/_bulk",
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id_)}",
            method="PUT",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/route-compositions/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OtoroshiNextModelsNgRouteComposition]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OtoroshiNextModelsNgRouteComposition]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/route-compositions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiNextModelsNgRouteComposition],
                    parse_obj_as(
                        type_=typing.List[OtoroshiNextModelsNgRouteComposition],
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

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
        self,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiNextModelsNgRouteComposition]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/route-compositions",
            method="POST",
            json={
                "capture": capture,
                "id": id,
                "debug_flow": debug_flow,
                "routes": convert_and_respect_annotation_metadata(
                    object_=routes, annotation=typing.Sequence[OtoroshiNextModelsNgMinimalRoute], direction="write"
                ),
                "enabled": enabled,
                "description": description,
                "metadata": metadata,
                "export_reporting": export_reporting,
                "tags": tags,
                "name": name,
                "_loc": loc,
                "client": client,
                "groups": groups,
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
                    OtoroshiNextModelsNgRouteComposition,
                    parse_obj_as(
                        type_=OtoroshiNextModelsNgRouteComposition,
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
