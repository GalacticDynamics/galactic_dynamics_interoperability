<h1 align='center'> galactic_dynamics_interoperability </h1>
<h2 align="center"> Interoperability Between Galactic Dynamics Libraries </h2>

> [!WARNING] This package is under active development and is not ready for
> public use.

`galactic_dynamics_interoperability` provides tools for converting objects
between galactic dynamics Python libraries.

## Installation

[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

```bash
pip install galactic_dynamics_interoperability
```

## Documentation

[![Documentation Status][rtd-badge]][rtd-link]

The main docs are in development.

### Quick Start

`galactic_dynamics_interoperability` provides type objects for representing
different galactic dynamics libraries. These types are used for dispatching to
converters:

- `AbstractInteroperableLibrary` : the base class
- `AgamaLibrary` : represents [`agama`][Agama]
- `GalaLibrary` : represents [`gala`][Gala]
- `GalaxLibrary` : represents [`galax`][Galax]
- `GalpyLibrary` : represents [`galpy`][Galpy]

To convert potential objects between libraries use `convert_potential`. As an
example, here is converting from a `gala` Potential to a `galax` Potential.

```pycon
>>> from galactic_dynamics_interoperability import convert_potential, GalaxLibrary
>>> import gala.potential
>>> from gala.units import galactic
>>> import galax.potential

>>> potential = gala.potential.KeplerPotential(m=1e11, units=galactic)
>>> convert_potential(GalaxLibrary, potential)
KeplerPotential(
    units=LTMAUnitSystem( length=Unit("kpc"), ...),
    constants=ImmutableMap({'G': ...}),
    m_tot=ConstantParameter( value=Quantity[...](value=f64[], unit=Unit("solMass")) )
)
```

### Q & A

- _Why have the argument order `convert_potential(to, from)`, not
  `convert_potential(from, to)`?_

  This is because of how Julia structures its conversions
  ([`convert`](https://docs.julialang.org/en/v1/base/base/#Base.convert)), from
  which this library draws inspiration. We aim to increase interoperability
  between galactic dynamics libraries and with the ongoing development of
  [Python-Julia bridges](https://juliapackages.com/p/pythoncall),
  Julia-wrapped-into-Python galactic dynamics libraries are well within our
  remit.

## Citation

[![DOI][zenodo-badge]][zenodo-link]

If you found this library to be useful and want to support the development and
maintenance of lower-level code libraries for the scientific community, please
consider citing this work.

## Development

[![codecov][codecov-badge]][codecov-link]
[![Actions Status][actions-badge]][actions-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

We welcome contributions!

<!-- prettier-ignore-start -->

<!-- Links -->

[Agama]:                    https://pypi.org/project/agama/
[Gala]:                     https://pypi.org/project/gala/
[Galax]:                    https://pypi.org/project/galax/
[Galpy]:                    https://pypi.org/project/galpy/

<!-- Badges -->

[actions-badge]:            https://github.com/GalacticDynamics/galactic_dynamics_interoperability/workflows/CI/badge.svg
[actions-link]:             https://github.com/GalacticDynamics/galactic_dynamics_interoperability/actions
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[codecov-badge]:            https://codecov.io/gh/GalacticDynamics/galactic_dynamics_interoperability/graph/badge.svg
[codecov-link]:             https://codecov.io/gh/GalacticDynamics/galactic_dynamics_interoperability
[github-discussions-link]:  https://github.com/GalacticDynamics/galactic_dynamics_interoperability/discussions
[pypi-link]:                https://pypi.org/project/galactic_dynamics_interoperability/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/galactic_dynamics_interoperability
[pypi-version]:             https://img.shields.io/pypi/v/galactic_dynamics_interoperability
[rtd-badge]:                https://readthedocs.org/projects/galactic_dynamics_interoperability/badge/?version=latest
[rtd-link]:                 https://galactic_dynamics_interoperability.readthedocs.io/en/latest/?badge=latest
[zenodo-badge]:             https://zenodo.org/badge/755708966.svg
[zenodo-link]:              https://zenodo.org/doi/10.5281/zenodo.10850557

<!-- prettier-ignore-end -->
