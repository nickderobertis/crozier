

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
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
from ..types.metadata_scheme_versions_item import MetadataSchemeVersionsItem
from ..types.mscid import Mscid
from ..types.namespace import Namespace
from ..types.response_item_metadata_scheme import ResponseItemMetadataScheme
from ..types.response_page_metadata_scheme import ResponsePageMetadataScheme
from ..types.response_success_metadata_scheme import ResponseSuccessMetadataScheme
from ..types.slug import Slug
from ..types.uri import Uri
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_metadata_schemes(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageMetadataScheme]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageMetadataScheme]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/m",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageMetadataScheme,
                    parse_obj_as(
                        type_=ResponsePageMetadataScheme,
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

    def submit_a_new_metadata_scheme_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessMetadataScheme]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessMetadataScheme]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/m",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "keywords": keywords,
                "dataTypes": data_types,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "namespaces": convert_and_respect_annotation_metadata(
                    object_=namespaces, annotation=typing.Sequence[Namespace], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[MetadataSchemeRelatedEntitiesItem],
                    direction="write",
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MetadataSchemeVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessMetadataScheme,
                    parse_obj_as(
                        type_=ResponseSuccessMetadataScheme,
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

    def retrieve_an_existing_metadata_scheme_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemMetadataScheme]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemMetadataScheme]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/m{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemMetadataScheme,
                    parse_obj_as(
                        type_=ResponseItemMetadataScheme,
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

    def modify_an_existing_metadata_scheme_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessMetadataScheme]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessMetadataScheme]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/m{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "keywords": keywords,
                "dataTypes": data_types,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "namespaces": convert_and_respect_annotation_metadata(
                    object_=namespaces, annotation=typing.Sequence[Namespace], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[MetadataSchemeRelatedEntitiesItem],
                    direction="write",
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MetadataSchemeVersionsItem], direction="write"
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
                    ResponseSuccessMetadataScheme,
                    parse_obj_as(
                        type_=ResponseSuccessMetadataScheme,
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

    def remove_an_existing_metadata_scheme_record(
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
            f"api2/m{encode_path_param(int_)}",
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


class AsyncRawMClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_metadata_schemes(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageMetadataScheme]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageMetadataScheme]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/m",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageMetadataScheme,
                    parse_obj_as(
                        type_=ResponsePageMetadataScheme,
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

    async def submit_a_new_metadata_scheme_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessMetadataScheme]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessMetadataScheme]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/m",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "keywords": keywords,
                "dataTypes": data_types,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "namespaces": convert_and_respect_annotation_metadata(
                    object_=namespaces, annotation=typing.Sequence[Namespace], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[MetadataSchemeRelatedEntitiesItem],
                    direction="write",
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MetadataSchemeVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessMetadataScheme,
                    parse_obj_as(
                        type_=ResponseSuccessMetadataScheme,
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

    async def retrieve_an_existing_metadata_scheme_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemMetadataScheme]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemMetadataScheme]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/m{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemMetadataScheme,
                    parse_obj_as(
                        type_=ResponseItemMetadataScheme,
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

    async def modify_an_existing_metadata_scheme_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessMetadataScheme]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessMetadataScheme]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/m{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "keywords": keywords,
                "dataTypes": data_types,
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "namespaces": convert_and_respect_annotation_metadata(
                    object_=namespaces, annotation=typing.Sequence[Namespace], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities,
                    annotation=typing.Sequence[MetadataSchemeRelatedEntitiesItem],
                    direction="write",
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[MetadataSchemeVersionsItem], direction="write"
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
                    ResponseSuccessMetadataScheme,
                    parse_obj_as(
                        type_=ResponseSuccessMetadataScheme,
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

    async def remove_an_existing_metadata_scheme_record(
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
            f"api2/m{encode_path_param(int_)}",
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
