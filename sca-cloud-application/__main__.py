import click

@click.command()
@click.option('--name', prompt='Your os is',)


 def is_tool(wget):
#     """Check whether `name` is on PATH and marked as executable."""

#     # from whichcraft import which
     from shutil import which

     return which(wget) is not None

 def is_tool(curl):
#     """Check whether `name` is on PATH and marked as executable."""

#     # from whichcraft import which
#     from shutil import which

#     return which(curl) is not None
if __name__ == '__main__':
    successful()