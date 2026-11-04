

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organization import Organization
from .organization_address import OrganizationAddress


class WhoIsResponse(UniversalBaseModel):
    aliases: typing.Optional[typing.Dict[str, str]] = None
    organization: typing.Optional[Organization] = None
    organization_address: typing_extensions.Annotated[
        typing.Optional[OrganizationAddress],
        FieldMetadata(alias="organizationAddress"),
        pydantic.Field(alias="organizationAddress"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
