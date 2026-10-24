

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_config import AppConfig
from .page import Page
from .page_info import PageInfo
from .section import Section


class Config(UniversalBaseModel):
    """
    A full config file. `conf.yml` requires `sections`; sub-pages may hold any subset.
    """

    page_info: typing_extensions.Annotated[
        typing.Optional[PageInfo], FieldMetadata(alias="pageInfo"), pydantic.Field(alias="pageInfo")
    ] = None
    app_config: typing_extensions.Annotated[
        typing.Optional[AppConfig], FieldMetadata(alias="appConfig"), pydantic.Field(alias="appConfig")
    ] = None
    sections: typing.Optional[typing.List[Section]] = None
    pages: typing.Optional[typing.List[Page]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
