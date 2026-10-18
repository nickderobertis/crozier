

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rekor_schema_data_hash import RekorSchemaDataHash


class RekorSchemaData(UniversalBaseModel):
    """
    Information about the content associated with the entry
    """

    hash: typing.Optional[RekorSchemaDataHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value for the content
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the content inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
