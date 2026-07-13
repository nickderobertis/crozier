

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonModelsDestiny2CoreSettings(UniversalBaseModel):
    active_seals_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeSealsRootNodeHash")
    ] = None
    active_triumphs_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeTriumphsRootNodeHash")
    ] = None
    ammo_type_heavy_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ammoTypeHeavyIcon")
    ] = None
    ammo_type_primary_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ammoTypePrimaryIcon")
    ] = None
    ammo_type_special_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ammoTypeSpecialIcon")
    ] = None
    badges_root_node: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="badgesRootNode")] = None
    collection_root_node: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="collectionRootNode")
    ] = None
    crafting_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="craftingRootNodeHash")
    ] = None
    current_rank_progression_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="currentRankProgressionHashes")
    ] = None
    current_season_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="currentSeasonHash")] = (
        None
    )
    current_seasonal_artifact_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentSeasonalArtifactHash")
    ] = None
    exotic_catalysts_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="exoticCatalystsRootNodeHash")
    ] = None
    future_season_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="futureSeasonHashes")
    ] = None
    guardian_rank_constants_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guardianRankConstantsHash")
    ] = None
    guardian_ranks_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guardianRanksRootNodeHash")
    ] = None
    insert_plug_free_blocked_socket_type_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="insertPlugFreeBlockedSocketTypeHashes")
    ] = None
    insert_plug_free_protected_plug_item_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="insertPlugFreeProtectedPlugItemHashes")
    ] = None
    legacy_seals_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="legacySealsRootNodeHash")
    ] = None
    legacy_triumphs_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="legacyTriumphsRootNodeHash")
    ] = None
    loadout_constants_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="loadoutConstantsHash")
    ] = None
    lore_root_node_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="loreRootNodeHash")] = (
        None
    )
    medals_root_node: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="medalsRootNode")] = None
    medals_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="medalsRootNodeHash")
    ] = None
    metrics_root_node: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="metricsRootNode")] = None
    past_season_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="pastSeasonHashes")
    ] = None
    records_root_node: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="recordsRootNode")] = None
    seasonal_challenges_presentation_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="seasonalChallengesPresentationNodeHash")
    ] = None
    undiscovered_collectible_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="undiscoveredCollectibleImage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
