# ignition-api-stubs

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ignition-api-stubs)](https://pypi.org/project/ignition-api-stubs/)
[![Downloads](https://pepy.tech/badge/ignition-api-stubs)](https://pepy.tech/project/ignition-api-stubs)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ignition-devs/ignition-api-8.1-stubs/main.svg)](https://results.pre-commit.ci/latest/github/ignition-devs/ignition-api-8.1-stubs/main)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/orgs/ignition-devs/discussions)

This package contains a collection of [stubs] for [`ignition-api-8.1`]. These
files were generated using `mypy`'s [`stubgen`].

## Installation and usage

To use ignition-api-stubs, you may install it with `pip`. It requires Python
3.7+ through 3.12.

> [!WARNING]
> Python 3.13 will not be supported.

```sh
python3 -m pip install ignition-api-stubs
```

To run `mypy` against your code, execute the following command passing the
source directory (typically `src`) or a single file:

```sh
mypy --py2 src
```

Or

```sh
mypy --py2 code.py
```

## Contributing

See [contributing guidelines].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here].

## License

See the [LICENSE].

## Code of conduct

See [code of conduct].

<!-- Links -->
[code of conduct]: https://github.com/ignition-devs/.github/blob/main/CODE_OF_CONDUCT.md
[contributing guidelines]: https://github.com/ignition-devs/ignition-api-8.1/blob/main/CONTRIBUTING.md
[Discussions]: https://github.com/ignition-devs/discussions/discussions
[here]: https://github.com/ignition-devs/ignition-api-8.1-stubs/graphs/contributors
[`ignition-api-8.1`]: https://github.com/ignition-devs/ignition-api-8.1
[LICENSE]: ./LICENSE
[`stubgen`]: https://mypy.readthedocs.io/en/stable/stubgen.html
[stubs]: https://www.python.org/dev/peps/pep-484/
