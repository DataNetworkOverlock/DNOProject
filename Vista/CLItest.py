import click

def imprimir_numeros_ascendentes():
    for i in range(1, 11):
        click.echo(i)

def imprimir_numeros_descendentes():
    for i in range(10, 0, -1):
        click.echo(i)

@click.command()
def menu_interactivo():
    # Imprime el título una sola vez al inicio
    click.echo("  _____        _          _   _      _                      _       ____                 _            _ ")
    click.echo(" |  __ \\      | |        | \\ | |    | |                    | |     / __ \\               | |          | |")
    click.echo(" | |  | | __ _| |_ __ _  |  \\| | ___| |___      _____  _ __| | __ | |  | |_   _____ _ __| | ___   ___| | __")
    click.echo(" | |  | |/ _` | __/ _` | | . ` |/ _ \\ __\\ \\ /\\ / / _ \\| '__| |/ / | |  | \\ \\ / / _ \\ '__| |/ _ \\ / __| |/ / ")
    click.echo(" | |__| | (_| | || (_| | | |\\  |  __/ |_ \\ V  V / (_) | |  |   <  | |__| |\\ V /  __/ |  | | (_) | (__|   < ")
    click.echo(" |_____/ \\__,_|\\__\\__,_| |_| \\_|\\___|\\__| \\_/\\_/ \\___/|_|  |_|\\_\\  \\____/  \\_/ \\___|_|  |_|\\___/ \\___|_|\\_\\ ")

    while True:
        click.echo("\nMenú interactivo:")
        click.echo("1. Realizar una tarea (Imprimir números del 1 al 10)")
        click.echo("2. Realizar otra tarea (Imprimir números del 10 al 1)")
        click.echo("3. Salir")

        opcion = click.prompt('Selecciona una opción', type=int)

        if opcion == 1:
            imprimir_numeros_ascendentes()
        elif opcion == 2:
            imprimir_numeros_descendentes()
        elif opcion == 3:
            click.echo('Saliendo de la aplicación.')
            break
        else:
            click.echo('Opción no válida. Por favor, elige una opción válida.')

if __name__ == '__main__':
    menu_interactivo()
