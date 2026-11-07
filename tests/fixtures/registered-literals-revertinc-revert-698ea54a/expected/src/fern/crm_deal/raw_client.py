

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
from ..types.common_deal_association import CommonDealAssociation
from ..types.crm_create_or_update_deal_response import CrmCreateOrUpdateDealResponse
from ..types.crm_get_deal_response import CrmGetDealResponse
from ..types.crm_get_deals_response import CrmGetDealsResponse
from ..types.crm_search_deals_response import CrmSearchDealsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrmDealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crm_deal_get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetDealResponse]:
        """
        Get details of a deal

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetDealResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/deals/{encode_path_param(id)}",
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
                    CrmGetDealResponse,
                    parse_obj_as(
                        type_=CrmGetDealResponse,
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

    def crm_deal_update_deal(
        self,
        id: str,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateDealResponse]:
        """
        Update a deal

        Parameters
        ----------
        id : str

        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateDealResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/deals/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonDealAssociation, direction="write"
                ),
                "amount": amount,
                "priority": priority,
                "stage": stage,
                "name": name,
                "expectedCloseDate": expected_close_date,
                "isWon": is_won,
                "probability": probability,
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
                    CrmCreateOrUpdateDealResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateDealResponse,
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

    def crm_deal_get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetDealsResponse]:
        """
        Get all the deals

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetDealsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/deals",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetDealsResponse,
                    parse_obj_as(
                        type_=CrmGetDealsResponse,
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

    def crm_deal_create_deal(
        self,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateDealResponse]:
        """
        Create a new deal

        Parameters
        ----------
        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateDealResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/deals",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonDealAssociation, direction="write"
                ),
                "amount": amount,
                "priority": priority,
                "stage": stage,
                "name": name,
                "expectedCloseDate": expected_close_date,
                "isWon": is_won,
                "probability": probability,
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
                    CrmCreateOrUpdateDealResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateDealResponse,
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

    def crm_deal_search_deals(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmSearchDealsResponse]:
        """
        Search for deals

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
        HttpResponse[CrmSearchDealsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/deals/search",
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
                    CrmSearchDealsResponse,
                    parse_obj_as(
                        type_=CrmSearchDealsResponse,
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


class AsyncRawCrmDealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crm_deal_get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetDealResponse]:
        """
        Get details of a deal

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetDealResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/deals/{encode_path_param(id)}",
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
                    CrmGetDealResponse,
                    parse_obj_as(
                        type_=CrmGetDealResponse,
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

    async def crm_deal_update_deal(
        self,
        id: str,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateDealResponse]:
        """
        Update a deal

        Parameters
        ----------
        id : str

        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateDealResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/deals/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonDealAssociation, direction="write"
                ),
                "amount": amount,
                "priority": priority,
                "stage": stage,
                "name": name,
                "expectedCloseDate": expected_close_date,
                "isWon": is_won,
                "probability": probability,
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
                    CrmCreateOrUpdateDealResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateDealResponse,
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

    async def crm_deal_get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetDealsResponse]:
        """
        Get all the deals

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetDealsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/deals",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetDealsResponse,
                    parse_obj_as(
                        type_=CrmGetDealsResponse,
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

    async def crm_deal_create_deal(
        self,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateDealResponse]:
        """
        Create a new deal

        Parameters
        ----------
        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateDealResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/deals",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonDealAssociation, direction="write"
                ),
                "amount": amount,
                "priority": priority,
                "stage": stage,
                "name": name,
                "expectedCloseDate": expected_close_date,
                "isWon": is_won,
                "probability": probability,
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
                    CrmCreateOrUpdateDealResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateDealResponse,
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

    async def crm_deal_search_deals(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmSearchDealsResponse]:
        """
        Search for deals

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
        AsyncHttpResponse[CrmSearchDealsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/deals/search",
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
                    CrmSearchDealsResponse,
                    parse_obj_as(
                        type_=CrmSearchDealsResponse,
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
