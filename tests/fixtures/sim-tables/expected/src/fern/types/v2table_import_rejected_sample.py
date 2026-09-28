

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2TableImportRejectedSample(UniversalBaseModel):
    """
    One source record a table import could not read.
    """

    code: str = pydantic.Field()
    """
    CSV parser error code, e.g. CSV_QUOTE_NOT_CLOSED.
    """

    line: typing.Optional[int] = pydantic.Field(default=None)
    """
    1-based source line the parser had reached when it gave up, or null.
    """

    message: str = pydantic.Field()
    """
    Parser message for the dropped record.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
