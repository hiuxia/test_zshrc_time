## Aim

A simple python script to evaluate the execution time of each command in your `~/.zshrc`. If your zsh has a long start-up time, this repository is for you.

## How to use

-   clone the file and replace the `zsh_path` with your own in the `get_execution_time` function.
-   run it and Enjoy!

## demo result

The final result format is `command_id: command_name, execution_time` for each command in `./zshrc`.

In the end, it will output the total spent executing the file. (in milliseconds)

## Support syntax

-   normal statement/command.
-   if/while/for/switch.
-   function
