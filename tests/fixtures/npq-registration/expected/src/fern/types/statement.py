

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id_attribute import IdAttribute
from .statement_attributes import StatementAttributes
from .statement_type import StatementType


class Statement(UniversalBaseModel):
    """
    A financial statement.
    """

    id: IdAttribute
    type: StatementType = pydantic.Field()
    """
    The data type.
    """

    attributes: StatementAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
