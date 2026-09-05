

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MetadataRequest(UniversalBaseModel):
    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the metadata object"),
    ] = None
    """
    The name of the metadata object
    """

    type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The type of metadata i.e. scope, grant_type..."),
    ] = None
    """
    The type of metadata i.e. scope, grant_type...
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
