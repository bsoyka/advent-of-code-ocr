# Contributing to Advent of Code OCR

Thank you for taking the time to contribute! Open-source projects are powered by and for
the community, and your help is always greatly appreciated.

All types of contributions are encouraged and valued—no matter how small or large.

## Social and financial support

If you like this project but don't have time to contribute in other ways, you can still
help out! Here are just a few ideas:

- Star the repository on GitHub.
- Discuss Advent of Code OCR out in the real world.
- Refer to this project in your readme.
- Sign up for [thanks.dev][thanks] to automatically spread financial support to the
  open-source maintainers you rely on. (See [my profile][thanks-me]!)
- Financially support my work directly via [GitHub Sponsors][sponsor].

## Ground rules

This project is governed by [a code of conduct][conduct]. By participating in this
project and its associated community spaces, you are expected to uphold this code.
Please follow the process described in that document to report any potential violations.

## Before you start

Before you start contributing, ensure you have the following:

- A computer
- A strong internet connection
- A [GitHub][github] account

Additionally, if you're interested in contributing code, you'll need a few other things:

- [Git][git] and some of the basic knowledge to use it
- [uv][uv], the package and project manager this project is built with

There are [many ways to do install uv][uv-install] depending on your system setup and
preferred package manager. If you're using macOS or Linux, the following command will
generally work:

