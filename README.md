# afterglow
A video and audio post-processing script for Plex (and other) HDTV DVR generated files using the ffmpeg-python binding library.

Features: 

- Very simple to use. No external configuration. 

- Can be used directly as a post-processing script for Plex's DVR features (subscription required)

- Can be called from a script to batch process a backlog of files (see shell/ts-all)


Support and feature requests:

Nope. You're on your own. Feel free to fork and have fun. I originally had plans to make Afterglow configurable with yaml files contianing profiles that could be assigned to specific TV Show titles (as example) or input file specs and matched on the fly. As I researched what I wanted to build I found Pytranscoder, which is pretty much *exactly* what I wanted. 

Afterglow still serves as a half-decent example of how to use ffmpeg-python, and possibly a useful post-processing script for those looking to use something without a lot of configuration, or as a base for your own modifications. Enjoy.
