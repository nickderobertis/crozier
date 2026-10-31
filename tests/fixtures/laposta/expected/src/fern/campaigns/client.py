

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.campaign_content import CampaignContent
from ..types.campaign_envelope import CampaignEnvelope
from ..types.campaign_list import CampaignList
from ..types.history import History
from .raw_client import AsyncRawCampaignsClient, RawCampaignsClient
from .types.campagnegeschiedenis_opvragen_request_order import CampagnegeschiedenisOpvragenRequestOrder


OMIT = typing.cast(typing.Any, ...)


class CampaignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCampaignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCampaignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCampaignsClient
        """
        return self._raw_client

    def alle_campagnes_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> CampaignList:
        """
        All campaigns in an array of campaign objects. The campaign objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.alle_campagnes_opvragen()
        """
        _response = self._raw_client.alle_campagnes_opvragen(request_options=request_options)
        return _response.data

    def campagne_aanmaken(
        self,
        *,
        type: str,
        name: str,
        subject: str,
        from_name: str,
        from_email: str,
        list_ids: typing.Dict[str, typing.Any],
        reply_to: typing.Optional[str] = OMIT,
        stats_ga: typing.Optional[str] = OMIT,
        stats_mtrack: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignEnvelope:
        """
        Creates a campaign. A campaign you create through the API can be filled with `/content` afterwards; campaigns built in the drag-and-drop editor cannot.

        Parameters
        ----------
        type : str
            Type of campaign (must be set to: regular)

        name : str
            A name for this campaign for internal use

        subject : str
            Subject line

        from_name : str
            The name of the sender

        from_email : str
            The email address of the sender (must be a sender address approved within the program)

        list_ids : typing.Dict[str, typing.Any]
            Recipients, array of list_ids and segment_ids if needed

        reply_to : typing.Optional[str]
            Email address for receiving replies

        stats_ga : typing.Optional[str]
            Link Google Analytics (true or false)

        stats_mtrack : typing.Optional[str]
            Link Mtrack (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_aanmaken(
            type="regular",
            name="Nieuwsbrief",
            subject="De nieuwsbrief van maart",
            from_name="Voorbeeld BV",
            from_email="nieuwsbrief@example.net",
            list_ids={"key": "value"},
        )
        """
        _response = self._raw_client.campagne_aanmaken(
            type=type,
            name=name,
            subject=subject,
            from_name=from_name,
            from_email=from_email,
            list_ids=list_ids,
            reply_to=reply_to,
            stats_ga=stats_ga,
            stats_mtrack=stats_mtrack,
            request_options=request_options,
        )
        return _response.data

    def campagne_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        All information about a campaign

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_opvragen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_opvragen(campaign_id, request_options=request_options)
        return _response.data

    def campagne_wijzigen(
        self,
        campaign_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        from_name: typing.Optional[str] = OMIT,
        from_email: typing.Optional[str] = OMIT,
        reply_to: typing.Optional[str] = OMIT,
        list_ids: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        stats_ga: typing.Optional[str] = OMIT,
        stats_mtrack: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignEnvelope:
        """
        You only have to submit the fields that require to be modified in the application. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        name : typing.Optional[str]
            A name for this campaign for internal use

        subject : typing.Optional[str]
            Subject line

        from_name : typing.Optional[str]
            The name of the sender

        from_email : typing.Optional[str]
            The email address of the sender (must be a sender address approved within the program)

        reply_to : typing.Optional[str]
            Email address for receiving replies

        list_ids : typing.Optional[typing.Dict[str, typing.Any]]
            Recipients, array of list_ids and segment_ids if needed

        stats_ga : typing.Optional[str]
            Link Google Analytics (true or false)

        stats_mtrack : typing.Optional[str]
            Link Mtrack (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_wijzigen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_wijzigen(
            campaign_id,
            name=name,
            subject=subject,
            from_name=from_name,
            from_email=from_email,
            reply_to=reply_to,
            list_ids=list_ids,
            stats_ga=stats_ga,
            stats_mtrack=stats_mtrack,
            request_options=request_options,
        )
        return _response.data

    def campagne_verwijderen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        This deletes a campaign. Unsent campaigns will be permanently deleted. Campaigns that have been sent are permanently deleted only after 180 days. In the meantime, they can be restored in the overview of campaigns in our program. In response you are shown another campaign object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the campaign.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_verwijderen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_verwijderen(campaign_id, request_options=request_options)
        return _response.data

    def campagne_content_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignContent:
        """
        Requesting the content of a campaign. Please note that this is only possible if it involves a campaign that has been exported, and not for a campaign created within the application using the drag & drop editor.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_content_opvragen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_content_opvragen(campaign_id, request_options=request_options)
        return _response.data

    def campagne_content_vullen(
        self,
        campaign_id: str,
        *,
        html: typing.Optional[str] = OMIT,
        import_url: typing.Optional[str] = OMIT,
        inline_css: typing.Optional[bool] = OMIT,
        javascript: typing.Optional[str] = OMIT,
        flash: typing.Optional[str] = OMIT,
        no_unsubscribe: typing.Optional[str] = OMIT,
        empty_unsubscribe: typing.Optional[str] = OMIT,
        css: typing.Optional[str] = OMIT,
        images: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Filling in the content of a campaign The campaign can either be filled directly with html, or through a URL, in which case Laposta imports the html found at the specified URL. One of the two must be chosen. If both parameters are given the html is taken. If the import fails, a 400 error message from the API will occur. If it does succeed in importing the html, but problems were found during the import, they are shown in the variable report in the response. These may include: Solving these problems is not necessary in order to properly send the newsletter, but it is highly recommended. In the case of a free account, our advertising is added to the bottom of the newsletter. If the offered html does not contain an unsubscribe link, it will simply be added by our program.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        html : typing.Optional[str]
            The html for the campaign

        import_url : typing.Optional[str]
            The URL from which the html must be imported

        inline_css : typing.Optional[bool]
            Potential inlining of css (true or false)

        javascript : typing.Optional[str]
            JavaScript was encountered

        flash : typing.Optional[str]
            Flash was encountered

        no_unsubscribe : typing.Optional[str]
            No unsubscribe could be located

        empty_unsubscribe : typing.Optional[str]
            Empty unsubscribe encountered

        css : typing.Optional[str]
            Missing external css files (listed)

        images : typing.Optional[str]
            Missing external images (listed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_content_vullen(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_content_vullen(
            campaign_id,
            html=html,
            import_url=import_url,
            inline_css=inline_css,
            javascript=javascript,
            flash=flash,
            no_unsubscribe=no_unsubscribe,
            empty_unsubscribe=empty_unsubscribe,
            css=css,
            images=images,
            request_options=request_options,
        )
        return _response.data

    def campagne_testen(
        self, campaign_id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Sending a test mail Note: only in the case of a campaign for which there already is content, but which has not yet been sent, is it possible for a test email to be sent.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        email : str
            The email address to which the test should be sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_testen(
            campaign_id="njhgaf61ye",
            email="relatie@example.net",
        )
        """
        _response = self._raw_client.campagne_testen(campaign_id, email=email, request_options=request_options)
        return _response.data

    def campagne_inplannen(
        self, campaign_id: str, *, delivery_requested: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Schedules the campaign for a moment in the future. You cancel a scheduled campaign by deleting it.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        delivery_requested : str
            The time and date of sending. Use the regular format or ISO format described above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_inplannen(
            campaign_id="njhgaf61ye",
            delivery_requested="2026-05-18 14:30:00",
        )
        """
        _response = self._raw_client.campagne_inplannen(
            campaign_id, delivery_requested=delivery_requested, request_options=request_options
        )
        return _response.data

    def campagne_verzenden(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Sends the campaign to all connected lists and segments right away. This call cannot be undone, and it is not blocked when the campaign was already sent: a second call starts delivery again.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagne_verzenden(
            campaign_id="njhgaf61ye",
        )
        """
        _response = self._raw_client.campagne_verzenden(campaign_id, request_options=request_options)
        return _response.data

    def campagnegeschiedenis_opvragen(
        self,
        campaign_id: str,
        *,
        event_date_from: typing.Optional[str] = None,
        event_date_to: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        order: typing.Optional[CampagnegeschiedenisOpvragenRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> History:
        """
        The full event history of a campaign. A campaign can contain many events; use pagination to retrieve additional pages.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        event_date_from : typing.Optional[str]
            Only return events from this date and time, inclusive. Use the regular format or ISO format described above.

        event_date_to : typing.Optional[str]
            Only return events before this date and time, exclusive. Use the regular format or ISO format described above.

        limit : typing.Optional[int]
            Maximum number of history items to return. Default is 100, maximum is 1000

        cursor : typing.Optional[str]
            Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.

        order_by : typing.Optional[str]
            Field to order by. Currently only event_date is supported

        order : typing.Optional[CampagnegeschiedenisOpvragenRequestOrder]
            Sort direction: desc or asc. Default is desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        History
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.campaigns.campagnegeschiedenis_opvragen(
            campaign_id="njhgaf61ye",
            event_date_from="2026-04-01 00:00:00",
            event_date_to="2026-05-01 00:00:00",
            cursor="opaque_cursor_value",
            order_by="event_date",
        )
        """
        _response = self._raw_client.campagnegeschiedenis_opvragen(
            campaign_id,
            event_date_from=event_date_from,
            event_date_to=event_date_to,
            limit=limit,
            cursor=cursor,
            order_by=order_by,
            order=order,
            request_options=request_options,
        )
        return _response.data


class AsyncCampaignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCampaignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCampaignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCampaignsClient
        """
        return self._raw_client

    async def alle_campagnes_opvragen(self, *, request_options: typing.Optional[RequestOptions] = None) -> CampaignList:
        """
        All campaigns in an array of campaign objects. The campaign objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignList
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.alle_campagnes_opvragen()


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_campagnes_opvragen(request_options=request_options)
        return _response.data

    async def campagne_aanmaken(
        self,
        *,
        type: str,
        name: str,
        subject: str,
        from_name: str,
        from_email: str,
        list_ids: typing.Dict[str, typing.Any],
        reply_to: typing.Optional[str] = OMIT,
        stats_ga: typing.Optional[str] = OMIT,
        stats_mtrack: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignEnvelope:
        """
        Creates a campaign. A campaign you create through the API can be filled with `/content` afterwards; campaigns built in the drag-and-drop editor cannot.

        Parameters
        ----------
        type : str
            Type of campaign (must be set to: regular)

        name : str
            A name for this campaign for internal use

        subject : str
            Subject line

        from_name : str
            The name of the sender

        from_email : str
            The email address of the sender (must be a sender address approved within the program)

        list_ids : typing.Dict[str, typing.Any]
            Recipients, array of list_ids and segment_ids if needed

        reply_to : typing.Optional[str]
            Email address for receiving replies

        stats_ga : typing.Optional[str]
            Link Google Analytics (true or false)

        stats_mtrack : typing.Optional[str]
            Link Mtrack (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_aanmaken(
                type="regular",
                name="Nieuwsbrief",
                subject="De nieuwsbrief van maart",
                from_name="Voorbeeld BV",
                from_email="nieuwsbrief@example.net",
                list_ids={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_aanmaken(
            type=type,
            name=name,
            subject=subject,
            from_name=from_name,
            from_email=from_email,
            list_ids=list_ids,
            reply_to=reply_to,
            stats_ga=stats_ga,
            stats_mtrack=stats_mtrack,
            request_options=request_options,
        )
        return _response.data

    async def campagne_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        All information about a campaign

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_opvragen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_opvragen(campaign_id, request_options=request_options)
        return _response.data

    async def campagne_wijzigen(
        self,
        campaign_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        from_name: typing.Optional[str] = OMIT,
        from_email: typing.Optional[str] = OMIT,
        reply_to: typing.Optional[str] = OMIT,
        list_ids: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        stats_ga: typing.Optional[str] = OMIT,
        stats_mtrack: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignEnvelope:
        """
        You only have to submit the fields that require to be modified in the application. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        name : typing.Optional[str]
            A name for this campaign for internal use

        subject : typing.Optional[str]
            Subject line

        from_name : typing.Optional[str]
            The name of the sender

        from_email : typing.Optional[str]
            The email address of the sender (must be a sender address approved within the program)

        reply_to : typing.Optional[str]
            Email address for receiving replies

        list_ids : typing.Optional[typing.Dict[str, typing.Any]]
            Recipients, array of list_ids and segment_ids if needed

        stats_ga : typing.Optional[str]
            Link Google Analytics (true or false)

        stats_mtrack : typing.Optional[str]
            Link Mtrack (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_wijzigen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_wijzigen(
            campaign_id,
            name=name,
            subject=subject,
            from_name=from_name,
            from_email=from_email,
            reply_to=reply_to,
            list_ids=list_ids,
            stats_ga=stats_ga,
            stats_mtrack=stats_mtrack,
            request_options=request_options,
        )
        return _response.data

    async def campagne_verwijderen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        This deletes a campaign. Unsent campaigns will be permanently deleted. Campaigns that have been sent are permanently deleted only after 180 days. In the meantime, they can be restored in the overview of campaigns in our program. In response you are shown another campaign object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the campaign.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_verwijderen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_verwijderen(campaign_id, request_options=request_options)
        return _response.data

    async def campagne_content_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignContent:
        """
        Requesting the content of a campaign. Please note that this is only possible if it involves a campaign that has been exported, and not for a campaign created within the application using the drag & drop editor.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_content_opvragen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_content_opvragen(campaign_id, request_options=request_options)
        return _response.data

    async def campagne_content_vullen(
        self,
        campaign_id: str,
        *,
        html: typing.Optional[str] = OMIT,
        import_url: typing.Optional[str] = OMIT,
        inline_css: typing.Optional[bool] = OMIT,
        javascript: typing.Optional[str] = OMIT,
        flash: typing.Optional[str] = OMIT,
        no_unsubscribe: typing.Optional[str] = OMIT,
        empty_unsubscribe: typing.Optional[str] = OMIT,
        css: typing.Optional[str] = OMIT,
        images: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CampaignContent:
        """
        Filling in the content of a campaign The campaign can either be filled directly with html, or through a URL, in which case Laposta imports the html found at the specified URL. One of the two must be chosen. If both parameters are given the html is taken. If the import fails, a 400 error message from the API will occur. If it does succeed in importing the html, but problems were found during the import, they are shown in the variable report in the response. These may include: Solving these problems is not necessary in order to properly send the newsletter, but it is highly recommended. In the case of a free account, our advertising is added to the bottom of the newsletter. If the offered html does not contain an unsubscribe link, it will simply be added by our program.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        html : typing.Optional[str]
            The html for the campaign

        import_url : typing.Optional[str]
            The URL from which the html must be imported

        inline_css : typing.Optional[bool]
            Potential inlining of css (true or false)

        javascript : typing.Optional[str]
            JavaScript was encountered

        flash : typing.Optional[str]
            Flash was encountered

        no_unsubscribe : typing.Optional[str]
            No unsubscribe could be located

        empty_unsubscribe : typing.Optional[str]
            Empty unsubscribe encountered

        css : typing.Optional[str]
            Missing external css files (listed)

        images : typing.Optional[str]
            Missing external images (listed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignContent
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_content_vullen(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_content_vullen(
            campaign_id,
            html=html,
            import_url=import_url,
            inline_css=inline_css,
            javascript=javascript,
            flash=flash,
            no_unsubscribe=no_unsubscribe,
            empty_unsubscribe=empty_unsubscribe,
            css=css,
            images=images,
            request_options=request_options,
        )
        return _response.data

    async def campagne_testen(
        self, campaign_id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Sending a test mail Note: only in the case of a campaign for which there already is content, but which has not yet been sent, is it possible for a test email to be sent.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        email : str
            The email address to which the test should be sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_testen(
                campaign_id="njhgaf61ye",
                email="relatie@example.net",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_testen(campaign_id, email=email, request_options=request_options)
        return _response.data

    async def campagne_inplannen(
        self, campaign_id: str, *, delivery_requested: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Schedules the campaign for a moment in the future. You cancel a scheduled campaign by deleting it.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        delivery_requested : str
            The time and date of sending. Use the regular format or ISO format described above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_inplannen(
                campaign_id="njhgaf61ye",
                delivery_requested="2026-05-18 14:30:00",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_inplannen(
            campaign_id, delivery_requested=delivery_requested, request_options=request_options
        )
        return _response.data

    async def campagne_verzenden(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CampaignEnvelope:
        """
        Sends the campaign to all connected lists and segments right away. This call cannot be undone, and it is not blocked when the campaign was already sent: a second call starts delivery again.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CampaignEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagne_verzenden(
                campaign_id="njhgaf61ye",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagne_verzenden(campaign_id, request_options=request_options)
        return _response.data

    async def campagnegeschiedenis_opvragen(
        self,
        campaign_id: str,
        *,
        event_date_from: typing.Optional[str] = None,
        event_date_to: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        order: typing.Optional[CampagnegeschiedenisOpvragenRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> History:
        """
        The full event history of a campaign. A campaign can contain many events; use pagination to retrieve additional pages.

        Parameters
        ----------
        campaign_id : str
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        event_date_from : typing.Optional[str]
            Only return events from this date and time, inclusive. Use the regular format or ISO format described above.

        event_date_to : typing.Optional[str]
            Only return events before this date and time, exclusive. Use the regular format or ISO format described above.

        limit : typing.Optional[int]
            Maximum number of history items to return. Default is 100, maximum is 1000

        cursor : typing.Optional[str]
            Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.

        order_by : typing.Optional[str]
            Field to order by. Currently only event_date is supported

        order : typing.Optional[CampagnegeschiedenisOpvragenRequestOrder]
            Sort direction: desc or asc. Default is desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        History
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.campaigns.campagnegeschiedenis_opvragen(
                campaign_id="njhgaf61ye",
                event_date_from="2026-04-01 00:00:00",
                event_date_to="2026-05-01 00:00:00",
                cursor="opaque_cursor_value",
                order_by="event_date",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.campagnegeschiedenis_opvragen(
            campaign_id,
            event_date_from=event_date_from,
            event_date_to=event_date_to,
            limit=limit,
            cursor=cursor,
            order_by=order_by,
            order=order,
            request_options=request_options,
        )
        return _response.data
