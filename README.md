<h1 align="center">Tazquiva</h1>

<p align="center">
  <img
    src="https://res.cloudinary.com/xpehvn66/image/upload/v1791663671/Tazquiva_Neon_Tech_Logo_iyoixd.png"
    alt="Tazquiva — AI-Powered Productivity Platform"
    width="100%"
  />
</p>

<p align="center">
  <strong>Plan smarter. Accomplish more.</strong>
  <br />
  An AI-powered productivity platform for intelligent task management,
  automated planning, and workflow optimization.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Development-blueviolet?style=flat-square" alt="Project Status" />
  <img src="https://img.shields.io/badge/Python-Django-092E20?style=flat-square&logo=django" alt="Django" />
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Architecture-Clean%20Architecture-purple?style=flat-square" alt="Clean Architecture" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License" />
</p>

---

## 📖 About Tazquiva

**Tazquiva** is an AI-powered productivity platform designed to make task management, planning, and personal productivity more intelligent.

Rather than functioning as a conventional to-do list, Tazquiva aims to help users understand their workload, prioritize meaningful tasks, break complex goals into manageable steps, and organize their time more effectively.

The platform is being developed with a modern full-stack architecture, emphasizing maintainability, modularity, scalability, and clean separation of responsibilities.

## ✨ Planned Features

- 🤖 **Natural Language Task Creation** — Create tasks using everyday language.
- 🎯 **Intelligent Prioritization** — Identify tasks that deserve attention first.
- 🧩 **Automatic Task Breakdown** — Transform complex goals into smaller, actionable subtasks.
- 📅 **Smart Daily Planning** — Generate structured daily plans based on tasks and priorities.
- ⏰ **Intelligent Reminders** — Keep important tasks from being overlooked.
- 🔄 **Recurring Tasks** — Automate the management of repeating activities.
- 📊 **Productivity Analytics** — Understand task completion and productivity patterns.
- 📝 **AI-Generated Summaries** — Review daily, weekly, and monthly progress.
- 🔐 **Secure Authentication** — Protect user accounts and API access.
- 📱 **Responsive Interface** — Deliver a consistent experience across screen sizes.

> Features are planned and will be implemented incrementally as development progresses.

## 🏗️ Architecture

Tazquiva follows a **Modular Monolith** approach combined with **Clean Architecture** principles.

The application is intended to be organized into independent feature modules, with clear boundaries between business logic, application use cases, infrastructure, and external interfaces.

Key architectural goals include:

- **Modularity** — Organize functionality into cohesive, feature-focused modules.
- **Separation of Concerns** — Keep business rules independent of frameworks and infrastructure.
- **Dependency Inversion** — Make core business logic independent of implementation details.
- **Maintainability** — Keep the codebase easy to understand, test, and extend.
- **Testability** — Design components so that business logic can be tested independently.
- **Extensibility** — Support additional AI providers and integrations without tightly coupling the application to a single provider.

The initial implementation prioritizes the backend architecture before expanding into frontend integration and advanced productivity features.

## 🛠️ Technology Stack

### Frontend
- **React** — Component-based user interface.
- **TypeScript** — Type-safe JavaScript development.
- **Vite** — Frontend development and build tooling.
- **Tailwind CSS** — Utility-first styling.

### Backend
- **Python** — Core backend programming language.
- **Django** — Backend framework.
- **Django REST Framework** — RESTful API development.

### Database
- **PostgreSQL** — Relational database management.

### Background Processing
- **Celery** — Asynchronous and scheduled task execution.
- **Redis** — Message broker and supporting in-memory data store.

### Authentication and API
- **JWT** — Token-based authentication.
- **drf-spectacular** — OpenAPI schema generation and API documentation.

### AI Integration
- **LLM APIs** — AI-assisted task understanding, planning, and prioritization.
- **Provider Abstraction** — An extensible integration layer designed to support different AI providers.

### Development and Quality
- **Git & GitHub** — Version control and collaborative development.
- **pytest** — Testing.
- **Docker** — Containerization as the project evolves.

> The stack represents the intended technology choices. Individual tools and features will be integrated as their respective development stages begin.

## 🗺️ Development Roadmap

Development is planned in incremental phases:

- [x] Create the GitHub repository and initialize project documentation.
- [ ] Establish the local development environment.
- [ ] Configure the Django backend and environment-specific settings.
- [ ] Implement the Clean Architecture foundation.
- [ ] Develop the accounts and authentication module.
- [ ] Build the initial REST API endpoints.
- [ ] Set up the React and TypeScript frontend.
- [ ] Integrate the frontend with the backend API.
- [ ] Implement task management and prioritization.
- [ ] Integrate AI-assisted task creation and planning.
- [ ] Introduce background processing with Celery and Redis.
- [ ] Add comprehensive automated tests.
- [ ] Prepare production deployment and monitoring.

## 🚀 Getting Started

Tazquiva is currently under active development. Setup instructions will be expanded as the backend and frontend foundations are established.

### Prerequisites

The planned development environment includes:

- Python
- Node.js and npm
- PostgreSQL
- Redis
- Git

### Development Setup

Once the initial project structure is implemented, detailed instructions for configuring the environment, installing dependencies, setting up the database, and running the application will be provided here.

## 🤝 Development Workflow

Tazquiva is developed with an emphasis on maintainable code and a clean Git history.

The planned workflow includes:

- Feature-based branches.
- Conventional commit messages.
- Pull requests for reviewing changes.
- Incremental implementation and testing.
- Clear documentation for significant architectural decisions.

Example commit messages:

```text
chore: initialize project structure
feat(accounts): add user registration
test(accounts): add registration unit tests
docs: document local development setup
refactor(tasks): separate business logic from API views
