### A python built rpg game with test coverage.


## Project Dependancies
   To run this project, ensure the following dependency is installed: 
    * PyTest (for running tests).

## Virtual Enviroment
  To install the project's dependancies you need to create a python virtual enviroment in the project's root directory.

  ```bash
  python -m venv venv
 ```

After runnning it sucessfully, run the following command to activate the terminal:

Windows:

  ```bash
  venv/Scripts/activate
 ```

If you encounter a permission policy issue, enter the following command:
  ```bash
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
 ```

Unix Systems:
  ```bash
source venv/bin/activate
 ```
## Install Dependancies
After activating the virtual environment, install the required dependencies:

  ```bash
pip install -r requirements.txt
 ```

### Running the Game

After setting up the environment, you can launch the RPG game:

  ```bash
python main.py
 ```

### Running Tests
To verify the functionality of the game, run the tests using PyTest:

  ```bash
pytest
 ```
This will execute all tests in the `tests/` directory and display the results.


### Contributing
Feel free to contribute to this project by submitting issues or pull requests. Please include test cases for any new features or bug fixes.


### License
This project is licensed under the MIT License.




