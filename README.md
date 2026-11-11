# Snake Game

Un joc Snake realizat cu React, TypeScript si Vite.

## Pornire rapida

```powershell
cd D:\Sara\Desktop\OSUT\Snake_game\Snake_Game\frontend
npm install
npm run dev
```

Aplicatia este in folderul [frontend](./frontend). Ghidul complet pentru fisiere,
comenzi si logica jocului se afla in [frontend/README.md](./frontend/README.md).

## Structura proiectului

```text
Snake_Game/
├── frontend/       Aplicatia web React
│   ├── public/     Resurse publice, inclusiv sprites
│   └── src/        Codul aplicatiei
└── README.md       Prezentarea generala a proiectului
```

## Starea actuala

- Pagina de start este functionala.
- Sarpele se misca automat si poate fi controlat cu sagetile sau WASD.
- Mancarea creste scorul si lungeste sarpele.
- Coliziunile afiseaza pagina Game Over.
- Logica este momentan locala in frontend; backend-ul Python poate fi adaugat ulterior.
