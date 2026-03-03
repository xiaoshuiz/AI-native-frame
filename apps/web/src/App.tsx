import "./App.css";

type InfoCard = {
  icon: string;
  title: string;
  description: string;
  path: string;
};

const cards: InfoCard[] = [
  {
    icon: "🧭",
    title: "Spec-first workflow",
    description: "Start implementation from reusable templates, not from ad-hoc tickets.",
    path: "specs/templates/",
  },
  {
    icon: "🏗️",
    title: "Frontend-first architecture",
    description: "Use docs and ADRs to keep design decisions explicit and traceable.",
    path: "docs/ARCHITECTURE.md",
  },
  {
    icon: "🔄",
    title: "Predictable delivery",
    description: "Run lint + build checks in CI and publish container images from CD.",
    path: ".github/workflows/",
  },
];

function App() {
  return (
    <main className="app">
      <header className="hero">
        <p className="badge">⚡ Frontend-First Template</p>
        <h1>AI Native Frame</h1>
        <p className="subtitle">
          Build AI-native product interfaces with clear specs, fast iteration loops, and
          release-friendly workflows.
        </p>
        <div className="hero-actions">
          <a className="button primary" href="https://vite.dev" target="_blank" rel="noreferrer">
            Vite Docs
          </a>
          <a className="button" href="https://react.dev" target="_blank" rel="noreferrer">
            React Docs
          </a>
        </div>
      </header>

      <section className="card-grid">
        {cards.map((card) => (
          <article key={card.title} className="card">
            <h2>
              <span>{card.icon}</span>
              {card.title}
            </h2>
            <p>{card.description}</p>
            <code>{card.path}</code>
          </article>
        ))}
      </section>
    </main>
  );
}

export default App;
