

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .category_ref import CategoryRef
from .ser_name import SerName
from .ser_version import SerVersion
from .transports_supported import TransportsSupported


class ServiceDescriptor(UniversalBaseModel):
    """
    'The ServiceDescriptor data type describes a MEC service produced by a service-providing MEC application.'
    """

    ser_category: typing_extensions.Annotated[typing.Optional[CategoryRef], FieldMetadata(alias="serCategory")] = None
    ser_name: typing_extensions.Annotated[SerName, FieldMetadata(alias="serName")]
    transports_supported: typing_extensions.Annotated[
        typing.Optional[TransportsSupported], FieldMetadata(alias="transportsSupported")
    ] = None
    version: SerVersion

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
