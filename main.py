import socket
import typer
from pathlib import Path
import datetime


app = typer.Typer()


@app.command('ping')
def ping(domains: str):
    hosts = domains.split(',')
    hosts_path = Path('hosts.txt')
    hosts_text = f'# HOSTS {datetime.datetime.now().isoformat()}\n'

    for host in hosts:
        typer.echo(
            f'{host} is {typer.style("OK", fg=typer.colors.GREEN, bold=True)}')
        ip = socket.gethostbyname(host)
        hosts_text = f'{hosts_text}{ip} {host}\n'

    hosts_text = f'{hosts_text}# GITHUB END\n'
    hosts_path.write_text(hosts_text)


if __name__ == '__main__':
    app()
