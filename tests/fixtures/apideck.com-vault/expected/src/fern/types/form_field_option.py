

import typing

from .form_field_option_group import FormFieldOptionGroup
from .simple_form_field_option import SimpleFormFieldOption

FormFieldOption = typing.Union[SimpleFormFieldOption, FormFieldOptionGroup]
