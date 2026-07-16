

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.destiny2awa_get_action_token_response import Destiny2AwaGetActionTokenResponse
from .types.destiny2awa_initialize_request_response import Destiny2AwaInitializeRequestResponse
from .types.destiny2awa_provide_authorization_result_response import Destiny2AwaProvideAuthorizationResultResponse
from .types.destiny2clear_loadout_response import Destiny2ClearLoadoutResponse
from .types.destiny2equip_item_response import Destiny2EquipItemResponse
from .types.destiny2equip_items_response import Destiny2EquipItemsResponse
from .types.destiny2equip_loadout_response import Destiny2EquipLoadoutResponse
from .types.destiny2get_activity_history_response import Destiny2GetActivityHistoryResponse
from .types.destiny2get_character_response import Destiny2GetCharacterResponse
from .types.destiny2get_clan_aggregate_stats_response import Destiny2GetClanAggregateStatsResponse
from .types.destiny2get_clan_banner_source_response import Destiny2GetClanBannerSourceResponse
from .types.destiny2get_clan_leaderboards_response import Destiny2GetClanLeaderboardsResponse
from .types.destiny2get_clan_weekly_reward_state_response import Destiny2GetClanWeeklyRewardStateResponse
from .types.destiny2get_collectible_node_details_response import Destiny2GetCollectibleNodeDetailsResponse
from .types.destiny2get_destiny_aggregate_activity_stats_response import (
    Destiny2GetDestinyAggregateActivityStatsResponse,
)
from .types.destiny2get_destiny_entity_definition_response import Destiny2GetDestinyEntityDefinitionResponse
from .types.destiny2get_destiny_manifest_response import Destiny2GetDestinyManifestResponse
from .types.destiny2get_historical_stats_definition_response import Destiny2GetHistoricalStatsDefinitionResponse
from .types.destiny2get_historical_stats_for_account_response import Destiny2GetHistoricalStatsForAccountResponse
from .types.destiny2get_historical_stats_response import Destiny2GetHistoricalStatsResponse
from .types.destiny2get_item_response import Destiny2GetItemResponse
from .types.destiny2get_leaderboards_for_character_response import Destiny2GetLeaderboardsForCharacterResponse
from .types.destiny2get_leaderboards_response import Destiny2GetLeaderboardsResponse
from .types.destiny2get_linked_profiles_response import Destiny2GetLinkedProfilesResponse
from .types.destiny2get_post_game_carnage_report_response import Destiny2GetPostGameCarnageReportResponse
from .types.destiny2get_profile_response import Destiny2GetProfileResponse
from .types.destiny2get_public_milestone_content_response import Destiny2GetPublicMilestoneContentResponse
from .types.destiny2get_public_milestones_response import Destiny2GetPublicMilestonesResponse
from .types.destiny2get_public_vendors_response import Destiny2GetPublicVendorsResponse
from .types.destiny2get_unique_weapon_history_response import Destiny2GetUniqueWeaponHistoryResponse
from .types.destiny2get_vendor_response import Destiny2GetVendorResponse
from .types.destiny2get_vendors_response import Destiny2GetVendorsResponse
from .types.destiny2insert_socket_plug_free_response import Destiny2InsertSocketPlugFreeResponse
from .types.destiny2insert_socket_plug_response import Destiny2InsertSocketPlugResponse
from .types.destiny2pull_from_postmaster_response import Destiny2PullFromPostmasterResponse
from .types.destiny2report_offensive_post_game_carnage_report_player_response import (
    Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
)
from .types.destiny2search_destiny_entities_response import Destiny2SearchDestinyEntitiesResponse
from .types.destiny2search_destiny_player_by_bungie_name_response import Destiny2SearchDestinyPlayerByBungieNameResponse
from .types.destiny2set_item_lock_state_response import Destiny2SetItemLockStateResponse
from .types.destiny2set_quest_tracked_state_response import Destiny2SetQuestTrackedStateResponse
from .types.destiny2snapshot_loadout_response import Destiny2SnapshotLoadoutResponse
from .types.destiny2transfer_item_response import Destiny2TransferItemResponse
from .types.destiny2update_loadout_identifiers_response import Destiny2UpdateLoadoutIdentifiersResponse
from pydantic import ValidationError


