

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.custom_profile_field_data_schema import CustomProfileFieldDataSchema
from ..types.custom_profile_field_display_in_profile_summary_schema import (
    CustomProfileFieldDisplayInProfileSummarySchema,
)
from ..types.custom_profile_field_editable_by_user_schema import CustomProfileFieldEditableByUserSchema
from ..types.custom_profile_field_hint_schema import CustomProfileFieldHintSchema
from ..types.custom_profile_field_required_schema import CustomProfileFieldRequiredSchema
from ..types.custom_profile_field_use_for_user_matching_schema import CustomProfileFieldUseForUserMatchingSchema
from ..types.ignored_parameters_success import IgnoredParametersSuccess
from ..types.json_success import JsonSuccess
from ..types.linkifier_pattern import LinkifierPattern
from ..types.linkifier_url_template import LinkifierUrlTemplate
from .types.add_code_playground_response import AddCodePlaygroundResponse
from .types.add_linkifier_response import AddLinkifierResponse
from .types.add_realm_domain_response import AddRealmDomainResponse
from .types.create_custom_profile_field_response import CreateCustomProfileFieldResponse
from .types.export_realm_request_export_type import ExportRealmRequestExportType
from .types.export_realm_response import ExportRealmResponse
from .types.get_custom_emoji_response import GetCustomEmojiResponse
from .types.get_custom_profile_fields_response import GetCustomProfileFieldsResponse
from .types.get_linkifiers_response import GetLinkifiersResponse
from .types.get_presence_response import GetPresenceResponse
from .types.get_realm_domains_response import GetRealmDomainsResponse
from .types.get_realm_export_consents_response import GetRealmExportConsentsResponse
from .types.get_realm_exports_response import GetRealmExportsResponse
from .types.get_server_settings_response import GetServerSettingsResponse
from .types.test_welcome_bot_custom_message_response import TestWelcomeBotCustomMessageResponse
from .types.update_realm_user_settings_defaults_request_resolved_topic_notice_auto_read_policy import (
    UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy,
)
from .types.update_realm_user_settings_defaults_request_web_animate_image_previews import (
    UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawServerAndOrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_custom_emoji(
        self,
        emoji_name: str,
        *,
        filename: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        This endpoint is used to upload a custom emoji for use in the user's
        organization. Access to this endpoint depends on the
        [organization's configuration](https://zulip.com/help/custom-emoji#change-who-can-add-custom-emoji).

        Parameters
        ----------
        emoji_name : str
            The name that should be associated with the uploaded emoji image/gif.
            The emoji name can only contain letters, numbers, dashes, and spaces.
            Upper and lower case letters are treated the same, and underscores (\\_)
            are treated the same as spaces (consistent with how the Zulip UI
            handles emoji).

        filename : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/emoji/{encode_path_param(emoji_name)}",
            method="POST",
            data={},
            files={
                **({"filename": filename} if filename is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deactivate_custom_emoji(
        self, emoji_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        [Deactivate a custom emoji](/help/custom-emoji#deactivate-custom-emoji) from
        the user's organization.

        Users can only deactivate custom emoji that they added themselves except for
        organization administrators, who can deactivate any custom emoji.

        Note that deactivated emoji will still be visible in old messages, reactions,
        user statuses and channel descriptions.

        **Changes**: Before Zulip 8.0 (feature level 190), this endpoint returned an
        HTTP status code of 400 when the emoji did not exist, instead of 404.

        Parameters
        ----------
        emoji_name : str
            The name of the custom emoji to deactivate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/emoji/{encode_path_param(emoji_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_custom_emoji(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCustomEmojiResponse]:
        """
        Get all the custom emoji in the user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomEmojiResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/emoji",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomEmojiResponse,
                    parse_obj_as(
                        type_=GetCustomEmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_presence(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPresenceResponse]:
        """
        Get the presence information of all the users in an organization.

        If the `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level
        setting is set to `true`, presence information of only accessible
        users are returned.

        Complete Zulip apps are recommended to fetch presence
        information when they post their own state using the [`POST
        /presence`](/api/update-presence) API endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPresenceResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/presence",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPresenceResponse,
                    parse_obj_as(
                        type_=GetPresenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_realm_domains(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRealmDomainsResponse]:
        """
        Get the set of allowed domains configured in the organization for user
        account email addresses.

        As each Zulip user account is associated with an email address, organization
        owners can [restrict new account creation (and email
        changes)](/help/restrict-account-creation) to email addresses with these
        domains.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRealmDomainsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmDomainsResponse,
                    parse_obj_as(
                        type_=GetRealmDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_realm_domain(
        self, *, domain: str, allow_subdomains: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddRealmDomainResponse]:
        """
        Add a domain to the set of allowed domains configured in the organization
        for [user account email addresses](/help/restrict-account-creation).

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The new domain.

            **Changes**: In Zulip 4.0 (feature level 63), the unnecessary
            JSON-encoding of this parameter was removed.

        allow_subdomains : bool
            Whether subdomains are allowed for this domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddRealmDomainResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/domains",
            method="POST",
            data={
                "domain": domain,
                "allow_subdomains": allow_subdomains,
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
                    AddRealmDomainResponse,
                    parse_obj_as(
                        type_=AddRealmDomainResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_realm_domain(
        self, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Remove the specified domain from the set of allowed domains configured in
        the organization for [user account email addresses](/help/restrict-account-creation).

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The domain to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/domains/{encode_path_param(domain)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_realm_domain(
        self, domain: str, *, allow_subdomains: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Update whether subdomains are allowed in [user account email
        addresses](/help/restrict-account-creation) for the specified domain.

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The domain to update.

        allow_subdomains : bool
            Whether subdomains are allowed for this domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/domains/{encode_path_param(domain)}",
            method="PATCH",
            data={
                "allow_subdomains": allow_subdomains,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deactivate_realm(
        self,
        *,
        deletion_delay_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        [Deactivate an organization](/help/deactivate-your-organization) on the
        Zulip server. Deactivating an organization immediately logs out all of
        its users and prevents them from logging in again.

        A deactivated organization can be reactivated via a [management
        command](https://zulip.readthedocs.io/en/latest/production/management-commands.html),
        unless its data has been permanently deleted (see the
        [`deletion_delay_days` parameter](/api/deactivate-realm#parameter-deletion_delay_days)
        below).

        This endpoint is primarily useful for Zulip servers that host
        [multiple organizations](https://zulip.readthedocs.io/en/latest/production/multiple-organizations.html).

        Parameters
        ----------
        deletion_delay_days : typing.Optional[int]
            The number of days to wait before permanently deleting all
            of the deactivated organization's data (users, channels,
            messages, etc.).

            A value of `0` will delete the organization's data
            immediately, which means that the organization cannot be
            reactivated. A `null` value indicates that the organization's
            data will not be deleted, but rather retained indefinitely.

            Valid values for this parameter are limited to the range
            permitted by the server, indicated by the
            `server_min_deactivated_realm_deletion_days` and
            `server_max_deactivated_realm_deletion_days` fields in the
            [`POST /register`](/api/register-queue) response. A value of
            `null` is only permitted when
            `server_max_deactivated_realm_deletion_days` is `null`. A
            value of `0` is only permitted when
            `server_min_deactivated_realm_deletion_days` is `null`.

            These limits do not apply to
            [Zulip Cloud demo organizations](/help/demo-organizations),
            for which this parameter is instead required: it must be `0`
            when the organization owner has not configured an email
            address, and otherwise must not exceed the number of days
            remaining before the demo organization's scheduled deletion.

            **Changes**: New in Zulip 10.0 (feature level 332).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/deactivate",
            method="POST",
            data={
                "deletion_delay_days": deletion_delay_days,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_custom_profile_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCustomProfileFieldsResponse]:
        """
        Get all the [custom profile fields](/help/custom-profile-fields)
        configured for the user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomProfileFieldsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomProfileFieldsResponse,
                    parse_obj_as(
                        type_=GetCustomProfileFieldsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_custom_profile_field(
        self,
        *,
        field_type: int,
        name: typing.Optional[str] = OMIT,
        hint: typing.Optional[CustomProfileFieldHintSchema] = OMIT,
        field_data: typing.Optional[CustomProfileFieldDataSchema] = OMIT,
        display_in_profile_summary: typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema] = OMIT,
        required: typing.Optional[CustomProfileFieldRequiredSchema] = OMIT,
        editable_by_user: typing.Optional[CustomProfileFieldEditableByUserSchema] = OMIT,
        use_for_user_matching: typing.Optional[CustomProfileFieldUseForUserMatchingSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCustomProfileFieldResponse]:
        """
        [Create a custom profile field](/help/custom-profile-fields#add-a-custom-profile-field) in the user's organization.

        Parameters
        ----------
        field_type : int
            The field type can be any of the supported custom profile field types. See the
            [custom profile fields documentation](/help/custom-profile-fields)
            for more details on what each type means.

            - **1**: Short text
            - **2**: Paragraph
            - **3**: Dropdown
            - **4**: Date
            - **5**: Link
            - **6**: Users
            - **7**: External account
            - **8**: Pronouns

            **Changes**: Field type `8` added in Zulip 6.0 (feature level 151).

        name : typing.Optional[str]
            The name of the custom profile field, which appears both in
            the user-facing settings UI for configuring the custom profile
            fields and in the UI displaying a user's profile.

        hint : typing.Optional[CustomProfileFieldHintSchema]

        field_data : typing.Optional[CustomProfileFieldDataSchema]

        display_in_profile_summary : typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema]

        required : typing.Optional[CustomProfileFieldRequiredSchema]

        editable_by_user : typing.Optional[CustomProfileFieldEditableByUserSchema]

        use_for_user_matching : typing.Optional[CustomProfileFieldUseForUserMatchingSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCustomProfileFieldResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="POST",
            data={
                "name": name,
                "field_type": field_type,
                "hint": hint,
                "field_data": field_data,
                "display_in_profile_summary": display_in_profile_summary,
                "required": required,
                "editable_by_user": editable_by_user,
                "use_for_user_matching": use_for_user_matching,
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
                    CreateCustomProfileFieldResponse,
                    parse_obj_as(
                        type_=CreateCustomProfileFieldResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reorder_custom_profile_fields(
        self, *, order: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Reorder the custom profile fields in the user's organization.

        Custom profile fields are displayed in Zulip UI widgets in order; this
        endpoint allows administrative settings UI to change the field ordering.

        This endpoint is used to implement the dragging feature described in the
        [custom profile fields documentation](/help/custom-profile-fields).

        Parameters
        ----------
        order : typing.Sequence[int]
            A list of the IDs of all the custom profile fields defined in this
            organization, in the desired new order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="PATCH",
            data={
                "order": order,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_custom_profile_field(
        self, field_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete a [custom profile field](/help/custom-profile-fields) in
        the user's organization.

        This will also permanently delete any value configured for the
        custom profile field from every user profile in the database.
        Therefore, it's recommended that clients warn the active user of
        the related data removal before submitting the request, e.g.,
        notify them of how many users will have their profile data
        deleted as a result of deleting the custom profile field.

        Parameters
        ----------
        field_id : int
            The ID of the target custom profile field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/profile_fields/{encode_path_param(field_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_custom_profile_field(
        self,
        field_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        hint: typing.Optional[CustomProfileFieldHintSchema] = OMIT,
        field_data: typing.Optional[CustomProfileFieldDataSchema] = OMIT,
        display_in_profile_summary: typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema] = OMIT,
        required: typing.Optional[CustomProfileFieldRequiredSchema] = OMIT,
        editable_by_user: typing.Optional[CustomProfileFieldEditableByUserSchema] = OMIT,
        use_for_user_matching: typing.Optional[CustomProfileFieldUseForUserMatchingSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Update the configuration of a
        [custom profile field](/help/custom-profile-fields) in the user's
        organization.

        The [type](/api/create-custom-profile-field#parameter-field_type)
        of a custom profile field cannot be changed.

        At most, 2 custom profile fields can have
        [`display_in_profile_summary`](/api/update-custom-profile-field#parameter-display_in_profile_summary)
        set to `true` in an organization.

        For custom profile fields with type 7 (External account) that use
        one of Zulip's configured default external account providers
        (e.g., GitHub, LinkedIn, etc.), the field's
        [`name`](/api/update-custom-profile-field#parameter-name),
        [`hint`](/api/update-custom-profile-field#parameter-hint), and
        [`field_data`](/api/update-custom-profile-field#parameter-field_data)
        cannot be changed, and attempting to do so will return an error.

        **Changes**: Before Zulip 9.0 (feature level 252), the `name`,
        `hint`, `field_data`, `required` and `display_in_profile_summary`
        parameters were all required in every request, even when their
        values were unchanged.

        Parameters
        ----------
        field_id : int
            The ID of the target custom profile field.

        name : typing.Optional[str]
            The name of the custom profile field, which appears both in
            the user-facing settings UI for configuring the custom profile
            fields and in the UI displaying a user's profile.

        hint : typing.Optional[CustomProfileFieldHintSchema]

        field_data : typing.Optional[CustomProfileFieldDataSchema]

        display_in_profile_summary : typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema]

        required : typing.Optional[CustomProfileFieldRequiredSchema]

        editable_by_user : typing.Optional[CustomProfileFieldEditableByUserSchema]

        use_for_user_matching : typing.Optional[CustomProfileFieldUseForUserMatchingSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/profile_fields/{encode_path_param(field_id)}",
            method="PATCH",
            data={
                "name": name,
                "hint": hint,
                "field_data": field_data,
                "display_in_profile_summary": display_in_profile_summary,
                "required": required,
                "editable_by_user": editable_by_user,
                "use_for_user_matching": use_for_user_matching,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_realm_user_settings_defaults(
        self,
        *,
        starred_message_counts: typing.Optional[bool] = OMIT,
        receives_typing_notifications: typing.Optional[bool] = OMIT,
        web_suggest_update_timezone: typing.Optional[bool] = OMIT,
        fluid_layout_width: typing.Optional[bool] = OMIT,
        high_contrast_mode: typing.Optional[bool] = OMIT,
        web_mark_read_on_scroll_policy: typing.Optional[int] = OMIT,
        web_channel_default_view: typing.Optional[int] = OMIT,
        web_font_size_px: typing.Optional[int] = OMIT,
        web_line_height_percent: typing.Optional[int] = OMIT,
        color_scheme: typing.Optional[int] = OMIT,
        enable_drafts_synchronization: typing.Optional[bool] = OMIT,
        translate_emoticons: typing.Optional[bool] = OMIT,
        display_emoji_reaction_users: typing.Optional[bool] = OMIT,
        web_home_view: typing.Optional[str] = OMIT,
        web_escape_navigates_to_home_view: typing.Optional[bool] = OMIT,
        left_side_userlist: typing.Optional[bool] = OMIT,
        emojiset: typing.Optional[str] = OMIT,
        demote_inactive_streams: typing.Optional[int] = OMIT,
        user_list_style: typing.Optional[int] = OMIT,
        web_animate_image_previews: typing.Optional[
            UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews
        ] = OMIT,
        web_stream_unreads_count_display_policy: typing.Optional[int] = OMIT,
        hide_ai_features: typing.Optional[bool] = OMIT,
        web_inbox_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_unreads_count_summary: typing.Optional[bool] = OMIT,
        enable_stream_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_stream_email_notifications: typing.Optional[bool] = OMIT,
        enable_stream_push_notifications: typing.Optional[bool] = OMIT,
        enable_stream_audible_notifications: typing.Optional[bool] = OMIT,
        notification_sound: typing.Optional[str] = OMIT,
        enable_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_sounds: typing.Optional[bool] = OMIT,
        enable_followed_topic_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_email_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_audible_notifications: typing.Optional[bool] = OMIT,
        email_notifications_batching_period_seconds: typing.Optional[int] = OMIT,
        enable_offline_email_notifications: typing.Optional[bool] = OMIT,
        enable_offline_push_notifications: typing.Optional[bool] = OMIT,
        enable_online_push_notifications: typing.Optional[bool] = OMIT,
        enable_digest_emails: typing.Optional[bool] = OMIT,
        message_content_in_email_notifications: typing.Optional[bool] = OMIT,
        pm_content_in_desktop_notifications: typing.Optional[bool] = OMIT,
        wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        enable_followed_topic_wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        desktop_icon_count_display: typing.Optional[int] = OMIT,
        realm_name_in_email_notifications_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_policy: typing.Optional[int] = OMIT,
        automatically_unmute_topics_in_muted_streams_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_where_mentioned: typing.Optional[bool] = OMIT,
        resolved_topic_notice_auto_read_policy: typing.Optional[
            UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy
        ] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        enter_sends: typing.Optional[bool] = OMIT,
        twenty_four_hour_time: typing.Optional[bool] = OMIT,
        send_private_typing_notifications: typing.Optional[bool] = OMIT,
        send_stream_typing_notifications: typing.Optional[bool] = OMIT,
        send_read_receipts: typing.Optional[bool] = OMIT,
        email_address_visibility: typing.Optional[int] = OMIT,
        web_navigate_to_sent_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IgnoredParametersSuccess]:
        """
        Change the [default values of settings][new-user-defaults] for new users
        joining the organization. Essentially all
        [personal preference settings](/api/update-settings) are supported.

        This feature can be invaluable for customizing Zulip's default
        settings for notifications or UI to be appropriate for how the
        organization is using Zulip. (Note that this only supports
        personal preference settings, like when to send push
        notifications or what emoji set to use, not profile or
        identity settings that naturally should be different for each user).

        Note that this endpoint cannot, at present, be used to modify
        settings for existing users in any way.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        New in Zulip 5.0 (feature level 96). If any parameters sent in the
        request are not supported by this endpoint, an
        [`ignored_parameters_unsupported`][ignored-parameters] array will
        be returned in the JSON success response.

        [new-user-defaults]: /help/configure-default-new-user-settings
        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        starred_message_counts : typing.Optional[bool]
            Whether clients should display the [number of starred
            messages](/help/star-a-message#display-the-number-of-starred-messages).

        receives_typing_notifications : typing.Optional[bool]
            Whether the user is configured to receive typing notifications from other users.
            The server will only deliver typing notifications events to users who for whom this
            is enabled.

            **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were
            only options to disable sending typing notifications.

        web_suggest_update_timezone : typing.Optional[bool]
            Whether the user should be shown an alert, offering to update their
            [profile time zone](/help/change-your-timezone), when the time displayed
            for the profile time zone differs from the current time displayed by the
            time zone configured on their device.

            **Changes**: New in Zulip 10.0 (feature level 329).

        fluid_layout_width : typing.Optional[bool]
            Whether to use the [maximum available screen width](/help/enable-full-width-display)
            for the web app's center panel (message feed, recent conversations) on wide screens.

        high_contrast_mode : typing.Optional[bool]
            This setting is reserved for use to control variations in Zulip's design
            to help visually impaired users.

        web_mark_read_on_scroll_policy : typing.Optional[int]
            Whether or not to mark messages as read when the user scrolls through their
            feed.

            - 1 - Always
            - 2 - Only in conversation views
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
            way for the user to configure this behavior on the web, and the Zulip web and
            desktop apps behaved like the "Always" setting when marking messages as read.

        web_channel_default_view : typing.Optional[int]
            Web/desktop app setting controlling the default navigation
            behavior when clicking on a channel link.

            - 1 - Top topic in the channel
            - 2 - Channel feed
            - 3 - List of topics
            - 4 - Top unread topic in channel

            **Changes**: The "Top unread topic in channel" is new in Zulip 11.0
            (feature level 401).

            The "List of topics" option is new in Zulip 11.0 (feature level 383).

            New in Zulip 9.0 (feature level 269). Previously, this
            was not configurable, and every user had the "Channel feed" behavior.

        web_font_size_px : typing.Optional[int]
            User-configured primary `font-size` for the web application, in pixels.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
            only adjustable via browser zoom. Note that this setting was not fully
            implemented at this feature level.

        web_line_height_percent : typing.Optional[int]
            User-configured primary `line-height` for the web application, in percent, so a
            value of 120 represents a `line-height` of 1.2.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
            not user-configurable. Note that this setting was not fully implemented at this
            feature level.

        color_scheme : typing.Optional[int]
            Controls which [color theme](/help/dark-theme) to use.

            - 1 - Automatic
            - 2 - Dark theme
            - 3 - Light theme

            Automatic detection is implementing using the standard `prefers-color-scheme`
            media query.

        enable_drafts_synchronization : typing.Optional[bool]
            A boolean parameter to control whether synchronizing drafts is enabled for
            the user. When synchronization is disabled, all drafts stored in the server
            will be automatically deleted from the server.

            This does not do anything (like sending events) to delete local copies of
            drafts stored in clients.

        translate_emoticons : typing.Optional[bool]
            Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
            in messages the user sends.

        display_emoji_reaction_users : typing.Optional[bool]
            Whether to display the names of reacting users on a message.

            When enabled, clients should display the names of reacting users, rather than
            a count, for messages with few total reactions. The ideal cutoff may depend on
            the space available for displaying reactions; the official web application
            displays names when 3 or fewer total reactions are present with this setting
            enabled.

            **Changes**: New in Zulip 6.0 (feature level 125).

        web_home_view : typing.Optional[str]
            The [home view](/help/configure-home-view) used when opening a new
            Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

            - "recent" - Recent conversations view
            - "inbox" - Inbox view
            - "all_messages" - Combined feed view

            **Changes**: Before Zulip 12.0 (feature level 454), the Recent
            view had `"recent_topics"` as its string encoding.

            New in Zulip 8.0 (feature level 219). Previously, this was
            called `default_view`, which was new in Zulip 4.0 (feature level 42).

        web_escape_navigates_to_home_view : typing.Optional[bool]
            Whether the escape key navigates to the
            [configured home view](/help/configure-home-view).

            **Changes**: New in Zulip 8.0 (feature level 219). Previously, this was called
            `escape_navigates_to_default_view`, which was new in Zulip 5.0 (feature level 107).

        left_side_userlist : typing.Optional[bool]
            Whether the users list on left sidebar in narrow windows.

            This feature is not heavily used and is likely to be reworked.

        emojiset : typing.Optional[str]
            The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
            used to display emoji to the user everywhere they appear in the UI.

            - "google" - Google
            - "twitter" - Twitter
            - "text" - Plain text

        demote_inactive_streams : typing.Optional[int]
            Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

        user_list_style : typing.Optional[int]
            The style selected by the user for the right sidebar user list.

            - 1 - Compact
            - 2 - With status
            - 3 - With avatar and status

            **Changes**: New in Zulip 6.0 (feature level 141).

        web_animate_image_previews : typing.Optional[UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews]
            Controls how animated images should be played in the message feed in the web/desktop application.

            - "always" - Always play the animated images in the message feed.
            - "on_hover" - Play the animated images on hover over them in the message feed.
            - "never" - Never play animated images in the message feed.

            **Changes**: New in Zulip 9.0 (feature level 275). Previously, animated images
            always used to play in the message feed by default. This setting controls this
            behaviour.

        web_stream_unreads_count_display_policy : typing.Optional[int]
            Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
            Channels that do not have an unread count will have a simple dot indicator for whether there are any
            unread messages.

            - 1 - All channels
            - 2 - Unmuted channels and topics
            - 3 - No channels

            **Changes**: New in Zulip 8.0 (feature level 210).

        hide_ai_features : typing.Optional[bool]
            Controls whether user wants AI features like topic summarization to
            be hidden in all Zulip clients.

            **Changes**: New in Zulip 10.0 (feature level 350).

        web_inbox_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how conversations with unread messages
            are displayed in the web/desktop application's Inbox view.

            **Changes**: New in Zulip 12.0 (feature level 431).

        web_left_sidebar_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how channels are displayed in the
            web/desktop application's left sidebar.

            **Changes**: New in Zulip 11.0 (feature level 411).

        web_left_sidebar_unreads_count_summary : typing.Optional[bool]
            Determines whether the web/desktop application's left sidebar displays
            the unread message count summary.

            **Changes**: New in Zulip 11.0 (feature level 398).

        enable_stream_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for channel messages.

        enable_stream_email_notifications : typing.Optional[bool]
            Enable email notifications for channel messages.

        enable_stream_push_notifications : typing.Optional[bool]
            Enable mobile notifications for channel messages.

        enable_stream_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for channel messages.

        notification_sound : typing.Optional[str]
            Notification sound name.

        enable_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for direct messages and @-mentions.

        enable_sounds : typing.Optional[bool]
            Enable audible desktop notifications for direct messages and
            @-mentions.

        enable_followed_topic_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_email_notifications : typing.Optional[bool]
            Enable email notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_push_notifications : typing.Optional[bool]
            Enable push notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        email_notifications_batching_period_seconds : typing.Optional[int]
            The duration (in seconds) for which the server should wait to batch
            email notifications before sending them.

        enable_offline_email_notifications : typing.Optional[bool]
            Enable email notifications for direct messages and @-mentions received
            when the user is offline.

        enable_offline_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is offline.

        enable_online_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is online.

        enable_digest_emails : typing.Optional[bool]
            Enable digest emails when the user is away.

        message_content_in_email_notifications : typing.Optional[bool]
            Include the message's content in email notifications for new messages.

        pm_content_in_desktop_notifications : typing.Optional[bool]
            Include content of direct messages in desktop notifications.

        wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (E.g. @**all**) should send notifications
            like a personal mention.

        enable_followed_topic_wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
            should send notifications like a personal mention.

            **Changes**: New in Zulip 8.0 (feature level 189).

        desktop_icon_count_display : typing.Optional[int]
            Unread count badge (appears in desktop sidebar and browser tab)

            - 1 - All unread messages
            - 2 - DMs, mentions, and followed topics
            - 3 - DMs and mentions
            - 4 - None

            **Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
            topics` option, renumbering the options to insert it in order.

        realm_name_in_email_notifications_policy : typing.Optional[int]
            Whether to [include organization name in subject of message notification
            emails](/help/email-notifications#include-organization-name-in-subject-line).

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 168), replacing the
            previous `realm_name_in_notifications` boolean;
            `true` corresponded to `Always`, and `false` to `Never`.

        automatically_follow_topics_policy : typing.Optional[int]
            Which [topics to follow automatically](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_unmute_topics_in_muted_streams_policy : typing.Optional[int]
            Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_follow_topics_where_mentioned : typing.Optional[bool]
            Whether the server will automatically mark the user as following
            topics where the user is mentioned.

            **Changes**: New in Zulip 8.0 (feature level 235).

        resolved_topic_notice_auto_read_policy : typing.Optional[UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy]
            Controls whether the resolved-topic notices are marked as read.

            - "always" - Always mark resolved-topic notices as read.
            - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
            - "never" - Never mark resolved-topic notices as read.

            **Changes**: New in Zulip 11.0 (feature level 385).

        presence_enabled : typing.Optional[bool]
            Display the presence status to other users when online.

        enter_sends : typing.Optional[bool]
            Whether pressing Enter in the compose box sends a message
            (or saves a message edit).

        twenty_four_hour_time : typing.Optional[bool]
            Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

            **Changes**: New in Zulip 5.0 (feature level 99).
            Previously, this default was edited using the
            `default_twenty_four_hour_time` parameter to the `PATCH /realm` endpoint.

        send_private_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            direct messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_stream_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            channel messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_read_receipts : typing.Optional[bool]
            Whether other users are allowed to see whether you've
            read messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        email_address_visibility : typing.Optional[int]
            The [policy][permission-level] for [which other users][help-email-visibility]
            in this organization can see the user's real email address.

            - 1 = Everyone
            - 2 = Members only
            - 3 = Administrators only
            - 4 = Nobody
            - 5 = Moderators only

            **Changes**: New in Zulip 7.0 (feature level 163), replacing the
            realm-level setting.

            [permission-level]: /api/roles-and-permissions#permission-levels
            [help-email-visibility]: /help/configure-email-visibility

        web_navigate_to_sent_message : typing.Optional[bool]
            Web/desktop app setting for whether the user's view should
            automatically go to the conversation where they sent a message.

            **Changes**: New in Zulip 9.0 (feature level 268). Previously,
            this behavior was not configurable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IgnoredParametersSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/user_settings_defaults",
            method="PATCH",
            data={
                "starred_message_counts": starred_message_counts,
                "receives_typing_notifications": receives_typing_notifications,
                "web_suggest_update_timezone": web_suggest_update_timezone,
                "fluid_layout_width": fluid_layout_width,
                "high_contrast_mode": high_contrast_mode,
                "web_mark_read_on_scroll_policy": web_mark_read_on_scroll_policy,
                "web_channel_default_view": web_channel_default_view,
                "web_font_size_px": web_font_size_px,
                "web_line_height_percent": web_line_height_percent,
                "color_scheme": color_scheme,
                "enable_drafts_synchronization": enable_drafts_synchronization,
                "translate_emoticons": translate_emoticons,
                "display_emoji_reaction_users": display_emoji_reaction_users,
                "web_home_view": web_home_view,
                "web_escape_navigates_to_home_view": web_escape_navigates_to_home_view,
                "left_side_userlist": left_side_userlist,
                "emojiset": emojiset,
                "demote_inactive_streams": demote_inactive_streams,
                "user_list_style": user_list_style,
                "web_animate_image_previews": web_animate_image_previews,
                "web_stream_unreads_count_display_policy": web_stream_unreads_count_display_policy,
                "hide_ai_features": hide_ai_features,
                "web_inbox_show_channel_folders": web_inbox_show_channel_folders,
                "web_left_sidebar_show_channel_folders": web_left_sidebar_show_channel_folders,
                "web_left_sidebar_unreads_count_summary": web_left_sidebar_unreads_count_summary,
                "enable_stream_desktop_notifications": enable_stream_desktop_notifications,
                "enable_stream_email_notifications": enable_stream_email_notifications,
                "enable_stream_push_notifications": enable_stream_push_notifications,
                "enable_stream_audible_notifications": enable_stream_audible_notifications,
                "notification_sound": notification_sound,
                "enable_desktop_notifications": enable_desktop_notifications,
                "enable_sounds": enable_sounds,
                "enable_followed_topic_desktop_notifications": enable_followed_topic_desktop_notifications,
                "enable_followed_topic_email_notifications": enable_followed_topic_email_notifications,
                "enable_followed_topic_push_notifications": enable_followed_topic_push_notifications,
                "enable_followed_topic_audible_notifications": enable_followed_topic_audible_notifications,
                "email_notifications_batching_period_seconds": email_notifications_batching_period_seconds,
                "enable_offline_email_notifications": enable_offline_email_notifications,
                "enable_offline_push_notifications": enable_offline_push_notifications,
                "enable_online_push_notifications": enable_online_push_notifications,
                "enable_digest_emails": enable_digest_emails,
                "message_content_in_email_notifications": message_content_in_email_notifications,
                "pm_content_in_desktop_notifications": pm_content_in_desktop_notifications,
                "wildcard_mentions_notify": wildcard_mentions_notify,
                "enable_followed_topic_wildcard_mentions_notify": enable_followed_topic_wildcard_mentions_notify,
                "desktop_icon_count_display": desktop_icon_count_display,
                "realm_name_in_email_notifications_policy": realm_name_in_email_notifications_policy,
                "automatically_follow_topics_policy": automatically_follow_topics_policy,
                "automatically_unmute_topics_in_muted_streams_policy": automatically_unmute_topics_in_muted_streams_policy,
                "automatically_follow_topics_where_mentioned": automatically_follow_topics_where_mentioned,
                "resolved_topic_notice_auto_read_policy": resolved_topic_notice_auto_read_policy,
                "presence_enabled": presence_enabled,
                "enter_sends": enter_sends,
                "twenty_four_hour_time": twenty_four_hour_time,
                "send_private_typing_notifications": send_private_typing_notifications,
                "send_stream_typing_notifications": send_stream_typing_notifications,
                "send_read_receipts": send_read_receipts,
                "email_address_visibility": email_address_visibility,
                "web_navigate_to_sent_message": web_navigate_to_sent_message,
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
                    IgnoredParametersSuccess,
                    parse_obj_as(
                        type_=IgnoredParametersSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_linkifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLinkifiersResponse]:
        """
        List all of an organization's configured
        [linkifiers](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        **Changes**: New in Zulip 4.0 (feature level 54). On older versions,
        a similar `GET /realm/filters` endpoint was available with each entry in
        a `[pattern, url_format, id]` tuple format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLinkifiersResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/linkifiers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinkifiersResponse,
                    parse_obj_as(
                        type_=GetLinkifiersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reorder_linkifiers(
        self, *, ordered_linkifier_ids: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Change the order that the regular expression patterns in the organization's
        [linkifiers](/help/add-a-custom-linkifier) are matched in messages and topics.
        Useful when defining linkifiers with overlapping patterns.

        **Changes**: New in Zulip 8.0 (feature level 202). Before this feature level,
        linkifiers were always processed in order by ID, which meant users would
        need to delete and recreate them to reorder the list of linkifiers.

        Parameters
        ----------
        ordered_linkifier_ids : typing.Sequence[int]
            A list of the IDs of all the linkifiers defined in this
            organization, in the desired new order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/linkifiers",
            method="PATCH",
            data={
                "ordered_linkifier_ids": ordered_linkifier_ids,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_linkifier(
        self,
        *,
        pattern: LinkifierPattern,
        url_template: LinkifierUrlTemplate,
        example_input: typing.Optional[str] = OMIT,
        reverse_template: typing.Optional[str] = OMIT,
        alternative_url_templates: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddLinkifierResponse]:
        """
        Configure [linkifiers](/help/add-a-custom-linkifier),
        regular expression patterns that are automatically linkified when they
        appear in messages and topics.

        Parameters
        ----------
        pattern : LinkifierPattern

        url_template : LinkifierUrlTemplate

        example_input : typing.Optional[str]
            An example input string that matches the linkifier's pattern.
            This is required for reverse linkifiers.

            **Changes**: New in Zulip 12.0 (feature level 471).

        reverse_template : typing.Optional[str]
            A simple template using `{variable}` for variables that can
            be used to generate the Markdown linkifier syntax, given a
            URL matching the URL template.

            `{{ "{{/}}" }}` can be used for literal `{/}` characters.

            Server verifies that variables extracted from example_input using
            url_pattern when passed to reverse_template returns example_input
            back to us.

            **Changes**: New in Zulip 12.0 (feature level 471).

        alternative_url_templates : typing.Optional[typing.Sequence[str]]
            An array of additional [RFC 6570][rfc6570] compliant URL
            template strings that are used for reverse linkification
            (converting pasted URLs to linkifier pattern text). These
            templates have no effect on forward linkification.

            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

            **Changes**: New in Zulip 12.0 (feature level e2b257).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddLinkifierResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/filters",
            method="POST",
            data={
                "pattern": pattern,
                "url_template": url_template,
                "example_input": example_input,
                "reverse_template": reverse_template,
                "alternative_url_templates": alternative_url_templates,
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
                    AddLinkifierResponse,
                    parse_obj_as(
                        type_=AddLinkifierResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_linkifier(
        self, filter_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Remove [linkifiers](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        Parameters
        ----------
        filter_id : int
            The ID of the linkifier that you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/filters/{encode_path_param(filter_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_linkifier(
        self,
        filter_id: int,
        *,
        pattern: LinkifierPattern,
        url_template: LinkifierUrlTemplate,
        example_input: typing.Optional[str] = OMIT,
        reverse_template: typing.Optional[str] = OMIT,
        alternative_url_templates: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Update a [linkifier](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        **Changes**: New in Zulip 4.0 (feature level 57).

        Parameters
        ----------
        filter_id : int
            The ID of the linkifier that you want to update.

        pattern : LinkifierPattern

        url_template : LinkifierUrlTemplate

        example_input : typing.Optional[str]
            An example input string that matches the linkifier's pattern.
            This is required for reverse linkifiers. Passing an empty string
            will set this field back to null.

            **Changes**: New in Zulip 12.0 (feature level 471).

        reverse_template : typing.Optional[str]
            A simple template using `{variable}` for variables that can
            be used to generate the Markdown linkifier syntax, given a
            URL matching the URL template. Passing an empty string
            will set this field back to null.

            Server verifies that variables extracted from example_input using
            url_pattern when passed to reverse_template returns example_input
            back to us.

            `{{ "{{/}}" }}` can be used for literal `{/}` characters.

            **Changes**: New in Zulip 12.0 (feature level 471).

        alternative_url_templates : typing.Optional[typing.Sequence[str]]
            An array of additional [RFC 6570][rfc6570] compliant URL
            template strings that are used for reverse linkification
            (converting pasted URLs to linkifier pattern text). These
            templates have no effect on forward linkification.

            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

            **Changes**: New in Zulip 12.0 (feature level e2b257).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/filters/{encode_path_param(filter_id)}",
            method="PATCH",
            data={
                "pattern": pattern,
                "url_template": url_template,
                "example_input": example_input,
                "reverse_template": reverse_template,
                "alternative_url_templates": alternative_url_templates,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_code_playground(
        self,
        *,
        name: str,
        pygments_language: str,
        url_template: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddCodePlaygroundResponse]:
        """
        Configure [code playgrounds](/help/code-blocks#code-playgrounds) for the organization.

        **Changes**: New in Zulip 4.0 (feature level 49). A parameter encoding bug was
        fixed in Zulip 4.0 (feature level 57).

        Parameters
        ----------
        name : str
            The user-visible display name of the playground which can be
            used to pick the target playground, especially when multiple
            playground options exist for that programming language.

        pygments_language : str
            The name of the Pygments language lexer for that
            programming language.

        url_template : str
            The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html)
            compliant URL template for the playground. The template should
            contain exactly one variable named `code`, which determines how the
            extracted code should be substituted in the playground URL.

            **Changes**: New in Zulip 8.0 (feature level 196). This replaced the
            `url_prefix` parameter, which was used to construct URLs by just
            concatenating `url_prefix` and `code`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddCodePlaygroundResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/playgrounds",
            method="POST",
            data={
                "name": name,
                "pygments_language": pygments_language,
                "url_template": url_template,
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
                    AddCodePlaygroundResponse,
                    parse_obj_as(
                        type_=AddCodePlaygroundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_code_playground(
        self, playground_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Remove a [code playground](/help/code-blocks#code-playgrounds) previously
        configured for an organization.

        **Changes**: New in Zulip 4.0 (feature level 49).

        Parameters
        ----------
        playground_id : int
            The ID of the playground that you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"realm/playgrounds/{encode_path_param(playground_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_realm_export(
        self, export_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete a completed public or standard [data export][export-data]
        of the organization.

        Data exports that happened on a previous server (i.e., an export
        with `"export_from_prior_server": true` in the
        [`GET /export/realm`](/api/get-realm-exports#response) response)
        cannot be deleted using this endpoint, since their tarball is no
        longer stored on this server; attempting to do so fails with
        the same error as for an export that has already been deleted.

        This endpoint's success response does not describe the resulting
        state of the organization's data exports. Clients should rely
        on the [`realm_export` event](/api/get-events#realm_export),
        which every organization administrator receives whenever a
        data export's state changes, for the current state of an
        organization's data exports.

        **Changes**: Prior to Zulip 13.0 (feature level 506), data
        exports without a tarball stored on this server had no
        dedicated status, so attempting to delete one resulted in an
        unexpected error. Starting at that feature level, such a
        delete attempt instead fails cleanly, as described above. This
        change was also backported to the Zulip 12.x series, at
        feature level 499.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format

        Parameters
        ----------
        export_id : int
            The ID of the data export to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"export/realm/{encode_path_param(export_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_realm_exports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRealmExportsResponse]:
        """
        Fetch all the public and standard [data exports][export-data]
        of the organization.

        **Changes**: Prior to Zulip 10.0 (feature level 304), only
        public data exports could be fetched using this endpoint.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRealmExportsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "export/realm",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmExportsResponse,
                    parse_obj_as(
                        type_=GetRealmExportsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def export_realm(
        self,
        *,
        export_type: typing.Optional[ExportRealmRequestExportType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportRealmResponse]:
        """
        !!! warn ""

            **Note**: If you're the administrator of a self-hosted installation,
            you may be looking for the documentation on [server data export and
            import][data-export] or [server backups][backups].

        Create a public or a standard [data export][export-data] of the
        organization.

        This endpoint only queues the data export; it does not wait for
        the export to complete, which depending on the size of the
        organization can take anywhere from seconds to an hour.
        Therefore, this endpoint's success response does not describe
        the outcome of the export.

        To find out the outcome of the export, clients should rely on the
        [`realm_export` event](/api/get-events#realm_export), which is
        which is sent to every organization administrator immediately
        when the export is requested, and again once it completes or
        fails. Additionally, when the export succeeds, the user who
        requested it will receive a direct message from the Notification
        Bot with a link to the organization's data exports panel, where
        the export can be downloaded.

        **Changes**: Prior to Zulip 10.0 (feature level 304), only public
        data exports could be created using this endpoint.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format
        [data-export]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#data-export
        [backups]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#backups

        Parameters
        ----------
        export_type : typing.Optional[ExportRealmRequestExportType]
            Whether the data export should be public, full with consent,
            or full without consent.

            - `public` = Public data only export.
            - `full_with_consent` = Public and private data export (with consent), which includes
              private data for users who have granted consent.
            - `full_without_consent` = All public and private data export, which includes private data for
              all users. This option requires the organization to have
              the `owner_full_content_access` feature enabled.

            If not specified, defaults to `public`.

            **Changes**: Zulip 12.0 (feature level 449) changed the type of
            this field from int to string with `1` being replaced by `public` and
            `2` being replaced by `full_with_consent`. The option `full_without_consent`
            was added for full exports without member consent.

            New in Zulip 10.0 (feature level 304). Previously,
            all export requests were public data exports.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportRealmResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "export/realm",
            method="POST",
            data={
                "export_type": export_type,
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
                    ExportRealmResponse,
                    parse_obj_as(
                        type_=ExportRealmResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_realm_export_consents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRealmExportConsentsResponse]:
        """
        Fetches which users have [consented](/help/export-your-organization#configure-whether-administrators-can-export-your-private-data)
        for their private data to be exported by organization administrators.

        **Changes**: Changes in Zulip 12.0 (feature level 430). Added an
        integer field `email_address_visibility` to the objects in the
        `export_consents` array.

        New in Zulip 10.0 (feature level 295).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRealmExportConsentsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "export/realm/consents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmExportConsentsResponse,
                    parse_obj_as(
                        type_=GetRealmExportConsentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_welcome_bot_custom_message(
        self, *, welcome_message_custom_text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestWelcomeBotCustomMessageResponse]:
        """
        Sends a test Welcome Bot custom message to the acting administrator.
        This allows administrators to preview how the custom welcome message will
        appear when received by new users upon joining the organization.

        **Changes**: New in Zulip 11.0 (feature level 416).

        Parameters
        ----------
        welcome_message_custom_text : str
            Custom message text, in Zulip Markdown format, to be used for
            this test message.

            Maximum length is 8000 Unicode code points.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestWelcomeBotCustomMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "realm/test_welcome_bot_custom_message",
            method="POST",
            data={
                "welcome_message_custom_text": welcome_message_custom_text,
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
                    TestWelcomeBotCustomMessageResponse,
                    parse_obj_as(
                        type_=TestWelcomeBotCustomMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_server_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetServerSettingsResponse]:
        """
        Fetch global settings for a Zulip server.

        **Note:** this endpoint does not require any authentication at all, and you can use it to check:

        - If this is a Zulip server, and if so, what version of Zulip it's running.
        - What a Zulip client (e.g. a mobile app or
          [zulip-terminal](https://github.com/zulip/zulip-terminal/)) needs to
          know in order to display a login prompt for the server (e.g. what
          authentication methods are available).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetServerSettingsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "server_settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServerSettingsResponse,
                    parse_obj_as(
                        type_=GetServerSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawServerAndOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_custom_emoji(
        self,
        emoji_name: str,
        *,
        filename: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        This endpoint is used to upload a custom emoji for use in the user's
        organization. Access to this endpoint depends on the
        [organization's configuration](https://zulip.com/help/custom-emoji#change-who-can-add-custom-emoji).

        Parameters
        ----------
        emoji_name : str
            The name that should be associated with the uploaded emoji image/gif.
            The emoji name can only contain letters, numbers, dashes, and spaces.
            Upper and lower case letters are treated the same, and underscores (\\_)
            are treated the same as spaces (consistent with how the Zulip UI
            handles emoji).

        filename : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/emoji/{encode_path_param(emoji_name)}",
            method="POST",
            data={},
            files={
                **({"filename": filename} if filename is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deactivate_custom_emoji(
        self, emoji_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        [Deactivate a custom emoji](/help/custom-emoji#deactivate-custom-emoji) from
        the user's organization.

        Users can only deactivate custom emoji that they added themselves except for
        organization administrators, who can deactivate any custom emoji.

        Note that deactivated emoji will still be visible in old messages, reactions,
        user statuses and channel descriptions.

        **Changes**: Before Zulip 8.0 (feature level 190), this endpoint returned an
        HTTP status code of 400 when the emoji did not exist, instead of 404.

        Parameters
        ----------
        emoji_name : str
            The name of the custom emoji to deactivate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/emoji/{encode_path_param(emoji_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_custom_emoji(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCustomEmojiResponse]:
        """
        Get all the custom emoji in the user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomEmojiResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/emoji",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomEmojiResponse,
                    parse_obj_as(
                        type_=GetCustomEmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_presence(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPresenceResponse]:
        """
        Get the presence information of all the users in an organization.

        If the `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level
        setting is set to `true`, presence information of only accessible
        users are returned.

        Complete Zulip apps are recommended to fetch presence
        information when they post their own state using the [`POST
        /presence`](/api/update-presence) API endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPresenceResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/presence",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPresenceResponse,
                    parse_obj_as(
                        type_=GetPresenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_realm_domains(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRealmDomainsResponse]:
        """
        Get the set of allowed domains configured in the organization for user
        account email addresses.

        As each Zulip user account is associated with an email address, organization
        owners can [restrict new account creation (and email
        changes)](/help/restrict-account-creation) to email addresses with these
        domains.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRealmDomainsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmDomainsResponse,
                    parse_obj_as(
                        type_=GetRealmDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_realm_domain(
        self, *, domain: str, allow_subdomains: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddRealmDomainResponse]:
        """
        Add a domain to the set of allowed domains configured in the organization
        for [user account email addresses](/help/restrict-account-creation).

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The new domain.

            **Changes**: In Zulip 4.0 (feature level 63), the unnecessary
            JSON-encoding of this parameter was removed.

        allow_subdomains : bool
            Whether subdomains are allowed for this domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddRealmDomainResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/domains",
            method="POST",
            data={
                "domain": domain,
                "allow_subdomains": allow_subdomains,
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
                    AddRealmDomainResponse,
                    parse_obj_as(
                        type_=AddRealmDomainResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_realm_domain(
        self, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Remove the specified domain from the set of allowed domains configured in
        the organization for [user account email addresses](/help/restrict-account-creation).

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The domain to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/domains/{encode_path_param(domain)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_realm_domain(
        self, domain: str, *, allow_subdomains: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Update whether subdomains are allowed in [user account email
        addresses](/help/restrict-account-creation) for the specified domain.

        **Changes**: Prior to Zulip 6.0 (feature level 143), organization
        administrators who were not owners could access this endpoint.

        Parameters
        ----------
        domain : str
            The domain to update.

        allow_subdomains : bool
            Whether subdomains are allowed for this domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/domains/{encode_path_param(domain)}",
            method="PATCH",
            data={
                "allow_subdomains": allow_subdomains,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deactivate_realm(
        self,
        *,
        deletion_delay_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        [Deactivate an organization](/help/deactivate-your-organization) on the
        Zulip server. Deactivating an organization immediately logs out all of
        its users and prevents them from logging in again.

        A deactivated organization can be reactivated via a [management
        command](https://zulip.readthedocs.io/en/latest/production/management-commands.html),
        unless its data has been permanently deleted (see the
        [`deletion_delay_days` parameter](/api/deactivate-realm#parameter-deletion_delay_days)
        below).

        This endpoint is primarily useful for Zulip servers that host
        [multiple organizations](https://zulip.readthedocs.io/en/latest/production/multiple-organizations.html).

        Parameters
        ----------
        deletion_delay_days : typing.Optional[int]
            The number of days to wait before permanently deleting all
            of the deactivated organization's data (users, channels,
            messages, etc.).

            A value of `0` will delete the organization's data
            immediately, which means that the organization cannot be
            reactivated. A `null` value indicates that the organization's
            data will not be deleted, but rather retained indefinitely.

            Valid values for this parameter are limited to the range
            permitted by the server, indicated by the
            `server_min_deactivated_realm_deletion_days` and
            `server_max_deactivated_realm_deletion_days` fields in the
            [`POST /register`](/api/register-queue) response. A value of
            `null` is only permitted when
            `server_max_deactivated_realm_deletion_days` is `null`. A
            value of `0` is only permitted when
            `server_min_deactivated_realm_deletion_days` is `null`.

            These limits do not apply to
            [Zulip Cloud demo organizations](/help/demo-organizations),
            for which this parameter is instead required: it must be `0`
            when the organization owner has not configured an email
            address, and otherwise must not exceed the number of days
            remaining before the demo organization's scheduled deletion.

            **Changes**: New in Zulip 10.0 (feature level 332).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/deactivate",
            method="POST",
            data={
                "deletion_delay_days": deletion_delay_days,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_custom_profile_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCustomProfileFieldsResponse]:
        """
        Get all the [custom profile fields](/help/custom-profile-fields)
        configured for the user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomProfileFieldsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomProfileFieldsResponse,
                    parse_obj_as(
                        type_=GetCustomProfileFieldsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_custom_profile_field(
        self,
        *,
        field_type: int,
        name: typing.Optional[str] = OMIT,
        hint: typing.Optional[CustomProfileFieldHintSchema] = OMIT,
        field_data: typing.Optional[CustomProfileFieldDataSchema] = OMIT,
        display_in_profile_summary: typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema] = OMIT,
        required: typing.Optional[CustomProfileFieldRequiredSchema] = OMIT,
        editable_by_user: typing.Optional[CustomProfileFieldEditableByUserSchema] = OMIT,
        use_for_user_matching: typing.Optional[CustomProfileFieldUseForUserMatchingSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCustomProfileFieldResponse]:
        """
        [Create a custom profile field](/help/custom-profile-fields#add-a-custom-profile-field) in the user's organization.

        Parameters
        ----------
        field_type : int
            The field type can be any of the supported custom profile field types. See the
            [custom profile fields documentation](/help/custom-profile-fields)
            for more details on what each type means.

            - **1**: Short text
            - **2**: Paragraph
            - **3**: Dropdown
            - **4**: Date
            - **5**: Link
            - **6**: Users
            - **7**: External account
            - **8**: Pronouns

            **Changes**: Field type `8` added in Zulip 6.0 (feature level 151).

        name : typing.Optional[str]
            The name of the custom profile field, which appears both in
            the user-facing settings UI for configuring the custom profile
            fields and in the UI displaying a user's profile.

        hint : typing.Optional[CustomProfileFieldHintSchema]

        field_data : typing.Optional[CustomProfileFieldDataSchema]

        display_in_profile_summary : typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema]

        required : typing.Optional[CustomProfileFieldRequiredSchema]

        editable_by_user : typing.Optional[CustomProfileFieldEditableByUserSchema]

        use_for_user_matching : typing.Optional[CustomProfileFieldUseForUserMatchingSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCustomProfileFieldResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="POST",
            data={
                "name": name,
                "field_type": field_type,
                "hint": hint,
                "field_data": field_data,
                "display_in_profile_summary": display_in_profile_summary,
                "required": required,
                "editable_by_user": editable_by_user,
                "use_for_user_matching": use_for_user_matching,
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
                    CreateCustomProfileFieldResponse,
                    parse_obj_as(
                        type_=CreateCustomProfileFieldResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reorder_custom_profile_fields(
        self, *, order: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Reorder the custom profile fields in the user's organization.

        Custom profile fields are displayed in Zulip UI widgets in order; this
        endpoint allows administrative settings UI to change the field ordering.

        This endpoint is used to implement the dragging feature described in the
        [custom profile fields documentation](/help/custom-profile-fields).

        Parameters
        ----------
        order : typing.Sequence[int]
            A list of the IDs of all the custom profile fields defined in this
            organization, in the desired new order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/profile_fields",
            method="PATCH",
            data={
                "order": order,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_custom_profile_field(
        self, field_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete a [custom profile field](/help/custom-profile-fields) in
        the user's organization.

        This will also permanently delete any value configured for the
        custom profile field from every user profile in the database.
        Therefore, it's recommended that clients warn the active user of
        the related data removal before submitting the request, e.g.,
        notify them of how many users will have their profile data
        deleted as a result of deleting the custom profile field.

        Parameters
        ----------
        field_id : int
            The ID of the target custom profile field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/profile_fields/{encode_path_param(field_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_custom_profile_field(
        self,
        field_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        hint: typing.Optional[CustomProfileFieldHintSchema] = OMIT,
        field_data: typing.Optional[CustomProfileFieldDataSchema] = OMIT,
        display_in_profile_summary: typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema] = OMIT,
        required: typing.Optional[CustomProfileFieldRequiredSchema] = OMIT,
        editable_by_user: typing.Optional[CustomProfileFieldEditableByUserSchema] = OMIT,
        use_for_user_matching: typing.Optional[CustomProfileFieldUseForUserMatchingSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Update the configuration of a
        [custom profile field](/help/custom-profile-fields) in the user's
        organization.

        The [type](/api/create-custom-profile-field#parameter-field_type)
        of a custom profile field cannot be changed.

        At most, 2 custom profile fields can have
        [`display_in_profile_summary`](/api/update-custom-profile-field#parameter-display_in_profile_summary)
        set to `true` in an organization.

        For custom profile fields with type 7 (External account) that use
        one of Zulip's configured default external account providers
        (e.g., GitHub, LinkedIn, etc.), the field's
        [`name`](/api/update-custom-profile-field#parameter-name),
        [`hint`](/api/update-custom-profile-field#parameter-hint), and
        [`field_data`](/api/update-custom-profile-field#parameter-field_data)
        cannot be changed, and attempting to do so will return an error.

        **Changes**: Before Zulip 9.0 (feature level 252), the `name`,
        `hint`, `field_data`, `required` and `display_in_profile_summary`
        parameters were all required in every request, even when their
        values were unchanged.

        Parameters
        ----------
        field_id : int
            The ID of the target custom profile field.

        name : typing.Optional[str]
            The name of the custom profile field, which appears both in
            the user-facing settings UI for configuring the custom profile
            fields and in the UI displaying a user's profile.

        hint : typing.Optional[CustomProfileFieldHintSchema]

        field_data : typing.Optional[CustomProfileFieldDataSchema]

        display_in_profile_summary : typing.Optional[CustomProfileFieldDisplayInProfileSummarySchema]

        required : typing.Optional[CustomProfileFieldRequiredSchema]

        editable_by_user : typing.Optional[CustomProfileFieldEditableByUserSchema]

        use_for_user_matching : typing.Optional[CustomProfileFieldUseForUserMatchingSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/profile_fields/{encode_path_param(field_id)}",
            method="PATCH",
            data={
                "name": name,
                "hint": hint,
                "field_data": field_data,
                "display_in_profile_summary": display_in_profile_summary,
                "required": required,
                "editable_by_user": editable_by_user,
                "use_for_user_matching": use_for_user_matching,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_realm_user_settings_defaults(
        self,
        *,
        starred_message_counts: typing.Optional[bool] = OMIT,
        receives_typing_notifications: typing.Optional[bool] = OMIT,
        web_suggest_update_timezone: typing.Optional[bool] = OMIT,
        fluid_layout_width: typing.Optional[bool] = OMIT,
        high_contrast_mode: typing.Optional[bool] = OMIT,
        web_mark_read_on_scroll_policy: typing.Optional[int] = OMIT,
        web_channel_default_view: typing.Optional[int] = OMIT,
        web_font_size_px: typing.Optional[int] = OMIT,
        web_line_height_percent: typing.Optional[int] = OMIT,
        color_scheme: typing.Optional[int] = OMIT,
        enable_drafts_synchronization: typing.Optional[bool] = OMIT,
        translate_emoticons: typing.Optional[bool] = OMIT,
        display_emoji_reaction_users: typing.Optional[bool] = OMIT,
        web_home_view: typing.Optional[str] = OMIT,
        web_escape_navigates_to_home_view: typing.Optional[bool] = OMIT,
        left_side_userlist: typing.Optional[bool] = OMIT,
        emojiset: typing.Optional[str] = OMIT,
        demote_inactive_streams: typing.Optional[int] = OMIT,
        user_list_style: typing.Optional[int] = OMIT,
        web_animate_image_previews: typing.Optional[
            UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews
        ] = OMIT,
        web_stream_unreads_count_display_policy: typing.Optional[int] = OMIT,
        hide_ai_features: typing.Optional[bool] = OMIT,
        web_inbox_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_unreads_count_summary: typing.Optional[bool] = OMIT,
        enable_stream_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_stream_email_notifications: typing.Optional[bool] = OMIT,
        enable_stream_push_notifications: typing.Optional[bool] = OMIT,
        enable_stream_audible_notifications: typing.Optional[bool] = OMIT,
        notification_sound: typing.Optional[str] = OMIT,
        enable_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_sounds: typing.Optional[bool] = OMIT,
        enable_followed_topic_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_email_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_audible_notifications: typing.Optional[bool] = OMIT,
        email_notifications_batching_period_seconds: typing.Optional[int] = OMIT,
        enable_offline_email_notifications: typing.Optional[bool] = OMIT,
        enable_offline_push_notifications: typing.Optional[bool] = OMIT,
        enable_online_push_notifications: typing.Optional[bool] = OMIT,
        enable_digest_emails: typing.Optional[bool] = OMIT,
        message_content_in_email_notifications: typing.Optional[bool] = OMIT,
        pm_content_in_desktop_notifications: typing.Optional[bool] = OMIT,
        wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        enable_followed_topic_wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        desktop_icon_count_display: typing.Optional[int] = OMIT,
        realm_name_in_email_notifications_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_policy: typing.Optional[int] = OMIT,
        automatically_unmute_topics_in_muted_streams_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_where_mentioned: typing.Optional[bool] = OMIT,
        resolved_topic_notice_auto_read_policy: typing.Optional[
            UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy
        ] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        enter_sends: typing.Optional[bool] = OMIT,
        twenty_four_hour_time: typing.Optional[bool] = OMIT,
        send_private_typing_notifications: typing.Optional[bool] = OMIT,
        send_stream_typing_notifications: typing.Optional[bool] = OMIT,
        send_read_receipts: typing.Optional[bool] = OMIT,
        email_address_visibility: typing.Optional[int] = OMIT,
        web_navigate_to_sent_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IgnoredParametersSuccess]:
        """
        Change the [default values of settings][new-user-defaults] for new users
        joining the organization. Essentially all
        [personal preference settings](/api/update-settings) are supported.

        This feature can be invaluable for customizing Zulip's default
        settings for notifications or UI to be appropriate for how the
        organization is using Zulip. (Note that this only supports
        personal preference settings, like when to send push
        notifications or what emoji set to use, not profile or
        identity settings that naturally should be different for each user).

        Note that this endpoint cannot, at present, be used to modify
        settings for existing users in any way.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        New in Zulip 5.0 (feature level 96). If any parameters sent in the
        request are not supported by this endpoint, an
        [`ignored_parameters_unsupported`][ignored-parameters] array will
        be returned in the JSON success response.

        [new-user-defaults]: /help/configure-default-new-user-settings
        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        starred_message_counts : typing.Optional[bool]
            Whether clients should display the [number of starred
            messages](/help/star-a-message#display-the-number-of-starred-messages).

        receives_typing_notifications : typing.Optional[bool]
            Whether the user is configured to receive typing notifications from other users.
            The server will only deliver typing notifications events to users who for whom this
            is enabled.

            **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were
            only options to disable sending typing notifications.

        web_suggest_update_timezone : typing.Optional[bool]
            Whether the user should be shown an alert, offering to update their
            [profile time zone](/help/change-your-timezone), when the time displayed
            for the profile time zone differs from the current time displayed by the
            time zone configured on their device.

            **Changes**: New in Zulip 10.0 (feature level 329).

        fluid_layout_width : typing.Optional[bool]
            Whether to use the [maximum available screen width](/help/enable-full-width-display)
            for the web app's center panel (message feed, recent conversations) on wide screens.

        high_contrast_mode : typing.Optional[bool]
            This setting is reserved for use to control variations in Zulip's design
            to help visually impaired users.

        web_mark_read_on_scroll_policy : typing.Optional[int]
            Whether or not to mark messages as read when the user scrolls through their
            feed.

            - 1 - Always
            - 2 - Only in conversation views
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
            way for the user to configure this behavior on the web, and the Zulip web and
            desktop apps behaved like the "Always" setting when marking messages as read.

        web_channel_default_view : typing.Optional[int]
            Web/desktop app setting controlling the default navigation
            behavior when clicking on a channel link.

            - 1 - Top topic in the channel
            - 2 - Channel feed
            - 3 - List of topics
            - 4 - Top unread topic in channel

            **Changes**: The "Top unread topic in channel" is new in Zulip 11.0
            (feature level 401).

            The "List of topics" option is new in Zulip 11.0 (feature level 383).

            New in Zulip 9.0 (feature level 269). Previously, this
            was not configurable, and every user had the "Channel feed" behavior.

        web_font_size_px : typing.Optional[int]
            User-configured primary `font-size` for the web application, in pixels.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
            only adjustable via browser zoom. Note that this setting was not fully
            implemented at this feature level.

        web_line_height_percent : typing.Optional[int]
            User-configured primary `line-height` for the web application, in percent, so a
            value of 120 represents a `line-height` of 1.2.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
            not user-configurable. Note that this setting was not fully implemented at this
            feature level.

        color_scheme : typing.Optional[int]
            Controls which [color theme](/help/dark-theme) to use.

            - 1 - Automatic
            - 2 - Dark theme
            - 3 - Light theme

            Automatic detection is implementing using the standard `prefers-color-scheme`
            media query.

        enable_drafts_synchronization : typing.Optional[bool]
            A boolean parameter to control whether synchronizing drafts is enabled for
            the user. When synchronization is disabled, all drafts stored in the server
            will be automatically deleted from the server.

            This does not do anything (like sending events) to delete local copies of
            drafts stored in clients.

        translate_emoticons : typing.Optional[bool]
            Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
            in messages the user sends.

        display_emoji_reaction_users : typing.Optional[bool]
            Whether to display the names of reacting users on a message.

            When enabled, clients should display the names of reacting users, rather than
            a count, for messages with few total reactions. The ideal cutoff may depend on
            the space available for displaying reactions; the official web application
            displays names when 3 or fewer total reactions are present with this setting
            enabled.

            **Changes**: New in Zulip 6.0 (feature level 125).

        web_home_view : typing.Optional[str]
            The [home view](/help/configure-home-view) used when opening a new
            Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

            - "recent" - Recent conversations view
            - "inbox" - Inbox view
            - "all_messages" - Combined feed view

            **Changes**: Before Zulip 12.0 (feature level 454), the Recent
            view had `"recent_topics"` as its string encoding.

            New in Zulip 8.0 (feature level 219). Previously, this was
            called `default_view`, which was new in Zulip 4.0 (feature level 42).

        web_escape_navigates_to_home_view : typing.Optional[bool]
            Whether the escape key navigates to the
            [configured home view](/help/configure-home-view).

            **Changes**: New in Zulip 8.0 (feature level 219). Previously, this was called
            `escape_navigates_to_default_view`, which was new in Zulip 5.0 (feature level 107).

        left_side_userlist : typing.Optional[bool]
            Whether the users list on left sidebar in narrow windows.

            This feature is not heavily used and is likely to be reworked.

        emojiset : typing.Optional[str]
            The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
            used to display emoji to the user everywhere they appear in the UI.

            - "google" - Google
            - "twitter" - Twitter
            - "text" - Plain text

        demote_inactive_streams : typing.Optional[int]
            Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

        user_list_style : typing.Optional[int]
            The style selected by the user for the right sidebar user list.

            - 1 - Compact
            - 2 - With status
            - 3 - With avatar and status

            **Changes**: New in Zulip 6.0 (feature level 141).

        web_animate_image_previews : typing.Optional[UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews]
            Controls how animated images should be played in the message feed in the web/desktop application.

            - "always" - Always play the animated images in the message feed.
            - "on_hover" - Play the animated images on hover over them in the message feed.
            - "never" - Never play animated images in the message feed.

            **Changes**: New in Zulip 9.0 (feature level 275). Previously, animated images
            always used to play in the message feed by default. This setting controls this
            behaviour.

        web_stream_unreads_count_display_policy : typing.Optional[int]
            Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
            Channels that do not have an unread count will have a simple dot indicator for whether there are any
            unread messages.

            - 1 - All channels
            - 2 - Unmuted channels and topics
            - 3 - No channels

            **Changes**: New in Zulip 8.0 (feature level 210).

        hide_ai_features : typing.Optional[bool]
            Controls whether user wants AI features like topic summarization to
            be hidden in all Zulip clients.

            **Changes**: New in Zulip 10.0 (feature level 350).

        web_inbox_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how conversations with unread messages
            are displayed in the web/desktop application's Inbox view.

            **Changes**: New in Zulip 12.0 (feature level 431).

        web_left_sidebar_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how channels are displayed in the
            web/desktop application's left sidebar.

            **Changes**: New in Zulip 11.0 (feature level 411).

        web_left_sidebar_unreads_count_summary : typing.Optional[bool]
            Determines whether the web/desktop application's left sidebar displays
            the unread message count summary.

            **Changes**: New in Zulip 11.0 (feature level 398).

        enable_stream_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for channel messages.

        enable_stream_email_notifications : typing.Optional[bool]
            Enable email notifications for channel messages.

        enable_stream_push_notifications : typing.Optional[bool]
            Enable mobile notifications for channel messages.

        enable_stream_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for channel messages.

        notification_sound : typing.Optional[str]
            Notification sound name.

        enable_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for direct messages and @-mentions.

        enable_sounds : typing.Optional[bool]
            Enable audible desktop notifications for direct messages and
            @-mentions.

        enable_followed_topic_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_email_notifications : typing.Optional[bool]
            Enable email notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_push_notifications : typing.Optional[bool]
            Enable push notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        email_notifications_batching_period_seconds : typing.Optional[int]
            The duration (in seconds) for which the server should wait to batch
            email notifications before sending them.

        enable_offline_email_notifications : typing.Optional[bool]
            Enable email notifications for direct messages and @-mentions received
            when the user is offline.

        enable_offline_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is offline.

        enable_online_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is online.

        enable_digest_emails : typing.Optional[bool]
            Enable digest emails when the user is away.

        message_content_in_email_notifications : typing.Optional[bool]
            Include the message's content in email notifications for new messages.

        pm_content_in_desktop_notifications : typing.Optional[bool]
            Include content of direct messages in desktop notifications.

        wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (E.g. @**all**) should send notifications
            like a personal mention.

        enable_followed_topic_wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
            should send notifications like a personal mention.

            **Changes**: New in Zulip 8.0 (feature level 189).

        desktop_icon_count_display : typing.Optional[int]
            Unread count badge (appears in desktop sidebar and browser tab)

            - 1 - All unread messages
            - 2 - DMs, mentions, and followed topics
            - 3 - DMs and mentions
            - 4 - None

            **Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
            topics` option, renumbering the options to insert it in order.

        realm_name_in_email_notifications_policy : typing.Optional[int]
            Whether to [include organization name in subject of message notification
            emails](/help/email-notifications#include-organization-name-in-subject-line).

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 168), replacing the
            previous `realm_name_in_notifications` boolean;
            `true` corresponded to `Always`, and `false` to `Never`.

        automatically_follow_topics_policy : typing.Optional[int]
            Which [topics to follow automatically](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_unmute_topics_in_muted_streams_policy : typing.Optional[int]
            Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_follow_topics_where_mentioned : typing.Optional[bool]
            Whether the server will automatically mark the user as following
            topics where the user is mentioned.

            **Changes**: New in Zulip 8.0 (feature level 235).

        resolved_topic_notice_auto_read_policy : typing.Optional[UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy]
            Controls whether the resolved-topic notices are marked as read.

            - "always" - Always mark resolved-topic notices as read.
            - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
            - "never" - Never mark resolved-topic notices as read.

            **Changes**: New in Zulip 11.0 (feature level 385).

        presence_enabled : typing.Optional[bool]
            Display the presence status to other users when online.

        enter_sends : typing.Optional[bool]
            Whether pressing Enter in the compose box sends a message
            (or saves a message edit).

        twenty_four_hour_time : typing.Optional[bool]
            Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

            **Changes**: New in Zulip 5.0 (feature level 99).
            Previously, this default was edited using the
            `default_twenty_four_hour_time` parameter to the `PATCH /realm` endpoint.

        send_private_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            direct messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_stream_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            channel messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_read_receipts : typing.Optional[bool]
            Whether other users are allowed to see whether you've
            read messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        email_address_visibility : typing.Optional[int]
            The [policy][permission-level] for [which other users][help-email-visibility]
            in this organization can see the user's real email address.

            - 1 = Everyone
            - 2 = Members only
            - 3 = Administrators only
            - 4 = Nobody
            - 5 = Moderators only

            **Changes**: New in Zulip 7.0 (feature level 163), replacing the
            realm-level setting.

            [permission-level]: /api/roles-and-permissions#permission-levels
            [help-email-visibility]: /help/configure-email-visibility

        web_navigate_to_sent_message : typing.Optional[bool]
            Web/desktop app setting for whether the user's view should
            automatically go to the conversation where they sent a message.

            **Changes**: New in Zulip 9.0 (feature level 268). Previously,
            this behavior was not configurable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IgnoredParametersSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/user_settings_defaults",
            method="PATCH",
            data={
                "starred_message_counts": starred_message_counts,
                "receives_typing_notifications": receives_typing_notifications,
                "web_suggest_update_timezone": web_suggest_update_timezone,
                "fluid_layout_width": fluid_layout_width,
                "high_contrast_mode": high_contrast_mode,
                "web_mark_read_on_scroll_policy": web_mark_read_on_scroll_policy,
                "web_channel_default_view": web_channel_default_view,
                "web_font_size_px": web_font_size_px,
                "web_line_height_percent": web_line_height_percent,
                "color_scheme": color_scheme,
                "enable_drafts_synchronization": enable_drafts_synchronization,
                "translate_emoticons": translate_emoticons,
                "display_emoji_reaction_users": display_emoji_reaction_users,
                "web_home_view": web_home_view,
                "web_escape_navigates_to_home_view": web_escape_navigates_to_home_view,
                "left_side_userlist": left_side_userlist,
                "emojiset": emojiset,
                "demote_inactive_streams": demote_inactive_streams,
                "user_list_style": user_list_style,
                "web_animate_image_previews": web_animate_image_previews,
                "web_stream_unreads_count_display_policy": web_stream_unreads_count_display_policy,
                "hide_ai_features": hide_ai_features,
                "web_inbox_show_channel_folders": web_inbox_show_channel_folders,
                "web_left_sidebar_show_channel_folders": web_left_sidebar_show_channel_folders,
                "web_left_sidebar_unreads_count_summary": web_left_sidebar_unreads_count_summary,
                "enable_stream_desktop_notifications": enable_stream_desktop_notifications,
                "enable_stream_email_notifications": enable_stream_email_notifications,
                "enable_stream_push_notifications": enable_stream_push_notifications,
                "enable_stream_audible_notifications": enable_stream_audible_notifications,
                "notification_sound": notification_sound,
                "enable_desktop_notifications": enable_desktop_notifications,
                "enable_sounds": enable_sounds,
                "enable_followed_topic_desktop_notifications": enable_followed_topic_desktop_notifications,
                "enable_followed_topic_email_notifications": enable_followed_topic_email_notifications,
                "enable_followed_topic_push_notifications": enable_followed_topic_push_notifications,
                "enable_followed_topic_audible_notifications": enable_followed_topic_audible_notifications,
                "email_notifications_batching_period_seconds": email_notifications_batching_period_seconds,
                "enable_offline_email_notifications": enable_offline_email_notifications,
                "enable_offline_push_notifications": enable_offline_push_notifications,
                "enable_online_push_notifications": enable_online_push_notifications,
                "enable_digest_emails": enable_digest_emails,
                "message_content_in_email_notifications": message_content_in_email_notifications,
                "pm_content_in_desktop_notifications": pm_content_in_desktop_notifications,
                "wildcard_mentions_notify": wildcard_mentions_notify,
                "enable_followed_topic_wildcard_mentions_notify": enable_followed_topic_wildcard_mentions_notify,
                "desktop_icon_count_display": desktop_icon_count_display,
                "realm_name_in_email_notifications_policy": realm_name_in_email_notifications_policy,
                "automatically_follow_topics_policy": automatically_follow_topics_policy,
                "automatically_unmute_topics_in_muted_streams_policy": automatically_unmute_topics_in_muted_streams_policy,
                "automatically_follow_topics_where_mentioned": automatically_follow_topics_where_mentioned,
                "resolved_topic_notice_auto_read_policy": resolved_topic_notice_auto_read_policy,
                "presence_enabled": presence_enabled,
                "enter_sends": enter_sends,
                "twenty_four_hour_time": twenty_four_hour_time,
                "send_private_typing_notifications": send_private_typing_notifications,
                "send_stream_typing_notifications": send_stream_typing_notifications,
                "send_read_receipts": send_read_receipts,
                "email_address_visibility": email_address_visibility,
                "web_navigate_to_sent_message": web_navigate_to_sent_message,
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
                    IgnoredParametersSuccess,
                    parse_obj_as(
                        type_=IgnoredParametersSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_linkifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLinkifiersResponse]:
        """
        List all of an organization's configured
        [linkifiers](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        **Changes**: New in Zulip 4.0 (feature level 54). On older versions,
        a similar `GET /realm/filters` endpoint was available with each entry in
        a `[pattern, url_format, id]` tuple format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLinkifiersResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/linkifiers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinkifiersResponse,
                    parse_obj_as(
                        type_=GetLinkifiersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reorder_linkifiers(
        self, *, ordered_linkifier_ids: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Change the order that the regular expression patterns in the organization's
        [linkifiers](/help/add-a-custom-linkifier) are matched in messages and topics.
        Useful when defining linkifiers with overlapping patterns.

        **Changes**: New in Zulip 8.0 (feature level 202). Before this feature level,
        linkifiers were always processed in order by ID, which meant users would
        need to delete and recreate them to reorder the list of linkifiers.

        Parameters
        ----------
        ordered_linkifier_ids : typing.Sequence[int]
            A list of the IDs of all the linkifiers defined in this
            organization, in the desired new order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/linkifiers",
            method="PATCH",
            data={
                "ordered_linkifier_ids": ordered_linkifier_ids,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_linkifier(
        self,
        *,
        pattern: LinkifierPattern,
        url_template: LinkifierUrlTemplate,
        example_input: typing.Optional[str] = OMIT,
        reverse_template: typing.Optional[str] = OMIT,
        alternative_url_templates: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddLinkifierResponse]:
        """
        Configure [linkifiers](/help/add-a-custom-linkifier),
        regular expression patterns that are automatically linkified when they
        appear in messages and topics.

        Parameters
        ----------
        pattern : LinkifierPattern

        url_template : LinkifierUrlTemplate

        example_input : typing.Optional[str]
            An example input string that matches the linkifier's pattern.
            This is required for reverse linkifiers.

            **Changes**: New in Zulip 12.0 (feature level 471).

        reverse_template : typing.Optional[str]
            A simple template using `{variable}` for variables that can
            be used to generate the Markdown linkifier syntax, given a
            URL matching the URL template.

            `{{ "{{/}}" }}` can be used for literal `{/}` characters.

            Server verifies that variables extracted from example_input using
            url_pattern when passed to reverse_template returns example_input
            back to us.

            **Changes**: New in Zulip 12.0 (feature level 471).

        alternative_url_templates : typing.Optional[typing.Sequence[str]]
            An array of additional [RFC 6570][rfc6570] compliant URL
            template strings that are used for reverse linkification
            (converting pasted URLs to linkifier pattern text). These
            templates have no effect on forward linkification.

            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

            **Changes**: New in Zulip 12.0 (feature level e2b257).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddLinkifierResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/filters",
            method="POST",
            data={
                "pattern": pattern,
                "url_template": url_template,
                "example_input": example_input,
                "reverse_template": reverse_template,
                "alternative_url_templates": alternative_url_templates,
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
                    AddLinkifierResponse,
                    parse_obj_as(
                        type_=AddLinkifierResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_linkifier(
        self, filter_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Remove [linkifiers](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        Parameters
        ----------
        filter_id : int
            The ID of the linkifier that you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/filters/{encode_path_param(filter_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_linkifier(
        self,
        filter_id: int,
        *,
        pattern: LinkifierPattern,
        url_template: LinkifierUrlTemplate,
        example_input: typing.Optional[str] = OMIT,
        reverse_template: typing.Optional[str] = OMIT,
        alternative_url_templates: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Update a [linkifier](/help/add-a-custom-linkifier), regular
        expression patterns that are automatically linkified when they appear
        in messages and topics.

        **Changes**: New in Zulip 4.0 (feature level 57).

        Parameters
        ----------
        filter_id : int
            The ID of the linkifier that you want to update.

        pattern : LinkifierPattern

        url_template : LinkifierUrlTemplate

        example_input : typing.Optional[str]
            An example input string that matches the linkifier's pattern.
            This is required for reverse linkifiers. Passing an empty string
            will set this field back to null.

            **Changes**: New in Zulip 12.0 (feature level 471).

        reverse_template : typing.Optional[str]
            A simple template using `{variable}` for variables that can
            be used to generate the Markdown linkifier syntax, given a
            URL matching the URL template. Passing an empty string
            will set this field back to null.

            Server verifies that variables extracted from example_input using
            url_pattern when passed to reverse_template returns example_input
            back to us.

            `{{ "{{/}}" }}` can be used for literal `{/}` characters.

            **Changes**: New in Zulip 12.0 (feature level 471).

        alternative_url_templates : typing.Optional[typing.Sequence[str]]
            An array of additional [RFC 6570][rfc6570] compliant URL
            template strings that are used for reverse linkification
            (converting pasted URLs to linkifier pattern text). These
            templates have no effect on forward linkification.

            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

            **Changes**: New in Zulip 12.0 (feature level e2b257).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/filters/{encode_path_param(filter_id)}",
            method="PATCH",
            data={
                "pattern": pattern,
                "url_template": url_template,
                "example_input": example_input,
                "reverse_template": reverse_template,
                "alternative_url_templates": alternative_url_templates,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_code_playground(
        self,
        *,
        name: str,
        pygments_language: str,
        url_template: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddCodePlaygroundResponse]:
        """
        Configure [code playgrounds](/help/code-blocks#code-playgrounds) for the organization.

        **Changes**: New in Zulip 4.0 (feature level 49). A parameter encoding bug was
        fixed in Zulip 4.0 (feature level 57).

        Parameters
        ----------
        name : str
            The user-visible display name of the playground which can be
            used to pick the target playground, especially when multiple
            playground options exist for that programming language.

        pygments_language : str
            The name of the Pygments language lexer for that
            programming language.

        url_template : str
            The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html)
            compliant URL template for the playground. The template should
            contain exactly one variable named `code`, which determines how the
            extracted code should be substituted in the playground URL.

            **Changes**: New in Zulip 8.0 (feature level 196). This replaced the
            `url_prefix` parameter, which was used to construct URLs by just
            concatenating `url_prefix` and `code`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddCodePlaygroundResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/playgrounds",
            method="POST",
            data={
                "name": name,
                "pygments_language": pygments_language,
                "url_template": url_template,
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
                    AddCodePlaygroundResponse,
                    parse_obj_as(
                        type_=AddCodePlaygroundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_code_playground(
        self, playground_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Remove a [code playground](/help/code-blocks#code-playgrounds) previously
        configured for an organization.

        **Changes**: New in Zulip 4.0 (feature level 49).

        Parameters
        ----------
        playground_id : int
            The ID of the playground that you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"realm/playgrounds/{encode_path_param(playground_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_realm_export(
        self, export_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete a completed public or standard [data export][export-data]
        of the organization.

        Data exports that happened on a previous server (i.e., an export
        with `"export_from_prior_server": true` in the
        [`GET /export/realm`](/api/get-realm-exports#response) response)
        cannot be deleted using this endpoint, since their tarball is no
        longer stored on this server; attempting to do so fails with
        the same error as for an export that has already been deleted.

        This endpoint's success response does not describe the resulting
        state of the organization's data exports. Clients should rely
        on the [`realm_export` event](/api/get-events#realm_export),
        which every organization administrator receives whenever a
        data export's state changes, for the current state of an
        organization's data exports.

        **Changes**: Prior to Zulip 13.0 (feature level 506), data
        exports without a tarball stored on this server had no
        dedicated status, so attempting to delete one resulted in an
        unexpected error. Starting at that feature level, such a
        delete attempt instead fails cleanly, as described above. This
        change was also backported to the Zulip 12.x series, at
        feature level 499.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format

        Parameters
        ----------
        export_id : int
            The ID of the data export to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"export/realm/{encode_path_param(export_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_realm_exports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRealmExportsResponse]:
        """
        Fetch all the public and standard [data exports][export-data]
        of the organization.

        **Changes**: Prior to Zulip 10.0 (feature level 304), only
        public data exports could be fetched using this endpoint.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRealmExportsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "export/realm",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmExportsResponse,
                    parse_obj_as(
                        type_=GetRealmExportsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def export_realm(
        self,
        *,
        export_type: typing.Optional[ExportRealmRequestExportType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportRealmResponse]:
        """
        !!! warn ""

            **Note**: If you're the administrator of a self-hosted installation,
            you may be looking for the documentation on [server data export and
            import][data-export] or [server backups][backups].

        Create a public or a standard [data export][export-data] of the
        organization.

        This endpoint only queues the data export; it does not wait for
        the export to complete, which depending on the size of the
        organization can take anywhere from seconds to an hour.
        Therefore, this endpoint's success response does not describe
        the outcome of the export.

        To find out the outcome of the export, clients should rely on the
        [`realm_export` event](/api/get-events#realm_export), which is
        which is sent to every organization administrator immediately
        when the export is requested, and again once it completes or
        fails. Additionally, when the export succeeds, the user who
        requested it will receive a direct message from the Notification
        Bot with a link to the organization's data exports panel, where
        the export can be downloaded.

        **Changes**: Prior to Zulip 10.0 (feature level 304), only public
        data exports could be created using this endpoint.

        New in Zulip 2.1.

        [export-data]: /help/export-your-organization#export-data-in-an-importable-format
        [data-export]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#data-export
        [backups]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#backups

        Parameters
        ----------
        export_type : typing.Optional[ExportRealmRequestExportType]
            Whether the data export should be public, full with consent,
            or full without consent.

            - `public` = Public data only export.
            - `full_with_consent` = Public and private data export (with consent), which includes
              private data for users who have granted consent.
            - `full_without_consent` = All public and private data export, which includes private data for
              all users. This option requires the organization to have
              the `owner_full_content_access` feature enabled.

            If not specified, defaults to `public`.

            **Changes**: Zulip 12.0 (feature level 449) changed the type of
            this field from int to string with `1` being replaced by `public` and
            `2` being replaced by `full_with_consent`. The option `full_without_consent`
            was added for full exports without member consent.

            New in Zulip 10.0 (feature level 304). Previously,
            all export requests were public data exports.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportRealmResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "export/realm",
            method="POST",
            data={
                "export_type": export_type,
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
                    ExportRealmResponse,
                    parse_obj_as(
                        type_=ExportRealmResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_realm_export_consents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRealmExportConsentsResponse]:
        """
        Fetches which users have [consented](/help/export-your-organization#configure-whether-administrators-can-export-your-private-data)
        for their private data to be exported by organization administrators.

        **Changes**: Changes in Zulip 12.0 (feature level 430). Added an
        integer field `email_address_visibility` to the objects in the
        `export_consents` array.

        New in Zulip 10.0 (feature level 295).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRealmExportConsentsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "export/realm/consents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRealmExportConsentsResponse,
                    parse_obj_as(
                        type_=GetRealmExportConsentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_welcome_bot_custom_message(
        self, *, welcome_message_custom_text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestWelcomeBotCustomMessageResponse]:
        """
        Sends a test Welcome Bot custom message to the acting administrator.
        This allows administrators to preview how the custom welcome message will
        appear when received by new users upon joining the organization.

        **Changes**: New in Zulip 11.0 (feature level 416).

        Parameters
        ----------
        welcome_message_custom_text : str
            Custom message text, in Zulip Markdown format, to be used for
            this test message.

            Maximum length is 8000 Unicode code points.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestWelcomeBotCustomMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "realm/test_welcome_bot_custom_message",
            method="POST",
            data={
                "welcome_message_custom_text": welcome_message_custom_text,
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
                    TestWelcomeBotCustomMessageResponse,
                    parse_obj_as(
                        type_=TestWelcomeBotCustomMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_server_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetServerSettingsResponse]:
        """
        Fetch global settings for a Zulip server.

        **Note:** this endpoint does not require any authentication at all, and you can use it to check:

        - If this is a Zulip server, and if so, what version of Zulip it's running.
        - What a Zulip client (e.g. a mobile app or
          [zulip-terminal](https://github.com/zulip/zulip-terminal/)) needs to
          know in order to display a login prompt for the server (e.g. what
          authentication methods are available).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetServerSettingsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "server_settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServerSettingsResponse,
                    parse_obj_as(
                        type_=GetServerSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
