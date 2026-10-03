

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.practice_event import PracticeEvent
from ..types.practice_intent import PracticeIntent
from ..types.practice_service_metadata import PracticeServiceMetadata
from .raw_client import AsyncRawPracticeClient, RawPracticeClient
from .types.create_insurance_product_request_coverage import CreateInsuranceProductRequestCoverage


OMIT = typing.cast(typing.Any, ...)


class PracticeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPracticeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPracticeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPracticeClient
        """
        return self._raw_client

    def create_service_metadata(
        self,
        practice_id: str,
        *,
        practice_service_metadata_create_practice_id: str,
        service_name: str,
        duration_minutes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeServiceMetadata:
        """
        Parameters
        ----------
        practice_id : str

        practice_service_metadata_create_practice_id : str

        service_name : str

        duration_minutes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeServiceMetadata
            The created metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.practice.create_service_metadata(
            practice_id="practice_id",
            practice_service_metadata_create_practice_id="practice_id",
            service_name="service_name",
        )
        """
        _response = self._raw_client.create_service_metadata(
            practice_id,
            practice_service_metadata_create_practice_id=practice_service_metadata_create_practice_id,
            service_name=service_name,
            duration_minutes=duration_minutes,
            request_options=request_options,
        )
        return _response.data

    def create_intent(
        self,
        practice_id: str,
        *,
        practice_intent_create_practice_id: str,
        intent: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeIntent:
        """
        Parameters
        ----------
        practice_id : str

        practice_intent_create_practice_id : str

        intent : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeIntent
            The created intent.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.practice.create_intent(
            practice_id="practice_id",
            practice_intent_create_practice_id="practice_id",
            intent="intent",
        )
        """
        _response = self._raw_client.create_intent(
            practice_id,
            practice_intent_create_practice_id=practice_intent_create_practice_id,
            intent=intent,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def create_insurance_product(
        self,
        practice_id: str,
        *,
        insurance_product_practice_id: str,
        coverage: typing.Optional[CreateInsuranceProductRequestCoverage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeEvent:
        """
        Parameters
        ----------
        practice_id : str

        insurance_product_practice_id : str

        coverage : typing.Optional[CreateInsuranceProductRequestCoverage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeEvent
            The created product's events.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.practice.create_insurance_product(
            practice_id="practice_id",
            insurance_product_practice_id="practice_id",
        )
        """
        _response = self._raw_client.create_insurance_product(
            practice_id,
            insurance_product_practice_id=insurance_product_practice_id,
            coverage=coverage,
            request_options=request_options,
        )
        return _response.data

    def create_note(
        self,
        practice_id: str,
        *,
        note_practice_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        practice_id : str

        note_practice_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.practice.create_note(
            practice_id="practice_id",
            note_practice_id="practice_id",
            body="body",
        )
        """
        _response = self._raw_client.create_note(
            practice_id, note_practice_id=note_practice_id, body=body, request_options=request_options
        )
        return _response.data


class AsyncPracticeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPracticeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPracticeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPracticeClient
        """
        return self._raw_client

    async def create_service_metadata(
        self,
        practice_id: str,
        *,
        practice_service_metadata_create_practice_id: str,
        service_name: str,
        duration_minutes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeServiceMetadata:
        """
        Parameters
        ----------
        practice_id : str

        practice_service_metadata_create_practice_id : str

        service_name : str

        duration_minutes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeServiceMetadata
            The created metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.practice.create_service_metadata(
                practice_id="practice_id",
                practice_service_metadata_create_practice_id="practice_id",
                service_name="service_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_service_metadata(
            practice_id,
            practice_service_metadata_create_practice_id=practice_service_metadata_create_practice_id,
            service_name=service_name,
            duration_minutes=duration_minutes,
            request_options=request_options,
        )
        return _response.data

    async def create_intent(
        self,
        practice_id: str,
        *,
        practice_intent_create_practice_id: str,
        intent: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeIntent:
        """
        Parameters
        ----------
        practice_id : str

        practice_intent_create_practice_id : str

        intent : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeIntent
            The created intent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.practice.create_intent(
                practice_id="practice_id",
                practice_intent_create_practice_id="practice_id",
                intent="intent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_intent(
            practice_id,
            practice_intent_create_practice_id=practice_intent_create_practice_id,
            intent=intent,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def create_insurance_product(
        self,
        practice_id: str,
        *,
        insurance_product_practice_id: str,
        coverage: typing.Optional[CreateInsuranceProductRequestCoverage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PracticeEvent:
        """
        Parameters
        ----------
        practice_id : str

        insurance_product_practice_id : str

        coverage : typing.Optional[CreateInsuranceProductRequestCoverage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PracticeEvent
            The created product's events.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.practice.create_insurance_product(
                practice_id="practice_id",
                insurance_product_practice_id="practice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_insurance_product(
            practice_id,
            insurance_product_practice_id=insurance_product_practice_id,
            coverage=coverage,
            request_options=request_options,
        )
        return _response.data

    async def create_note(
        self,
        practice_id: str,
        *,
        note_practice_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        practice_id : str

        note_practice_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.practice.create_note(
                practice_id="practice_id",
                note_practice_id="practice_id",
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note(
            practice_id, note_practice_id=note_practice_id, body=body, request_options=request_options
        )
        return _response.data
