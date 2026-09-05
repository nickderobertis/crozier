

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProjectShareAccepted(UniversalBaseModel):
    sharee_email: typing_extensions.Annotated[
        str, FieldMetadata(alias="shareeEmail"), pydantic.Field(alias="shareeEmail")
    ]
    confirmation_link: typing_extensions.Annotated[
        str, FieldMetadata(alias="confirmationLink"), pydantic.Field(alias="confirmationLink")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
