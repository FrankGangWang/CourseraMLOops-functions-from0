import click
from mylib.bot import scrape


# To add parameters, use the option() and argument() decorators:
@click.command()
@click.option("--name", prompt="Wikipedia page to scrape", help="Web page to scrape")
@click.option(
    "--length",
    prompt="Number of sentences from wikipedia",
    help="number of sentences from wikipedia",
)
def cli(name="Microsoft", length=1):
    r = scrape(name, sentences=length)
    click.echo(click.style(f"{r}:", fg="white", bg="black"))


if __name__ == "__main__":
    cli()
