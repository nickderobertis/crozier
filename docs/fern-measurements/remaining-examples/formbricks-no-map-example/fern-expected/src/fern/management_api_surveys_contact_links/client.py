

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManagementApiSurveysContactLinksClient, RawManagementApiSurveysContactLinksClient
from .types.get_contact_links_by_segment_response import GetContactLinksBySegmentResponse
from .types.get_personalized_survey_link_response import GetPersonalizedSurveyLinkResponse


class ManagementApiSurveysContactLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementApiSurveysContactLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementApiSurveysContactLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementApiSurveysContactLinksClient
        """
        return self._raw_client

    def get_personalized_survey_link(
        self,
        survey_id: str,
        contact_id: str,
        *,
        expiration_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPersonalizedSurveyLinkResponse:
        """
        Retrieves a personalized link for a specific survey.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        contact_id : str
            The ID of the contact

        expiration_days : typing.Optional[int]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPersonalizedSurveyLinkResponse
            Personalized survey link retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_surveys_contact_links.get_personalized_survey_link(
            survey_id="surveyId",
            contact_id="contactId",
        )
        """
        _response = self._raw_client.get_personalized_survey_link(
            survey_id, contact_id, expiration_days=expiration_days, request_options=request_options
        )
        return _response.data

    def get_contact_links_by_segment(
        self,
        survey_id: str,
        segment_id: str,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        expiration_days: typing.Optional[float] = None,
        attribute_keys: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactLinksBySegmentResponse:
        """
        Generates personalized survey links for contacts in a segment.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        segment_id : str
            The ID of the segment

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        expiration_days : typing.Optional[float]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        attribute_keys : typing.Optional[str]
            Comma-separated list of contact attribute keys to include in the response. You can have max 20 keys. If not provided, no attributes will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactLinksBySegmentResponse
            Contact links generated successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_surveys_contact_links.get_contact_links_by_segment(
            survey_id="surveyId",
            segment_id="segmentId",
        )
        """
        _response = self._raw_client.get_contact_links_by_segment(
            survey_id,
            segment_id,
            limit=limit,
            skip=skip,
            expiration_days=expiration_days,
            attribute_keys=attribute_keys,
            request_options=request_options,
        )
        return _response.data


class AsyncManagementApiSurveysContactLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementApiSurveysContactLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementApiSurveysContactLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementApiSurveysContactLinksClient
        """
        return self._raw_client

    async def get_personalized_survey_link(
        self,
        survey_id: str,
        contact_id: str,
        *,
        expiration_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPersonalizedSurveyLinkResponse:
        """
        Retrieves a personalized link for a specific survey.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        contact_id : str
            The ID of the contact

        expiration_days : typing.Optional[int]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPersonalizedSurveyLinkResponse
            Personalized survey link retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_surveys_contact_links.get_personalized_survey_link(
                survey_id="surveyId",
                contact_id="contactId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_personalized_survey_link(
            survey_id, contact_id, expiration_days=expiration_days, request_options=request_options
        )
        return _response.data

    async def get_contact_links_by_segment(
        self,
        survey_id: str,
        segment_id: str,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        expiration_days: typing.Optional[float] = None,
        attribute_keys: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactLinksBySegmentResponse:
        """
        Generates personalized survey links for contacts in a segment.

        Parameters
        ----------
        survey_id : str
            The ID of the survey

        segment_id : str
            The ID of the segment

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        expiration_days : typing.Optional[float]
            Number of days until the generated JWT expires. If not provided, there is no expiration.

        attribute_keys : typing.Optional[str]
            Comma-separated list of contact attribute keys to include in the response. You can have max 20 keys. If not provided, no attributes will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactLinksBySegmentResponse
            Contact links generated successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_surveys_contact_links.get_contact_links_by_segment(
                survey_id="surveyId",
                segment_id="segmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contact_links_by_segment(
            survey_id,
            segment_id,
            limit=limit,
            skip=skip,
            expiration_days=expiration_days,
            attribute_keys=attribute_keys,
            request_options=request_options,
        )
        return _response.data
