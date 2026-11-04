

import typing

from .fragment_parameter import FragmentParameter
from .nil import Nil

ListFragmentParameter = typing.Union[Nil, typing.List[FragmentParameter]]
