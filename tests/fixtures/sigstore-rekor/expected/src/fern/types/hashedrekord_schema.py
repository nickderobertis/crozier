

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hashedrekord_schema_data import HashedrekordSchemaData
from .hashedrekord_schema_signature import HashedrekordSchemaSignature


class HashedrekordSchema(UniversalBaseModel):
    """
    Schema for Hashed Rekord object
    """

    signature: HashedrekordSchemaSignature = pydantic.Field()
    """
    Information about the detached signature associated with the entry
    """

    data: HashedrekordSchemaData = pydantic.Field()
    """
    Information about the content associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
