

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
from ..types.mscid import Mscid
from ..types.response_item_tool import ResponseItemTool
from ..types.response_page_tool import ResponsePageTool
from ..types.response_success_tool import ResponseSuccessTool
from ..types.slug import Slug
from ..types.tool_related_entities_item import ToolRelatedEntitiesItem
from ..types.tool_versions_item import ToolVersionsItem
from ..types.uri import Uri
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_tools(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageTool]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageTool]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/t",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageTool,
                    parse_obj_as(
                        type_=ResponsePageTool,
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

    def submit_a_new_tool_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessTool]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessTool]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/t",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "types": types,
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[ToolRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[ToolVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessTool,
                    parse_obj_as(
                        type_=ResponseSuccessTool,
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

    def retrieve_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseItemTool]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemTool]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/t{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemTool,
                    parse_obj_as(
                        type_=ResponseItemTool,
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

    def modify_an_existing_tool_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessTool]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessTool]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/t{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "types": types,
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[ToolRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[ToolVersionsItem], direction="write"
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
                    ResponseSuccessTool,
                    parse_obj_as(
                        type_=ResponseSuccessTool,
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

    def remove_an_existing_tool_record(
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
            f"api2/t{encode_path_param(int_)}",
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


class AsyncRawTClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_tools(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageTool]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageTool]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/t",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageTool,
                    parse_obj_as(
                        type_=ResponsePageTool,
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

    async def submit_a_new_tool_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessTool]:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessTool]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/t",
            method="POST",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "types": types,
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[ToolRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[ToolVersionsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessTool,
                    parse_obj_as(
                        type_=ResponseSuccessTool,
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

    async def retrieve_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseItemTool]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemTool]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/t{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemTool,
                    parse_obj_as(
                        type_=ResponseItemTool,
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

    async def modify_an_existing_tool_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessTool]:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessTool]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/t{encode_path_param(int_)}",
            method="PUT",
            json={
                "slug": slug,
                "mscid": mscid,
                "uri": uri,
                "title": title,
                "description": description,
                "types": types,
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers, annotation=typing.Sequence[Identifier], direction="write"
                ),
                "locations": convert_and_respect_annotation_metadata(
                    object_=locations, annotation=typing.Sequence[Location], direction="write"
                ),
                "creators": convert_and_respect_annotation_metadata(
                    object_=creators, annotation=typing.Sequence[Creator], direction="write"
                ),
                "relatedEntities": convert_and_respect_annotation_metadata(
                    object_=related_entities, annotation=typing.Sequence[ToolRelatedEntitiesItem], direction="write"
                ),
                "versions": convert_and_respect_annotation_metadata(
                    object_=versions, annotation=typing.Sequence[ToolVersionsItem], direction="write"
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
                    ResponseSuccessTool,
                    parse_obj_as(
                        type_=ResponseSuccessTool,
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

    async def remove_an_existing_tool_record(
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
            f"api2/t{encode_path_param(int_)}",
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
