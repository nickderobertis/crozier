

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExportStatementPaymentRead(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the statement model's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the single payment statement model.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the export.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the statement model's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
