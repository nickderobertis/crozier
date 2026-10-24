

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateBridgeTokenEndpointOutput(UniversalBaseModel):
    read_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="readKey"),
        pydantic.Field(alias="readKey", description="The read key used to retrieve the authentication result."),
    ]
    """
    The read key used to retrieve the authentication result.
    """

    write_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="writeKey"),
        pydantic.Field(alias="writeKey", description="The write key used to store the authentication result."),
    ]
    """
    The write key used to store the authentication result.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
