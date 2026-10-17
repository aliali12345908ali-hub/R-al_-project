module.exports = {
  apps: [
    {
      name: "omni-core",
      script: "./omni_core.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    },
    {
      name: "autonomous-whale",
      script: "./autonomous_whale_hunter.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    },
    {
      name: "omega-command",
      script: "./omega_command_nexus.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    },
    {
      name: "lead-scraper",
      script: "./lead_scraper.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    },
    {
      name: "ai-outreach",
      script: "./ai_outreach_gen.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    },
    {
      name: "neural-evolution",
      script: "./omega_neural_evolution_core.py",
      interpreter: "python3",
      autorestart: true,
      max_memory_restart: '150M'
    }
  ]
};


