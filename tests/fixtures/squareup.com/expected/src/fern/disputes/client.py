

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accept_dispute_response import AcceptDisputeResponse
from ..types.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from ..types.delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
from ..types.list_dispute_evidence_response import ListDisputeEvidenceResponse
from ..types.list_disputes_response import ListDisputesResponse
from ..types.retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
from ..types.retrieve_dispute_response import RetrieveDisputeResponse
from ..types.submit_evidence_response import SubmitEvidenceResponse
from .raw_client import AsyncRawDisputesClient, RawDisputesClient


OMIT = typing.cast(typing.Any, ...)


class DisputesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDisputesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDisputesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDisputesClient
        """
        return self._raw_client

    def list_disputes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        states: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDisputesResponse:
        """
        Returns a list of disputes associated with a particular account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        states : typing.Optional[str]
            The dispute states to filter the result.
            If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
            or `LOST`).

        location_id : typing.Optional[str]
            The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
            all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDisputesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.list_disputes()
        """
        _response = self._raw_client.list_disputes(
            cursor=cursor, states=states, location_id=location_id, request_options=request_options
        )
        return _response.data

    def retrieve_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveDisputeResponse:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDisputeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.retrieve_dispute(
            dispute_id="dispute_id",
        )
        """
        _response = self._raw_client.retrieve_dispute(dispute_id, request_options=request_options)
        return _response.data

    def accept_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptDisputeResponse:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptDisputeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.accept_dispute(
            dispute_id="dispute_id",
        )
        """
        _response = self._raw_client.accept_dispute(dispute_id, request_options=request_options)
        return _response.data

    def list_dispute_evidence(
        self,
        dispute_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDisputeEvidenceResponse:
        """
        Returns a list of evidence associated with a dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDisputeEvidenceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.list_dispute_evidence(
            dispute_id="dispute_id",
        )
        """
        _response = self._raw_client.list_dispute_evidence(dispute_id, cursor=cursor, request_options=request_options)
        return _response.data

    def create_dispute_evidence_text(
        self,
        dispute_id: str,
        *,
        evidence_text: str,
        idempotency_key: str,
        evidence_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDisputeEvidenceTextResponse:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to upload evidence for.

        evidence_text : str
            The evidence string.

        idempotency_key : str
            The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_type : typing.Optional[str]
            The type of evidence you are uploading.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDisputeEvidenceTextResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.create_dispute_evidence_text(
            dispute_id="dispute_id",
            evidence_text="evidence_text",
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.create_dispute_evidence_text(
            dispute_id,
            evidence_text=evidence_text,
            idempotency_key=idempotency_key,
            evidence_type=evidence_type,
            request_options=request_options,
        )
        return _response.data

    def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveDisputeEvidenceResponse:
        """
        Returns the evidence metadata specified by the evidence ID in the request URL path

        You must maintain a copy of the evidence you upload if you want to reference it later. You cannot
        download the evidence after you upload it.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to retrieve evidence from.

        evidence_id : str
            The ID of the evidence to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDisputeEvidenceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.retrieve_dispute_evidence(
            dispute_id="dispute_id",
            evidence_id="evidence_id",
        )
        """
        _response = self._raw_client.retrieve_dispute_evidence(dispute_id, evidence_id, request_options=request_options)
        return _response.data

    def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDisputeEvidenceResponse:
        """
        Removes specified evidence from a dispute.

        Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after
        submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to remove evidence from.

        evidence_id : str
            The ID of the evidence you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDisputeEvidenceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.delete_dispute_evidence(
            dispute_id="dispute_id",
            evidence_id="evidence_id",
        )
        """
        _response = self._raw_client.delete_dispute_evidence(dispute_id, evidence_id, request_options=request_options)
        return _response.data

    def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubmitEvidenceResponse:
        """
        Submits evidence to the cardholder's bank.

        Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded
        using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and
        [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and
        evidence automatically provided by Square, when available.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to submit evidence for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitEvidenceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.disputes.submit_evidence(
            dispute_id="dispute_id",
        )
        """
        _response = self._raw_client.submit_evidence(dispute_id, request_options=request_options)
        return _response.data


class AsyncDisputesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDisputesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDisputesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDisputesClient
        """
        return self._raw_client

    async def list_disputes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        states: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDisputesResponse:
        """
        Returns a list of disputes associated with a particular account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        states : typing.Optional[str]
            The dispute states to filter the result.
            If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
            or `LOST`).

        location_id : typing.Optional[str]
            The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
            all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDisputesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.list_disputes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_disputes(
            cursor=cursor, states=states, location_id=location_id, request_options=request_options
        )
        return _response.data

    async def retrieve_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveDisputeResponse:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDisputeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.retrieve_dispute(
                dispute_id="dispute_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_dispute(dispute_id, request_options=request_options)
        return _response.data

    async def accept_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptDisputeResponse:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptDisputeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.accept_dispute(
                dispute_id="dispute_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_dispute(dispute_id, request_options=request_options)
        return _response.data

    async def list_dispute_evidence(
        self,
        dispute_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDisputeEvidenceResponse:
        """
        Returns a list of evidence associated with a dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDisputeEvidenceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.list_dispute_evidence(
                dispute_id="dispute_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dispute_evidence(
            dispute_id, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def create_dispute_evidence_text(
        self,
        dispute_id: str,
        *,
        evidence_text: str,
        idempotency_key: str,
        evidence_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDisputeEvidenceTextResponse:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to upload evidence for.

        evidence_text : str
            The evidence string.

        idempotency_key : str
            The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_type : typing.Optional[str]
            The type of evidence you are uploading.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDisputeEvidenceTextResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.create_dispute_evidence_text(
                dispute_id="dispute_id",
                evidence_text="evidence_text",
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dispute_evidence_text(
            dispute_id,
            evidence_text=evidence_text,
            idempotency_key=idempotency_key,
            evidence_type=evidence_type,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveDisputeEvidenceResponse:
        """
        Returns the evidence metadata specified by the evidence ID in the request URL path

        You must maintain a copy of the evidence you upload if you want to reference it later. You cannot
        download the evidence after you upload it.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to retrieve evidence from.

        evidence_id : str
            The ID of the evidence to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDisputeEvidenceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.retrieve_dispute_evidence(
                dispute_id="dispute_id",
                evidence_id="evidence_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_dispute_evidence(
            dispute_id, evidence_id, request_options=request_options
        )
        return _response.data

    async def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDisputeEvidenceResponse:
        """
        Removes specified evidence from a dispute.

        Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after
        submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to remove evidence from.

        evidence_id : str
            The ID of the evidence you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDisputeEvidenceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.delete_dispute_evidence(
                dispute_id="dispute_id",
                evidence_id="evidence_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dispute_evidence(
            dispute_id, evidence_id, request_options=request_options
        )
        return _response.data

    async def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubmitEvidenceResponse:
        """
        Submits evidence to the cardholder's bank.

        Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded
        using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and
        [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and
        evidence automatically provided by Square, when available.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to submit evidence for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitEvidenceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.disputes.submit_evidence(
                dispute_id="dispute_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_evidence(dispute_id, request_options=request_options)
        return _response.data
