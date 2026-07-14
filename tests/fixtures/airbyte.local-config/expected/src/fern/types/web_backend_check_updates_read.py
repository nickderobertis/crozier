

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebBackendCheckUpdatesRead(UniversalBaseModel):
    """
    Summary of source and destination definitions that could be updated
    """

    destination_definitions: typing_extensions.Annotated[int, FieldMetadata(alias="destinationDefinitions")]
    source_definitions: typing_extensions.Annotated[int, FieldMetadata(alias="sourceDefinitions")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
