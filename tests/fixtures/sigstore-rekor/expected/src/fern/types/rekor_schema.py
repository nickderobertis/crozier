

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rekor_schema_data import RekorSchemaData
from .rekor_schema_signature import RekorSchemaSignature


class RekorSchema(UniversalBaseModel):
    """
    Schema for Rekord object
    """

    signature: RekorSchemaSignature = pydantic.Field()
    """
    Information about the detached signature associated with the entry
    """

    data: RekorSchemaData = pydantic.Field()
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
