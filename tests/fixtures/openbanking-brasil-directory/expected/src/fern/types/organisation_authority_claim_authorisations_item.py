

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .status_enum import StatusEnum


class OrganisationAuthorityClaimAuthorisationsItem(UniversalBaseModel):
    member_state: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MemberState"),
        pydantic.Field(alias="MemberState", description="Abbreviated states information i.e. GB, IE, NL etc"),
    ] = None
    """
    Abbreviated states information i.e. GB, IE, NL etc
    """

    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
