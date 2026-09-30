

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.substance import Substance
from .types.get_substance_by_uuid_request_db import GetSubstanceByUuidRequestDb
from .types.get_substances_request_db import GetSubstancesRequestDb
from .types.get_substances_request_type import GetSubstancesRequestType
from pydantic import ValidationError


class RawSubstancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_substances(
        self,
        db: GetSubstancesRequestDb,
        *,
        search: typing.Optional[str] = None,
        type: typing.Optional[GetSubstancesRequestType] = None,
        compound_uri: typing.Optional[str] = None,
        bundle_uri: typing.Optional[str] = None,
        add_dummy_substance: typing.Optional[bool] = None,
        studysummary: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Substance]:
        """
        Returns a list of substances, according to the search criteria

        Parameters
        ----------
        db : GetSubstancesRequestDb
            Database ID

        search : typing.Optional[str]
            Search parameter

        type : typing.Optional[GetSubstancesRequestType]

        compound_uri : typing.Optional[str]
            If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure

        bundle_uri : typing.Optional[str]
            Retrieves if selected in this bundle

        add_dummy_substance : typing.Optional[bool]
            Adds a compound record as substance in JSON; only if type=related

        studysummary : typing.Optional[bool]
            If true retrieves study summary for each substance

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Substance]
            OK. Substances found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance",
            method="GET",
            params={
                "search": search,
                "type": type,
                "compound_uri": compound_uri,
                "bundle_uri": bundle_uri,
                "addDummySubstance": add_dummy_substance,
                "studysummary": studysummary,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Substance,
                    parse_obj_as(
                        type_=Substance,
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

    def get_substance_by_uuid(
        self,
        db: GetSubstanceByUuidRequestDb,
        uuid_: str,
        *,
        property_uris: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Substance]:
        """
        Returns substance representation

        Parameters
        ----------
        db : GetSubstanceByUuidRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        property_uris : typing.Optional[str]
            Property URIs

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Substance]
            OK. Substances found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}",
            method="GET",
            params={
                "property_uris[]": property_uris,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Substance,
                    parse_obj_as(
                        type_=Substance,
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


class AsyncRawSubstancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_substances(
        self,
        db: GetSubstancesRequestDb,
        *,
        search: typing.Optional[str] = None,
        type: typing.Optional[GetSubstancesRequestType] = None,
        compound_uri: typing.Optional[str] = None,
        bundle_uri: typing.Optional[str] = None,
        add_dummy_substance: typing.Optional[bool] = None,
        studysummary: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Substance]:
        """
        Returns a list of substances, according to the search criteria

        Parameters
        ----------
        db : GetSubstancesRequestDb
            Database ID

        search : typing.Optional[str]
            Search parameter

        type : typing.Optional[GetSubstancesRequestType]

        compound_uri : typing.Optional[str]
            If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure

        bundle_uri : typing.Optional[str]
            Retrieves if selected in this bundle

        add_dummy_substance : typing.Optional[bool]
            Adds a compound record as substance in JSON; only if type=related

        studysummary : typing.Optional[bool]
            If true retrieves study summary for each substance

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Substance]
            OK. Substances found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance",
            method="GET",
            params={
                "search": search,
                "type": type,
                "compound_uri": compound_uri,
                "bundle_uri": bundle_uri,
                "addDummySubstance": add_dummy_substance,
                "studysummary": studysummary,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Substance,
                    parse_obj_as(
                        type_=Substance,
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

    async def get_substance_by_uuid(
        self,
        db: GetSubstanceByUuidRequestDb,
        uuid_: str,
        *,
        property_uris: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Substance]:
        """
        Returns substance representation

        Parameters
        ----------
        db : GetSubstanceByUuidRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        property_uris : typing.Optional[str]
            Property URIs

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Substance]
            OK. Substances found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}",
            method="GET",
            params={
                "property_uris[]": property_uris,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Substance,
                    parse_obj_as(
                        type_=Substance,
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
