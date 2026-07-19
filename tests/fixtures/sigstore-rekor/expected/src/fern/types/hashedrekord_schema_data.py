

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hashedrekord_schema_data_hash import HashedrekordSchemaDataHash


class HashedrekordSchemaData(UniversalBaseModel):
    """
    Information about the content associated with the entry
    """

    hash: typing.Optional[HashedrekordSchemaDataHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value for the content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
