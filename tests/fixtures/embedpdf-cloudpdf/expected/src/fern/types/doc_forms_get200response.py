

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_calculation_order_item import DocFormsGet200ResponseCalculationOrderItem
from .doc_forms_get200response_fields_item import DocFormsGet200ResponseFieldsItem
from .doc_forms_get200response_form_kind import DocFormsGet200ResponseFormKind


class DocFormsGet200Response(UniversalBaseModel):
    form_kind: typing_extensions.Annotated[
        DocFormsGet200ResponseFormKind, FieldMetadata(alias="formKind"), pydantic.Field(alias="formKind")
    ]
    needs_appearances: typing_extensions.Annotated[
        bool, FieldMetadata(alias="needsAppearances"), pydantic.Field(alias="needsAppearances")
    ]
    fields: typing.List[DocFormsGet200ResponseFieldsItem]
    calculation_order: typing_extensions.Annotated[
        typing.List[typing.Optional[DocFormsGet200ResponseCalculationOrderItem]],
        FieldMetadata(alias="calculationOrder"),
        pydantic.Field(alias="calculationOrder"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
