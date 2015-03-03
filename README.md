# Rotten Tomatoes CLI
A simple command line interface for the Rotten Tomatoes API.

Setup:

1. Install through pip
2. [Get a Rotten Tomatoes API Key](http://developer.rottentomatoes.com/)
3. Put the RT API Key in your OS Environment
	* E.g., in your .bashrc:
	

	```shell
	export RT_API_KEY=[api_key]
	```
4. Use the CLI in your terminal!
```python
python rtCLI.py
```

![Main Menu](/images/1.png)
![Search](/images/2.png)
![Movie Reviews](/images/3.png)


To-Do:
  1. ~~[Figure out what data I have access to](https://github.com/jimjshields/rotten_tomatoes_CLI/wiki/Rotten-Tomatoes-Data)~~
  2. Design best way to organize it (put classes in a module?)
  3. ~~[Refactor code to be OO - classes for each type of request?](https://github.com/jimjshields/rotten_tomatoes_CLI/commit/29477096be44a7a239e2da3a3ebd1a36b6dec661)~~
  4. Allow for commands to access different types of data