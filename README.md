# 🐍 Snake Workshop – Learn Python Backend Development

An interactive, educational workshop project designed to introduce participants to **Python programming and backend development** by building the core logic of the classic Snake game.

The application is being built with a **React + TypeScript frontend** and a **Python FastAPI backend**. The frontend will handle rendering and user interactions, while the backend will manage the game state and implement the core game mechanics. For the workshop, the frontend and API routing will be prepared in advance so participants can focus on completing the Python game logic.

## 🎯 Project Goal

The main objective is to provide a hands-on learning experience where participants progressively implement the game's backend logic while immediately seeing the results of their code in a playable interface.

Instead of building an entire application from scratch, participants receive a prepared project structure with predefined functions that they will complete during the workshop.

## 🚀 Key Features

- **Interactive Snake Game:** A modern, visually engaging interface built with React and TypeScript.
- **Python Game Logic:** Implement snake movement, direction handling, collision detection, food generation, and scoring.
- **REST API Integration:** Communication between the frontend and backend using FastAPI.
- **Progressive Learning:** Each completed function unlocks additional gameplay functionality.
- **Hands-on Workshop:** Learn Python concepts through practical implementation and immediate visual feedback.
- **API Development (Bonus):** Explore backend routing, HTTP requests, and JSON responses by creating FastAPI endpoints.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Backend | Python, FastAPI |
| Communication | REST API / JSON |
| Testing | Pytest |

## 📁 Frontend Structure

The tree below describes the target frontend structure. It is an implementation plan, not a list of files that are all complete today.

Currently, the frontend is initialized and includes `GameBoard`, `GameHeader`, shared game types, asset configuration, and preview data. `GameControls`, the overlay, hooks, API service, and API environment configuration still need to be added. `App.tsx`, `App.css`, and `index.css` currently contain the Vite starter screen and must be updated to display the game.

```text

Snake_Game/
│
├── backend/                       # Python + FastAPI
│   │
│   ├── app/                       # API si comunicare
│   │   ├── main.py                # Configurarea FastAPI
│   │   ├── routers/               # Endpoint-uri HTTP
│   │   │   ├── game.py            # Cererile jocului
│   │   │   └── health.py          # Verificarea serverului
│   │   ├── schemas.py            # Validarea datelor
│   │   ├── services/              # Legatura cu logica
│   │   │   └── game_service.py
│   │   └── core/                  # Configurari generale
│   │
│   ├── game/                      # Logica Snake
│   │   ├── models.py              # Datele jocului
│   │   ├── movement.py            # Miscarea sarpelui
│   │   ├── collisions.py          # Coliziunile
│   │   ├── food.py                # Generarea mancarii
│   │   └── engine.py              # Regulile jocului
│   │
│   ├── tests/                     # Teste Python
│   └── requirements.txt           # Dependente Python
│
└── frontend/                      # React + TypeScript
    ├── public/
    │   └── assets/               # Imaginile jocului
    ├── src/
    │   ├── components/           # Elemente vizuale
    │   ├── pages/                # Start si Game Over
    │   ├── hooks/                # Stare si taste
    │   ├── services/             # Comunicare cu Python
    │   ├── App.tsx               # Componenta principala
    │   └── main.tsx              # Pornirea React
    └── package.json              # Dependente npm

```

### Components

Each component lives alongside its own CSS file. Components receive data through props and expose callbacks for user actions.

| File | Responsibility |
|---|---|
| `components/GameBoard/GameBoard.tsx` | Render the grid, snake segments, and food from the supplied board size and coordinates. It does not calculate movement or collisions. |
| `components/GameBoard/GameBoard.css` | Style the board frame, alternating cells, and sprites. |
| `components/GameHeader/GameHeader.tsx` | Display the game title and current score. |
| `components/GameHeader/GameHeader.css` | Style the title, header layout, and score card. |
| `components/GameControls/GameControls.tsx` | Display Start/Restart controls and keyboard instructions. Invoke callbacks supplied by the parent and disable controls when necessary. |
| `components/GameControls/GameControls.css` | Style the controls, button states, and layout on small screens. |
| `components/GameOverlay/GameOverlay.tsx` | Display messages over the board, such as the initial prompt or Game over, based on the supplied game status. |
| `components/GameOverlay/GameOverlay.css` | Position and style the overlay without changing the underlying game state. |

