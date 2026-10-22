

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_response_organization_access_access_control import MeResponseOrganizationAccessAccessControl


class MeResponseOrganizationAccess(UniversalBaseModel):
    access_control: typing_extensions.Annotated[
        MeResponseOrganizationAccessAccessControl,
        FieldMetadata(alias="accessControl"),
        pydantic.Field(alias="accessControl"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
