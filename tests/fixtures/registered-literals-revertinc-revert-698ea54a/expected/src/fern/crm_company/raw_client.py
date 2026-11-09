

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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.common_company_address import CommonCompanyAddress
from ..types.common_company_association import CommonCompanyAssociation
from ..types.crm_create_or_update_company_response import CrmCreateOrUpdateCompanyResponse
from ..types.crm_get_companies_response import CrmGetCompaniesResponse
from ..types.crm_get_company_response import CrmGetCompanyResponse
from ..types.crm_search_companies_response import CrmSearchCompaniesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrmCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crm_company_get_company(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetCompanyResponse]:
        """
        Get details of a company

        Parameters
        ----------
        id : str
            The unique `id` of the company in the CRM.

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetCompanyResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/companies/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetCompanyResponse,
                    parse_obj_as(
                        type_=CrmGetCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def crm_company_update_company(
        self,
        id_: str,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateCompanyResponse]:
        """
        Update a company

        Parameters
        ----------
        id_ : str

        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateCompanyResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/companies/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "name": name,
                "industry": industry,
                "description": description,
                "annualRevenue": annual_revenue,
                "size": size,
                "phone": phone,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CommonCompanyAddress, direction="write"
                ),
                "id": id,
                "remoteId": remote_id,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "additional": additional,
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
                    CrmCreateOrUpdateCompanyResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def crm_company_get_companies(
        self,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetCompaniesResponse]:
        """
        Get all the companies

        Parameters
        ----------
        fields : typing.Optional[str]

        associations : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetCompaniesResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetCompaniesResponse,
                    parse_obj_as(
                        type_=CrmGetCompaniesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def crm_company_create_company(
        self,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        associations: typing.Optional[CommonCompanyAssociation] = OMIT,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateCompanyResponse]:
        """
        Create a new company

        Parameters
        ----------
        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        associations : typing.Optional[CommonCompanyAssociation]

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateCompanyResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="POST",
            json={
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonCompanyAssociation, direction="write"
                ),
                "name": name,
                "industry": industry,
                "description": description,
                "annualRevenue": annual_revenue,
                "size": size,
                "phone": phone,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CommonCompanyAddress, direction="write"
                ),
                "id": id,
                "remoteId": remote_id,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "additional": additional,
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
                    CrmCreateOrUpdateCompanyResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def crm_company_search_companies(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmSearchCompaniesResponse]:
        """
        Search for companies

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmSearchCompaniesResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/companies/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
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
                    CrmSearchCompaniesResponse,
                    parse_obj_as(
                        type_=CrmSearchCompaniesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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


class AsyncRawCrmCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crm_company_get_company(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetCompanyResponse]:
        """
        Get details of a company

        Parameters
        ----------
        id : str
            The unique `id` of the company in the CRM.

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetCompanyResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/companies/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetCompanyResponse,
                    parse_obj_as(
                        type_=CrmGetCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def crm_company_update_company(
        self,
        id_: str,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateCompanyResponse]:
        """
        Update a company

        Parameters
        ----------
        id_ : str

        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateCompanyResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/companies/{encode_path_param(id_)}",
            method="PATCH",
            json={
                "name": name,
                "industry": industry,
                "description": description,
                "annualRevenue": annual_revenue,
                "size": size,
                "phone": phone,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CommonCompanyAddress, direction="write"
                ),
                "id": id,
                "remoteId": remote_id,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "additional": additional,
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
                    CrmCreateOrUpdateCompanyResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def crm_company_get_companies(
        self,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetCompaniesResponse]:
        """
        Get all the companies

        Parameters
        ----------
        fields : typing.Optional[str]

        associations : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetCompaniesResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetCompaniesResponse,
                    parse_obj_as(
                        type_=CrmGetCompaniesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def crm_company_create_company(
        self,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        associations: typing.Optional[CommonCompanyAssociation] = OMIT,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateCompanyResponse]:
        """
        Create a new company

        Parameters
        ----------
        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        associations : typing.Optional[CommonCompanyAssociation]

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateCompanyResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/companies",
            method="POST",
            json={
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonCompanyAssociation, direction="write"
                ),
                "name": name,
                "industry": industry,
                "description": description,
                "annualRevenue": annual_revenue,
                "size": size,
                "phone": phone,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CommonCompanyAddress, direction="write"
                ),
                "id": id,
                "remoteId": remote_id,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "additional": additional,
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
                    CrmCreateOrUpdateCompanyResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateCompanyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def crm_company_search_companies(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmSearchCompaniesResponse]:
        """
        Search for companies

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmSearchCompaniesResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/companies/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
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
                    CrmSearchCompaniesResponse,
                    parse_obj_as(
                        type_=CrmSearchCompaniesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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
