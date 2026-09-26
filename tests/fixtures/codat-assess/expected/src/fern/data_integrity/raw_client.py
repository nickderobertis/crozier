

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.details import Details
from ..types.status import Status
from ..types.summaries import Summaries
from .types.get_data_integrity_details_request_data_type import GetDataIntegrityDetailsRequestDataType
from .types.get_data_integrity_status_request_data_type import GetDataIntegrityStatusRequestDataType
from .types.get_data_integrity_summaries_request_data_type import GetDataIntegritySummariesRequestDataType
from pydantic import ValidationError


class RawDataIntegrityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_data_integrity_details(
        self,
        company_id: str,
        data_type: GetDataIntegrityDetailsRequestDataType,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Details]:
        """
        Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityDetailsRequestDataType
            A key for a Codat data type.

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Details]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/details",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
                "orderBy": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Details,
                    parse_obj_as(
                        type_=Details,
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

    def get_data_integrity_status(
        self,
        company_id: str,
        data_type: GetDataIntegrityStatusRequestDataType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Status]:
        """
        Gets match status for a given company and datatype.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityStatusRequestDataType
            A key for a Codat data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Status]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Status,
                    parse_obj_as(
                        type_=Status,
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

    def get_data_integrity_summaries(
        self,
        company_id: str,
        data_type: GetDataIntegritySummariesRequestDataType,
        *,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Summaries]:
        """
        Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegritySummariesRequestDataType
            A key for a Codat data type.

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Summaries]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/summaries",
            method="GET",
            params={
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Summaries,
                    parse_obj_as(
                        type_=Summaries,
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


class AsyncRawDataIntegrityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_data_integrity_details(
        self,
        company_id: str,
        data_type: GetDataIntegrityDetailsRequestDataType,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Details]:
        """
        Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityDetailsRequestDataType
            A key for a Codat data type.

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Details]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/details",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
                "orderBy": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Details,
                    parse_obj_as(
                        type_=Details,
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

    async def get_data_integrity_status(
        self,
        company_id: str,
        data_type: GetDataIntegrityStatusRequestDataType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Status]:
        """
        Gets match status for a given company and datatype.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegrityStatusRequestDataType
            A key for a Codat data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Status]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Status,
                    parse_obj_as(
                        type_=Status,
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

    async def get_data_integrity_summaries(
        self,
        company_id: str,
        data_type: GetDataIntegritySummariesRequestDataType,
        *,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Summaries]:
        """
        Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

        Parameters
        ----------
        company_id : str

        data_type : GetDataIntegritySummariesRequestDataType
            A key for a Codat data type.

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Summaries]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/dataTypes/{encode_path_param(data_type)}/dataIntegrity/summaries",
            method="GET",
            params={
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Summaries,
                    parse_obj_as(
                        type_=Summaries,
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
