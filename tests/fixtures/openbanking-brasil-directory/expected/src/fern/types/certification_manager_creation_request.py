

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CertificationManagerCreationRequest(UniversalBaseModel):
    email: typing_extensions.Annotated[
        str, FieldMetadata(alias="Email"), pydantic.Field(alias="Email", description="The super user email address")
    ]
    """
    The super user email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
