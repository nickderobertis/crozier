

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Export(UniversalBaseModel):
    download_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="downloadUrl"), pydantic.Field(alias="downloadUrl")
    ] = None
    finished: typing.Optional[dt.datetime] = None
    id: str
    owner: str
    progress: typing.Optional[float] = None
    started: dt.datetime
    step: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
