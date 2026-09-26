

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProcareMessageStatus(UniversalBaseModel):
    """
    Status object returned by the configured message service. The bundled service returns task_id and status, and may emit zero-value created_at/updated_at timestamps (0001-01-01T00:00:00Z) because this lookup does not load them. Unknown tasks return null with HTTP 200. Additional upstream properties are preserved by V3.
    """

    task_id: str
    status: str
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
