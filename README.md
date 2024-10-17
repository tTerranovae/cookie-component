# Streamlit Cookie Component

This Streamlit component allows you to easily retrieve a cookie value from the browser within your Streamlit app. It provides a simple interface to access specific cookies by name using a Python function that interacts with JavaScript.

## Features

- **Easy to use**: Retrieve cookie values with a single function call.
- **Streamlit integration**: Seamlessly integrates with Streamlit as a custom component.
- **Flexible**: Fetch the value of any cookie by its name.

## Installation

1. Clone or download this repository.
2. Install the Python dependencies using [Poetry](https://python-poetry.org/):

   ```bash
   poetry install
3. Navigate to the cookie_component directory to view the component's source code and the example Streamlit app.

## Usage
You can use the get_cookie function from the cookie_component module to retrieve the value of any cookie:
```python
import streamlit as st
from cookie_component import cookie_manager
```

## Specify the cookie name you want to retrieve
```python
cookie_name = '_streamlit_xsrf'
```

## Display the cookie value in your Streamlit app
```python
st.write(f"Cookie Value of {cookie_name}: {cookie_manager(cookie_name)}")
```
## Component Overview
1. cookie_component/__init__.py: The Python interface to the cookie component.
2. cookie_component/index.js: JavaScript logic that retrieves the cookie value from the browser.
3. cookie_component/streamlit-component-lib.js: Connects the Streamlit app to the JavaScript component using Streamlit's component library.

## Development
To develop or make changes to the component:

1. Modify the JavaScript code in cookie_component/index.js.
2. Run your Streamlit app to test the changes:
```python
streamlit run app.py
```
3. Managing Dependencies with Poetry
To add or update dependencies for this project, use the following Poetry commands:

Add a new dependency:
```bash
poetry add <package_name>
poetry update
poetry shell
```
## Testing
```python
poetry run pytest tests
```
## Contributing
Feel free to submit issues or pull requests if you'd like to contribute to this component.