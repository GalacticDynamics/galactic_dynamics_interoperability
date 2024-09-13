"""Input/output/conversion of potential objects.

This module contains the machinery for I/O and conversion of potential objects.
Conversion is useful for e.g. converting a
:class:`galax.potential.AbstractPotential` object to a
:class:`gala.potential.PotentialBase` object.
"""

from __future__ import annotations

__all__ = [
    "convert_potential",
    "AbstractInteroperableLibrary",
    "GalaxLibrary",
    "GalaLibrary",
    "GalpyLibrary",
]


from typing import Any, final

from plum import dispatch
from typing_extensions import Never


class AbstractInteroperableLibrary:
    """Abstract base class for library type on which to dispatch."""

    def __new__(cls: type[AbstractInteroperableLibrary]) -> Never:
        msg = "cannot instantiate AbstractInteroperableLibrary"

        raise ValueError(msg)


@final
class GalaxLibrary(AbstractInteroperableLibrary):
    """The :mod:`galax` library."""


@final
class GalaLibrary(AbstractInteroperableLibrary):
    """The :mod:`gala` library."""


@final
class GalpyLibrary(AbstractInteroperableLibrary):
    """The :mod:`galpy` library."""


@dispatch.abstract  # type: ignore[misc]
def convert_potential(
    to_: AbstractInteroperableLibrary | Any,  # noqa: ANN401
    from_: Any,  # noqa: ANN401
    /,
    **kwargs: Any,  # noqa: ANN401, ARG001
) -> object:
    msg = f"cannot convert {from_} to {to_}"
    raise NotImplementedError(msg)
