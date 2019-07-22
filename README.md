# Git + Github setup

1. Iniciar un repositorio nuevo: `git init .`
2. Asignar el repositorio remoto: `git remote add origin <URL>`

Esta URL puede ser por SSH o HTTPS (los protocolos):
- SSH: Secure Shell -> No tienes que recordar contraseñas, se usan llaves para autenticar
- HTTPS: HyperText Transfer Protocol Secure -> Usuario y contrase;a

Con esto ya estamos listos. La otra opción es...

1. Moverse al lugar donde estara el repositorio
2. Clonar un repositorio ya existente: `git clone https://github.com/alfonsolzrg/hackingtime-ejercicios.git .`

Actualizando codigo:
`git status` -> Muestra los cambios/modificaciones a mi directorio de trabajo.
`git diff [file]` -> Muestra los cambios en uno o mas archivos

## Area de trabajo

-> Si el cambio todavia no esta en el area de staging, puedo utilizar `git checkout <file_name>` para descartarlo.

-> Staging: `git add [<file>|.]`

## Area de staging

-> Regresar al area de trabajo -> `git reset HEAD <file>`

-> Guardar los cambios que esten en el area de staging -> `git commit`

 `git commit -m // git commit` y escribir un mensaje en el editor de textos que abre

 `git commit -a // git add . && git commit`

 `git commit -am "Este es mi cambio" // git add . && git commit -m "Este es mi cambio"`

## Commit (Local)

-> Subir al repositorio remoto -> `git push origin <branch_name>`

-> Ver el historial de cambios -> `git log`

-> Eliminar el commit local y dejar todo en el area de staging -> `git reset HEAD~ --soft`

-> Modificar, eliminar o reordenar commits locales -> `git rebase -i HEAD~<numero de commits hacia atras>`

## Commit (Remoto)
-> Cuando tu commit local tiene cambios que la rama remota no -> `git push origin <branch_name> --force`

## Trabajando con ramas

- Ver mis ramas locales: `git branch`
- Crear una rama: `git branch <nombre rama>`
- Moverse a otra rama: `git checkout <nombre rama>`
- Shortcut: `git checkout -b <nombre rama>`