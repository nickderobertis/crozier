

import typing

TemplateParameters = typing.List[str]
"""
The parameters are an array of strings, with the first string being used for {{1}} in the template, with the second being {{2}} etc. Only required if the template specified by `name` contains parameters.
"""
