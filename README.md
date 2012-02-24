# touchas

## What is it?

`touchas` is a script written in Python that creates new files from pre existing templates.  The name dirives from the unix command `touch`; which creates a new, empty file. 

## Templates

The syntax will be soon changing.  Currently it works like this.

Text in the template is copied from the template to the new file as-is.

The exception is text between a `(%` and a `%)`.  These markers are used for dynamic text.  Currently they come from the command line in the form of `name=value`.  For example,

    My name is (% name|the default %).

Here are two example runs of touchas, assuming our template is stored in `txt.tmpl`.

    $ touchas -t txt
      My name is the default.

    $ touchas -t txt -r name=John
      My name is John.

## How can I help?

There are two parts to this project.

1. `touchas.py` which parses templates
1. The individual templates

If there are files you reglarly create, consider making a template for them and sharing it with us.  The more templates; the more useful `touchas` will be.


