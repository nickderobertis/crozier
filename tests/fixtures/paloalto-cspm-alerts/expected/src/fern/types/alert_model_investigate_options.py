

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AlertModelInvestigateOptions(UniversalBaseModel):
    """
    Investigate Options for search using RQL
    """

    alert_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alertId"), pydantic.Field(alias="alertId", description="alert id")
    ] = None
    """
    alert id
    """

    has_search_execution_support: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasSearchExecutionSupport"),
        pydantic.Field(
            alias="hasSearchExecutionSupport", description="The flag indicates if the policy has RQL execution support"
        ),
    ] = None
    """
    The flag indicates if the policy has RQL execution support
    """

    search_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="searchId"),
        pydantic.Field(alias="searchId", description="searchId for the policy RQL"),
    ] = None
    """
    searchId for the policy RQL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
