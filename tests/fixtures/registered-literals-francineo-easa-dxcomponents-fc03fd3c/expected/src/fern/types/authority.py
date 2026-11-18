

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authority_contact_name_item import AuthorityContactNameItem
from .authority_name_item import AuthorityNameItem
from .authority_purpose import AuthorityPurpose
from .authority_service_item import AuthorityServiceItem


class Authority(UniversalBaseModel):
    """
    A relevant authority that is in charge for authorizing, being notified or providing
    information for UAS operations in the UAS Geographical Zone.
    """

    name: typing.Optional[typing.List[AuthorityNameItem]] = None
    service: typing.Optional[typing.List[AuthorityServiceItem]] = None
    contact_name: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorityContactNameItem]],
        FieldMetadata(alias="contactName"),
        pydantic.Field(alias="contactName"),
    ] = None
    site_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="siteURL"), pydantic.Field(alias="siteURL")
    ] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    purpose: AuthorityPurpose = pydantic.Field()
    """
    Roles that an authority has in relation with the UAS zone, represented by
    a string with an enumerated list of values.
    """

    interval_before: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="intervalBefore"),
        pydantic.Field(
            alias="intervalBefore",
            description="A period of time expressed according to the ISO 8601 rules for time intervals.",
        ),
    ] = None
    """
    A period of time expressed according to the ISO 8601 rules for time intervals.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
