

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssetHolderName(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    full_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="FullName"),
        pydantic.Field(alias="FullName", description="The unparsed name of either an individual or a legal entity."),
    ]
    """
    The unparsed name of either an individual or a legal entity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
