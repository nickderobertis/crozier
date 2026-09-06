

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.email_settings import EmailSettings
from ..types.ereader_device_object import EreaderDeviceObject
from ..types.ereader_name import EreaderName
from ..types.library_item_id import LibraryItemId
from .types.update_e_reader_devices_response import UpdateEReaderDevicesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEmailClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_email_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmailSettings]:
        """
        Get email settings for sending e-books to e-readers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmailSettings]
            Successful response - Email
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/emails/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailSettings,
                    parse_obj_as(
                        type_=EmailSettings,
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

    def update_email_settings(
        self,
        *,
        id: str,
        port: int,
        secure: bool,
        ereader_devices: typing.Sequence[EreaderDeviceObject],
        host: typing.Optional[str] = OMIT,
        reject_unauthorized: typing.Optional[bool] = OMIT,
        user: typing.Optional[str] = OMIT,
        pass_: typing.Optional[str] = OMIT,
        test_address: typing.Optional[str] = OMIT,
        from_address: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmailSettings]:
        """
        Parameters
        ----------
        id : str
            The unique identifier for the email settings. Currently this is always `email-settings`

        port : int
            The port number for the SMTP server.

        secure : bool
            Indicates if the connection should use SSL/TLS.

        ereader_devices : typing.Sequence[EreaderDeviceObject]
            List of configured e-reader devices.

        host : typing.Optional[str]
            The SMTP host address.

        reject_unauthorized : typing.Optional[bool]
            Indicates if unauthorized SSL/TLS certificates should be rejected.

        user : typing.Optional[str]
            The username for SMTP authentication.

        pass_ : typing.Optional[str]
            The password for SMTP authentication.

        test_address : typing.Optional[str]
            The test email address used for sending test emails.

        from_address : typing.Optional[str]
            The default "from" email address for outgoing emails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmailSettings]
            Successful response - Email
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/emails/settings",
            method="PATCH",
            json={
                "id": id,
                "host": host,
                "port": port,
                "secure": secure,
                "rejectUnauthorized": reject_unauthorized,
                "user": user,
                "pass": pass_,
                "testAddress": test_address,
                "fromAddress": from_address,
                "ereaderDevices": convert_and_respect_annotation_metadata(
                    object_=ereader_devices, annotation=typing.Sequence[EreaderDeviceObject], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailSettings,
                    parse_obj_as(
                        type_=EmailSettings,
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

    def send_test_email(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/emails/test",
            method="POST",
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

    def update_e_reader_devices(
        self,
        *,
        ereader_devices: typing.Optional[typing.Sequence[EreaderDeviceObject]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateEReaderDevicesResponse]:
        """
        Parameters
        ----------
        ereader_devices : typing.Optional[typing.Sequence[EreaderDeviceObject]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateEReaderDevicesResponse]
            Successful response - Ereader
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/emails/ereader-devices",
            method="POST",
            json={
                "ereaderDevices": convert_and_respect_annotation_metadata(
                    object_=ereader_devices, annotation=typing.Sequence[EreaderDeviceObject], direction="write"
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
                    UpdateEReaderDevicesResponse,
                    parse_obj_as(
                        type_=UpdateEReaderDevicesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def send_e_book_to_device(
        self,
        *,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        device_name: typing.Optional[EreaderName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        library_item_id : typing.Optional[LibraryItemId]

        device_name : typing.Optional[EreaderName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/emails/send-ebook-to-device",
            method="POST",
            json={
                "libraryItemId": library_item_id,
                "deviceName": device_name,
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


class AsyncRawEmailClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_email_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmailSettings]:
        """
        Get email settings for sending e-books to e-readers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmailSettings]
            Successful response - Email
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/emails/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailSettings,
                    parse_obj_as(
                        type_=EmailSettings,
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

    async def update_email_settings(
        self,
        *,
        id: str,
        port: int,
        secure: bool,
        ereader_devices: typing.Sequence[EreaderDeviceObject],
        host: typing.Optional[str] = OMIT,
        reject_unauthorized: typing.Optional[bool] = OMIT,
        user: typing.Optional[str] = OMIT,
        pass_: typing.Optional[str] = OMIT,
        test_address: typing.Optional[str] = OMIT,
        from_address: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmailSettings]:
        """
        Parameters
        ----------
        id : str
            The unique identifier for the email settings. Currently this is always `email-settings`

        port : int
            The port number for the SMTP server.

        secure : bool
            Indicates if the connection should use SSL/TLS.

        ereader_devices : typing.Sequence[EreaderDeviceObject]
            List of configured e-reader devices.

        host : typing.Optional[str]
            The SMTP host address.

        reject_unauthorized : typing.Optional[bool]
            Indicates if unauthorized SSL/TLS certificates should be rejected.

        user : typing.Optional[str]
            The username for SMTP authentication.

        pass_ : typing.Optional[str]
            The password for SMTP authentication.

        test_address : typing.Optional[str]
            The test email address used for sending test emails.

        from_address : typing.Optional[str]
            The default "from" email address for outgoing emails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmailSettings]
            Successful response - Email
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/emails/settings",
            method="PATCH",
            json={
                "id": id,
                "host": host,
                "port": port,
                "secure": secure,
                "rejectUnauthorized": reject_unauthorized,
                "user": user,
                "pass": pass_,
                "testAddress": test_address,
                "fromAddress": from_address,
                "ereaderDevices": convert_and_respect_annotation_metadata(
                    object_=ereader_devices, annotation=typing.Sequence[EreaderDeviceObject], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmailSettings,
                    parse_obj_as(
                        type_=EmailSettings,
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

    async def send_test_email(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/emails/test",
            method="POST",
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

    async def update_e_reader_devices(
        self,
        *,
        ereader_devices: typing.Optional[typing.Sequence[EreaderDeviceObject]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateEReaderDevicesResponse]:
        """
        Parameters
        ----------
        ereader_devices : typing.Optional[typing.Sequence[EreaderDeviceObject]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateEReaderDevicesResponse]
            Successful response - Ereader
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/emails/ereader-devices",
            method="POST",
            json={
                "ereaderDevices": convert_and_respect_annotation_metadata(
                    object_=ereader_devices, annotation=typing.Sequence[EreaderDeviceObject], direction="write"
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
                    UpdateEReaderDevicesResponse,
                    parse_obj_as(
                        type_=UpdateEReaderDevicesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def send_e_book_to_device(
        self,
        *,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        device_name: typing.Optional[EreaderName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        library_item_id : typing.Optional[LibraryItemId]

        device_name : typing.Optional[EreaderName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/emails/send-ebook-to-device",
            method="POST",
            json={
                "libraryItemId": library_item_id,
                "deviceName": device_name,
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
