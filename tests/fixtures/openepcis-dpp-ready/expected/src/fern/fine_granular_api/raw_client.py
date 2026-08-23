

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
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.data_element import DataElement
from ..types.identifier import Identifier
from ..types.result import Result
from .types.read_data_element_request_representation import ReadDataElementRequestRepresentation
from .types.update_data_element_request_representation import UpdateDataElementRequestRepresentation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFineGranularApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        representation: typing.Optional[ReadDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DataElement]:
        """
        Returns a single data element of a DPP by its absolute path. `elementIdPath` follows RFC 9535 JSONPath and is percent-encoded. Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        representation : typing.Optional[ReadDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataElement]
            The requested data element.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}/elements/{encode_path_param(element_id_path)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataElement,
                    parse_obj_as(
                        type_=DataElement,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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

    def update_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        request: DataElement,
        representation: typing.Optional[UpdateDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DataElement]:
        """
        Updates, amends, or removes a single data element of a DPP at the given RFC 9535 JSONPath. Changes are archived per EN 18221. Conformance: should where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        request : DataElement

        representation : typing.Optional[UpdateDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataElement]
            The updated data element.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}/elements/{encode_path_param(element_id_path)}",
            method="PATCH",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(object_=request, annotation=DataElement, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataElement,
                    parse_obj_as(
                        type_=DataElement,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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


class AsyncRawFineGranularApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        representation: typing.Optional[ReadDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DataElement]:
        """
        Returns a single data element of a DPP by its absolute path. `elementIdPath` follows RFC 9535 JSONPath and is percent-encoded. Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        representation : typing.Optional[ReadDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataElement]
            The requested data element.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}/elements/{encode_path_param(element_id_path)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataElement,
                    parse_obj_as(
                        type_=DataElement,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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

    async def update_data_element(
        self,
        dpp_id: Identifier,
        element_id_path: str,
        *,
        request: DataElement,
        representation: typing.Optional[UpdateDataElementRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DataElement]:
        """
        Updates, amends, or removes a single data element of a DPP at the given RFC 9535 JSONPath. Changes are archived per EN 18221. Conformance: should where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        element_id_path : str
            RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.

        request : DataElement

        representation : typing.Optional[UpdateDataElementRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataElement]
            The updated data element.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}/elements/{encode_path_param(element_id_path)}",
            method="PATCH",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(object_=request, annotation=DataElement, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataElement,
                    parse_obj_as(
                        type_=DataElement,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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
