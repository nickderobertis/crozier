

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_records_destiny_record_component import DestinyComponentsRecordsDestinyRecordComponent


class DestinyComponentsRecordsDestinyProfileRecordsComponent(UniversalBaseModel):
    active_score: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activeScore")] = (
        pydantic.Field(default=None)
    )
    """
    Your 'active' Triumphs score.
    """

    legacy_score: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="legacyScore")] = (
        pydantic.Field(default=None)
    )
    """
    Your 'legacy' Triumphs score.
    """

    lifetime_score: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="lifetimeScore")] = (
        pydantic.Field(default=None)
    )
    """
    Your 'lifetime' Triumphs score.
    """

    record_categories_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordCategoriesRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Triumph categories.
    """

    record_seals_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordSealsRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Triumph Seals.
    """

    records: typing.Optional[typing.Dict[str, DestinyComponentsRecordsDestinyRecordComponent]] = None
    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Your 'active' Triumphs score, maintained for backwards compatibility.
    """

    tracked_record_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="trackedRecordHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this profile is tracking a record, this is the hash identifier of the record it is tracking.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
