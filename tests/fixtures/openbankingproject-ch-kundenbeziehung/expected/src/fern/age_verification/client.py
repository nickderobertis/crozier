

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.age_verification_response import AgeVerificationResponse
from .raw_client import AsyncRawAgeVerificationClient, RawAgeVerificationClient
from .types.age_verification_request_purpose import AgeVerificationRequestPurpose


OMIT = typing.cast(typing.Any, ...)


class AgeVerificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgeVerificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgeVerificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgeVerificationClient
        """
        return self._raw_client

    def verify_age(
        self,
        *,
        customer_id: str,
        required_attribute: str,
        minimum_age: int,
        purpose: typing.Optional[AgeVerificationRequestPurpose] = OMIT,
        requesting_service: typing.Optional[str] = OMIT,
        attribute_only: typing.Optional[bool] = OMIT,
        data_minimization: typing.Optional[bool] = OMIT,
        existing_verification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgeVerificationResponse:
        """
        Privacy-preserving Altersverifikation ohne vollständige Identitätspreisgabe

        Parameters
        ----------
        customer_id : str

        required_attribute : str

        minimum_age : int

        purpose : typing.Optional[AgeVerificationRequestPurpose]

        requesting_service : typing.Optional[str]

        attribute_only : typing.Optional[bool]
            Nur Attribut (ja/nein) zurückgeben

        data_minimization : typing.Optional[bool]

        existing_verification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgeVerificationResponse
            Altersverifikation erfolgreich

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.age_verification.verify_age(
            customer_id="customerId",
            required_attribute="age_minimum_18",
            minimum_age=1,
        )
        """
        _response = self._raw_client.verify_age(
            customer_id=customer_id,
            required_attribute=required_attribute,
            minimum_age=minimum_age,
            purpose=purpose,
            requesting_service=requesting_service,
            attribute_only=attribute_only,
            data_minimization=data_minimization,
            existing_verification_id=existing_verification_id,
            request_options=request_options,
        )
        return _response.data


class AsyncAgeVerificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgeVerificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgeVerificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgeVerificationClient
        """
        return self._raw_client

    async def verify_age(
        self,
        *,
        customer_id: str,
        required_attribute: str,
        minimum_age: int,
        purpose: typing.Optional[AgeVerificationRequestPurpose] = OMIT,
        requesting_service: typing.Optional[str] = OMIT,
        attribute_only: typing.Optional[bool] = OMIT,
        data_minimization: typing.Optional[bool] = OMIT,
        existing_verification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgeVerificationResponse:
        """
        Privacy-preserving Altersverifikation ohne vollständige Identitätspreisgabe

        Parameters
        ----------
        customer_id : str

        required_attribute : str

        minimum_age : int

        purpose : typing.Optional[AgeVerificationRequestPurpose]

        requesting_service : typing.Optional[str]

        attribute_only : typing.Optional[bool]
            Nur Attribut (ja/nein) zurückgeben

        data_minimization : typing.Optional[bool]

        existing_verification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgeVerificationResponse
            Altersverifikation erfolgreich

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.age_verification.verify_age(
                customer_id="customerId",
                required_attribute="age_minimum_18",
                minimum_age=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_age(
            customer_id=customer_id,
            required_attribute=required_attribute,
            minimum_age=minimum_age,
            purpose=purpose,
            requesting_service=requesting_service,
            attribute_only=attribute_only,
            data_minimization=data_minimization,
            existing_verification_id=existing_verification_id,
            request_options=request_options,
        )
        return _response.data
