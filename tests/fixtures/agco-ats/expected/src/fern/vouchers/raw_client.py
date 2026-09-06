

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_voucher_history import ApiPagedResponseDealerDbModelsVoucherHistory
from ..types.dealer_db_models_voucher import DealerDbModelsVoucher
from ..types.dealer_db_models_voucher_type import DealerDbModelsVoucherType
from .types.vouchers_get_request_deleted import VouchersGetRequestDeleted
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVouchersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        voucher_code: str,
        *,
        deleted: typing.Optional[VouchersGetRequestDeleted] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DealerDbModelsVoucher]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to get.

        deleted : typing.Optional[VouchersGetRequestDeleted]
            Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DealerDbModelsVoucher]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}",
            method="GET",
            params={
                "Deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DealerDbModelsVoucher,
                    parse_obj_as(
                        type_=DealerDbModelsVoucher,
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

    def post(
        self,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Vouchers",
            method="POST",
            json={
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Deleted": deleted,
                "Email": email,
                "ExpirationDate": expiration_date,
                "LicenseTo": license_to,
                "ModifiedBy": modified_by,
                "OrderNumber": order_number,
                "Punched": punched,
                "PunchedDate": punched_date,
                "Purpose": purpose,
                "Type": type,
                "VoucherCode": voucher_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def put(
        self,
        voucher_code_: str,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code_ : str
            The voucher code of the voucher to update.

        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code_)}",
            method="PUT",
            json={
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Deleted": deleted,
                "Email": email,
                "ExpirationDate": expiration_date,
                "LicenseTo": license_to,
                "ModifiedBy": modified_by,
                "OrderNumber": order_number,
                "Punched": punched,
                "PunchedDate": punched_date,
                "Purpose": purpose,
                "Type": type,
                "VoucherCode": voucher_code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, voucher_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getvoucherhistory(
        self,
        voucher_code: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code to get history for.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}/VoucherHistory",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseDealerDbModelsVoucherHistory,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsVoucherHistory,
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


class AsyncRawVouchersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        voucher_code: str,
        *,
        deleted: typing.Optional[VouchersGetRequestDeleted] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DealerDbModelsVoucher]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to get.

        deleted : typing.Optional[VouchersGetRequestDeleted]
            Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DealerDbModelsVoucher]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}",
            method="GET",
            params={
                "Deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DealerDbModelsVoucher,
                    parse_obj_as(
                        type_=DealerDbModelsVoucher,
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

    async def post(
        self,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Vouchers",
            method="POST",
            json={
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Deleted": deleted,
                "Email": email,
                "ExpirationDate": expiration_date,
                "LicenseTo": license_to,
                "ModifiedBy": modified_by,
                "OrderNumber": order_number,
                "Punched": punched,
                "PunchedDate": punched_date,
                "Purpose": purpose,
                "Type": type,
                "VoucherCode": voucher_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def put(
        self,
        voucher_code_: str,
        *,
        created_date: typing.Optional[dt.datetime] = OMIT,
        dealer_code: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[dt.datetime] = OMIT,
        license_to: typing.Optional[str] = OMIT,
        modified_by: typing.Optional[str] = OMIT,
        order_number: typing.Optional[str] = OMIT,
        punched: typing.Optional[bool] = OMIT,
        punched_date: typing.Optional[dt.datetime] = OMIT,
        purpose: typing.Optional[str] = OMIT,
        type: typing.Optional[DealerDbModelsVoucherType] = OMIT,
        voucher_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code_ : str
            The voucher code of the voucher to update.

        created_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was created.

        dealer_code : typing.Optional[str]
            The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers.

        deleted : typing.Optional[bool]
            Read-Only. True if voucher has been deleted.

        email : typing.Optional[str]
            Required for internal vouchers.

        expiration_date : typing.Optional[dt.datetime]
            The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers.

        license_to : typing.Optional[str]
            Required for Internal Vouchers

        modified_by : typing.Optional[str]
            Read-Only. The user that made the last modification to the voucher.

        order_number : typing.Optional[str]
            The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers.

        punched : typing.Optional[bool]
            True if voucher has aleady been used.  False if the voucher has not been used.

        punched_date : typing.Optional[dt.datetime]
            Read-Only. The date the voucher was punched.

        purpose : typing.Optional[str]
            Required for Internal Vouchers. Not supported for other Vouchers.

        type : typing.Optional[DealerDbModelsVoucherType]
            The type of voucher. Commercial is the default if not specified.

        voucher_code : typing.Optional[str]
            The voucher code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code_)}",
            method="PUT",
            json={
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Deleted": deleted,
                "Email": email,
                "ExpirationDate": expiration_date,
                "LicenseTo": license_to,
                "ModifiedBy": modified_by,
                "OrderNumber": order_number,
                "Punched": punched,
                "PunchedDate": punched_date,
                "Purpose": purpose,
                "Type": type,
                "VoucherCode": voucher_code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, voucher_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code of the voucher to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getvoucherhistory(
        self,
        voucher_code: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str
            The voucher code to get history for.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Vouchers/{encode_path_param(voucher_code)}/VoucherHistory",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseDealerDbModelsVoucherHistory,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsVoucherHistory,
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
