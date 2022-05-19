# tcli
## Very simple Trello card creater

Usage: tcli.py [-h] -b BOARD -l LIST -n NAME -d DESCRIPTION <br />

Note: <br />
      You either have to provide board, list, name and description <br />
      or <br />
      provide a CSV file with -c <br />

### There are two ways to run it:
#### Manually by cloning the repo

1. `git clone https://github.com/inikolcev/tcli && cd tcli` <br />
2. `pip3 install -r requirements.txt` <br />
3. `python3 tcli.py` <br />
4. To actually be able to create cards set the environment variables TCLI_APIKEY and TCLI_TOKEN to your Trello Apikey and Token

#### Or by using the provided docker container
1.`docker pull inikolcev/tcli` <br />
2.`docker run -e TCLI_APIKEY=<Your Trello APIKEY> -e TCLI_TOKEN=<Your Trello Token> inikolcev/tcli --help` <br />
Note: <br />
To use CSV files with a docker container you need first to start the container with something like `docker run -it --entrypoint /bin/bash inikolcev/tcli` and then run `docker cp csvfile <containerID>:/` to copy the file inside the container.<br />
After that you can run tcli normally from inside the container.

### Example usage:
`python3 tcli.py -b Default -l "To Do" -n "NewCard" -d "New useless card"` <br />
This will create a new card named NewCard with description "New useless card" in the "To Do" list which belongs to the Default board.

### TODOs:
  - Fix the argument parsing, currently it is hacky.
  - Add tests.
  - Add aditional functionality.

## License

Refer to [LICENSE](LICENSE).
