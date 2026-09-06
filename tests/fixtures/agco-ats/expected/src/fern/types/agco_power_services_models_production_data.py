

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgcoPowerServicesModelsProductionData(UniversalBaseModel):
    """
    Production data for an AGCO Power engine.
    """

    data_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DataType"),
        pydantic.Field(
            alias="DataType",
            description="Type of data. Valid types are (but not limited to)\r\n            'PowerCalibration'",
        ),
    ]
    """
    Type of data. Valid types are (but not limited to)
                'PowerCalibration'
    """

    data_values: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DataValues"),
        pydantic.Field(alias="DataValues", description="Raw values of the calibration data"),
    ]
    """
    Raw values of the calibration data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
