

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams(UniversalBaseModel):
    """
    Extra field parameters.
    """

    max_length: str = pydantic.Field()
    """
    An optional parameter for VarChar values that determines the maximum length of the value in the current field.
    """

    dim: str = pydantic.Field()
    """
    An optional parameter for FloatVector or BinaryVector fields that determines the vector dimension.
    """

    max_capacity: str = pydantic.Field()
    """
    An optional parameter for Array field values that determines the maximum number of elements in the current array field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