### State, Input, and Backend Communication

| File | Responsibility |
|---|---|
| `hooks/useGame.ts` | Coordinate the current game state, loading and error states, starting/restarting a game, and requests for the next step. Prevent overlapping step requests and clean up scheduled work when the game stops or the component unmounts. Game rules remain in Python. |
| `hooks/useKeyboardControls.ts` | Listen for arrow keys and WASD, translate them into requested directions, prevent page scrolling for handled game keys while controls are active, and remove listeners on cleanup. The backend validates whether a direction change is allowed. |
| `services/gameApi.ts` | Send requests to FastAPI, read JSON responses, and report request failures. Keep HTTP details out of visual components. Endpoint names and payloads will follow the agreed backend contract. |
| `types/game.ts` | Define shared TypeScript types such as `Position`, `Direction`, `GameStatus`, and `GameState`. This file contains no JSX or game rules. |
| `config/game.ts` | Centralize sprite paths and other frontend display configuration. |
| `config/api.ts` | Read and expose the backend base URL from the frontend environment configuration. |
| `fixtures/previewGame.ts` | Provide a sample game state for building and previewing the interface before connecting the backend. It is not the source of live game state. |

### Application Entry and Global Styles

| File | Responsibility |
|---|---|
| `App.tsx` | Compose the screen from the game components. Initially use preview data; later connect the components to `useGame` and keyboard input. |
| `App.css` | Define the page layout, spacing, and maximum width of the game area. |
| `index.css` | Define global styles, typography, shared color variables, and basic browser resets. Component-specific styles stay with their components. |
| `main.tsx` | Mount the React application into the HTML root and load global styles. |

### Assets and Project Configuration

| File or folder | Responsibility |
|---|---|
| `public/assets/png/` | Store the downloaded game sprites. Files are accessed through URLs such as `/assets/png/apple_red_32.png`; the URL does not include `public`. |
| `public/assets/preview.png` | Keep the asset pack preview for reference. It is not required to render the board. |
| `public/assets/readme.txt` | Preserve the asset author's usage information and credits. |
| `.env.example` | Document the required public frontend environment variables using example values, such as the backend URL. Never include secrets. |
| `.gitignore` | Exclude generated files, installed dependencies, and local environment files from version control. |
| `index.html` | Provide the HTML document, page metadata, and root element where React mounts. |
| `package.json` | Declare dependencies and development, build, and lint scripts. |
| `package-lock.json` | Record resolved dependency versions for reproducible installation. |
| `eslint.config.js` | Configure static code checks for the frontend. |
| `tsconfig.json` | Reference the application and tooling TypeScript configurations. |
| `tsconfig.app.json` | Configure TypeScript checks for application source files. |
| `tsconfig.node.json` | Configure TypeScript checks for tooling files such as the Vite configuration. |
| `vite.config.ts` | Configure Vite and its React integration. |

The generated `src/assets/` images and starter public icons can be removed once the Vite starter screen no longer imports or references them. New modules should be added when their functionality is implemented rather than creating empty placeholder files.

### Responsibility Boundaries

- **Components** render data and emit user actions.
- **Hooks** coordinate input, interface state, and the request lifecycle.
- **Services** handle HTTP communication with FastAPI.
- **Python backend** owns movement, direction validation, collision detection, food generation, growth, and scoring.
- **Workshop participants** complete the Python logic functions; the frontend and API routing are prepared for them.

## 📚 Learning Objectives

By completing this workshop, participants will gain practical experience with Python functions, data structures, conditional logic, game state management, and fundamental backend development concepts.

The project demonstrates how backend logic connects to a real frontend application, transforming individual Python functions into a fully playable game.

## 💡 Workshop Philosophy

**Learn by building. Code by code, feature by feature.**

The focus is not simply on playing Snake, but on understanding how software works behind the scenes and experiencing how every line of code contributes to a functioning application.
