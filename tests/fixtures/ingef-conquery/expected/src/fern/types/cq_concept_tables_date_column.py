

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validity_date_id import ValidityDateId


class CqConceptTablesDateColumn(UniversalBaseModel):
    """
    Allows the selection of one of pre-defined date for date-restrictions.
    """

    value: typing.Optional[ValidityDateId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
