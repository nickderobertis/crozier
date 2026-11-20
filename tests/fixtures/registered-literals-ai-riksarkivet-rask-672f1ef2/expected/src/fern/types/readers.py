

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reader_info import ReaderInfo


class Readers(UniversalBaseModel):
    """
    Who has READ ``dataset`` — the access-audit surface that turns the #41 read log (capture-only until
    now) into a query. Owner/writer-gated (stricter than reader-gated ``/producers``): an access log
    reveals who touched a dataset, so only a data owner may audit it, not any casual reader.
    """

    dataset: str
    readers: typing.Optional[typing.List[ReaderInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
