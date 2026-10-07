"""Test the package itself.

Copyright (c) 2024 Galactic Dynamics Interoperability Library Maintainers. All
rights reserved.
"""

import importlib.metadata

import galactic_dynamics_interoperability as m


def test_version():
    """Test the package version."""
    assert (
        importlib.metadata.version("galactic_dynamics_interoperability")
        == m.__version__
    )
