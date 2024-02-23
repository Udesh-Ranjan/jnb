

# jnb 
- Powerful Jupyter Notebook Management
- jnb is a Python package that empowers you to effortlessly **create**, **manage**, and **organize** your Jupyter Notebooks.
- Easily generate new notebooks, explore existing ones, and seamlessly keep your workflow organized.

## Installing and Uninstalling jnb 🛠️

**Prerequisites:**

_Python 3.8_ or later Python versions are supported

### Installing jnb

```
py -m pip install --upgrade jnb
```

### Uninstalling jnb
```
py -m pip uninstall jnb 
py cache purge
```

## jnb package usage 🛈

### Command for creating new notebooks

- Create a new notebook
```
py -m jnb -c file1.ipynb
```
- Create a new notebook at specified location
```
py -m jnb -c C:/users/username/.../file1.ipynb
```
- Create multiple notebooks
```
py -m jnb -c file1.ipynb C:/users/username/documents/file2.ipynb "C:/users/username/desktop/file_n.ipynb"
```

### Display help and usage for jnb 💡
```
py -m jnb -h
```

## How to contribute ❤️

First of all, thank you for taking the time to contribute to this project. 
We've tried to make a stable project and try to fix bugs and add new features continuously. You can help us do more.

Contributing to a project on GitHub is pretty straight forward. If this is you're first time, these are the steps you should take.

- Fork this repo.

And that's it! Read the code available and change the part you don't like! You're change should not break the existing code and should pass the **tests** ✅.

If you're adding a new functionality, start from the branch **master**. It would be a better practice to create a new **branch** and work in there.

When you're done, submit a ****pull request**** and for one of the maintainers to check it out. We would let you know if there is any problem or any changes that should be considered.

### Tests ✅
We've written tests ♾️ and you can run them to assure the stability of the code, just try command. If you're adding a new functionality please write a test for it.

### Documentation 📜
Every chunk of code that may be hard to understand has some comments above it. If you write some new code or change some part of the existing code in a way that it would not be functional without changing it's usages, it needs to be documented.

### Contact 📧
If you have any questions, feel free to reach out to us at _devparzival404@gmail.com_.

### License ©️
**jnb** is licensed under the terms of the ```MIT license```. For more details, see the ```LICENSE file```.