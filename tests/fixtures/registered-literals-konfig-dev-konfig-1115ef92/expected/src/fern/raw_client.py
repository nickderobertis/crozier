

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.not_found_error import NotFoundError
from .errors.unauthorized_error import UnauthorizedError
from .types.create_async_file_upload_response import CreateAsyncFileUploadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def receipt_match(
        self, *, receipt_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateAsyncFileUploadResponse]:
        """

        The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

        Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.

        Parameters
        ----------
        receipt_name : str
            The name of the receipt (with the file extension). It will be used in the matching result email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAsyncFileUploadResponse]
            receiptMatch 200 response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/expenses/card/receipt_match",
            method="POST",
            json={
                "receipt_name": receipt_name,
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
                    CreateAsyncFileUploadResponse,
                    parse_obj_as(
                        type_=CreateAsyncFileUploadResponse,
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

    def receipt_upload(
        self, expense_id: str, *, receipt_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateAsyncFileUploadResponse]:
        """

        The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

        Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.

        Parameters
        ----------
        expense_id : str

        receipt_name : str
            The name of the receipt (with the file extension).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAsyncFileUploadResponse]
            receiptUpload 200 response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}/receipt_upload",
            method="POST",
            json={
                "receipt_name": receipt_name,
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
                    CreateAsyncFileUploadResponse,
                    parse_obj_as(
                        type_=CreateAsyncFileUploadResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def receipt_match(
        self, *, receipt_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateAsyncFileUploadResponse]:
        """

        The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

        Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.

        Parameters
        ----------
        receipt_name : str
            The name of the receipt (with the file extension). It will be used in the matching result email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAsyncFileUploadResponse]
            receiptMatch 200 response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/expenses/card/receipt_match",
            method="POST",
            json={
                "receipt_name": receipt_name,
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
                    CreateAsyncFileUploadResponse,
                    parse_obj_as(
                        type_=CreateAsyncFileUploadResponse,
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

    async def receipt_upload(
        self, expense_id: str, *, receipt_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateAsyncFileUploadResponse]:
        """

        The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

        Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.

        Parameters
        ----------
        expense_id : str

        receipt_name : str
            The name of the receipt (with the file extension).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAsyncFileUploadResponse]
            receiptUpload 200 response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}/receipt_upload",
            method="POST",
            json={
                "receipt_name": receipt_name,
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
                    CreateAsyncFileUploadResponse,
                    parse_obj_as(
                        type_=CreateAsyncFileUploadResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
