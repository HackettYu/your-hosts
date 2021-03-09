import socket
import typer
from pathlib import Path
import datetime


app = typer.Typer()


@app.command('ping')
def ping(domains: str, output: str):
    """example

    python main.py 'github.com,gist.github.com,assets-cdn.github.com,raw.githubusercontent.com,gist.githubusercontent.com,cloud.githubusercontent.com,camo.githubusercontent.com,avatars.githubusercontent.com,avatars0.githubusercontent.com,avatars1.githubusercontent.com,avatars2.githubusercontent.com,avatars3.githubusercontent.com,avatars4.githubusercontent.com,avatars5.githubusercontent.com,avatars6.githubusercontent.com,avatars7.githubusercontent.com,avatars8.githubusercontent.com,avatars.githubusercontent.com,github.githubassets.com,user-images.githubusercontent.com,codeload.github.com,favicons.githubusercontent.com,marketplace-screenshots.githubusercontent.com,repository-images.githubusercontent.com,api.github.com'  # noqa
    """
    hosts = domains.split(',')
    hosts_path = Path(output)
    hosts_text = f'# HOSTS {datetime.datetime.now().isoformat()} <br>\n'

    for host in hosts:
        typer.echo(
            f'{host} is {typer.style("OK", fg=typer.colors.GREEN, bold=True)}')
        ip = socket.gethostbyname(host)
        hosts_text = f'{hosts_text}{ip} {host} <br>\n'

    hosts_text = f'{hosts_text}# GITHUB END <br>\n'
    hosts_path.write_text(hosts_text)


if __name__ == '__main__':
    app()
