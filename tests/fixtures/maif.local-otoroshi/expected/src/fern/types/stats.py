

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Stats(UniversalBaseModel):
    """
    Live stats for a service or globally
    """

    calls: int = pydantic.Field()
    """
    Number of calls on the specified service or globally
    """

    concurrent_handled_requests: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="concurrentHandledRequests"),
        pydantic.Field(alias="concurrentHandledRequests", description="The number of concurrent request currently"),
    ]
    """
    The number of concurrent request currently
    """

    data_in: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dataIn"),
        pydantic.Field(
            alias="dataIn", description="The amount of data sent to the specified service or Otoroshi globally"
        ),
    ]
    """
    The amount of data sent to the specified service or Otoroshi globally
    """

    data_in_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="dataInRate"),
        pydantic.Field(
            alias="dataInRate", description="The rate of data sent to the specified service or Otoroshi globally"
        ),
    ]
    """
    The rate of data sent to the specified service or Otoroshi globally
    """

    data_out: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dataOut"),
        pydantic.Field(
            alias="dataOut", description="The amount of data sent from the specified service or Otoroshi globally"
        ),
    ]
    """
    The amount of data sent from the specified service or Otoroshi globally
    """

    data_out_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="dataOutRate"),
        pydantic.Field(
            alias="dataOutRate", description="The rate of data sent from the specified service or Otoroshi globally"
        ),
    ]
    """
    The rate of data sent from the specified service or Otoroshi globally
    """

    duration: float = pydantic.Field()
    """
    The average duration for a call
    """

    overhead: float = pydantic.Field()
    """
    The average overhead time induced by Otoroshi for each call
    """

    rate: float = pydantic.Field()
    """
    The rate of data sent from and to the specified service or Otoroshi globally
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
