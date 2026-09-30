

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.skg_if_json_ld_response import SkgIfJsonLdResponse
from pydantic import ValidationError


class RawProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search6(
        self,
        *,
        filter: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SkgIfJsonLdResponse]:
        """
        Get a list of `product` matching the provided filter criteria.

        Parameters
        ----------
        filter : str
               Filter string with pipe-separated values for multiple values per key.

               **Format:** `key1:value1|value2,key2:value3`

               **Examples:**
               - Single values: `product_type:publication,cf.search.title:ocean`
               - Multiple values: `product_type:publication|dataset|software`
               - Mixed: `product_type:publication|dataset,cf.search.title:ocean`

               **IMPORTANT:** Duplicate keys are not allowed (use pipe `|` to separate multiple values)

               **Attribute Filters:**
            - `product_type`: publication, dataset, software, other
            - `identifiers.id`: product identifier (DOI, arXiv, etc.)
            - `identifiers.scheme`: identifier scheme (doi, arxiv, etc.)
            - `contributions.by.local_identifier`: contributor local ID
            - `contributions.by.identifiers.id`: contributor identifier (ORCID, etc.)
            - `contributions.by.identifiers.scheme`: contributor ID scheme (orcid, etc.)
            - `contributions.by.family_name`: contributor family name
            - `contributions.by.given_name`: contributor given name
            - `contributions.by.name`: contributor full name
            - `contributions.declared_affiliations.local_identifier`: affiliation local ID
            - `contributions.declared_affiliations.identifiers.id`: affiliation identifier
            - `contributions.declared_affiliations.identifiers.scheme`: affiliation ID scheme
            - `contributions.declared_affiliations.name`: affiliation name
            - `contributions.declared_affiliations.short_name`: affiliation short name
            - `funding.local_identifier`: funding local identifier
            - `funding.grant_number`: funding grant number
            - `funding.identifiers.id`: funding identifier
            - `funding.identifiers.scheme`: funding identifier scheme

            **Convenience Filters:**
            - `cf.search.title`: title search
            - `cf.search.title_abstract`: title and abstract search
            - `cf.contributions_orcid`: ORCID-based contributor search
            - `cf.cites`: citation relationships
            - `cf.subject`: subject classification
            - `cf.publication_year`: publication year
            - `cf.language`: language filter
            - `cf.access_rights`: access rights filter

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SkgIfJsonLdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "skg-if/v1/products",
            method="GET",
            params={
                "filter": filter,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SkgIfJsonLdResponse,
                    parse_obj_as(
                        type_=SkgIfJsonLdResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_by_id6(
        self, local_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SkgIfJsonLdResponse]:
        """
        Get product by local identifier.

        Parameters
        ----------
        local_identifier : str
            The local identifier of the product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SkgIfJsonLdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"skg-if/v1/products/{encode_path_param(local_identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SkgIfJsonLdResponse,
                    parse_obj_as(
                        type_=SkgIfJsonLdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search6(
        self,
        *,
        filter: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SkgIfJsonLdResponse]:
        """
        Get a list of `product` matching the provided filter criteria.

        Parameters
        ----------
        filter : str
               Filter string with pipe-separated values for multiple values per key.

               **Format:** `key1:value1|value2,key2:value3`

               **Examples:**
               - Single values: `product_type:publication,cf.search.title:ocean`
               - Multiple values: `product_type:publication|dataset|software`
               - Mixed: `product_type:publication|dataset,cf.search.title:ocean`

               **IMPORTANT:** Duplicate keys are not allowed (use pipe `|` to separate multiple values)

               **Attribute Filters:**
            - `product_type`: publication, dataset, software, other
            - `identifiers.id`: product identifier (DOI, arXiv, etc.)
            - `identifiers.scheme`: identifier scheme (doi, arxiv, etc.)
            - `contributions.by.local_identifier`: contributor local ID
            - `contributions.by.identifiers.id`: contributor identifier (ORCID, etc.)
            - `contributions.by.identifiers.scheme`: contributor ID scheme (orcid, etc.)
            - `contributions.by.family_name`: contributor family name
            - `contributions.by.given_name`: contributor given name
            - `contributions.by.name`: contributor full name
            - `contributions.declared_affiliations.local_identifier`: affiliation local ID
            - `contributions.declared_affiliations.identifiers.id`: affiliation identifier
            - `contributions.declared_affiliations.identifiers.scheme`: affiliation ID scheme
            - `contributions.declared_affiliations.name`: affiliation name
            - `contributions.declared_affiliations.short_name`: affiliation short name
            - `funding.local_identifier`: funding local identifier
            - `funding.grant_number`: funding grant number
            - `funding.identifiers.id`: funding identifier
            - `funding.identifiers.scheme`: funding identifier scheme

            **Convenience Filters:**
            - `cf.search.title`: title search
            - `cf.search.title_abstract`: title and abstract search
            - `cf.contributions_orcid`: ORCID-based contributor search
            - `cf.cites`: citation relationships
            - `cf.subject`: subject classification
            - `cf.publication_year`: publication year
            - `cf.language`: language filter
            - `cf.access_rights`: access rights filter

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SkgIfJsonLdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "skg-if/v1/products",
            method="GET",
            params={
                "filter": filter,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SkgIfJsonLdResponse,
                    parse_obj_as(
                        type_=SkgIfJsonLdResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_by_id6(
        self, local_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SkgIfJsonLdResponse]:
        """
        Get product by local identifier.

        Parameters
        ----------
        local_identifier : str
            The local identifier of the product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SkgIfJsonLdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"skg-if/v1/products/{encode_path_param(local_identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SkgIfJsonLdResponse,
                    parse_obj_as(
                        type_=SkgIfJsonLdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
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
