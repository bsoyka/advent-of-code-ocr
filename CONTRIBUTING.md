# Contributing

Thanks for taking the time to contribute! Here are a few guidelines to follow:

* First things first, please **follow our
  [code of conduct](https://github.com/bsoyka/.github/blob/master/CODE_OF_CONDUCT.md)**
  in all your interactions with this project.
* All contributions should **start with a GitHub issue** to avoid unneccessary
  contributions.
* If you'd like to work on an issue, **please comment** on it. A maintainer will
  then remove any "help wanted" tags and assign the issue to you to make sure no
  duplicate pull requests are made.
* Please test your code (see [Testing](#testing)) before committing it.
* After making updates to the code, **please format it** using the latest
  versions of `black` and `isort` (see
  [Development Dependencies](#development-dependencies)) before pushing.
* Making a pull request will automatically request a review from the appropriate
  reviewer(s).
* Once your pull request has the necessary reviews and checks, it'll be merged
  in!

## Development Dependencies

To help out on this project, it's recommended and helpful that you install and
use the following tools:

* [`black`](https://black.readthedocs.io/en/stable/)
* [`isort`](https://pycqa.github.io/isort/)
* [`pytest`](https://docs.pytest.org/en/stable/)

To install all of these tools at once, just use the `requirements.txt` file:

```sh
$ pip install -r requirements.txt
```

If possible, it's also recommended that you install the
[EditorConfig](https://editorconfig.org/) plugin/extension for your code editor.

### Testing

This project uses `pytest` (see
[Development Dependencies](#development-dependencies)) for testing code
functionality. All tests will be automatically run when you make a pull request,
but it's recommended that you check your code against the tests before you
commit and push.

You can run the tests with one simple command:

```sh
$ pytest
```

If you add any new functionality to the project, please add the appropriate test
cases to cover it.
