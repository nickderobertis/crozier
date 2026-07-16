

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ImportExportStats(UniversalBaseModel):
    """
    Global stats for the current Otoroshi instances
    """

    calls: int = pydantic.Field()
    """
    Number of calls to Otoroshi globally
    """

    data_in: typing_extensions.Annotated[int, FieldMetadata(alias="dataIn")] = pydantic.Field()
    """
    The amount of data sent to Otoroshi globally
    """

    data_out: typing_extensions.Annotated[int, FieldMetadata(alias="dataOut")] = pydantic.Field()
    """
    The amount of data sent from Otoroshi globally
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
