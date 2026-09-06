

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.patch_links_bundle_id_links_request_body_item import PatchLinksBundleIdLinksRequestBodyItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLinkBundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_bundle_templates(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Returns all available bundle templates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/bundle/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_bundle_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns bundle details by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_bundle(
        self,
        id: str,
        *,
        domain_id: typing.Optional[float] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates bundle details, social media links, and branding

        Parameters
        ----------
        id : str
            Bundle ULID id

        domain_id : typing.Optional[float]

        template_id : typing.Optional[str]
            Template ID

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="PUT",
            json={
                "DomainId": domain_id,
                "TemplateId": template_id,
                "title": title,
                "description": description,
                "logoURL": logo_url,
                "backgroundImageURL": background_image_url,
                "twitterUsername": twitter_username,
                "fbUsername": fb_username,
                "linkedinCompanyname": linkedin_companyname,
                "linkedinUsername": linkedin_username,
                "instagramUsername": instagram_username,
                "whatsappURL": whatsapp_url,
                "viberURL": viber_url,
                "telegramURL": telegram_url,
                "threadsUsername": threads_username,
                "mastodonUsername": mastodon_username,
                "blueskyUsername": bluesky_username,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_bundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Deletes a bundle by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upload_bundle_logo(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Uploads a logo image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/photo",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upload_bundle_background_image(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Uploads a background image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/background-image",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_bundle(
        self,
        *,
        domain_id: float,
        template_id: str,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates a new link bundle with customizable template, social media links, and branding

        Parameters
        ----------
        domain_id : float
            Domain ID where the bundle will be created

        template_id : str
            Template ID from available templates

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/bundle",
            method="POST",
            json={
                "DomainId": domain_id,
                "TemplateId": template_id,
                "title": title,
                "description": description,
                "logoURL": logo_url,
                "backgroundImageURL": background_image_url,
                "twitterUsername": twitter_username,
                "fbUsername": fb_username,
                "linkedinCompanyname": linkedin_companyname,
                "linkedinUsername": linkedin_username,
                "instagramUsername": instagram_username,
                "whatsappURL": whatsapp_url,
                "viberURL": viber_url,
                "telegramURL": telegram_url,
                "threadsUsername": threads_username,
                "mastodonUsername": mastodon_username,
                "blueskyUsername": bluesky_username,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_bundle_links(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns all links in a bundle, ordered by sort order

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_link_to_bundle(
        self, id: str, *, path: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Adds a short link to a bundle. If the link doesn't exist, it will be created.

        Parameters
        ----------
        id : str
            Bundle ULID id

        path : str
            Short link path or full URL

        title : str
            Display title for the link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="POST",
            json={
                "path": path,
                "title": title,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_link_sort_order(
        self,
        id: str,
        *,
        request: typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the sort order of links in a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_link_from_bundle(
        self, id: str, link_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Removes a link from a bundle by its link template ID

        Parameters
        ----------
        id : str
            Bundle ULID id

        link_template_id : str
            Link template ID to remove

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links/{encode_path_param(link_template_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLinkBundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_bundle_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns all available bundle templates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/bundle/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_bundle_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns bundle details by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_bundle(
        self,
        id: str,
        *,
        domain_id: typing.Optional[float] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates bundle details, social media links, and branding

        Parameters
        ----------
        id : str
            Bundle ULID id

        domain_id : typing.Optional[float]

        template_id : typing.Optional[str]
            Template ID

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="PUT",
            json={
                "DomainId": domain_id,
                "TemplateId": template_id,
                "title": title,
                "description": description,
                "logoURL": logo_url,
                "backgroundImageURL": background_image_url,
                "twitterUsername": twitter_username,
                "fbUsername": fb_username,
                "linkedinCompanyname": linkedin_companyname,
                "linkedinUsername": linkedin_username,
                "instagramUsername": instagram_username,
                "whatsappURL": whatsapp_url,
                "viberURL": viber_url,
                "telegramURL": telegram_url,
                "threadsUsername": threads_username,
                "mastodonUsername": mastodon_username,
                "blueskyUsername": bluesky_username,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_bundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a bundle by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upload_bundle_logo(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Uploads a logo image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/photo",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upload_bundle_background_image(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Uploads a background image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/background-image",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_bundle(
        self,
        *,
        domain_id: float,
        template_id: str,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates a new link bundle with customizable template, social media links, and branding

        Parameters
        ----------
        domain_id : float
            Domain ID where the bundle will be created

        template_id : str
            Template ID from available templates

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/bundle",
            method="POST",
            json={
                "DomainId": domain_id,
                "TemplateId": template_id,
                "title": title,
                "description": description,
                "logoURL": logo_url,
                "backgroundImageURL": background_image_url,
                "twitterUsername": twitter_username,
                "fbUsername": fb_username,
                "linkedinCompanyname": linkedin_companyname,
                "linkedinUsername": linkedin_username,
                "instagramUsername": instagram_username,
                "whatsappURL": whatsapp_url,
                "viberURL": viber_url,
                "telegramURL": telegram_url,
                "threadsUsername": threads_username,
                "mastodonUsername": mastodon_username,
                "blueskyUsername": bluesky_username,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_bundle_links(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns all links in a bundle, ordered by sort order

        Parameters
        ----------
        id : str
            Bundle ULID id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_link_to_bundle(
        self, id: str, *, path: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Adds a short link to a bundle. If the link doesn't exist, it will be created.

        Parameters
        ----------
        id : str
            Bundle ULID id

        path : str
            Short link path or full URL

        title : str
            Display title for the link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="POST",
            json={
                "path": path,
                "title": title,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_link_sort_order(
        self,
        id: str,
        *,
        request: typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the sort order of links in a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_link_from_bundle(
        self, id: str, link_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Removes a link from a bundle by its link template ID

        Parameters
        ----------
        id : str
            Bundle ULID id

        link_template_id : str
            Link template ID to remove

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/bundle/{encode_path_param(id)}/links/{encode_path_param(link_template_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
