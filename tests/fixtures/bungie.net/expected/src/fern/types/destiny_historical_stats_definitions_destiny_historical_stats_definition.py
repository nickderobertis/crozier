

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyHistoricalStatsDefinitionsDestinyHistoricalStatsDefinition(UniversalBaseModel):
    category: typing.Optional[int] = pydantic.Field(default=None)
    """
    Category for the stat.
    """

    group: typing.Optional[int] = pydantic.Field(default=None)
    """
    Statistic group
    """

    icon_image: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="iconImage")] = pydantic.Field(
        default=None
    )
    """
    Optional URI to an icon for the statistic
    """

    medal_tier_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="medalTierHash")] = (
        pydantic.Field(default=None)
    )
    """
    The tier associated with this medal - be it implicitly or explicitly.
    """

    merge_method: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="mergeMethod")] = (
        pydantic.Field(default=None)
    )
    """
    Optional icon for the statistic
    """

    modes: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Game modes where this statistic can be reported.
    """

    period_types: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="periodTypes")] = (
        pydantic.Field(default=None)
    )
    """
    Time periods the statistic covers
    """

    stat_description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="statDescription")] = (
        pydantic.Field(default=None)
    )
    """
    Description of a stat if applicable.
    """

    stat_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="statId")] = pydantic.Field(
        default=None
    )
    """
    Unique programmer friendly ID for this stat
    """

    stat_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="statName")] = pydantic.Field(
        default=None
    )
    """
    Display name
    """

    stat_name_abbr: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="statNameAbbr")] = (
        pydantic.Field(default=None)
    )
    """
    Display name abbreviated
    """

    unit_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="unitLabel")] = pydantic.Field(
        default=None
    )
    """
    Localized Unit Name for the stat.
    """

    unit_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="unitType")] = pydantic.Field(
        default=None
    )
    """
    Unit, if any, for the statistic
    """

    weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    Weight assigned to this stat indicating its relative impressiveness.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
