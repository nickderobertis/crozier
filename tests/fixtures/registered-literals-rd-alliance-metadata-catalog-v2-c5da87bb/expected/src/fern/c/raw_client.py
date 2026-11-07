

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
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mapping_related_entities_item import MappingRelatedEntitiesItem
from ..types.mapping_versions_item import MappingVersionsItem
from ..types.mscid import Mscid
from ..types.response_item_mapping import ResponseItemMapping
from ..types.response_page_mapping import ResponsePageMapping
from ..types.response_success_mapping import ResponseSuccessMapping
from ..types.slug import Slug
from ..types.uri import Uri
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_mappings(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageMapping]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageMapping]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/c",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageMapping,
                    parse_obj_as(
                        type_=ResponsePageMapping,
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

    def submit_a_new_mapping_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessMapping]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessMapping]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/c",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "name": name,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[MappingRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MappingVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessMapping,
                    parse_obj_as(
                        type_=ResponseSuccessMapping,
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

    def retrieve_an_existing_mapping_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemMapping]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemMapping]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/c{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemMapping,
                    parse_obj_as(
                        type_=ResponseItemMapping,
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

    def modify_an_existing_mapping_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessMapping]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessMapping]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/c{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "name": name,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[MappingRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MappingVersionsItem], direction="write"
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
                    ResponseSuccessMapping,
                    parse_obj_as(
                        type_=ResponseSuccessMapping,
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

    def remove_an_existing_mapping_record(
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
            f"api2/c{encode_path_param(int_)}",
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


class AsyncRawCClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_mappings(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageMapping]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageMapping]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/c",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageMapping,
                    parse_obj_as(
                        type_=ResponsePageMapping,
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

    async def submit_a_new_mapping_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessMapping]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessMapping]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/c",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "name": name,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[MappingRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MappingVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessMapping,
                    parse_obj_as(
                        type_=ResponseSuccessMapping,
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

    async def retrieve_an_existing_mapping_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemMapping]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemMapping]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/c{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemMapping,
                    parse_obj_as(
                        type_=ResponseItemMapping,
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

    async def modify_an_existing_mapping_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessMapping]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessMapping]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/c{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "name": name,
                "description": description,
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[MappingRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MappingVersionsItem], direction="write"
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
                    ResponseSuccessMapping,
                    parse_obj_as(
                        type_=ResponseSuccessMapping,
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

    async def remove_an_existing_mapping_record(
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
            f"api2/c{encode_path_param(int_)}",
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
