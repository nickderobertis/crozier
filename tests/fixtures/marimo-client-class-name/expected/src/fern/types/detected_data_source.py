

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detected_data_source_category import DetectedDataSourceCategory
from .detected_data_source_confidence import DetectedDataSourceConfidence
from .detected_data_source_configuration import DetectedDataSourceConfiguration
from .detected_data_source_hides_when import DetectedDataSourceHidesWhen
from .detected_data_source_origin import DetectedDataSourceOrigin


class DetectedDataSource(UniversalBaseModel):
    """
    A secret-free datasource suggestion produced by the kernel.
    """

    category: DetectedDataSourceCategory
    code: str
    confidence: DetectedDataSourceConfidence
    configuration: typing.List[DetectedDataSourceConfiguration]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    hides_when: typing_extensions.Annotated[
        DetectedDataSourceHidesWhen, FieldMetadata(alias="hidesWhen"), pydantic.Field(alias="hidesWhen")
    ]
    id: str
    integration: str
    origins: typing.List[DetectedDataSourceOrigin]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
