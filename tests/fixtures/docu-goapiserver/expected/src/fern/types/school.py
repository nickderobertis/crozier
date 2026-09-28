

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class School(UniversalBaseModel):
    """
    School.
    """

    id: str
    name: str
    capacity: int
    full_name: str
    gusto_company_uuid: typing.Optional[str] = None
    gusto_company_id: typing.Optional[str] = None
    company_id: str = pydantic.Field()
    """
    Company id.
    """

    street_address: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state: typing.Optional[str] = None
    zip: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    time_zone: typing.Optional[str] = None
    inquiry_call_pre_screen: bool
    is_active: bool
    is_procare_online: bool
    is_procare_online_leads: bool
    procare_desktop_id: typing.Optional[str] = None
    procare_desktop_name: typing.Optional[str] = None
    hide_billing_plan_alerts: bool
    intellikid_location_id: typing.Optional[str] = None
    is_intellikid_school_with_no_leads_in_procare: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsIntellikidSchoolWithNoLeadsInProcare"),
        pydantic.Field(
            alias="IsIntellikidSchoolWithNoLeadsInProcare",
            description="The API currently serializes this property with the exact capitalization shown.",
        ),
    ]
    """
    The API currently serializes this property with the exact capitalization shown.
    """

    lineleader_center_id: typing.Optional[int] = None
    lineleader_center_name: typing.Optional[str] = None
    lineleader_center_code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
