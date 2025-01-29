# My Pre-Commit Hooks

This repository will contain custom pre-commit hooks that I use in various repositories. Check the `.pre-commit-hooks.yaml` for list and matching `src/<hook_name>/` for the hook implementation.

## How to use in a project

Use must first create the `.pre-commit-config.yaml` file in the root of the repository. The file should contain the following:

```yaml
repos:
  - repo: https://github.com/sourander/pre-commit-hooks
    rev: v0.1.0
    hooks:
      - id: extract-exercise-list
```

After this, you need to install the pre-commit library using uv.

```bash
uv add pre-commit --dev
```

Now, you may run the pre-commit hooks using the following command:

```bash
# To target all files, whether they are staged or not
uv run pre-commit --all-files

# Alternatively, you can add it as a dev decependency and run locally
uv add git+https://github.com/sourander/pre-commit-hooks --dev
uv run extract-exercise-list

# To run it normally, simply add and commit files
git add .
git commit -m "Add some changes"
```

**NOTE!** If the commit has to write changes to a file, like `docs/exercises.md`, it will show as failed. This is the expected behaviour. Check the file and commit the changes if you are happy with the changes.

## How to update

If there is a reason to increase the version, do the following:

```bash
# Make some changes
nano src/my_pre_commit_hooks/main.py

# Increase the version number
# Change the version number in the pyproject.toml file
# Rough example with find and replace from 0.1.0 to 0.2.0
sed -i 's/0.1.0/0.2.0/g' pyproject.toml

# Make sure the lock file is updated
uv lock --upgrade

# Add changes to git
git add .
git commit -m "Update to version 0.2.0"
git push 

# Attach a tag to the latest commit
git tag -a v0.2.0 -m "Version 0.2.0"
git push --tags
```