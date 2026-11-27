

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_form_definition_fields_item import NestedFormDefinitionFieldsItem


class NestedFormDefinition(UniversalBaseModel):
    fields: typing.Optional[typing.List[NestedFormDefinitionFieldsItem]] = pydantic.Field(default=None)
    """
    Each element defines a field in our form. Form fields are composed of a set of attributes at the top level, and a polymorphic set of attributes under the properties attribute. The specific properties that can be passed to a form field are unique to whatever is set in the type attribute. For example, a form field of type STRING_SELECTION will have an attribute within properties of options; however, this options attribute does not make sense for a form field of type ENTITY_LINK.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
