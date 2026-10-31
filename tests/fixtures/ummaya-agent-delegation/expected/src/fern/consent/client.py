

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consent_record import ConsentRecord
from .raw_client import AsyncRawConsentClient, RawConsentClient


OMIT = typing.cast(typing.Any, ...)


class ConsentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsentClient
        """
        return self._raw_client

    def create_consent_record(
        self,
        *,
        citizen_identity: str,
        scopes: typing.Sequence[str],
        synthesis_consent: bool,
        expires_at: dt.datetime,
        dpa_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsentRecord:
        """
        Citizen-signed consent artifact. MUST include `dpa_reference` whenever any requested
        scope touches a PII-bound tool (PIPA §26 위탁 documentation gap closure).
        MUST include `synthesis_consent` as a separate boolean reflecting the LLM-synthesis
        controller-level carve-out.

        Parameters
        ----------
        citizen_identity : str
            Opaque citizen identifier bound by PASS/공동인증서 at collection time.

        scopes : typing.Sequence[str]
            Scope entries shaped as `<tool_id>:<verb>[:resource]`.

        synthesis_consent : bool
            Separate consent for the LLM-synthesis controller-level carve-out (FR-015).

        expires_at : dt.datetime

        dpa_reference : typing.Optional[str]
            Non-null when any scope is PII-bound (FR-014).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentRecord
            Consent recorded.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.consent.create_consent_record(
            citizen_identity="citizen_identity",
            scopes=["scopes"],
            synthesis_consent=True,
            expires_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_consent_record(
            citizen_identity=citizen_identity,
            scopes=scopes,
            synthesis_consent=synthesis_consent,
            expires_at=expires_at,
            dpa_reference=dpa_reference,
            request_options=request_options,
        )
        return _response.data


class AsyncConsentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsentClient
        """
        return self._raw_client

    async def create_consent_record(
        self,
        *,
        citizen_identity: str,
        scopes: typing.Sequence[str],
        synthesis_consent: bool,
        expires_at: dt.datetime,
        dpa_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsentRecord:
        """
        Citizen-signed consent artifact. MUST include `dpa_reference` whenever any requested
        scope touches a PII-bound tool (PIPA §26 위탁 documentation gap closure).
        MUST include `synthesis_consent` as a separate boolean reflecting the LLM-synthesis
        controller-level carve-out.

        Parameters
        ----------
        citizen_identity : str
            Opaque citizen identifier bound by PASS/공동인증서 at collection time.

        scopes : typing.Sequence[str]
            Scope entries shaped as `<tool_id>:<verb>[:resource]`.

        synthesis_consent : bool
            Separate consent for the LLM-synthesis controller-level carve-out (FR-015).

        expires_at : dt.datetime

        dpa_reference : typing.Optional[str]
            Non-null when any scope is PII-bound (FR-014).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentRecord
            Consent recorded.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent.create_consent_record(
                citizen_identity="citizen_identity",
                scopes=["scopes"],
                synthesis_consent=True,
                expires_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_consent_record(
            citizen_identity=citizen_identity,
            scopes=scopes,
            synthesis_consent=synthesis_consent,
            expires_at=expires_at,
            dpa_reference=dpa_reference,
            request_options=request_options,
        )
        return _response.data
