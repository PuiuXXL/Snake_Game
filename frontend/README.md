# Snake Game - Ghid rapid

Acesta este frontend-ul jocului Snake. Este construit cu React, TypeScript si Vite.

## Cum pornesti proiectul

Deschide PowerShell in folderul `frontend`:

```powershell
cd D:\Sara\Desktop\OSUT\Snake_game\Snake_Game\frontend
npm install
npm run dev
```

Comenzi utile:

| Comanda | Ce face |
|---|---|
| `npm run dev` | Porneste aplicatia pentru dezvoltare |
| `npm run build` | Verifica si construieste versiunea finala |
| `npm run lint` | Verifica problemele de stil si cod |

## Unde gasesti fiecare lucru

```text
frontend/
├── public/assets/          Imagini publice folosite de tabla
├── src/
│   ├── assets/             Imagini importate direct in pagini
│   ├── components/         Bucati vizuale reutilizabile
│   │   ├── GameBoard/      Tabla, celule, sarpe si mancare
│   │   └── GameHeader/     Titlul jocului si scorul
│   ├── config/             Cai catre resursele jocului
│   ├── fixtures/           Date demonstrative pentru joc
│   ├── game/               Reguli pure: miscarea si coliziunile
│   ├── hooks/              Starea si bucla principala a jocului
│   ├── pages/              Ecrane complete: Start si Game Over
│   ├── types/              Tipuri TypeScript comune
│   ├── App.tsx             Leaga toate ecranele si componentele
│   ├── App.css             Layout-ul ecranului de joc
│   ├── index.css           Resetari si stiluri globale
│   └── main.tsx            Punctul de pornire React
├── package.json            Dependentele si comenzile proiectului
└── vite.config.ts          Configurarea serverului Vite
```

## Cum urmaresti logica jocului

1. [App.tsx](./src/App.tsx) alege ecranul afisat si trimite datele catre componente.
2. [useSnakeGame.ts](./src/hooks/useSnakeGame.ts) tine starea: sarpe, directie, mancare, scor si ecran.
3. [gameRules.ts](./src/game/gameRules.ts) calculeaza urmatoarea pozitie si coliziunile.
4. [GameBoard.tsx](./src/components/GameBoard/GameBoard.tsx) afiseaza tabla.
5. [StartPage.tsx](./src/pages/StartPage.tsx) si [GameOverPage.tsx](./src/pages/GameOverPage.tsx) afiseaza ecranele de inceput si final.

## Controale

- `W`, `A`, `S`, `D` sau sagetile schimba directia.
- Sarpele se misca automat.
- Lovirea peretelui sau a propriului corp afiseaza Game Over.
- Mancarea creste scorul cu 10 puncte si lungeste sarpele.

## Unde modifici ceva

- Vrei sa schimbi viteza? Modifica `MOVE_INTERVAL_MS` in `src/game/gameRules.ts`.
- Vrei sa schimbi dimensiunea tablei sau pozitia initiala? Modifica `src/fixtures/previewGame.ts`.
- Vrei sa schimbi aspectul tablei? Modifica `src/components/GameBoard/GameBoard.css`.
- Vrei sa schimbi pagina de start? Modifica fisierele din `src/pages/StartPage`.
- Vrei sa schimbi Game Over? Modifica fisierele din `src/pages/GameOverPage`.

