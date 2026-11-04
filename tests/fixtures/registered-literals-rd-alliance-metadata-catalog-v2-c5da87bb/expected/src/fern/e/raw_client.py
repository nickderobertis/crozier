

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
from ..types.creator import Creator
from ..types.endorsement_related_entities_item import EndorsementRelatedEntitiesItem
from ..types.endorsement_valid import EndorsementValid
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mscid import Mscid
from ..types.response_item_endorsement import ResponseItemEndorsement
from ..types.response_page_endorsement import ResponsePageEndorsement
from ..types.response_success_endorsement import ResponseSuccessEndorsement
from ..types.slug import Slug
from ..types.uri import Uri
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_endorsements(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageEndorsement]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageEndorsement]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/e",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageEndorsement,
                    parse_obj_as(
                        type_=ResponsePageEndorsement,
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

    def submit_a_new_endorsement_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessEndorsement]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessEndorsement]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/e",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "publication": publication,
                "issued": issued,
                "valid": convert_and_respect_annotation_metadata(
                    object_=valid, annotation=EndorsementValid, direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[EndorsementRelatedEntitiesItem],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessEndorsement,
                    parse_obj_as(
                        type_=ResponseSuccessEndorsement,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def retrieve_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemEndorsement]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemEndorsement]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemEndorsement,
                    parse_obj_as(
                        type_=ResponseItemEndorsement,
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

    def modify_an_existing_endorsement_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessEndorsement]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessEndorsement]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "publication": publication,
                "issued": issued,
                "valid": convert_and_respect_annotation_metadata(
                    object_=valid, annotation=EndorsementValid, direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[EndorsementRelatedEntitiesItem],
                    direction="write",
                ),
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
                    ResponseSuccessEndorsement,
                    parse_obj_as(
                        type_=ResponseSuccessEndorsement,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def remove_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
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


class AsyncRawEClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_endorsements(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageEndorsement]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageEndorsement]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/e",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageEndorsement,
                    parse_obj_as(
                        type_=ResponsePageEndorsement,
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

    async def submit_a_new_endorsement_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessEndorsement]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessEndorsement]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/e",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "publication": publication,
                "issued": issued,
                "valid": convert_and_respect_annotation_metadata(
                    object_=valid, annotation=EndorsementValid, direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[EndorsementRelatedEntitiesItem],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessEndorsement,
                    parse_obj_as(
                        type_=ResponseSuccessEndorsement,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def retrieve_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemEndorsement]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemEndorsement]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemEndorsement,
                    parse_obj_as(
                        type_=ResponseItemEndorsement,
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

    async def modify_an_existing_endorsement_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessEndorsement]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessEndorsement]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "publication": publication,
                "issued": issued,
                "valid": convert_and_respect_annotation_metadata(
                    object_=valid, annotation=EndorsementValid, direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[EndorsementRelatedEntitiesItem],
                    direction="write",
                ),
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
                    ResponseSuccessEndorsement,
                    parse_obj_as(
                        type_=ResponseSuccessEndorsement,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def remove_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/e{encode_path_param(int_)}",
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