```shell
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

> [!NOTE]
> uv takes care of installing and running all the other tools used in this project. If
> you'd like, you can choose to install some of them separately,
> like [Ruff][ruff], [pre-commit][pre-commit], and [tox][tox], but you don't need to, as
> you can run all of these through uv.

## Contributing code

At the core of any Python library is its code, and Advent of Code OCR is no
different. Take a look at [existing issues][issues] to see if there's something you'd
like to work on, or [open a new issue][issues-new] if you have another idea!

### Tooling overview

Here's a quick look at the tools used behind the scenes of this project! Assuming you
set up uv correctly, these commands should just work, with no manual installation steps
necessary.

If this looks like a lot, don't worry—all of these tools also run automatically on
GitHub when you submit a pull request. While running these checks before you commit your
changes is helpful, it's not an absolute requirement as we can work through any fixes
together later.

> [!TIP]
> Many of these tools have multiple ways to run them. Use whichever one you'd like—each
> method listed for a tool should do the same thing.

| Tool                     | What it does                                                   | How to use it                                                                                                                                                                                                                              |
|--------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Ruff][ruff]             | Python linting and formatting                                  | <ul><li>By itself: `uv run ruff check --fix && uv run ruff format`</li> <li>Through pre-commit</li> <li>Through tox (runs all pre-commit hooks): `uv run tox -e style`</li></ul>                                                           |
| [pre-commit][pre-commit] | Automated checks before you commit                             | <ul><li>Set up automated runs before you commit: `uv run pre-commit install`</li> <li>Run manually only on changed files: `uv run pre-commit run`</li> <li>Run on all files: `uv run pre-commit run -a` or `uv run tox -e style`</li></ul> |
| [pytest][pytest]         | Unit testing                                                   | <ul><li>Run only on one Python version: `uv run pytest`</li> <li>Across all supported Python versions (through tox): `uv run tox`</li></ul>                                                                                                |
| [mypy][mypy]             | Static type checking                                           | <ul><li>By itself: `uv run mypy .`</li> <li>Through tox: `uv run tox -e typing`</li></ul>                                                                                                                                                  |
| [tox][tox]               | Testing automation across multiple Python virtual environments | *See instructions for each tool above.*                                                                                                                                                                                                    |

Optionally, you can use [`just`][just] to run the commands listed above. [Install
`just`][just-install], then run `just --list` to see available commands.

### Code style

In general, don't worry too much about code style rules. Automation can take care of
most of the little things—if the tools listed above like your code, I probably do too.

If you really must know what code should look like in this project, we generally follow
the [Black style][black-style], as [implemented by Ruff][ruff-philosophy]. An exception
is that we prefer single quotes (`''` rather than `""`), but this is also handled by our
Ruff configuration. Let Ruff do its thing!

For docstrings, [Google style][google-docstrings] is preferred. See existing
documentation in the codebase for examples!

Additionally, the [Zen of Python][pep-20] (PEP 20) by Tim Peters is recommended reading:
> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.  
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one-- and preferably only one --obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.  
> Now is better than never.  
> Although never is often better than *right* now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea—let's do more of those!

### Code contribution process

Follow the standard [fork-and-branch workflow][fork-branch] for an idea of how to
contribute to this and other open-source projects. Generally, this involves a few steps:

1. [Fork and clone][git-fork] the bsoyka/advent-of-code-ocr repository to make a copy
   you can edit. I also recommend making a new branch on your fork for your changes.
2. Make your changes, testing along the way
   using [this project's tools](#tooling-overview).
3. In most cases, you should add or edit unit tests that automatically check the
   functionality you're adding or changing. See existing test cases for examples, or ask
   for help when you submit your changes!
4. [Commit][git-commit] your changes and [push][git-push] them to GitHub.
5. [Create a pull request][git-pr] to propose that your changes be merged into the main
   repository.
6. Wait for a review and respond to any comments or requested changes.
7. Take a deep breath and pat yourself on the back. Once your pull request is approved
   and merged, I'll take care of the rest. Thank you for your contributions!

If you have any questions throughout the contribution process (or you don't hear from me
within a few days after submitting a pull request), please email hello@bsoyka.me.

## Contributing documentation

Documentation is a key part of this project, and additions and improvements are always
appreciated. We use [Sphinx][sphinx] with [reStructuredText (rST)][rst] for authoring
documentation. If you’re new to Sphinx or reST, check out
the [Sphinx rST Primer][rst-primer] for a quick introduction.

To build the documentation locally, run:

```shell
uv run tox -e docs
```

or, if you have `just` installed:

```shell
just docs
```

This project aims to follow the [Diátaxis documentation framework][diataxis], which
recognizes four distinct types of documentation:

- **Tutorials**: Learning-oriented, step-by-step guides for newcomers.
- **How-to guides**: Problem-oriented instructions for accomplishing specific tasks.
- **Technical reference**: Information-oriented, detailed descriptions of APIs and
  configuration.
- **Explanation**: Understanding-oriented material that provides context, background,
  and rationale.

When contributing documentation, please consider which of these needs your addition
addresses and structure your content accordingly. This helps keep the documentation
clear, discoverable, and useful for everyone.

[black-style]: https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html

[conduct]: https://github.com/bsoyka/policy/blob/main/code-of-conduct.md

[diataxis]: https://diataxis.fr/

[fork-branch]: https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/

[git]: https://git-scm.com/

[git-commit]: https://training.github.com/downloads/github-git-cheat-sheet/#make-changes

[git-fork]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo

[git-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

[git-push]: https://training.github.com/downloads/github-git-cheat-sheet/#synchronize-changes

[github]: https://github.com/

[google-docstrings]: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

[just]: https://just.systems/

[just-install]: https://just.systems/man/en/packages.html

[mypy]: https://mypy-lang.org/

[pep-20]: https://peps.python.org/pep-0020/

[pre-commit]: https://pre-commit.com/

[pytest]: https://docs.pytest.org/en/stable/

[rst]: https://docutils.sourceforge.io/rst.html

[rst-primer]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

[ruff]: https://docs.astral.sh/ruff/

[ruff-philosophy]: https://docs.astral.sh/ruff/formatter/#philosophy

[sphinx]: https://www.sphinx-doc.org/

[sponsor]: https://github.com/sponsors/bsoyka

[thanks]: https://thanks.dev/home

[thanks-me]: https://thanks.dev/u/gh/bsoyka

[tox]: https://tox.wiki/en/latest/index.html

[uv]: https://docs.astral.sh/uv/

[uv-install]: https://docs.astral.sh/uv/getting-started/installation/

[issues]: https://github.com/bsoyka/advent-of-code-ocr/issues

[issues-new]: https://github.com/bsoyka/advent-of-code-ocr/issues/new
