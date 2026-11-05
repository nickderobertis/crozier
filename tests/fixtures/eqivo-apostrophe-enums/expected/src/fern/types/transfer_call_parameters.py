

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransferCallParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call"),
    ]
    """
    Unique identifier of the call
    """

    url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Url"),
        pydantic.Field(alias="Url", description="Absolute URL which will return the updated RestXML flow"),
    ]
    """
    Absolute URL which will return the updated RestXML flow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
