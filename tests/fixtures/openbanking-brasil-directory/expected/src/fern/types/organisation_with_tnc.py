

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organisation import Organisation
from .organisation_with_tnc_tnc_details import OrganisationWithTncTncDetails


class OrganisationWithTnc(UniversalBaseModel):
    org_details: typing_extensions.Annotated[
        typing.Optional[Organisation], FieldMetadata(alias="OrgDetails"), pydantic.Field(alias="OrgDetails")
    ] = None
    tnc_details: typing_extensions.Annotated[
        typing.Optional[OrganisationWithTncTncDetails],
        FieldMetadata(alias="TncDetails"),
        pydantic.Field(alias="TncDetails"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
