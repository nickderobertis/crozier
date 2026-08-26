

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .road_operator_road_operator_type import RoadOperatorRoadOperatorType


class RoadOperator(UniversalBaseModel):
    """
    A road operator is someone who is responsible for the maintenance of road sections.
    """

    road_operator_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="roadOperatorName"),
        pydantic.Field(alias="roadOperatorName", description="The name of the road operator."),
    ] = None
    """
    The name of the road operator.
    """

    road_operator_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="roadOperatorCode"),
        pydantic.Field(alias="roadOperatorCode", description="The code of the road operator."),
    ] = None
    """
    The code of the road operator.
    """

    road_operator_type: typing_extensions.Annotated[
        typing.Optional[RoadOperatorRoadOperatorType],
        FieldMetadata(alias="roadOperatorType"),
        pydantic.Field(alias="roadOperatorType", description="The road operator type."),
    ] = None
    """
    The road operator type.
    """

    municipality_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="municipalityId"),
        pydantic.Field(
            alias="municipalityId",
            description="The municipality id of the road operator. This is only applicable of road operators of type Municipality.",
        ),
    ] = None
    """
    The municipality id of the road operator. This is only applicable of road operators of type Municipality.
    """

    request_exemption_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestExemptionUrl"),
        pydantic.Field(alias="requestExemptionUrl", description="URL to request an exemption."),
    ] = None
    """
    URL to request an exemption.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
