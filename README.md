# rescue-walk

This is a script that walks through a directory tree and copies every file with the passed exceptions.


### Usage
	from copy_on_walk import prep, rescue_copy

	root_dir = '/mount/my_hdd'
	avoid_exts = [".py", ".pyc", ".plist"]
	avoid_words = ["Thumbs"]
	avoid_dirs = ["temp"]
	directory = "/mount/backup"

    files = prep(rootDir, avoid_exts=avoid_exts, avoid_dirs=avoid_dirs, avoid_words=avoid_words)
    rescue_copy(files, target)


* ```root_dir``` is the directory to walk.
* ```avoid_exts``` are the file extensions to avoid.
* ```avoid_dirs``` are the directorys to avoid.
* ```avoid_words``` are the filenames to avoid.
* ```directory``` is the direcotry where the files will be copied.

### TODO
It's currently missing any sort of error handling whatsoever.

It's also missing terminal arguments.


Help, issues, feedback and pull requests are welcomed.

