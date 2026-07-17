

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

    icon_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconImage"),
        pydantic.Field(alias="iconImage", description="Optional URI to an icon for the statistic"),
    ] = None
    """
    Optional URI to an icon for the statistic
    """

    medal_tier_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="medalTierHash"),
        pydantic.Field(
            alias="medalTierHash", description="The tier associated with this medal - be it implicitly or explicitly."
        ),
    ] = None
    """
    The tier associated with this medal - be it implicitly or explicitly.
    """

    merge_method: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mergeMethod"),
        pydantic.Field(alias="mergeMethod", description="Optional icon for the statistic"),
    ] = None
    """
    Optional icon for the statistic
    """

    modes: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Game modes where this statistic can be reported.
    """

    period_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="periodTypes"),
        pydantic.Field(alias="periodTypes", description="Time periods the statistic covers"),
    ] = None
    """
    Time periods the statistic covers
    """

    stat_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statDescription"),
        pydantic.Field(alias="statDescription", description="Description of a stat if applicable."),
    ] = None
    """
    Description of a stat if applicable.
    """

    stat_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statId"),
        pydantic.Field(alias="statId", description="Unique programmer friendly ID for this stat"),
    ] = None
    """
    Unique programmer friendly ID for this stat
    """

    stat_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statName"),
        pydantic.Field(alias="statName", description="Display name"),
    ] = None
    """
    Display name
    """

    stat_name_abbr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statNameAbbr"),
        pydantic.Field(alias="statNameAbbr", description="Display name abbreviated"),
    ] = None
    """
    Display name abbreviated
    """

    unit_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitLabel"),
        pydantic.Field(alias="unitLabel", description="Localized Unit Name for the stat."),
    ] = None
    """
    Localized Unit Name for the stat.
    """

    unit_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unitType"),
        pydantic.Field(alias="unitType", description="Unit, if any, for the statistic"),
    ] = None
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
