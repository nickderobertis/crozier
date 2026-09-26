

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPredictionClient, RawPredictionClient


OMIT = typing.cast(typing.Any, ...)


class PredictionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPredictionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPredictionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPredictionClient
        """
        return self._raw_client

    def predict(
        self,
        account: str,
        product: str,
        version: str,
        *,
        document: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submit a document for synchronous parsing and prediction.

        Parameters
        ----------
        account : str
            Account name or 'mindee' for built-in products.

        product : str
            Product name (e.g., invoices, receipts, passports).

        version : str
            Product version.

        document : typing.Optional[str]
            Base64-encoded document or URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful prediction.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prediction.predict(
            account="account",
            product="product",
            version="version",
        )
        """
        _response = self._raw_client.predict(
            account, product, version, document=document, request_options=request_options
        )
        return _response.data

    def predict_async(
        self,
        account: str,
        product: str,
        version: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submit a document for asynchronous parsing. Returns a job ID.

        Parameters
        ----------
        account : str

        product : str

        version : str

        document : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Async job created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prediction.predict_async(
            account="account",
            product="product",
            version="version",
        )
        """
        _response = self._raw_client.predict_async(
            account, product, version, document=document, request_options=request_options
        )
        return _response.data

    def get_async_result(
        self,
        account: str,
        product: str,
        version: str,
        job_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Poll for the result of an asynchronous prediction job.

        Parameters
        ----------
        account : str

        product : str

        version : str

        job_id : str
            Async job ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Job result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prediction.get_async_result(
            account="account",
            product="product",
            version="version",
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_async_result(
            account, product, version, job_id, request_options=request_options
        )
        return _response.data


class AsyncPredictionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPredictionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPredictionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPredictionClient
        """
        return self._raw_client

    async def predict(
        self,
        account: str,
        product: str,
        version: str,
        *,
        document: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submit a document for synchronous parsing and prediction.

        Parameters
        ----------
        account : str
            Account name or 'mindee' for built-in products.

        product : str
            Product name (e.g., invoices, receipts, passports).

        version : str
            Product version.

        document : typing.Optional[str]
            Base64-encoded document or URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful prediction.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prediction.predict(
                account="account",
                product="product",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.predict(
            account, product, version, document=document, request_options=request_options
        )
        return _response.data

    async def predict_async(
        self,
        account: str,
        product: str,
        version: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submit a document for asynchronous parsing. Returns a job ID.

        Parameters
        ----------
        account : str

        product : str

        version : str

        document : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Async job created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prediction.predict_async(
                account="account",
                product="product",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.predict_async(
            account, product, version, document=document, request_options=request_options
        )
        return _response.data

    async def get_async_result(
        self,
        account: str,
        product: str,
        version: str,
        job_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Poll for the result of an asynchronous prediction job.

        Parameters
        ----------
        account : str

        product : str

        version : str

        job_id : str
            Async job ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Job result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prediction.get_async_result(
                account="account",
                product="product",
                version="version",
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_result(
            account, product, version, job_id, request_options=request_options
        )
        return _response.data
