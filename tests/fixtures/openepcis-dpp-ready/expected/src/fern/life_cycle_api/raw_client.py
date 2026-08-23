

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
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
from ..types.create_dpp_result import CreateDppResult
from ..types.digital_product_passport import DigitalProductPassport
from ..types.dpp_id_page import DppIdPage
from ..types.identifier import Identifier
from ..types.result import Result
from ..types.timestamp import Timestamp
from .types.create_dpp_request_representation import CreateDppRequestRepresentation
from .types.read_dpp_by_id_request_representation import ReadDppByIdRequestRepresentation
from .types.read_dpp_by_product_id_request_representation import ReadDppByProductIdRequestRepresentation
from .types.read_dpp_version_by_id_and_date_request_representation import ReadDppVersionByIdAndDateRequestRepresentation
from .types.update_dpp_by_id_request_representation import UpdateDppByIdRequestRepresentation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLifeCycleApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DigitalProductPassport]:
        """
        Returns the DPP with the specified DPP ID. Conformance: shall.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        representation : typing.Optional[ReadDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DigitalProductPassport]
            The requested DPP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    def delete_dpp_by_id(
        self, dpp_id: Identifier, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Removes the DPP with the specified DPP ID (end of life). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def update_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[UpdateDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DigitalProductPassport]:
        """
        Partial update of a DPP. The body carries only the parts to update or extend
        (RFC 7396 JSON Merge Patch may be used). If any part fails, the whole update
        fails and no change is adopted. All changes are archived per EN 18221.
        Conformance: shall where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request : DigitalProductPassport

        representation : typing.Optional[UpdateDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DigitalProductPassport]
            The updated DPP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="PATCH",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=DigitalProductPassport, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    def read_dpp_by_product_id(
        self,
        product_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByProductIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DigitalProductPassport]:
        """
        Returns the current active DPP (latest version) for the unique product identifier (EN 18219 GS1 Digital Link). Conformance: shall.

        Parameters
        ----------
        product_id : Identifier
            Unique product identifier (EN 18219 GS1 Digital Link), percent-encoded.

        representation : typing.Optional[ReadDppByProductIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DigitalProductPassport]
            The latest active DPP for the product.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dppsByProductId/{encode_path_param(product_id)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    def read_dpp_version_by_id_and_date(
        self,
        dpp_id: Identifier,
        *,
        date: Timestamp,
        representation: typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DigitalProductPassport]:
        """
        Returns the DPP version current at the given date (archived versions per EN 18221). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        date : Timestamp
            UTC-based timestamp (ISO 8601-1) for which the version is requested.

        representation : typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DigitalProductPassport]
            The DPP version at the given date.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dppsByIdAndDate/{encode_path_param(dpp_id)}",
            method="GET",
            params={
                "date": serialize_datetime(date),
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    def read_dpp_ids_by_product_ids(
        self,
        *,
        product_ids: typing.Sequence[Identifier],
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DppIdPage]:
        """
        Returns the DPP identifiers matching a set of product identifiers (discovery). Paginated by `limit` and `cursor` (the cursor shall not be empty). Conformance: shall.

        Parameters
        ----------
        product_ids : typing.Sequence[Identifier]

        limit : typing.Optional[int]
            Maximum number of identifiers to return in this page.

        cursor : typing.Optional[str]
            Opaque, non-empty pagination token from a prior response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DppIdPage]
            The matching DPP identifiers, with an optional next-page cursor.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dppsByProductIds",
            method="POST",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            json={
                "productIds": product_ids,
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
                    DppIdPage,
                    parse_obj_as(
                        type_=DppIdPage,
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

    def create_dpp(
        self,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[CreateDppRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDppResult]:
        """
        Creates a new DPP and returns its DPP ID. Conformance: should.

        Parameters
        ----------
        request : DigitalProductPassport

        representation : typing.Optional[CreateDppRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDppResult]
            DPP created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dpps",
            method="POST",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=DigitalProductPassport, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDppResult,
                    parse_obj_as(
                        type_=CreateDppResult,
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


class AsyncRawLifeCycleApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DigitalProductPassport]:
        """
        Returns the DPP with the specified DPP ID. Conformance: shall.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        representation : typing.Optional[ReadDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DigitalProductPassport]
            The requested DPP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    async def delete_dpp_by_id(
        self, dpp_id: Identifier, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Removes the DPP with the specified DPP ID (end of life). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def update_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[UpdateDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DigitalProductPassport]:
        """
        Partial update of a DPP. The body carries only the parts to update or extend
        (RFC 7396 JSON Merge Patch may be used). If any part fails, the whole update
        fails and no change is adopted. All changes are archived per EN 18221.
        Conformance: shall where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request : DigitalProductPassport

        representation : typing.Optional[UpdateDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DigitalProductPassport]
            The updated DPP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dpps/{encode_path_param(dpp_id)}",
            method="PATCH",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=DigitalProductPassport, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    async def read_dpp_by_product_id(
        self,
        product_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByProductIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DigitalProductPassport]:
        """
        Returns the current active DPP (latest version) for the unique product identifier (EN 18219 GS1 Digital Link). Conformance: shall.

        Parameters
        ----------
        product_id : Identifier
            Unique product identifier (EN 18219 GS1 Digital Link), percent-encoded.

        representation : typing.Optional[ReadDppByProductIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DigitalProductPassport]
            The latest active DPP for the product.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dppsByProductId/{encode_path_param(product_id)}",
            method="GET",
            params={
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    async def read_dpp_version_by_id_and_date(
        self,
        dpp_id: Identifier,
        *,
        date: Timestamp,
        representation: typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DigitalProductPassport]:
        """
        Returns the DPP version current at the given date (archived versions per EN 18221). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        date : Timestamp
            UTC-based timestamp (ISO 8601-1) for which the version is requested.

        representation : typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DigitalProductPassport]
            The DPP version at the given date.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dppsByIdAndDate/{encode_path_param(dpp_id)}",
            method="GET",
            params={
                "date": serialize_datetime(date),
                "representation": representation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DigitalProductPassport,
                    parse_obj_as(
                        type_=DigitalProductPassport,
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

    async def read_dpp_ids_by_product_ids(
        self,
        *,
        product_ids: typing.Sequence[Identifier],
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DppIdPage]:
        """
        Returns the DPP identifiers matching a set of product identifiers (discovery). Paginated by `limit` and `cursor` (the cursor shall not be empty). Conformance: shall.

        Parameters
        ----------
        product_ids : typing.Sequence[Identifier]

        limit : typing.Optional[int]
            Maximum number of identifiers to return in this page.

        cursor : typing.Optional[str]
            Opaque, non-empty pagination token from a prior response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DppIdPage]
            The matching DPP identifiers, with an optional next-page cursor.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dppsByProductIds",
            method="POST",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            json={
                "productIds": product_ids,
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
                    DppIdPage,
                    parse_obj_as(
                        type_=DppIdPage,
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

    async def create_dpp(
        self,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[CreateDppRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDppResult]:
        """
        Creates a new DPP and returns its DPP ID. Conformance: should.

        Parameters
        ----------
        request : DigitalProductPassport

        representation : typing.Optional[CreateDppRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDppResult]
            DPP created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dpps",
            method="POST",
            params={
                "representation": representation,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=DigitalProductPassport, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDppResult,
                    parse_obj_as(
                        type_=CreateDppResult,
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
