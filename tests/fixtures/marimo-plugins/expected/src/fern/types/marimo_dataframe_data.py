

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoDataframeData(UniversalBaseModel):
    label: typing.Optional[str] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    show_download: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showDownload"), pydantic.Field(alias="showDownload")
    ] = None
    dataframe_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dataframeName"), pydantic.Field(alias="dataframeName")
    ] = None
    columns: typing.List[typing.List[typing.Any]]
    lazy: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
