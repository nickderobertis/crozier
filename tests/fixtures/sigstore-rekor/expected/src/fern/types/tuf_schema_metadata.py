

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TufSchemaMetadata(UniversalBaseModel):
    """
    TUF metadata
    """

    content: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Specifies the metadata inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
