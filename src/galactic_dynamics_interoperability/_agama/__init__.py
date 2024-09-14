"""Agama interoperability."""

from __future__ import annotations

__all__ = ["AgamaLibrary"]


from typing import Any, final

from plum import conversion_method

from galactic_dynamics_interoperability._base import AbstractInteroperableLibrary
from galactic_dynamics_interoperability._core import convert_potential


@final
class AgamaLibrary(AbstractInteroperableLibrary):
    """The :mod:`agama` library."""


# plum support
@conversion_method(type_from=object, type_to=AgamaLibrary)  # type: ignore[misc]
def convert_to_agama_library(obj: object) -> Any:
    """Convert to an :class:`AgamaLibrary` object."""
    convert_potential(AgamaLibrary, obj)
