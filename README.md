# TaskFlow ![CI](https://github.com/MechatronicCoder/taskflow/actions/workflows/ci.yml/badge.svg)

Gestor de tareas en Python · Proyecto integrador del curso **DevOps & Project Management**.

Sitio: https://mechatroniccoder.github.io/taskflow/ · Jira: https://wfhh2001.atlassian.net/jira/software/projects/TF/boards/2 (proyecto TF)

## Equipo
- William Fabian Huaman Huaman — @MechatronicCoder

## Funcionalidades
| Clave | Funcionalidad |
|-------|---------------|
| TF-4  | Agregar, completar y listar tareas con prioridad |
| TF-5  | Eliminar tareas por id |
| TF-8  | Filtrar tareas por prioridad |
| TF-9  | Buscar tareas por texto (ignora mayúsculas) |
| TF-10 | Resumen de avance (total, completadas, pendientes, %) |
| TF-11 | Rechazo de títulos duplicados (bug corregido) |

## Cómo ejecutarlo y probarlo
```bash
python -m venv .venv
source .venv/bin/activate        # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt
python -m taskflow               # demo con las funcionalidades del Sprint 1
python -m pytest -v              # 17 pruebas
```

## Flujo de trabajo
- Estrategia: GitHub Flow · merge: squash · `main` protegida con el ruleset `proteger-main`
- Convenciones: ramas `tipo/TF-n-descripcion`, Conventional Commits, PRs con plantilla

## CI/CD
- `ci.yml`: pruebas en Python 3.11, 3.12 y 3.13 en cada PR (checks requeridos)
- `deploy.yml`: pruebas + publicación en GitHub Pages en cada merge a `main`

## Gestión ágil
- Épicas: TF-1 Gestión de tareas · TF-2 Calidad y automatización · TF-3 Visibilidad del proyecto
- Sprint 0 · Hitos 1 y 2: 11 puntos completados (TF-4 a TF-7)
- Sprint 1 · Meta: *"Encontrar tareas rápido y conocer el avance"*: 13 de 13 puntos completados (TF-8 a TF-11)
- Velocity: 11 → 13 puntos · Burndown: [docs/evidencias/2-burndown-sprint1.png](docs/evidencias/2-burndown-sprint1.png)

## Evidencias
**Hito 1 y 2**
- PR #1 · Plantilla de PR: https://github.com/MechatronicCoder/taskflow/pull/1
- PR #2 · Pipeline de CI: https://github.com/MechatronicCoder/taskflow/pull/2
- PR #3 · Funcionalidad eliminar: https://github.com/MechatronicCoder/taskflow/pull/3
- PR #4 · Despliegue en GitHub Pages: https://github.com/MechatronicCoder/taskflow/pull/4
- PR #5 · Avance del Hito 2: https://github.com/MechatronicCoder/taskflow/pull/5
- Release v0.2.0: https://github.com/MechatronicCoder/taskflow/releases/tag/v0.2.0

**Hito 3 · Sprint 1**
- PR #7 · TF-8 Filtrar por prioridad: https://github.com/MechatronicCoder/taskflow/pull/7
- PR #8 · TF-9 Buscar por texto: https://github.com/MechatronicCoder/taskflow/pull/8
- PR #9 · TF-10 Resumen de avance: https://github.com/MechatronicCoder/taskflow/pull/9
- PR #10 · TF-11 Títulos duplicados: https://github.com/MechatronicCoder/taskflow/pull/10

**Capturas de Jira** (`docs/evidencias/`)
- [Tablero al final del Sprint 1](docs/evidencias/1-tablero-sprint1.png) (vista Lista filtrada por Sprint 1, tomada tras completar el sprint)
- [Burndown del Sprint 1](docs/evidencias/2-burndown-sprint1.png)
- [Sprint report](docs/evidencias/3-sprint-report-sprint1.png)
- [Panel Desarrollo de TF-9](docs/evidencias/4-panel-desarrollo-tf9.png)
- [Backlog con épicas](docs/evidencias/5-backlog-epicas.png)

## Avance del proyecto
- [x] Hito 1 — Repositorio, código base y pruebas locales
- [x] Hito 2 — GitHub Flow, CI/CD y GitHub Pages
- [x] Hito 3 — Jira, sprint e integración con GitHub

## Retrospectiva del Sprint 1
| Mantener | Mejorar | Acción (clave Jira) |
|----------|---------|---------------------|
| Escribir las pruebas antes que el código (rojo → verde) y un PR por elemento con su clave de Jira | Las tarjetas de Jira se movieron a mano y es fácil olvidarlo | Configurar la automatización de Jira (rama creada → In Progress, PR fusionado → Done) |

## Lecciones aprendidas
- Proteger `main` con PRs y checks obligatorios evita que un cambio roto llegue a producción.
- Traducir los criterios de aceptación en pruebas hace que "terminado" sea verificable.
- Usar la clave de Jira en ramas, commits y PRs da trazabilidad completa entre el plan y el código.