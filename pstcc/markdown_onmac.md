
https://stackoverflow.com/questions/7694887/is-there-a-command-line-utility-for-rendering-github-flavored-markdown

Install it with:

$ pip install grip
And to use it, simply:

$ grip
Then visit localhost:5000 to view the readme.md file at that location.

You can also specify your own file:

$ grip CHANGES.md
And change port:

$ grip 8080
And of course, specifically render GitHub-Flavored Markdown, optionally with repository context:

$ grip --gfm --context=username/repo issue.md
Notable features:

Renders pages to appear exactly like on GitHub
Fenced blocks
Python API
Navigate between linked files (thanks, vladwing!) added in 2.0
Export to a single file (thanks, iliggio!) added in 2.0
New: Read from stdin and export to stdout added in 3.0
