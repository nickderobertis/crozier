

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cancel_response import CancelResponse
from ..types.rest_response import RestResponse
from .raw_client import AsyncRawBulkSmsClient, RawBulkSmsClient
from .types.rest_send_request_messages_item import RestSendRequestMessagesItem


OMIT = typing.cast(typing.Any, ...)


class BulkSmsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBulkSmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBulkSmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBulkSmsClient
        """
        return self._raw_client

    def send_rest_sms(
        self,
        *,
        msgheader: str,
        messages: typing.Sequence[RestSendRequestMessagesItem],
        encoding: typing.Optional[str] = OMIT,
        iysfilter: typing.Optional[str] = OMIT,
        partnercode: typing.Optional[str] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RestResponse:
        """
        Send SMS via REST protocol

        Parameters
        ----------
        msgheader : str
            Message header/sender ID

        messages : typing.Sequence[RestSendRequestMessagesItem]

        encoding : typing.Optional[str]
            Message encoding

        iysfilter : typing.Optional[str]
            IYS filter

        partnercode : typing.Optional[str]
            Partner code

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestResponse
            success

        Examples
        --------
        from fern.bulk_sms import RestSendRequestMessagesItem

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.bulk_sms.send_rest_sms(
            msgheader="msgheader",
            messages=[RestSendRequestMessagesItem()],
        )
        """
        _response = self._raw_client.send_rest_sms(
            msgheader=msgheader,
            messages=messages,
            encoding=encoding,
            iysfilter=iysfilter,
            partnercode=partnercode,
            appname=appname,
            request_options=request_options,
        )
        return _response.data

    def cancel_sms(
        self,
        *,
        jobid: str,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CancelResponse:
        """
        Cancel a scheduled SMS

        Parameters
        ----------
        jobid : str
            Job ID of the SMS to cancel

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.bulk_sms.cancel_sms(
            jobid="jobid",
        )
        """
        _response = self._raw_client.cancel_sms(jobid=jobid, appname=appname, request_options=request_options)
        return _response.data


class AsyncBulkSmsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBulkSmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBulkSmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBulkSmsClient
        """
        return self._raw_client

    async def send_rest_sms(
        self,
        *,
        msgheader: str,
        messages: typing.Sequence[RestSendRequestMessagesItem],
        encoding: typing.Optional[str] = OMIT,
        iysfilter: typing.Optional[str] = OMIT,
        partnercode: typing.Optional[str] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RestResponse:
        """
        Send SMS via REST protocol

        Parameters
        ----------
        msgheader : str
            Message header/sender ID

        messages : typing.Sequence[RestSendRequestMessagesItem]

        encoding : typing.Optional[str]
            Message encoding

        iysfilter : typing.Optional[str]
            IYS filter

        partnercode : typing.Optional[str]
            Partner code

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestResponse
            success

        Examples
        --------
        import asyncio

        from fern.bulk_sms import RestSendRequestMessagesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.bulk_sms.send_rest_sms(
                msgheader="msgheader",
                messages=[RestSendRequestMessagesItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_rest_sms(
            msgheader=msgheader,
            messages=messages,
            encoding=encoding,
            iysfilter=iysfilter,
            partnercode=partnercode,
            appname=appname,
            request_options=request_options,
        )
        return _response.data

    async def cancel_sms(
        self,
        *,
        jobid: str,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CancelResponse:
        """
        Cancel a scheduled SMS

        Parameters
        ----------
        jobid : str
            Job ID of the SMS to cancel

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.bulk_sms.cancel_sms(
                jobid="jobid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_sms(jobid=jobid, appname=appname, request_options=request_options)
        return _response.data
