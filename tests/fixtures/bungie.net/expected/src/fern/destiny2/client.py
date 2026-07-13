

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDestiny2Client, RawDestiny2Client
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


class Destiny2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestiny2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestiny2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestiny2Client
        """
        return self._raw_client

    def equipitem(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2EquipItemResponse:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipItemResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.equipitem()
        """
        _response = self._raw_client.equipitem(request_options=request_options)
        return _response.data

    def equipitems(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2EquipItemsResponse:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipItemsResponse
            The results of a bulk Equipping operation performed through the Destiny API.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.equipitems()
        """
        _response = self._raw_client.equipitems(request_options=request_options)
        return _response.data

    def insertsocketplug(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2InsertSocketPlugResponse:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2InsertSocketPlugResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.insertsocketplug()
        """
        _response = self._raw_client.insertsocketplug(request_options=request_options)
        return _response.data

    def insertsocketplugfree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2InsertSocketPlugFreeResponse:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2InsertSocketPlugFreeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.insertsocketplugfree()
        """
        _response = self._raw_client.insertsocketplugfree(request_options=request_options)
        return _response.data

    def pullfrompostmaster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2PullFromPostmasterResponse:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2PullFromPostmasterResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.pullfrompostmaster()
        """
        _response = self._raw_client.pullfrompostmaster(request_options=request_options)
        return _response.data

    def setitemlockstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SetItemLockStateResponse:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SetItemLockStateResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.setitemlockstate()
        """
        _response = self._raw_client.setitemlockstate(request_options=request_options)
        return _response.data

    def setquesttrackedstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SetQuestTrackedStateResponse:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SetQuestTrackedStateResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.setquesttrackedstate()
        """
        _response = self._raw_client.setquesttrackedstate(request_options=request_options)
        return _response.data

    def transferitem(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2TransferItemResponse:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2TransferItemResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.transferitem()
        """
        _response = self._raw_client.transferitem(request_options=request_options)
        return _response.data

    def clearloadout(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2ClearLoadoutResponse:
        """
        Clear the identifiers and items of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2ClearLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.clearloadout()
        """
        _response = self._raw_client.clearloadout(request_options=request_options)
        return _response.data

    def equiploadout(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2EquipLoadoutResponse:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.equiploadout()
        """
        _response = self._raw_client.equiploadout(request_options=request_options)
        return _response.data

    def snapshotloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SnapshotLoadoutResponse:
        """
        Snapshot a loadout with the currently equipped items.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SnapshotLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.snapshotloadout()
        """
        _response = self._raw_client.snapshotloadout(request_options=request_options)
        return _response.data

    def updateloadoutidentifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2UpdateLoadoutIdentifiersResponse:
        """
        Update the color, icon, and name of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2UpdateLoadoutIdentifiersResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.updateloadoutidentifiers()
        """
        _response = self._raw_client.updateloadoutidentifiers(request_options=request_options)
        return _response.data

    def searchdestinyentities(
        self,
        type: str,
        search_term: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2SearchDestinyEntitiesResponse:
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
        Destiny2SearchDestinyEntitiesResponse
            The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.searchdestinyentities(
            type="type",
            search_term="searchTerm",
        )
        """
        _response = self._raw_client.searchdestinyentities(
            type, search_term, page=page, request_options=request_options
        )
        return _response.data

    def awaprovideauthorizationresult(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaProvideAuthorizationResultResponse:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2AwaProvideAuthorizationResultResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.awaprovideauthorizationresult()
        """
        _response = self._raw_client.awaprovideauthorizationresult(request_options=request_options)
        return _response.data

    def awagetactiontoken(
        self, correlation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaGetActionTokenResponse:
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
        Destiny2AwaGetActionTokenResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.awagetactiontoken(
            correlation_id="correlationId",
        )
        """
        _response = self._raw_client.awagetactiontoken(correlation_id, request_options=request_options)
        return _response.data

    def awainitializerequest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaInitializeRequestResponse:
        """
        Initialize a request to perform an advanced write action.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2AwaInitializeRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.awainitializerequest()
        """
        _response = self._raw_client.awainitializerequest(request_options=request_options)
        return _response.data

    def getclanbannersource(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetClanBannerSourceResponse:
        """
        Returns the dictionary of values for the Clan Banner

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetClanBannerSourceResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getclanbannersource()
        """
        _response = self._raw_client.getclanbannersource(request_options=request_options)
        return _response.data

    def getclanweeklyrewardstate(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetClanWeeklyRewardStateResponse:
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
        Destiny2GetClanWeeklyRewardStateResponse
            Represents a runtime instance of a user's milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said "things to do." Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getclanweeklyrewardstate(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getclanweeklyrewardstate(group_id, request_options=request_options)
        return _response.data

    def getdestinymanifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetDestinyManifestResponse:
        """
        Returns the current version of the manifest as a json object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetDestinyManifestResponse
            DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getdestinymanifest()
        """
        _response = self._raw_client.getdestinymanifest(request_options=request_options)
        return _response.data

    def getdestinyentitydefinition(
        self, entity_type: str, hash_identifier: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetDestinyEntityDefinitionResponse:
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
        Destiny2GetDestinyEntityDefinitionResponse
            Provides common properties for destiny definitions.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getdestinyentitydefinition(
            entity_type="entityType",
            hash_identifier=1,
        )
        """
        _response = self._raw_client.getdestinyentitydefinition(
            entity_type, hash_identifier, request_options=request_options
        )
        return _response.data

    def getpublicmilestones(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPublicMilestonesResponse:
        """
        Gets public information about currently available Milestones.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetPublicMilestonesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getpublicmilestones()
        """
        _response = self._raw_client.getpublicmilestones(request_options=request_options)
        return _response.data

    def getpublicmilestonecontent(
        self, milestone_hash: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPublicMilestoneContentResponse:
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
        Destiny2GetPublicMilestoneContentResponse
            Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getpublicmilestonecontent(
            milestone_hash=1,
        )
        """
        _response = self._raw_client.getpublicmilestonecontent(milestone_hash, request_options=request_options)
        return _response.data

    def searchdestinyplayerbybungiename(
        self, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SearchDestinyPlayerByBungieNameResponse:
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
        Destiny2SearchDestinyPlayerByBungieNameResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.searchdestinyplayerbybungiename(
            membership_type=1,
        )
        """
        _response = self._raw_client.searchdestinyplayerbybungiename(membership_type, request_options=request_options)
        return _response.data

    def getclanaggregatestats(
        self,
        group_id: int,
        *,
        modes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetClanAggregateStatsResponse:
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
        Destiny2GetClanAggregateStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getclanaggregatestats(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getclanaggregatestats(group_id, modes=modes, request_options=request_options)
        return _response.data

    def gethistoricalstatsdefinition(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetHistoricalStatsDefinitionResponse:
        """
        Gets historical stats definitions.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetHistoricalStatsDefinitionResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.gethistoricalstatsdefinition()
        """
        _response = self._raw_client.gethistoricalstatsdefinition(request_options=request_options)
        return _response.data

    def getclanleaderboards(
        self,
        group_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetClanLeaderboardsResponse:
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
        Destiny2GetClanLeaderboardsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getclanleaderboards(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getclanleaderboards(
            group_id, maxtop=maxtop, modes=modes, statid=statid, request_options=request_options
        )
        return _response.data

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
    ) -> Destiny2GetLeaderboardsForCharacterResponse:
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
        Destiny2GetLeaderboardsForCharacterResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getleaderboardsforcharacter(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getleaderboardsforcharacter(
            membership_type,
            destiny_membership_id,
            character_id,
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            request_options=request_options,
        )
        return _response.data

    def getpostgamecarnagereport(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPostGameCarnageReportResponse:
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
        Destiny2GetPostGameCarnageReportResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getpostgamecarnagereport(
            activity_id=1000000,
        )
        """
        _response = self._raw_client.getpostgamecarnagereport(activity_id, request_options=request_options)
        return _response.data

    def reportoffensivepostgamecarnagereportplayer(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2ReportOffensivePostGameCarnageReportPlayerResponse:
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
        Destiny2ReportOffensivePostGameCarnageReportPlayerResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.reportoffensivepostgamecarnagereportplayer(
            activity_id=1000000,
        )
        """
        _response = self._raw_client.reportoffensivepostgamecarnagereportplayer(
            activity_id, request_options=request_options
        )
        return _response.data

    def getpublicvendors(
        self,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetPublicVendorsResponse:
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
        Destiny2GetPublicVendorsResponse
            A response containing all valid components for the public Vendors endpoint.
             It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
             If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getpublicvendors()
        """
        _response = self._raw_client.getpublicvendors(components=components, request_options=request_options)
        return _response.data

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
    ) -> Destiny2GetHistoricalStatsResponse:
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
        Destiny2GetHistoricalStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.gethistoricalstats(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.gethistoricalstats(
            membership_type,
            destiny_membership_id,
            character_id,
            dayend=dayend,
            daystart=daystart,
            groups=groups,
            modes=modes,
            period_type=period_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Destiny2GetActivityHistoryResponse:
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
        Destiny2GetActivityHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getactivityhistory(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getactivityhistory(
            membership_type,
            destiny_membership_id,
            character_id,
            count=count,
            mode=mode,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def getdestinyaggregateactivitystats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetDestinyAggregateActivityStatsResponse:
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
        Destiny2GetDestinyAggregateActivityStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getdestinyaggregateactivitystats(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getdestinyaggregateactivitystats(
            membership_type, destiny_membership_id, character_id, request_options=request_options
        )
        return _response.data

    def getuniqueweaponhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetUniqueWeaponHistoryResponse:
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
        Destiny2GetUniqueWeaponHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getuniqueweaponhistory(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getuniqueweaponhistory(
            membership_type, destiny_membership_id, character_id, request_options=request_options
        )
        return _response.data

    def gethistoricalstatsforaccount(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetHistoricalStatsForAccountResponse:
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
        Destiny2GetHistoricalStatsForAccountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.gethistoricalstatsforaccount(
            membership_type=1,
            destiny_membership_id=1000000,
        )
        """
        _response = self._raw_client.gethistoricalstatsforaccount(
            membership_type, destiny_membership_id, groups=groups, request_options=request_options
        )
        return _response.data

    def getleaderboards(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetLeaderboardsResponse:
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
        Destiny2GetLeaderboardsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getleaderboards(
            membership_type=1,
            destiny_membership_id=1000000,
        )
        """
        _response = self._raw_client.getleaderboards(
            membership_type,
            destiny_membership_id,
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            request_options=request_options,
        )
        return _response.data

    def getprofile(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetProfileResponse:
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
        Destiny2GetProfileResponse
            The response for GetDestinyProfile, with components for character and item-level data.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getprofile(
            membership_type=1,
            destiny_membership_id=1000000,
        )
        """
        _response = self._raw_client.getprofile(
            membership_type, destiny_membership_id, components=components, request_options=request_options
        )
        return _response.data

    def getcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetCharacterResponse:
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
        Destiny2GetCharacterResponse
            The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getcharacter(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getcharacter(
            membership_type, destiny_membership_id, character_id, components=components, request_options=request_options
        )
        return _response.data

    def getcollectiblenodedetails(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        collectible_presentation_node_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetCollectibleNodeDetailsResponse:
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
        Destiny2GetCollectibleNodeDetailsResponse
            Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getcollectiblenodedetails(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
            collectible_presentation_node_hash=1,
        )
        """
        _response = self._raw_client.getcollectiblenodedetails(
            membership_type,
            destiny_membership_id,
            character_id,
            collectible_presentation_node_hash,
            components=components,
            request_options=request_options,
        )
        return _response.data

    def getvendors(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        filter: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetVendorsResponse:
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
        Destiny2GetVendorsResponse
            A response containing all of the components for all requested vendors.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getvendors(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
        )
        """
        _response = self._raw_client.getvendors(
            membership_type,
            destiny_membership_id,
            character_id,
            components=components,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    def getvendor(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        vendor_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetVendorResponse:
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
        Destiny2GetVendorResponse
            A response containing all of the components for a vendor.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getvendor(
            membership_type=1,
            destiny_membership_id=1000000,
            character_id=1000000,
            vendor_hash=1,
        )
        """
        _response = self._raw_client.getvendor(
            membership_type,
            destiny_membership_id,
            character_id,
            vendor_hash,
            components=components,
            request_options=request_options,
        )
        return _response.data

    def getitem(
        self,
        membership_type: int,
        destiny_membership_id: int,
        item_instance_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetItemResponse:
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
        Destiny2GetItemResponse
            The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getitem(
            membership_type=1,
            destiny_membership_id=1000000,
            item_instance_id=1000000,
        )
        """
        _response = self._raw_client.getitem(
            membership_type,
            destiny_membership_id,
            item_instance_id,
            components=components,
            request_options=request_options,
        )
        return _response.data

    def getlinkedprofiles(
        self,
        membership_type: int,
        membership_id: int,
        *,
        get_all_memberships: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetLinkedProfilesResponse:
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
        Destiny2GetLinkedProfilesResponse
            I know what you seek. You seek linked accounts. Found them, you have.
            This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.destiny2.getlinkedprofiles(
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.getlinkedprofiles(
            membership_type, membership_id, get_all_memberships=get_all_memberships, request_options=request_options
        )
        return _response.data


class AsyncDestiny2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestiny2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestiny2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestiny2Client
        """
        return self._raw_client

    async def equipitem(self, *, request_options: typing.Optional[RequestOptions] = None) -> Destiny2EquipItemResponse:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipItemResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.equipitem()


        asyncio.run(main())
        """
        _response = await self._raw_client.equipitem(request_options=request_options)
        return _response.data

    async def equipitems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2EquipItemsResponse:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipItemsResponse
            The results of a bulk Equipping operation performed through the Destiny API.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.equipitems()


        asyncio.run(main())
        """
        _response = await self._raw_client.equipitems(request_options=request_options)
        return _response.data

    async def insertsocketplug(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2InsertSocketPlugResponse:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2InsertSocketPlugResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.insertsocketplug()


        asyncio.run(main())
        """
        _response = await self._raw_client.insertsocketplug(request_options=request_options)
        return _response.data

    async def insertsocketplugfree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2InsertSocketPlugFreeResponse:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2InsertSocketPlugFreeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.insertsocketplugfree()


        asyncio.run(main())
        """
        _response = await self._raw_client.insertsocketplugfree(request_options=request_options)
        return _response.data

    async def pullfrompostmaster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2PullFromPostmasterResponse:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2PullFromPostmasterResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.pullfrompostmaster()


        asyncio.run(main())
        """
        _response = await self._raw_client.pullfrompostmaster(request_options=request_options)
        return _response.data

    async def setitemlockstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SetItemLockStateResponse:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SetItemLockStateResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.setitemlockstate()


        asyncio.run(main())
        """
        _response = await self._raw_client.setitemlockstate(request_options=request_options)
        return _response.data

    async def setquesttrackedstate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SetQuestTrackedStateResponse:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SetQuestTrackedStateResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.setquesttrackedstate()


        asyncio.run(main())
        """
        _response = await self._raw_client.setquesttrackedstate(request_options=request_options)
        return _response.data

    async def transferitem(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2TransferItemResponse:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2TransferItemResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.transferitem()


        asyncio.run(main())
        """
        _response = await self._raw_client.transferitem(request_options=request_options)
        return _response.data

    async def clearloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2ClearLoadoutResponse:
        """
        Clear the identifiers and items of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2ClearLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.clearloadout()


        asyncio.run(main())
        """
        _response = await self._raw_client.clearloadout(request_options=request_options)
        return _response.data

    async def equiploadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2EquipLoadoutResponse:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2EquipLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.equiploadout()


        asyncio.run(main())
        """
        _response = await self._raw_client.equiploadout(request_options=request_options)
        return _response.data

    async def snapshotloadout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SnapshotLoadoutResponse:
        """
        Snapshot a loadout with the currently equipped items.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2SnapshotLoadoutResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.snapshotloadout()


        asyncio.run(main())
        """
        _response = await self._raw_client.snapshotloadout(request_options=request_options)
        return _response.data

    async def updateloadoutidentifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2UpdateLoadoutIdentifiersResponse:
        """
        Update the color, icon, and name of a loadout.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2UpdateLoadoutIdentifiersResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.updateloadoutidentifiers()


        asyncio.run(main())
        """
        _response = await self._raw_client.updateloadoutidentifiers(request_options=request_options)
        return _response.data

    async def searchdestinyentities(
        self,
        type: str,
        search_term: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2SearchDestinyEntitiesResponse:
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
        Destiny2SearchDestinyEntitiesResponse
            The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.searchdestinyentities(
                type="type",
                search_term="searchTerm",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchdestinyentities(
            type, search_term, page=page, request_options=request_options
        )
        return _response.data

    async def awaprovideauthorizationresult(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaProvideAuthorizationResultResponse:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2AwaProvideAuthorizationResultResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.awaprovideauthorizationresult()


        asyncio.run(main())
        """
        _response = await self._raw_client.awaprovideauthorizationresult(request_options=request_options)
        return _response.data

    async def awagetactiontoken(
        self, correlation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaGetActionTokenResponse:
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
        Destiny2AwaGetActionTokenResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.awagetactiontoken(
                correlation_id="correlationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.awagetactiontoken(correlation_id, request_options=request_options)
        return _response.data

    async def awainitializerequest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2AwaInitializeRequestResponse:
        """
        Initialize a request to perform an advanced write action.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2AwaInitializeRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.awainitializerequest()


        asyncio.run(main())
        """
        _response = await self._raw_client.awainitializerequest(request_options=request_options)
        return _response.data

    async def getclanbannersource(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetClanBannerSourceResponse:
        """
        Returns the dictionary of values for the Clan Banner

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetClanBannerSourceResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getclanbannersource()


        asyncio.run(main())
        """
        _response = await self._raw_client.getclanbannersource(request_options=request_options)
        return _response.data

    async def getclanweeklyrewardstate(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetClanWeeklyRewardStateResponse:
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
        Destiny2GetClanWeeklyRewardStateResponse
            Represents a runtime instance of a user's milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said "things to do." Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getclanweeklyrewardstate(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getclanweeklyrewardstate(group_id, request_options=request_options)
        return _response.data

    async def getdestinymanifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetDestinyManifestResponse:
        """
        Returns the current version of the manifest as a json object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetDestinyManifestResponse
            DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getdestinymanifest()


        asyncio.run(main())
        """
        _response = await self._raw_client.getdestinymanifest(request_options=request_options)
        return _response.data

    async def getdestinyentitydefinition(
        self, entity_type: str, hash_identifier: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetDestinyEntityDefinitionResponse:
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
        Destiny2GetDestinyEntityDefinitionResponse
            Provides common properties for destiny definitions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getdestinyentitydefinition(
                entity_type="entityType",
                hash_identifier=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdestinyentitydefinition(
            entity_type, hash_identifier, request_options=request_options
        )
        return _response.data

    async def getpublicmilestones(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPublicMilestonesResponse:
        """
        Gets public information about currently available Milestones.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetPublicMilestonesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getpublicmilestones()


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicmilestones(request_options=request_options)
        return _response.data

    async def getpublicmilestonecontent(
        self, milestone_hash: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPublicMilestoneContentResponse:
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
        Destiny2GetPublicMilestoneContentResponse
            Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getpublicmilestonecontent(
                milestone_hash=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicmilestonecontent(milestone_hash, request_options=request_options)
        return _response.data

    async def searchdestinyplayerbybungiename(
        self, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2SearchDestinyPlayerByBungieNameResponse:
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
        Destiny2SearchDestinyPlayerByBungieNameResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.searchdestinyplayerbybungiename(
                membership_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchdestinyplayerbybungiename(
            membership_type, request_options=request_options
        )
        return _response.data

    async def getclanaggregatestats(
        self,
        group_id: int,
        *,
        modes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetClanAggregateStatsResponse:
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
        Destiny2GetClanAggregateStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getclanaggregatestats(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getclanaggregatestats(group_id, modes=modes, request_options=request_options)
        return _response.data

    async def gethistoricalstatsdefinition(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetHistoricalStatsDefinitionResponse:
        """
        Gets historical stats definitions.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Destiny2GetHistoricalStatsDefinitionResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.gethistoricalstatsdefinition()


        asyncio.run(main())
        """
        _response = await self._raw_client.gethistoricalstatsdefinition(request_options=request_options)
        return _response.data

    async def getclanleaderboards(
        self,
        group_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetClanLeaderboardsResponse:
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
        Destiny2GetClanLeaderboardsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getclanleaderboards(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getclanleaderboards(
            group_id, maxtop=maxtop, modes=modes, statid=statid, request_options=request_options
        )
        return _response.data

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
    ) -> Destiny2GetLeaderboardsForCharacterResponse:
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
        Destiny2GetLeaderboardsForCharacterResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getleaderboardsforcharacter(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getleaderboardsforcharacter(
            membership_type,
            destiny_membership_id,
            character_id,
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            request_options=request_options,
        )
        return _response.data

    async def getpostgamecarnagereport(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2GetPostGameCarnageReportResponse:
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
        Destiny2GetPostGameCarnageReportResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getpostgamecarnagereport(
                activity_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpostgamecarnagereport(activity_id, request_options=request_options)
        return _response.data

    async def reportoffensivepostgamecarnagereportplayer(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Destiny2ReportOffensivePostGameCarnageReportPlayerResponse:
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
        Destiny2ReportOffensivePostGameCarnageReportPlayerResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.reportoffensivepostgamecarnagereportplayer(
                activity_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reportoffensivepostgamecarnagereportplayer(
            activity_id, request_options=request_options
        )
        return _response.data

    async def getpublicvendors(
        self,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetPublicVendorsResponse:
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
        Destiny2GetPublicVendorsResponse
            A response containing all valid components for the public Vendors endpoint.
             It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
             If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getpublicvendors()


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicvendors(components=components, request_options=request_options)
        return _response.data

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
    ) -> Destiny2GetHistoricalStatsResponse:
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
        Destiny2GetHistoricalStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.gethistoricalstats(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gethistoricalstats(
            membership_type,
            destiny_membership_id,
            character_id,
            dayend=dayend,
            daystart=daystart,
            groups=groups,
            modes=modes,
            period_type=period_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Destiny2GetActivityHistoryResponse:
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
        Destiny2GetActivityHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getactivityhistory(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivityhistory(
            membership_type,
            destiny_membership_id,
            character_id,
            count=count,
            mode=mode,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def getdestinyaggregateactivitystats(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetDestinyAggregateActivityStatsResponse:
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
        Destiny2GetDestinyAggregateActivityStatsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getdestinyaggregateactivitystats(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdestinyaggregateactivitystats(
            membership_type, destiny_membership_id, character_id, request_options=request_options
        )
        return _response.data

    async def getuniqueweaponhistory(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetUniqueWeaponHistoryResponse:
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
        Destiny2GetUniqueWeaponHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getuniqueweaponhistory(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getuniqueweaponhistory(
            membership_type, destiny_membership_id, character_id, request_options=request_options
        )
        return _response.data

    async def gethistoricalstatsforaccount(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        groups: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetHistoricalStatsForAccountResponse:
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
        Destiny2GetHistoricalStatsForAccountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.gethistoricalstatsforaccount(
                membership_type=1,
                destiny_membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gethistoricalstatsforaccount(
            membership_type, destiny_membership_id, groups=groups, request_options=request_options
        )
        return _response.data

    async def getleaderboards(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        maxtop: typing.Optional[int] = None,
        modes: typing.Optional[str] = None,
        statid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetLeaderboardsResponse:
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
        Destiny2GetLeaderboardsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getleaderboards(
                membership_type=1,
                destiny_membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getleaderboards(
            membership_type,
            destiny_membership_id,
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            request_options=request_options,
        )
        return _response.data

    async def getprofile(
        self,
        membership_type: int,
        destiny_membership_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetProfileResponse:
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
        Destiny2GetProfileResponse
            The response for GetDestinyProfile, with components for character and item-level data.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getprofile(
                membership_type=1,
                destiny_membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprofile(
            membership_type, destiny_membership_id, components=components, request_options=request_options
        )
        return _response.data

    async def getcharacter(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetCharacterResponse:
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
        Destiny2GetCharacterResponse
            The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getcharacter(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcharacter(
            membership_type, destiny_membership_id, character_id, components=components, request_options=request_options
        )
        return _response.data

    async def getcollectiblenodedetails(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        collectible_presentation_node_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetCollectibleNodeDetailsResponse:
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
        Destiny2GetCollectibleNodeDetailsResponse
            Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getcollectiblenodedetails(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
                collectible_presentation_node_hash=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcollectiblenodedetails(
            membership_type,
            destiny_membership_id,
            character_id,
            collectible_presentation_node_hash,
            components=components,
            request_options=request_options,
        )
        return _response.data

    async def getvendors(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        filter: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetVendorsResponse:
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
        Destiny2GetVendorsResponse
            A response containing all of the components for all requested vendors.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getvendors(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getvendors(
            membership_type,
            destiny_membership_id,
            character_id,
            components=components,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

    async def getvendor(
        self,
        membership_type: int,
        destiny_membership_id: int,
        character_id: int,
        vendor_hash: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetVendorResponse:
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
        Destiny2GetVendorResponse
            A response containing all of the components for a vendor.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getvendor(
                membership_type=1,
                destiny_membership_id=1000000,
                character_id=1000000,
                vendor_hash=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getvendor(
            membership_type,
            destiny_membership_id,
            character_id,
            vendor_hash,
            components=components,
            request_options=request_options,
        )
        return _response.data

    async def getitem(
        self,
        membership_type: int,
        destiny_membership_id: int,
        item_instance_id: int,
        *,
        components: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetItemResponse:
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
        Destiny2GetItemResponse
            The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getitem(
                membership_type=1,
                destiny_membership_id=1000000,
                item_instance_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getitem(
            membership_type,
            destiny_membership_id,
            item_instance_id,
            components=components,
            request_options=request_options,
        )
        return _response.data

    async def getlinkedprofiles(
        self,
        membership_type: int,
        membership_id: int,
        *,
        get_all_memberships: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Destiny2GetLinkedProfilesResponse:
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
        Destiny2GetLinkedProfilesResponse
            I know what you seek. You seek linked accounts. Found them, you have.
            This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.destiny2.getlinkedprofiles(
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getlinkedprofiles(
            membership_type, membership_id, get_all_memberships=get_all_memberships, request_options=request_options
        )
        return _response.data
