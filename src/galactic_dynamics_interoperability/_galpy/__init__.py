"""Galpy interoperability."""

from __future__ import annotations

__all__ = ["GalpyLibrary"]


from typing import Any, final

from plum import conversion_method

from galactic_dynamics_interoperability._base import AbstractInteroperableLibrary
from galactic_dynamics_interoperability._core import convert_potential


@final
class GalpyLibrary(AbstractInteroperableLibrary):
    """The :mod:`galpy` library."""


# plum support
@conversion_method(type_from=object, type_to=GalpyLibrary)  # type: ignore[misc]
def convert_to_galpy_library(obj: object) -> Any:
    """Convert to an :class:`GalpyLibrary` object."""
    convert_potential(GalpyLibrary, obj)
