

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authority import Authority
from .time_period import TimePeriod
from .uas_zone_version_message_item import UasZoneVersionMessageItem
from .uas_zone_version_name_item import UasZoneVersionNameItem
from .uas_zone_version_other_reason_info_item import UasZoneVersionOtherReasonInfoItem
from .uas_zone_version_reason_item import UasZoneVersionReasonItem
from .uas_zone_version_regulation_exemption import UasZoneVersionRegulationExemption
from .uas_zone_version_type import UasZoneVersionType
from .uas_zone_version_variant import UasZoneVersionVariant


class UasZoneVersion(UniversalBaseModel):
    """
    A specific version of an airspace of defined dimensions, above the land areas
    or territorial waters of a State, within which a particular restriction or
    condition for UAS flights applies.
    """

    identifier: str
    country: str
    name: typing.Optional[typing.List[UasZoneVersionNameItem]] = None
    type: UasZoneVersionType
    variant: UasZoneVersionVariant
    restriction_conditions: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="restrictionConditions"),
        pydantic.Field(alias="restrictionConditions"),
    ] = None
    region: typing.Optional[int] = None
    reason: typing.Optional[typing.List[UasZoneVersionReasonItem]] = pydantic.Field(default=None)
    """
    An indication of a reason that justifies the existence of an UAS Zone,
    represented as a string with a list of enumerated values.
    """

    other_reason_info: typing_extensions.Annotated[
        typing.Optional[typing.List[UasZoneVersionOtherReasonInfoItem]],
        FieldMetadata(alias="otherReasonInfo"),
        pydantic.Field(alias="otherReasonInfo"),
    ] = None
    regulation_exemption: typing_extensions.Annotated[
        typing.Optional[UasZoneVersionRegulationExemption],
        FieldMetadata(alias="regulationExemption"),
        pydantic.Field(
            alias="regulationExemption",
            description="A choice between a positive (yes) or a negative (no) applicability,\nrepresented as a string with a list of enumerated values.",
        ),
    ] = None
    """
    A choice between a positive (yes) or a negative (no) applicability,
    represented as a string with a list of enumerated values.
    """

    message: typing.Optional[typing.List[UasZoneVersionMessageItem]] = None
    zone_authority: typing_extensions.Annotated[
        typing.List[Authority], FieldMetadata(alias="zoneAuthority"), pydantic.Field(alias="zoneAuthority")
    ]
    limited_applicability: typing_extensions.Annotated[
        typing.Optional[typing.List[TimePeriod]],
        FieldMetadata(alias="limitedApplicability"),
        pydantic.Field(alias="limitedApplicability"),
    ] = None
    extended_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="extendedProperties"),
        pydantic.Field(alias="extendedProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