class RawDestiny2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def equipitem(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2EquipItemResponse]:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2EquipItemResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/EquipItem/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipItemResponse,
                    parse_obj_as(
                        type_=Destiny2EquipItemResponse,
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

    def equipitems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2EquipItemsResponse]:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2EquipItemsResponse]
            The results of a bulk Equipping operation performed through the Destiny API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/EquipItems/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipItemsResponse,
                    parse_obj_as(
                        type_=Destiny2EquipItemsResponse,
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

    def insertsocketplug(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2InsertSocketPlugResponse]:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2InsertSocketPlugResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/InsertSocketPlug/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2InsertSocketPlugResponse,
                    parse_obj_as(
                        type_=Destiny2InsertSocketPlugResponse,
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

    def insertsocketplugfree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2InsertSocketPlugFreeResponse]:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2InsertSocketPlugFreeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/InsertSocketPlugFree/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2InsertSocketPlugFreeResponse,
                    parse_obj_as(
                        type_=Destiny2InsertSocketPlugFreeResponse,
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

    def pullfrompostmaster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2PullFromPostmasterResponse]:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2PullFromPostmasterResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/PullFromPostmaster/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2PullFromPostmasterResponse,
                    parse_obj_as(
                        type_=Destiny2PullFromPostmasterResponse,
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

    def setitemlockstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2SetItemLockStateResponse]:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2SetItemLockStateResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/SetLockState/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SetItemLockStateResponse,
                    parse_obj_as(
                        type_=Destiny2SetItemLockStateResponse,
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

    def setquesttrackedstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2SetQuestTrackedStateResponse]:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2SetQuestTrackedStateResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/SetTrackedState/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SetQuestTrackedStateResponse,
                    parse_obj_as(
                        type_=Destiny2SetQuestTrackedStateResponse,
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

    def transferitem(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2TransferItemResponse]:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2TransferItemResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/TransferItem/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2TransferItemResponse,
                    parse_obj_as(
                        type_=Destiny2TransferItemResponse,
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

    def clearloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2ClearLoadoutResponse]:
        """
        Clear the identifiers and items of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2ClearLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/ClearLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2ClearLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2ClearLoadoutResponse,
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

    def equiploadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2EquipLoadoutResponse]:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2EquipLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/EquipLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2EquipLoadoutResponse,
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

    def snapshotloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2SnapshotLoadoutResponse]:
        """
        Snapshot a loadout with the currently equipped items.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2SnapshotLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/SnapshotLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SnapshotLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2SnapshotLoadoutResponse,
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

    def updateloadoutidentifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2UpdateLoadoutIdentifiersResponse]:
        """
        Update the color, icon, and name of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2UpdateLoadoutIdentifiersResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2UpdateLoadoutIdentifiersResponse,
                    parse_obj_as(
                        type_=Destiny2UpdateLoadoutIdentifiersResponse,
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

    def searchdestinyentities(
        self,
        type: str,
        search_term: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2SearchDestinyEntitiesResponse]:
        """
        Gets a page list of Destiny items.

        Parameters
        ----------
        type : str
            The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.

        search_term : str
            The string to use when searching for Destiny entities.

        page : typing.Optional[int]
            Page number to return, starting with 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2SearchDestinyEntitiesResponse]
            The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Armory/Search/{encode_path_param(type)}/{encode_path_param(search_term)}/",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SearchDestinyEntitiesResponse,
                    parse_obj_as(
                        type_=Destiny2SearchDestinyEntitiesResponse,
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

    def awaprovideauthorizationresult(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2AwaProvideAuthorizationResultResponse]:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2AwaProvideAuthorizationResultResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Awa/AwaProvideAuthorizationResult/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaProvideAuthorizationResultResponse,
                    parse_obj_as(
                        type_=Destiny2AwaProvideAuthorizationResultResponse,
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

    def awagetactiontoken(
        self, correlation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2AwaGetActionTokenResponse]:
        """
        Returns the action token if user approves the request.

        Parameters
        ----------
        correlation_id : str
            The identifier for the advanced write action request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2AwaGetActionTokenResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Awa/GetActionToken/{encode_path_param(correlation_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaGetActionTokenResponse,
                    parse_obj_as(
                        type_=Destiny2AwaGetActionTokenResponse,
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

    def awainitializerequest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2AwaInitializeRequestResponse]:
        """
        Initialize a request to perform an advanced write action.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2AwaInitializeRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Awa/Initialize/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaInitializeRequestResponse,
                    parse_obj_as(
                        type_=Destiny2AwaInitializeRequestResponse,
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

    def getclanbannersource(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetClanBannerSourceResponse]:
        """
        Returns the dictionary of values for the Clan Banner

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetClanBannerSourceResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Clan/ClanBannerDictionary/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanBannerSourceResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanBannerSourceResponse,
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

    def getclanweeklyrewardstate(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetClanWeeklyRewardStateResponse]:
        """
        Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

        Parameters
        ----------
        group_id : int
            A valid group id of clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetClanWeeklyRewardStateResponse]
            Represents a runtime instance of a user's milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said "things to do." Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Clan/{encode_path_param(group_id)}/WeeklyRewardState/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanWeeklyRewardStateResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanWeeklyRewardStateResponse,
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

    def getdestinymanifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetDestinyManifestResponse]:
        """
        Returns the current version of the manifest as a json object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetDestinyManifestResponse]
            DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Manifest/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyManifestResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyManifestResponse,
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

    def getdestinyentitydefinition(
        self, entity_type: str, hash_identifier: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetDestinyEntityDefinitionResponse]:
        """
        Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

        Parameters
        ----------
        entity_type : str
            The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.

        hash_identifier : int
            The hash identifier for the specific Entity you want returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetDestinyEntityDefinitionResponse]
            Provides common properties for destiny definitions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Manifest/{encode_path_param(entity_type)}/{encode_path_param(hash_identifier)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyEntityDefinitionResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyEntityDefinitionResponse,
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

    def getpublicmilestones(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetPublicMilestonesResponse]:
        """
        Gets public information about currently available Milestones.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetPublicMilestonesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Milestones/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicMilestonesResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicMilestonesResponse,
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

    def getpublicmilestonecontent(
        self, milestone_hash: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetPublicMilestoneContentResponse]:
        """
        Gets custom localized content for the milestone of the given hash, if it exists.

        Parameters
        ----------
        milestone_hash : int
            The identifier for the milestone to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetPublicMilestoneContentResponse]
            Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Milestones/{encode_path_param(milestone_hash)}/Content/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicMilestoneContentResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicMilestoneContentResponse,
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

    def searchdestinyplayerbybungiename(
        self, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2SearchDestinyPlayerByBungieNameResponse]:
        """
        Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2SearchDestinyPlayerByBungieNameResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/SearchDestinyPlayerByBungieName/{encode_path_param(membership_type)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SearchDestinyPlayerByBungieNameResponse,
                    parse_obj_as(
                        type_=Destiny2SearchDestinyPlayerByBungieNameResponse,
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

    def getclanaggregatestats(
        self,
        group_id: int,
        *,
        modes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetClanAggregateStatsResponse]:
        """
        Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        group_id : int
            Group ID of the clan whose leaderboards you wish to fetch.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetClanAggregateStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/AggregateClanStats/{encode_path_param(group_id)}/",
            method="GET",
            params={
                "modes": modes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanAggregateStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanAggregateStatsResponse,
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

    def gethistoricalstatsdefinition(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetHistoricalStatsDefinitionResponse]:
        """
        Gets historical stats definitions.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetHistoricalStatsDefinitionResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Stats/Definition/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsDefinitionResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsDefinitionResponse,
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

    def getclanleaderboards(
        self,
        group_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetClanLeaderboardsResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        group_id : int
            Group ID of the clan whose leaderboards you wish to fetch.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetClanLeaderboardsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/Leaderboards/Clans/{encode_path_param(group_id)}/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanLeaderboardsResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanLeaderboardsResponse,
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

    def getleaderboardsforcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetLeaderboardsForCharacterResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The specific character to build the leaderboard around for the provided Destiny Membership.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetLeaderboardsForCharacterResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/Leaderboards/{encode_path_param(membership_type)}/{encode_path_param(destiny_membership_id)}/{encode_path_param(character_id)}/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLeaderboardsForCharacterResponse,
                    parse_obj_as(
                        type_=Destiny2GetLeaderboardsForCharacterResponse,
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

    def getpostgamecarnagereport(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2GetPostGameCarnageReportResponse]:
        """
        Gets the available post game carnage report for the activity ID.

        Parameters
        ----------
        activity_id : int
            The ID of the activity whose PGCR is requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetPostGameCarnageReportResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/PostGameCarnageReport/{encode_path_param(activity_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPostGameCarnageReportResponse,
                    parse_obj_as(
                        type_=Destiny2GetPostGameCarnageReportResponse,
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

    def reportoffensivepostgamecarnagereportplayer(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Destiny2ReportOffensivePostGameCarnageReportPlayerResponse]:
        """
        Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

        Parameters
        ----------
        activity_id : int
            The ID of the activity where you ran into the brigand that you're reporting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2ReportOffensivePostGameCarnageReportPlayerResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/PostGameCarnageReport/{encode_path_param(activity_id)}/Report/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
                    parse_obj_as(
                        type_=Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
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

    def getpublicvendors(
        self,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetPublicVendorsResponse]:
        """
        Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'

        Parameters
        ----------
        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetPublicVendorsResponse]
            A response containing all valid components for the public Vendors endpoint.
             It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
             If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.
        """
        _response = self._client_wrapper.httpx_client.request(
            "Destiny2/Vendors/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicVendorsResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicVendorsResponse,
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

    def gethistoricalstats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        dayend: typing.Optional[dt.datetime] = None,
        daystart: typing.Optional[dt.datetime] = None,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        modes: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        period_type: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetHistoricalStatsResponse]:
        """
        Gets historical stats for indicated character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.

        dayend : typing.Optional[dt.datetime]
            Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.

        daystart : typing.Optional[dt.datetime]
            First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.

        groups : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals

        modes : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        period_type : typing.Optional[int]
            Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetHistoricalStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/",
            method="GET",
            params={
                "dayend": serialize_datetime(dayend) if dayend is not None else None,
                "daystart": serialize_datetime(daystart) if daystart is not None else None,
                "groups": ",".join(map(str, groups)) if isinstance(groups, (list, tuple, set)) else groups,
                "modes": ",".join(map(str, modes)) if isinstance(modes, (list, tuple, set)) else modes,
                "periodType": period_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsResponse,
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

    def getactivityhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        count: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetActivityHistoryResponse]:
        """
        Gets activity history stats for indicated character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve.

        count : typing.Optional[int]
            Number of rows to return

        mode : typing.Optional[int]
            A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.

        page : typing.Optional[int]
            Page number to return, starting with 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetActivityHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/Activities/",
            method="GET",
            params={
                "count": count,
                "mode": mode,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetActivityHistoryResponse,
                    parse_obj_as(
                        type_=Destiny2GetActivityHistoryResponse,
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

    def getdestinyaggregateactivitystats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetDestinyAggregateActivityStatsResponse]:
        """
        Gets all activities the character has participated in together with aggregate statistics for those activities.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The specific character whose activities should be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetDestinyAggregateActivityStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/AggregateActivityStats/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyAggregateActivityStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyAggregateActivityStatsResponse,
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

    def getuniqueweaponhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetUniqueWeaponHistoryResponse]:
        """
        Gets details about unique weapon usage, including all exotic weapons.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetUniqueWeaponHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/UniqueWeapons/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetUniqueWeaponHistoryResponse,
                    parse_obj_as(
                        type_=Destiny2GetUniqueWeaponHistoryResponse,
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

    def gethistoricalstatsforaccount(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetHistoricalStatsForAccountResponse]:
        """
        Gets aggregate historical stats organized around each character for a given account.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        groups : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetHistoricalStatsForAccountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Stats/",
            method="GET",
            params={
                "groups": ",".join(map(str, groups)) if isinstance(groups, (list, tuple, set)) else groups,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsForAccountResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsForAccountResponse,
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

    def getleaderboards(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetLeaderboardsResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetLeaderboardsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Stats/Leaderboards/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLeaderboardsResponse,
                    parse_obj_as(
                        type_=Destiny2GetLeaderboardsResponse,
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

    def getprofile(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetProfileResponse]:
        """
        Returns Destiny Profile information for the supplied membership.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetProfileResponse]
            The response for GetDestinyProfile, with components for character and item-level data.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetProfileResponse,
                    parse_obj_as(
                        type_=Destiny2GetProfileResponse,
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

    def getcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetCharacterResponse]:
        """
        Returns character information for the supplied character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID.

        character_id : int
            ID of the character.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetCharacterResponse]
            The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetCharacterResponse,
                    parse_obj_as(
                        type_=Destiny2GetCharacterResponse,
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

    def getcollectiblenodedetails(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        collectible_presentation_node_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetCollectibleNodeDetailsResponse]:
        """
        Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting collectible detail info.

        collectible_presentation_node_hash : int
            The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetCollectibleNodeDetailsResponse]
            Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Collectibles/{encode_path_param(collectible_presentation_node_hash)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetCollectibleNodeDetailsResponse,
                    parse_obj_as(
                        type_=Destiny2GetCollectibleNodeDetailsResponse,
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

    def getvendors(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        filter: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetVendorsResponse]:
        """
        Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting vendor info.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        filter : typing.Optional[int]
            The filter of what vendors and items to return, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetVendorsResponse]
            A response containing all of the components for all requested vendors.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Vendors/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetVendorsResponse,
                    parse_obj_as(
                        type_=Destiny2GetVendorsResponse,
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

    def getvendor(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        vendor_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetVendorResponse]:
        """
        Get the details of a specific Vendor.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting vendor info.

        vendor_hash : int
            The Hash identifier of the Vendor to be returned.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetVendorResponse]
            A response containing all of the components for a vendor.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Vendors/{encode_path_param(vendor_hash)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetVendorResponse,
                    parse_obj_as(
                        type_=Destiny2GetVendorResponse,
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

    def getitem(
        self,
        membership_type: int,
        destiny_membership_id: int,
        item_instance_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetItemResponse]:
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The membership ID of the destiny profile.

        item_instance_id : int
            The Instance ID of the destiny item.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetItemResponse]
            The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Item/{encode_path_param(item_instance_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetItemResponse,
                    parse_obj_as(
                        type_=Destiny2GetItemResponse,
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

    def getlinkedprofiles(
        self,
        membership_type: int,
        membership_id: int,
        *,
        get_all_memberships: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Destiny2GetLinkedProfilesResponse]:
        """
        Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

        Parameters
        ----------
        membership_type : int
            The type for the membership whose linked Destiny accounts you want returned.

        membership_id : int
            The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!

        get_all_memberships : typing.Optional[bool]
            (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Destiny2GetLinkedProfilesResponse]
            I know what you seek. You seek linked accounts. Found them, you have.
            This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(membership_id)}/LinkedProfiles/",
            method="GET",
            params={
                "getAllMemberships": get_all_memberships,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLinkedProfilesResponse,
                    parse_obj_as(
                        type_=Destiny2GetLinkedProfilesResponse,
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


class AsyncRawDestiny2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def equipitem(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2EquipItemResponse]:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2EquipItemResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/EquipItem/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipItemResponse,
                    parse_obj_as(
                        type_=Destiny2EquipItemResponse,
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

    async def equipitems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2EquipItemsResponse]:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2EquipItemsResponse]
            The results of a bulk Equipping operation performed through the Destiny API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/EquipItems/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipItemsResponse,
                    parse_obj_as(
                        type_=Destiny2EquipItemsResponse,
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

    async def insertsocketplug(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2InsertSocketPlugResponse]:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2InsertSocketPlugResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/InsertSocketPlug/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2InsertSocketPlugResponse,
                    parse_obj_as(
                        type_=Destiny2InsertSocketPlugResponse,
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

    async def insertsocketplugfree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2InsertSocketPlugFreeResponse]:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2InsertSocketPlugFreeResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/InsertSocketPlugFree/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2InsertSocketPlugFreeResponse,
                    parse_obj_as(
                        type_=Destiny2InsertSocketPlugFreeResponse,
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

    async def pullfrompostmaster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2PullFromPostmasterResponse]:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2PullFromPostmasterResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/PullFromPostmaster/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2PullFromPostmasterResponse,
                    parse_obj_as(
                        type_=Destiny2PullFromPostmasterResponse,
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

    async def setitemlockstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2SetItemLockStateResponse]:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2SetItemLockStateResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/SetLockState/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SetItemLockStateResponse,
                    parse_obj_as(
                        type_=Destiny2SetItemLockStateResponse,
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

    async def setquesttrackedstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2SetQuestTrackedStateResponse]:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2SetQuestTrackedStateResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/SetTrackedState/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SetQuestTrackedStateResponse,
                    parse_obj_as(
                        type_=Destiny2SetQuestTrackedStateResponse,
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

    async def transferitem(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2TransferItemResponse]:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2TransferItemResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Items/TransferItem/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2TransferItemResponse,
                    parse_obj_as(
                        type_=Destiny2TransferItemResponse,
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

    async def clearloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2ClearLoadoutResponse]:
        """
        Clear the identifiers and items of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2ClearLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/ClearLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2ClearLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2ClearLoadoutResponse,
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

    async def equiploadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2EquipLoadoutResponse]:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2EquipLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/EquipLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2EquipLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2EquipLoadoutResponse,
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

    async def snapshotloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2SnapshotLoadoutResponse]:
        """
        Snapshot a loadout with the currently equipped items.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2SnapshotLoadoutResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/SnapshotLoadout/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SnapshotLoadoutResponse,
                    parse_obj_as(
                        type_=Destiny2SnapshotLoadoutResponse,
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

    async def updateloadoutidentifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2UpdateLoadoutIdentifiersResponse]:
        """
        Update the color, icon, and name of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2UpdateLoadoutIdentifiersResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2UpdateLoadoutIdentifiersResponse,
                    parse_obj_as(
                        type_=Destiny2UpdateLoadoutIdentifiersResponse,
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

    async def searchdestinyentities(
        self,
        type: str,
        search_term: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2SearchDestinyEntitiesResponse]:
        """
        Gets a page list of Destiny items.

        Parameters
        ----------
        type : str
            The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.

        search_term : str
            The string to use when searching for Destiny entities.

        page : typing.Optional[int]
            Page number to return, starting with 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2SearchDestinyEntitiesResponse]
            The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Armory/Search/{encode_path_param(type)}/{encode_path_param(search_term)}/",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SearchDestinyEntitiesResponse,
                    parse_obj_as(
                        type_=Destiny2SearchDestinyEntitiesResponse,
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

    async def awaprovideauthorizationresult(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2AwaProvideAuthorizationResultResponse]:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2AwaProvideAuthorizationResultResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Awa/AwaProvideAuthorizationResult/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaProvideAuthorizationResultResponse,
                    parse_obj_as(
                        type_=Destiny2AwaProvideAuthorizationResultResponse,
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

    async def awagetactiontoken(
        self, correlation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2AwaGetActionTokenResponse]:
        """
        Returns the action token if user approves the request.

        Parameters
        ----------
        correlation_id : str
            The identifier for the advanced write action request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2AwaGetActionTokenResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Awa/GetActionToken/{encode_path_param(correlation_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaGetActionTokenResponse,
                    parse_obj_as(
                        type_=Destiny2AwaGetActionTokenResponse,
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

    async def awainitializerequest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2AwaInitializeRequestResponse]:
        """
        Initialize a request to perform an advanced write action.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2AwaInitializeRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Awa/Initialize/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2AwaInitializeRequestResponse,
                    parse_obj_as(
                        type_=Destiny2AwaInitializeRequestResponse,
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

    async def getclanbannersource(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetClanBannerSourceResponse]:
        """
        Returns the dictionary of values for the Clan Banner

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetClanBannerSourceResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Clan/ClanBannerDictionary/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanBannerSourceResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanBannerSourceResponse,
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

    async def getclanweeklyrewardstate(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetClanWeeklyRewardStateResponse]:
        """
        Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

        Parameters
        ----------
        group_id : int
            A valid group id of clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetClanWeeklyRewardStateResponse]
            Represents a runtime instance of a user's milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said "things to do." Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Clan/{encode_path_param(group_id)}/WeeklyRewardState/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanWeeklyRewardStateResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanWeeklyRewardStateResponse,
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

    async def getdestinymanifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetDestinyManifestResponse]:
        """
        Returns the current version of the manifest as a json object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetDestinyManifestResponse]
            DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Manifest/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyManifestResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyManifestResponse,
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

    async def getdestinyentitydefinition(
        self, entity_type: str, hash_identifier: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetDestinyEntityDefinitionResponse]:
        """
        Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

        Parameters
        ----------
        entity_type : str
            The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.

        hash_identifier : int
            The hash identifier for the specific Entity you want returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetDestinyEntityDefinitionResponse]
            Provides common properties for destiny definitions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Manifest/{encode_path_param(entity_type)}/{encode_path_param(hash_identifier)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyEntityDefinitionResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyEntityDefinitionResponse,
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

    async def getpublicmilestones(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetPublicMilestonesResponse]:
        """
        Gets public information about currently available Milestones.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetPublicMilestonesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Milestones/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicMilestonesResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicMilestonesResponse,
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

    async def getpublicmilestonecontent(
        self, milestone_hash: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetPublicMilestoneContentResponse]:
        """
        Gets custom localized content for the milestone of the given hash, if it exists.

        Parameters
        ----------
        milestone_hash : int
            The identifier for the milestone to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetPublicMilestoneContentResponse]
            Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Milestones/{encode_path_param(milestone_hash)}/Content/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicMilestoneContentResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicMilestoneContentResponse,
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

    async def searchdestinyplayerbybungiename(
        self, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2SearchDestinyPlayerByBungieNameResponse]:
        """
        Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2SearchDestinyPlayerByBungieNameResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/SearchDestinyPlayerByBungieName/{encode_path_param(membership_type)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2SearchDestinyPlayerByBungieNameResponse,
                    parse_obj_as(
                        type_=Destiny2SearchDestinyPlayerByBungieNameResponse,
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

    async def getclanaggregatestats(
        self,
        group_id: int,
        *,
        modes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetClanAggregateStatsResponse]:
        """
        Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        group_id : int
            Group ID of the clan whose leaderboards you wish to fetch.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetClanAggregateStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/AggregateClanStats/{encode_path_param(group_id)}/",
            method="GET",
            params={
                "modes": modes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanAggregateStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanAggregateStatsResponse,
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

    async def gethistoricalstatsdefinition(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetHistoricalStatsDefinitionResponse]:
        """
        Gets historical stats definitions.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetHistoricalStatsDefinitionResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Stats/Definition/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsDefinitionResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsDefinitionResponse,
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

    async def getclanleaderboards(
        self,
        group_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetClanLeaderboardsResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        group_id : int
            Group ID of the clan whose leaderboards you wish to fetch.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetClanLeaderboardsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/Leaderboards/Clans/{encode_path_param(group_id)}/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetClanLeaderboardsResponse,
                    parse_obj_as(
                        type_=Destiny2GetClanLeaderboardsResponse,
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

    async def getleaderboardsforcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetLeaderboardsForCharacterResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The specific character to build the leaderboard around for the provided Destiny Membership.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetLeaderboardsForCharacterResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/Leaderboards/{encode_path_param(membership_type)}/{encode_path_param(destiny_membership_id)}/{encode_path_param(character_id)}/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLeaderboardsForCharacterResponse,
                    parse_obj_as(
                        type_=Destiny2GetLeaderboardsForCharacterResponse,
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

    async def getpostgamecarnagereport(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2GetPostGameCarnageReportResponse]:
        """
        Gets the available post game carnage report for the activity ID.

        Parameters
        ----------
        activity_id : int
            The ID of the activity whose PGCR is requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetPostGameCarnageReportResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/PostGameCarnageReport/{encode_path_param(activity_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPostGameCarnageReportResponse,
                    parse_obj_as(
                        type_=Destiny2GetPostGameCarnageReportResponse,
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

    async def reportoffensivepostgamecarnagereportplayer(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Destiny2ReportOffensivePostGameCarnageReportPlayerResponse]:
        """
        Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

        Parameters
        ----------
        activity_id : int
            The ID of the activity where you ran into the brigand that you're reporting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2ReportOffensivePostGameCarnageReportPlayerResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/Stats/PostGameCarnageReport/{encode_path_param(activity_id)}/Report/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
                    parse_obj_as(
                        type_=Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
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

    async def getpublicvendors(
        self,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetPublicVendorsResponse]:
        """
        Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'

        Parameters
        ----------
        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetPublicVendorsResponse]
            A response containing all valid components for the public Vendors endpoint.
             It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
             If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Destiny2/Vendors/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetPublicVendorsResponse,
                    parse_obj_as(
                        type_=Destiny2GetPublicVendorsResponse,
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

    async def gethistoricalstats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        dayend: typing.Optional[dt.datetime] = None,
        daystart: typing.Optional[dt.datetime] = None,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        modes: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        period_type: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetHistoricalStatsResponse]:
        """
        Gets historical stats for indicated character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.

        dayend : typing.Optional[dt.datetime]
            Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.

        daystart : typing.Optional[dt.datetime]
            First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.

        groups : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals

        modes : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        period_type : typing.Optional[int]
            Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetHistoricalStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/",
            method="GET",
            params={
                "dayend": serialize_datetime(dayend) if dayend is not None else None,
                "daystart": serialize_datetime(daystart) if daystart is not None else None,
                "groups": ",".join(map(str, groups)) if isinstance(groups, (list, tuple, set)) else groups,
                "modes": ",".join(map(str, modes)) if isinstance(modes, (list, tuple, set)) else modes,
                "periodType": period_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsResponse,
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

    async def getactivityhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        count: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetActivityHistoryResponse]:
        """
        Gets activity history stats for indicated character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve.

        count : typing.Optional[int]
            Number of rows to return

        mode : typing.Optional[int]
            A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.

        page : typing.Optional[int]
            Page number to return, starting with 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetActivityHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/Activities/",
            method="GET",
            params={
                "count": count,
                "mode": mode,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetActivityHistoryResponse,
                    parse_obj_as(
                        type_=Destiny2GetActivityHistoryResponse,
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

    async def getdestinyaggregateactivitystats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetDestinyAggregateActivityStatsResponse]:
        """
        Gets all activities the character has participated in together with aggregate statistics for those activities.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The specific character whose activities should be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetDestinyAggregateActivityStatsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/AggregateActivityStats/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetDestinyAggregateActivityStatsResponse,
                    parse_obj_as(
                        type_=Destiny2GetDestinyAggregateActivityStatsResponse,
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

    async def getuniqueweaponhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetUniqueWeaponHistoryResponse]:
        """
        Gets details about unique weapon usage, including all exotic weapons.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        character_id : int
            The id of the character to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetUniqueWeaponHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Stats/UniqueWeapons/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetUniqueWeaponHistoryResponse,
                    parse_obj_as(
                        type_=Destiny2GetUniqueWeaponHistoryResponse,
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

    async def gethistoricalstatsforaccount(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetHistoricalStatsForAccountResponse]:
        """
        Gets aggregate historical stats organized around each character for a given account.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        groups : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetHistoricalStatsForAccountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Stats/",
            method="GET",
            params={
                "groups": ",".join(map(str, groups)) if isinstance(groups, (list, tuple, set)) else groups,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetHistoricalStatsForAccountResponse,
                    parse_obj_as(
                        type_=Destiny2GetHistoricalStatsForAccountResponse,
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

    async def getleaderboards(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetLeaderboardsResponse]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The Destiny membershipId of the user to retrieve.

        maxtop : typing.Optional[int]
            Maximum number of top players to return. Use a large number to get entire leaderboard.

        modes : typing.Optional[str]
            List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.

        statid : typing.Optional[str]
            ID of stat to return rather than returning all Leaderboard stats.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetLeaderboardsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Account/{encode_path_param(destiny_membership_id)}/Stats/Leaderboards/",
            method="GET",
            params={
                "maxtop": maxtop,
                "modes": modes,
                "statid": statid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLeaderboardsResponse,
                    parse_obj_as(
                        type_=Destiny2GetLeaderboardsResponse,
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

    async def getprofile(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetProfileResponse]:
        """
        Returns Destiny Profile information for the supplied membership.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetProfileResponse]
            The response for GetDestinyProfile, with components for character and item-level data.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetProfileResponse,
                    parse_obj_as(
                        type_=Destiny2GetProfileResponse,
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

    async def getcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetCharacterResponse]:
        """
        Returns character information for the supplied character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID.

        character_id : int
            ID of the character.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetCharacterResponse]
            The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetCharacterResponse,
                    parse_obj_as(
                        type_=Destiny2GetCharacterResponse,
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

    async def getcollectiblenodedetails(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        collectible_presentation_node_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetCollectibleNodeDetailsResponse]:
        """
        Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting collectible detail info.

        collectible_presentation_node_hash : int
            The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetCollectibleNodeDetailsResponse]
            Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Collectibles/{encode_path_param(collectible_presentation_node_hash)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetCollectibleNodeDetailsResponse,
                    parse_obj_as(
                        type_=Destiny2GetCollectibleNodeDetailsResponse,
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

    async def getvendors(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        filter: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetVendorsResponse]:
        """
        Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting vendor info.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        filter : typing.Optional[int]
            The filter of what vendors and items to return, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetVendorsResponse]
            A response containing all of the components for all requested vendors.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Vendors/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetVendorsResponse,
                    parse_obj_as(
                        type_=Destiny2GetVendorsResponse,
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

    async def getvendor(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        vendor_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetVendorResponse]:
        """
        Get the details of a specific Vendor.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            Destiny membership ID of another user. You may be denied.

        character_id : int
            The Destiny Character ID of the character for whom we're getting vendor info.

        vendor_hash : int
            The Hash identifier of the Vendor to be returned.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetVendorResponse]
            A response containing all of the components for a vendor.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Character/{encode_path_param(character_id)}/Vendors/{encode_path_param(vendor_hash)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetVendorResponse,
                    parse_obj_as(
                        type_=Destiny2GetVendorResponse,
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

    async def getitem(
        self,
        membership_type: int,
        destiny_membership_id: int,
        item_instance_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetItemResponse]:
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Parameters
        ----------
        membership_type : int
            A valid non-BungieNet membership type.

        destiny_membership_id : int
            The membership ID of the destiny profile.

        item_instance_id : int
            The Instance ID of the destiny item.

        components : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetItemResponse]
            The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(destiny_membership_id)}/Item/{encode_path_param(item_instance_id)}/",
            method="GET",
            params={
                "components": ",".join(map(str, components))
                if isinstance(components, (list, tuple, set))
                else components,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetItemResponse,
                    parse_obj_as(
                        type_=Destiny2GetItemResponse,
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

    async def getlinkedprofiles(
        self,
        membership_type: int,
        membership_id: int,
        *,
        get_all_memberships: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Destiny2GetLinkedProfilesResponse]:
        """
        Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

        Parameters
        ----------
        membership_type : int
            The type for the membership whose linked Destiny accounts you want returned.

        membership_id : int
            The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!

        get_all_memberships : typing.Optional[bool]
            (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Destiny2GetLinkedProfilesResponse]
            I know what you seek. You seek linked accounts. Found them, you have.
            This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Destiny2/{encode_path_param(membership_type)}/Profile/{encode_path_param(membership_id)}/LinkedProfiles/",
            method="GET",
            params={
                "getAllMemberships": get_all_memberships,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Destiny2GetLinkedProfilesResponse,
                    parse_obj_as(
                        type_=Destiny2GetLinkedProfilesResponse,
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
