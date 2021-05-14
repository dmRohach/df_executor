## Usage
`df_executor` is a command line program, executing and parsing linux system command `df`.

 running without arguments

    $ python3 app.py
    
 will return you `JSON dict` with following keys:
 
- `status`
- `error`
- `result`

You could add argument `--human` or `--inode` to execute 

`df -h` and `df -i` respectively 
