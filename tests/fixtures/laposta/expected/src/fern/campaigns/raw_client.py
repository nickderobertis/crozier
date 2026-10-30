

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.campaign_content import CampaignContent
from ..types.campaign_envelope import CampaignEnvelope
from ..types.campaign_list import CampaignList
from ..types.error import Error
from ..types.history import History
from .types.campagnegeschiedenis_opvragen_request_order import CampagnegeschiedenisOpvragenRequestOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCampaignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alle_campagnes_opvragen(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignList]:
        """
        All campaigns in an array of campaign objects. The campaign objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CampaignList]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "campaign",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignList,
                    parse_obj_as(
                        type_=CampaignList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "campaign",
            method="POST",
            data={
                "type": type,
                "name": name,
                "subject": subject,
                "from[name]": from_name,
                "from[email]": from_email,
                "reply_to": reply_to,
                "list_ids": list_ids,
                "stats[ga]": stats_ga,
                "stats[mtrack]": stats_mtrack,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="POST",
            data={
                "name": name,
                "subject": subject,
                "from[name]": from_name,
                "from[email]": from_email,
                "reply_to": reply_to,
                "list_ids": list_ids,
                "stats[ga]": stats_ga,
                "stats[mtrack]": stats_mtrack,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_verwijderen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_content_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignContent]:
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
        HttpResponse[CampaignContent]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignContent,
                    parse_obj_as(
                        type_=CampaignContent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> HttpResponse[CampaignContent]:
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
        HttpResponse[CampaignContent]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/content",
            method="POST",
            data={
                "html": html,
                "import_url": import_url,
                "inline_css": inline_css,
                "javascript": javascript,
                "flash": flash,
                "no_unsubscribe": no_unsubscribe,
                "empty_unsubscribe": empty_unsubscribe,
                "css": css,
                "images": images,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignContent,
                    parse_obj_as(
                        type_=CampaignContent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_testen(
        self, campaign_id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/testmail",
            method="POST",
            data={
                "email": email,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_inplannen(
        self, campaign_id: str, *, delivery_requested: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/schedule",
            method="POST",
            data={
                "delivery_requested": delivery_requested,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def campagne_verzenden(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CampaignEnvelope]:
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
        HttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/send",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> HttpResponse[History]:
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
        HttpResponse[History]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/history",
            method="GET",
            params={
                "event_date_from": event_date_from,
                "event_date_to": event_date_to,
                "limit": limit,
                "cursor": cursor,
                "order_by": order_by,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    History,
                    parse_obj_as(
                        type_=History,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawCampaignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def alle_campagnes_opvragen(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignList]:
        """
        All campaigns in an array of campaign objects. The campaign objects have been ordered in an array with the name 'data'.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CampaignList]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "campaign",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignList,
                    parse_obj_as(
                        type_=CampaignList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "campaign",
            method="POST",
            data={
                "type": type,
                "name": name,
                "subject": subject,
                "from[name]": from_name,
                "from[email]": from_email,
                "reply_to": reply_to,
                "list_ids": list_ids,
                "stats[ga]": stats_ga,
                "stats[mtrack]": stats_mtrack,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="POST",
            data={
                "name": name,
                "subject": subject,
                "from[name]": from_name,
                "from[email]": from_email,
                "reply_to": reply_to,
                "list_ids": list_ids,
                "stats[ga]": stats_ga,
                "stats[mtrack]": stats_mtrack,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_verwijderen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_content_opvragen(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignContent]:
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
        AsyncHttpResponse[CampaignContent]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignContent,
                    parse_obj_as(
                        type_=CampaignContent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> AsyncHttpResponse[CampaignContent]:
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
        AsyncHttpResponse[CampaignContent]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/content",
            method="POST",
            data={
                "html": html,
                "import_url": import_url,
                "inline_css": inline_css,
                "javascript": javascript,
                "flash": flash,
                "no_unsubscribe": no_unsubscribe,
                "empty_unsubscribe": empty_unsubscribe,
                "css": css,
                "images": images,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignContent,
                    parse_obj_as(
                        type_=CampaignContent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_testen(
        self, campaign_id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/testmail",
            method="POST",
            data={
                "email": email,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_inplannen(
        self, campaign_id: str, *, delivery_requested: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/schedule",
            method="POST",
            data={
                "delivery_requested": delivery_requested,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def campagne_verzenden(
        self, campaign_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CampaignEnvelope]:
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
        AsyncHttpResponse[CampaignEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/action/send",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CampaignEnvelope,
                    parse_obj_as(
                        type_=CampaignEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
    ) -> AsyncHttpResponse[History]:
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
        AsyncHttpResponse[History]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"campaign/{encode_path_param(campaign_id)}/history",
            method="GET",
            params={
                "event_date_from": event_date_from,
                "event_date_to": event_date_to,
                "limit": limit,
                "cursor": cursor,
                "order_by": order_by,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    History,
                    parse_obj_as(
                        type_=History,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
