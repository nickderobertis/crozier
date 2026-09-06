

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrgAdminUserCreateRequest(UniversalBaseModel):
    user_email: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserEmail"), pydantic.Field(alias="UserEmail", description="Admin user email address")
    ]
    """
    Admin user email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
