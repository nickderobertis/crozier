

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.record import Record
from .raw_client import AsyncRawRecordsClient, RawRecordsClient


OMIT = typing.cast(typing.Any, ...)


class RecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecordsClient
        """
        return self._raw_client

    def create_record(
        self,
        *,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        args: typing.Optional[str] = OMIT,
        json: typing.Optional[str] = OMIT,
        data: typing.Optional[str] = OMIT,
        files: typing.Optional[str] = OMIT,
        headers: typing.Optional[str] = OMIT,
        params: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        cls: typing.Optional[str] = OMIT,
        client: typing.Optional[str] = OMIT,
        dict: typing.Optional[str] = OMIT,
        model_config: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        schema: typing.Optional[str] = OMIT,
        validate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Record:
        """
        Parameters
        ----------
        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        args : typing.Optional[str]

        json : typing.Optional[str]

        data : typing.Optional[str]

        files : typing.Optional[str]

        headers : typing.Optional[str]

        params : typing.Optional[str]

        content : typing.Optional[str]

        timeout : typing.Optional[str]

        cls : typing.Optional[str]

        client : typing.Optional[str]

        dict : typing.Optional[str]

        model_config : typing.Optional[str]

        type : typing.Optional[str]

        id : typing.Optional[str]

        copy : typing.Optional[str]

        schema : typing.Optional[str]

        validate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Record
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.records.create_record()
        """
        _response = self._raw_client.create_record(
            kwargs_=kwargs_,
            self_=self_,
            args=args,
            json=json,
            data=data,
            files=files,
            headers=headers,
            params=params,
            content=content,
            timeout=timeout,
            cls=cls,
            client=client,
            dict=dict,
            model_config=model_config,
            type=type,
            id=id,
            copy=copy,
            schema=schema,
            validate=validate,
            request_options=request_options,
        )
        return _response.data


class AsyncRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecordsClient
        """
        return self._raw_client

    async def create_record(
        self,
        *,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        args: typing.Optional[str] = OMIT,
        json: typing.Optional[str] = OMIT,
        data: typing.Optional[str] = OMIT,
        files: typing.Optional[str] = OMIT,
        headers: typing.Optional[str] = OMIT,
        params: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        cls: typing.Optional[str] = OMIT,
        client: typing.Optional[str] = OMIT,
        dict: typing.Optional[str] = OMIT,
        model_config: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        schema: typing.Optional[str] = OMIT,
        validate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Record:
        """
        Parameters
        ----------
        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        args : typing.Optional[str]

        json : typing.Optional[str]

        data : typing.Optional[str]

        files : typing.Optional[str]

        headers : typing.Optional[str]

        params : typing.Optional[str]

        content : typing.Optional[str]

        timeout : typing.Optional[str]

        cls : typing.Optional[str]

        client : typing.Optional[str]

        dict : typing.Optional[str]

        model_config : typing.Optional[str]

        type : typing.Optional[str]

        id : typing.Optional[str]

        copy : typing.Optional[str]

        schema : typing.Optional[str]

        validate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Record
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.records.create_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_record(
            kwargs_=kwargs_,
            self_=self_,
            args=args,
            json=json,
            data=data,
            files=files,
            headers=headers,
            params=params,
            content=content,
            timeout=timeout,
            cls=cls,
            client=client,
            dict=dict,
            model_config=model_config,
            type=type,
            id=id,
            copy=copy,
            schema=schema,
            validate=validate,
            request_options=request_options,
        )
        return _response.data
